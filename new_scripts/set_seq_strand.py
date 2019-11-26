import origami_utils as oru
import base, readers

l = readers.LorenzoReader('prova.conf', 'prova.top')
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = 'virt2nuc')

infile = open("seq_strand","r")

s.map_nucleotides_to_strands()
for line in infile:
	vh, vb, nuctype, seq = int(line.split()[0]), int(line.split()[1]), line.split()[2], line.split()[3]
	nucid = o.get_nucleotides(vh, vb, type=nuctype)[0]
	strandid = s._nucleotide_to_strand[nucid]
	s._strands[strandid].set_sequence(seq)
s.print_lorenzo_output('new.conf','new.top')
