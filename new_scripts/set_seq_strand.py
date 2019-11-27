import sys
import origami_utils as oru
import base, readers

if len(sys.argv) != 5:
	base.Logger.die("Usage is 'python set_seq_strands.py conf top virt2nuc seq_file'")

base.Logger.log("Remember: oxDNA sequences run 3'-5' (opposite to the usual way of 5'-3')!", base.Logger.INFO)

l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])

infile = open(sys.argv[4],"r")

s.map_nucleotides_to_strands()
for line in infile:
	vh, vb, nuctype, seq = int(line.split()[0]), int(line.split()[1]), line.split()[2], line.split()[3]
	nucid = o.get_nucleotides(vh, vb, type=nuctype)[0]
	strandid = s._nucleotide_to_strand[nucid]
	s._strands[strandid].set_sequence(seq)

s.print_lorenzo_output('new_'+sys.argv[1],'new_'+sys.argv[2])
base.Logger.log("Printed output files %s %s" % ('new_'+sys.argv[1],'new_'+sys.argv[2]), base.Logger.INFO)
