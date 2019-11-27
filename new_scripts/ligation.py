import sys
import origami_utils as oru
import base, readers

if len(sys.argv) != 5:
	base.Logger.die("Usage is 'python ligation.py conf top virt2nuc ligate_file'")

l = readers.LorenzoReader(sys.argv[1],sys.argv[2])
s = l.get_system()
o = oru.Origami(system = s, cad2cuda_file = sys.argv[3])

infile = open(sys.argv[4],"r")
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
	base.Logger.log("Ligating strand %d and strand %d" % (strandid1, strandid2), base.Logger.INFO)
	if (nucid1 != s._strands[strandid1]._last) or (nucid2 != s._strands[strandid2]._first):
		base.Logger.die("You should put the 5' nucleotide before the 3' nucleotide in ligate_file.")
	new_strand = s._strands[strandid1].append(s._strands[strandid2])
	new_strands.append(new_strand)

if len(set(ligate_list)) != len(ligate_list):
	base.Logger.die("Multiple ligations on one strand detected. This cannot be handled by the script.")

new_system = base.System(s._box)
for idx, strand in enumerate(s._strands):
	if idx not in ligate_list:
		new_system.add_strand(strand.copy(), check_overlap=False)

for new_strand in new_strands:
	new_system.add_strand(new_strand.copy(), check_overlap=False)

new_system.print_lorenzo_output('ligated.conf','ligated.top')
base.Logger.log("Printed output files ligated.conf and ligated.top", base.Logger.INFO)
