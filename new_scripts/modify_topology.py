import sys
import origami_utils as oru
import base, readers

if len(sys.argv) != 5:
	base.Logger.die("Usage is 'python modify_topology.py conf top virt2nuc seq_file'")

l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])
n_nuc = s._N
modify = [[],[],[],[]]
basedict = {'A':0, 'G':1, 'C':2, 'T':3}
infile = open(sys.argv[4],'r')

for line in infile:
	base_id = basedict[line.split(':')[0]]
	need_modify = line.split(':')[1].split()
	for item in need_modify:
		vhs = item.split(',')[0]
		vhstart = int(vhs.split('-')[0])
		vhend = int(vhs.split('-')[1])
		vhlist = range(vhstart,vhend+1)

		vbs = item.split(',')[1]
		vbstart = int(vbs.split('-')[0])
		vbend = int(vbs.split('-')[1])
		vblist = range(vbstart,vbend+1)

		base_type = item.split(',')[2]		# 'scaf' or 'stap'

		for vh in vhlist:
			for vb in vblist:
				nucidx = o.get_nucleotides(vh,vb,type = base_type)[0]
				print vh,vb
				modify[base_id].append(nucidx)

oldtop = open(sys.argv[2],'r').readlines()
newtop = open('new_'+sys.argv[2],'w')
newtop.write(oldtop[0])

for i in range(n_nuc):
	if i in modify[0]:
		words = oldtop[i+1].split()
		words[1] = 'A'
		newtop.write(' '.join(words)+'\n')

	elif i in modify[1]:
		words = oldtop[i+1].split()
		words[1] = 'G'
		newtop.write(' '.join(words)+'\n')

	elif i in modify[2]:
		words = oldtop[i+1].split()
		words[1] = 'C'
		newtop.write(' '.join(words)+'\n')

	elif i in modify[3]:
		words = oldtop[i+1].split()
		words[1] = 'T'
		newtop.write(' '.join(words)+'\n')

	else:
		newtop.write(oldtop[i+1])

base.Logger.log("Printed output file %s" % ('new_'+sys.argv[2]), base.Logger.INFO)
