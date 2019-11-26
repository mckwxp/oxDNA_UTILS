import origami_utils as oru
import base, readers

l = readers.LorenzoReader('prova.conf', 'prova.top')
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = 'virt2nuc')

infile = open("ligate","r")
s.map_nucleotides_to_strands()
ligate_list = []
new_strands = []
for line in infile:
	vh1, vb1, nuctype1, vh2, vb2, nuctype2 = int(line.split()[0]), int(line.split()[1]), line.split()[2], int(line.split()[3]), int(line.split()[4]), line.split()[5]
	nucid1 = o.get_nucleotides(vh1, vb1, type=nuctype1)[0]
	nucid2 = o.get_nucleotides(vh2, vb2, type=nuctype2)[0]
	strandid1 = s._nucleotide_to_strand[nucid1]
	strandid2 = s._nucleotide_to_strand[nucid2]
	ligate_list.append(strandid1)
	ligate_list.append(strandid2)
	print(strandid1, strandid2)
	if (nucid1 != s._strands[strandid1]._last) or (nucid2 != s._strands[strandid2]._first):
		print("WARNING: Wrong ligation detected. Assume you know what you are doing.")
	new_strand = s._strands[strandid1].append(s._strands[strandid2])
	new_strands.append(new_strand)

new_system = base.System(s._box)
for idx, strand in enumerate(s._strands):
	if idx not in ligate_list:
		new_system.add_strand(strand.copy(), check_overlap=False)

for new_strand in new_strands:
	new_system.add_strand(new_strand.copy(), check_overlap=False)

new_system.print_lorenzo_output('ligated.conf','ligated.top')

