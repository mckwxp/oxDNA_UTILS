import sys, base, readers
import origami_utils as oru

l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])

outfile = open('eq.force','w')
outfile2 = open('dist_input','w')
outfile2.write('data_output_1 = {\n\tprint_every = 1e3\n\tname = window1.dist\n\tcol_1 = {\n\t\ttype = step\n\t}\n\tcol_2 = {\n\t\ttype = distance\n\t\tparticle_1 = ')

def write_output(vh1list, vb1list, vh2list, vb2list):
	outfile.write('{\ntype = com\n')
	
	r0 = 75
	stiff = 0.2
	rate = -5e-7
	outfile.write('stiff = %f\nr0 = %f\nrate = %e\n'%(stiff,r0,rate))
	
	outfile.write('com_list = ')
	for (ori, vh) in vh1list:
		for vb in vb1list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile.write('%d,' % scafidx)
			except: pass
	outfile.write('\n')
	
	outfile.write('ref_list = ')
	for (ori, vh) in vh2list:
		for vb in vb2list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile.write('%d,' % scafidx)
			except: pass
	outfile.write('\n')
	
	outfile.write('}\n\n')
	
	outfile.write('{\ntype = com\n')
	outfile.write('stiff = %f\nr0 = %f\nrate = %e\n'%(stiff,r0,rate))
	
	outfile.write('com_list = ')
	for (ori, vh) in vh2list:
		for vb in vb2list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile.write('%d,' % scafidx)
			except: pass
	outfile.write('\n')
	
	outfile.write('ref_list = ')
	for (ori, vh) in vh1list:
		for vb in vb1list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile.write('%d,' % scafidx)
			except: pass
	outfile.write('\n')
	
	outfile.write('}\n\n')

vh1list = [[0,i] for i in range(5,12) + range(20,27)]
vb1list = range(49,62)
vh2list = [[0,i] for i in range(5,12) + range(20,27)]
vb2list = range(259,272)

write_output(vh1list, vb1list, vh2list, vb2list)

for (ori, vh) in vh2list:
	for vb in vb2list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile2.write('%d,' % scafidx)
			except: pass
outfile2.write('\n\t\tparticle_2 = ')

for (ori, vh) in vh1list:
	for vb in vb1list:
			try:
				scafidx = o.get_nucleotides(vh,vb,type = 'scaf')[0] + ori * s._N
				outfile2.write('%d,' % scafidx)
			except: pass

outfile2.write('\n\t\tPBC = 0\n\t}')
outfile2.write('\n}')
