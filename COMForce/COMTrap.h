/*
 * COMTrap.h
 *
 *  Created on: 4 Dec 2019
 *      Author: marco
 */

#ifndef COMTRAP_H_
#define COMTRAP_H_

#include <set>
#include <string>
#include <vector>

#include "BaseForce.h"

/**
 * @brief A trap acting on the centre of mass of an ensemble of particles.
 *
 * @verbatim
com_list = <string> (comma-separated list containing the ids of all the particles whose centre of mass is subject to the force)
pos0 = <3 floats separated by commas> (equilibrium position of the trap)
stiff = <float> (stiffness of the trap)
rate = <float> (speed of the trap)
dir = <3 floats separated by commas> (direction of movement of the trap)
@endverbatim
 */
template<typename number>
class COMTrap : public BaseForce<number> {
protected:
	llint _last_step;

	BaseBox<number> * _box_ptr;

	LR_vector<number> _com;

	std::string _com_string;

	std::set<BaseParticle<number> *> _com_list;

	void _compute_coms(llint step);
	void _check_index(int idx, int N);

public:
	number _rate;
	int _com_indexes[252];
	int _n_com;

	COMTrap();
	virtual ~COMTrap();

	virtual void get_settings(input_file &inp);

	virtual void init(BaseParticle<number> **particles, int N, BaseBox<number> * box_side);

	virtual LR_vector<number> value(llint step, LR_vector<number> &pos);
	virtual number potential(llint step, LR_vector<number> &pos);
};

#endif /* COMTRAP_H_ */
