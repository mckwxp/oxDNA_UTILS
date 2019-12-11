/**
 * @file    COMTwist.h
 * @date    9 Dec 2019
 * @author  marco
 *
 */

#ifndef COMTWIST_H_
#define COMTWIST_H_

#include <set>
#include <string>
#include <vector>

#include "BaseForce.h"

/// Constant Torque implemented as moving traps
template<typename number>
class COMTwist : public BaseForce<number> {
private:
	llint _last_step;

	BaseBox<number> * _box_ptr;

	LR_vector<number> _com;

	std::string _com_string;

	std::set<BaseParticle<number> *> _com_list;

	void _compute_coms(llint step);
	void _check_index(int idx, int N);

public:
	LR_vector<number> _center, _pos0, _axis, _mask;
	number _rate;
	int _com_indexes[252];
	int _n_com;
	
	COMTwist ();
	virtual ~COMTwist();

	void get_settings (input_file &);
	void init (BaseParticle<number> **, int, BaseBox<number> *);

	virtual LR_vector<number> value(llint step, LR_vector<number> &pos);
	virtual number potential(llint step, LR_vector<number> &pos);
};

#endif // COMTWIST_H_
