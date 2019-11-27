.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

set_seq_strand
=======================================

Used for changing sequences of whole strands in an origami and prints out the new topology file. 

Remember: oxDNA sequences run 3'-5' (opposite to the usual way of 5'-3')!

Usage:

.. code:: python

   python set_seq_strand.py conf_file top_file virt2nuc seq_file

Args:
    - conf_file: configuration file
    - top_file: topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)
    - seq_file: file containing strand sequences (details described below)

Notes:
    An example seq_file is shown below:

    0 16 stap AAAAAAAAAAAAAAAA

    This will change the sequence for the strand containing the specified nucleotide at (vh, vb, type) to AAAAAAAAAAAAAAAA.
