import origami_utils as oru
import numpy as np
import sys, readers, base

# usage: python *.py conf top virt2nuc conf top
l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])
n = s._N
l2 = readers.LorenzoReader(sys.argv[4],sys.argv[5])
s2 = l2.get_system()
n2 = s2._N
assert n2 % n == 0
n_monomer = n2 / n
forcefile = open('pull.force','w')
eqforcefile = open('eq.force','w')
inputfile = open('data_input','w')
inputfile.write('data_output_1 = {\n\tprint_every = 1e4\n\tname = pull.dist\n\tcol_1 = {\n\t\ttype = step\n\t}\n')

pairs = [
	[vh1, vb1, vh2, vb2, k, k+1]
	for (vh1, vh2) in zip(range(28,18,-1), range(30,40))
	for (vb1, vb2) in ([127,128], [170,169])
	for k in range(n_monomer - 1)
]


for idx, item in enumerate(pairs):
	#print item[0], item[1], o.get_nucleotides(item[0],item[1],type = 'stap')
	#print item[2], item[3], o.get_nucleotides(item[2],item[3],type = 'stap')
	nuc1idx = o.get_nucleotides(item[0],item[1],type = 'scaf')[0] + n*item[4]
	nuc2idx = o.get_nucleotides(item[2],item[3],type = 'scaf')[0] + n*item[5]
	nuc1 = s2._nucleotides[nuc1idx]
	nuc2 = s2._nucleotides[nuc2idx]
	r0_vector = nuc1.distance(nuc2, box=s2._box)
	r0 = np.linalg.norm(r0_vector)
	rate = (0.6 - r0) / 1e6
	forcefile.write('{\ntype = mutual_trap\nparticle = %d\nref_particle = %d\nstiff = 1.\nr0 = %f\nrate = %.6e\n}\n\n' % (nuc1idx, nuc2idx, r0, rate))
	forcefile.write('{\ntype = mutual_trap\nparticle = %d\nref_particle = %d\nstiff = 1.\nr0 = %f\nrate = %.6e\n}\n\n' % (nuc2idx, nuc1idx, r0, rate))
	eqforcefile.write('{\ntype = mutual_trap\nparticle = %d\nref_particle = %d\nstiff = 1.\nr0 = %f\nrate = %.6e\n}\n\n' % (nuc1idx, nuc2idx, 0.6, 0.0))
	eqforcefile.write('{\ntype = mutual_trap\nparticle = %d\nref_particle = %d\nstiff = 1.\nr0 = %f\nrate = %.6e\n}\n\n' % (nuc2idx, nuc1idx, 0.6, 0.0))
	inputfile.write('\tcol_%d = {\n\t\ttype = distance\n\t\tparticle_1 = %d\n\t\tparticle_2 = %d\n\t}\n' % (idx+2, nuc1idx, nuc2idx))

inputfile.write('}\n')
