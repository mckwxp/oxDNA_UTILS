import origami_utils as oru
import base, readers

l = readers.LorenzoReader('prova.conf', 'prova.top')
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = 'virt2nuc')

oldtop = open('prova.top','r').readlines()
newtop = open('new_prova.top','w')

infile = open("seq_vh_vb","r")

s.map_nucleotides_to_strands()
for line in infile:
	vh, vb_list, nuctype, seq = int(line.split()[0]), line.split()[1], line.split()[2], line.split()[3]
	vb_range = range(int(vb_list.split('-')[0]), int(vb_list.split('-')[1])+1)
	if len(vb_range) != len(seq):
		print("sequence length is different from the given vb range")
		exit()
	for idx, vb in enumerate(vb_range):
		nucid = o.get_nucleotides(vh, vb, type=nuctype)[0]
		words = oldtop[idx+1].split()
		words[1] = seq[idx]
		oldtop[idx+1] = ' '.join(words)+'\n'

for line in oldtop:
	newtop.write(line)
