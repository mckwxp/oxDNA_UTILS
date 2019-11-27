import sys
import origami_utils as oru
import base, readers

if len(sys.argv) != 5:
	base.Logger.die("Usage is 'python set_seq_vh_vb.py conf top virt2nuc seq_file'")

l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])

oldtop = open(sys.argv[2],'r').readlines()
newtop = open('new_'+sys.argv[2],'w')

infile = open(sys.argv[4],"r")

s.map_nucleotides_to_strands()
for line in infile:
	vh, vb_list, nuctype, seq = int(line.split()[0]), line.split()[1], line.split()[2], line.split()[3]
	vb_range = range(int(vb_list.split('-')[0]), int(vb_list.split('-')[1])+1)
	if len(vb_range) != len(seq):
		base.Logger.die("Sequence length is different from the given vb range. Double check your input.")
	for idx, vb in enumerate(vb_range):
		nucid = o.get_nucleotides(vh, vb, type=nuctype)[0]
		words = oldtop[idx+1].split()
		words[1] = seq[idx]
		oldtop[idx+1] = ' '.join(words)+'\n'

for line in oldtop:
	newtop.write(line)

base.Logger.log("Printed output file %s" % ('new_'+sys.argv[2]), base.Logger.INFO)
