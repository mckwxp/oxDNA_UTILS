/*
 * COMTwist.cpp
 *
 *  Created on: 9 Dec 2019
 *      Author: marco
 */

#include <vector>
#include "COMTwist.h"
#include "../Utilities/Utils.h"
#include "../Boxes/BaseBox.h"
#include "../Utilities/oxDNAException.h"
#include "../Particles/BaseParticle.h"

using namespace std;

template<typename number>
COMTwist<number>::COMTwist(){
	_rate = 0;
	_last_step = -1;
	_box_ptr = NULL;	
}

template<typename number>
COMTwist<number>::~COMTwist(){

}

template<typename number>
void COMTwist<number>::get_settings (input_file &inp) {
	getInputString(&inp, "com_list", _com_string, 1);
	
	getInputNumber(&inp, "stiff", &this->_stiff, 1);
	getInputNumber(&inp, "rate", &this->_rate, 1);
	getInputNumber(&inp, "base", &this->_F0, 1);

	std::string (strdir);
	double tmpf[3];
	int tmpi;
	getInputString (&inp, "axis", strdir, 1);
	tmpi = sscanf (strdir.c_str(), "%lf, %lf, %lf", tmpf, tmpf + 1, tmpf +2);
	if (tmpi != 3) throw oxDNAException ("Could not parse axis `%s\' for COMTwist. Aborting", strdir.c_str());
	this->_axis = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]);
	this->_axis.normalize();
	
	getInputString (&inp, "pos0", strdir, 1);
	tmpi = sscanf (strdir.c_str(), "%lf, %lf, %lf", tmpf, tmpf + 1, tmpf +2);
	if (tmpi != 3) throw oxDNAException ("Could not parse pos0 `%s\' for COMTwist. Aborting", strdir.c_str());
	this->_pos0 = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]);
	
	getInputString (&inp, "center", strdir, 1);
	tmpi = sscanf (strdir.c_str(), "%lf, %lf, %lf", tmpf, tmpf + 1, tmpf +2);
	if (tmpi != 3) throw oxDNAException ("Could not parse center `%s\' for COMTwist. Aborting", strdir.c_str());
	this->_center = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]);

	if (getInputString (&inp, "mask", strdir, 0) == KEY_FOUND) {
		tmpi = sscanf (strdir.c_str(), "%lf, %lf, %lf", tmpf, tmpf + 1, tmpf + 2);
		if (tmpi != 3) throw oxDNAException("Could not parse mask `%s\' for COMTwist. Aborting", strdir.c_str());
		this->_mask = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]); 
	}
	else this->_mask = LR_vector<number> (0., 0., 0.);
}

template<typename number>
void COMTwist<number>::_check_index(int idx, int N) {
	if(idx < 0 || idx >= N) throw oxDNAException("COMTwist: invalid id %d", idx);
}

template <typename number>
void COMTwist<number>::init (BaseParticle<number> ** particles, int N, BaseBox<number> * box_ptr) {
	_box_ptr = box_ptr;

	vector<int> com_indexes = Utils::getParticlesFromString(particles, N, _com_string, "COMTwist");
	_n_com = com_indexes.size();
	for(int i = 0; i < _n_com; i++){
		_com_indexes[i] = com_indexes[i];
	}

	for(vector<int>::iterator it = com_indexes.begin(); it != com_indexes.end(); it++) {
		_check_index(*it, N);
		_com_list.insert(particles[*it]);
		particles[*it]->add_ext_force(this);
	}
	
	OX_LOG (Logger::LOG_INFO, "Adding COMTwist (F0=%g, rate=%g, pos0=%g,%g,%g, axis=%g,%g,%g, center=%g,%g,%g, mask=%g,%g,%g", this->_F0, this->_rate, this->_pos0.x, this->_pos0.y, this->_pos0.z, this->_axis.x, this->_axis.y, this->_axis.z, this->_center.x, this->_center.y, this->_center.z, this->_mask.x, this->_mask.y, this->_mask.z);
}

template<typename number>
void COMTwist<number>::_compute_coms(llint step) {
	if(step != _last_step) {
		_com = LR_vector<number>(0, 0, 0);
		for(typename set<BaseParticle<number> *>::iterator it = _com_list.begin(); it != _com_list.end(); it++) {
			_com += _box_ptr->get_abs_pos(*it);
		}
		_com /= _com_list.size();

		_last_step = step;
	}
}

template<typename number>
number COMTwist<number>::potential(llint step, LR_vector<number> &pos) {
	_compute_coms(step);
	number t = (this->_F0 + this->_rate * (number) step);

	number sintheta = sin (t);
	number costheta = cos (t);
	number olcos = ((number) 1.) - costheta;

	number xyo = this->_axis.x * this->_axis.y * olcos;
	number xzo = this->_axis.x * this->_axis.z * olcos;
	number yzo = this->_axis.y * this->_axis.z * olcos;
	number xsin = this->_axis.x * sintheta;
	number ysin = this->_axis.y * sintheta;
	number zsin = this->_axis.z * sintheta;

	LR_matrix<number> R(this->_axis.x * this->_axis.x * olcos + costheta,
						xyo - zsin,
						xzo + ysin,

						xyo + zsin,
						this->_axis.y * this->_axis.y * olcos + costheta,
						yzo - xsin,

						xzo - ysin,
						yzo + xsin,
						this->_axis.z * this->_axis.z * olcos + costheta);

	LR_vector<number> postrap = R * (_pos0 - _center) + _center;

	// we "mask" the resulting vector;
	LR_vector<number> dr = _com - postrap;
	dr.x *= _mask.x;
	dr.y *= _mask.y;
	dr.z *= _mask.z;

	return (number) (0.5 * this->_stiff * (dr * dr) / _com_list.size());
}


template<typename number>
LR_vector<number> COMTwist<number>::value(llint step, LR_vector<number> &pos) {
	//
	// dobbiamo ruotare pos0 di (base + rate * t) radianti
	// intorno all'asse passante per il centro.
	// e quello ci da la pos della trappola;
	//
	_compute_coms(step);
	number t = (this->_F0 + this->_rate * (number) step);

	number sintheta = sin (t);
	number costheta = cos (t);
	number olcos = ((number) 1.) - costheta;

	number xyo = this->_axis.x * this->_axis.y * olcos;
	number xzo = this->_axis.x * this->_axis.z * olcos;
	number yzo = this->_axis.y * this->_axis.z * olcos;
	number xsin = this->_axis.x * sintheta;
	number ysin = this->_axis.y * sintheta;
	number zsin = this->_axis.z * sintheta;

	LR_matrix<number> R(this->_axis.x * this->_axis.x * olcos + costheta,
						xyo - zsin,
						xzo + ysin,

						xyo + zsin,
						this->_axis.y * this->_axis.y * olcos + costheta,
						yzo - xsin,

						xzo - ysin,
						yzo + xsin,
						this->_axis.z * this->_axis.z * olcos + costheta);

	LR_vector<number> postrap = R * (_pos0 - _center) + _center;

	// we "mask" the resulting vector;
	number x = - this->_stiff * (_com.x - postrap.x) * _mask.x / _com_list.size();
	number y = - this->_stiff * (_com.y - postrap.y) * _mask.y / _com_list.size();
	number z = - this->_stiff * (_com.z - postrap.z) * _mask.z / _com_list.size();

	return LR_vector<number>(x, y, z);
}

template class COMTwist<double>;
template class COMTwist<float>;
