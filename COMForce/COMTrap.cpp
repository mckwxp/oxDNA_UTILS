/*
 * COMTrap.cpp
 *
 *  Created on: 4 Dec 2019
 *      Author: marco
 */

#include <vector>

#include "COMTrap.h"

#include "../Utilities/Utils.h"
#include "../Utilities/oxDNAException.h"
#include "../Boxes/BaseBox.h"

using namespace std;

template<typename number>
COMTrap<number>::COMTrap() {
	_rate = 0;
	_last_step = -1;
	_box_ptr = NULL;
}

template<typename number>
COMTrap<number>::~COMTrap() {

}

template<typename number>
void COMTrap<number>::get_settings(input_file &inp) {
	getInputString(&inp, "com_list", _com_string, 1);

	double stiff;
	getInputDouble(&inp, "stiff", &stiff, 1);
	this->_stiff = stiff;

	double rate;
	getInputDouble(&inp, "rate", &rate, 0);
	_rate = rate;

	int tmpi;
	double tmpf[3];
	std::string strdir;
	getInputString (&inp, "dir", strdir, 1);
	tmpi = sscanf(strdir.c_str(), "%lf,%lf,%lf", tmpf, tmpf + 1, tmpf + 2);
	if (tmpi != 3) throw oxDNAException ("Could not parse dir %s in external forces file. Aborting", strdir.c_str());
	this->_direction = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]);
	this->_direction.normalize();

	getInputString (&inp, "pos0", strdir, 1);
	tmpi = sscanf(strdir.c_str(), "%lf,%lf,%lf", tmpf, tmpf + 1, tmpf + 2);
	if (tmpi != 3) throw oxDNAException ("Could not parse pos0 %s in external forces file. Aborting", strdir.c_str());
	this->_pos0 = LR_vector<number> ((number) tmpf[0], (number) tmpf[1], (number) tmpf[2]);
}

template<typename number>
void COMTrap<number>::_check_index(int idx, int N) {
	if(idx < 0 || idx >= N) throw oxDNAException("COMTrap: invalid id %d", idx);
}

template<typename number>
void COMTrap<number>::init(BaseParticle<number> **particles, int N, BaseBox<number> * box_ptr) {
	_box_ptr = box_ptr;

	vector<int> com_indexes = Utils::getParticlesFromString(particles, N, _com_string, "COMTrap");
	_n_com = com_indexes.size();
	for(int i = 0; i < _n_com; i++){
		_com_indexes[i] = com_indexes[i];
	}

	for(vector<int>::iterator it = com_indexes.begin(); it != com_indexes.end(); it++) {
		_check_index(*it, N);
		_com_list.insert(particles[*it]);
		particles[*it]->add_ext_force(this);
	}
	
	OX_LOG (Logger::LOG_INFO, "Adding COMTrap (stiff=%g, rate=%g, dir=%g,%g,%g, pos0=%g,%g,%g", this->_stiff, this->_rate, this->_direction.x, this->_direction.y, this->_direction.z, this->_pos0.x, this->_pos0.y, this->_pos0.z);
}

template<typename number>
void COMTrap<number>::_compute_coms(llint step) {
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
LR_vector<number> COMTrap<number>::value(llint step, LR_vector<number> &pos) {
    _compute_coms(step);
	LR_vector<number> postrap;
    number x, y, z;

    postrap.x = this->_pos0.x + (this->_rate * step) * this-> _direction.x;
    postrap.y = this->_pos0.y + (this->_rate * step) * this-> _direction.y;
    postrap.z = this->_pos0.z + (this->_rate * step) * this-> _direction.z;

    x = - this->_stiff * (_com.x - postrap.x) / _com_list.size();;
    y = - this->_stiff * (_com.y - postrap.y) / _com_list.size();;
    z = - this->_stiff * (_com.z - postrap.z) / _com_list.size();;

    return LR_vector<number>(x, y, z);
}

template<typename number>
number COMTrap<number>::potential(llint step, LR_vector<number> &pos) {
	_compute_coms(step);
	LR_vector<number> postrap;

    postrap.x = this->_pos0.x + (this->_rate * step) * this-> _direction.x;
    postrap.y = this->_pos0.y + (this->_rate * step) * this-> _direction.y;
    postrap.z = this->_pos0.z + (this->_rate * step) * this-> _direction.z;

    return (number) (0.5 * this->_stiff * (_com - postrap).norm()) / _com_list.size();
}

template class COMTrap<double>;
template class COMTrap<float>;
