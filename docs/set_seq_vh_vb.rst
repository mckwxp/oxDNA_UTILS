.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

set_seq_vh_vb
=======================================

Used for changing sequences in an origami, particularly making sticky ends, and prints out the new topology file. 

Usage:

.. code:: python

   python set_seq_vh_vb.py conf_file top_file virt2nuc seq_file

Args:
    - conf_file: configuration file
    - top_file: topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)
    - seq_file: file containing which base to change (details described below)

Notes:
    An example seq_file is shown below:

    0 16-23 stap ATCGATCG

    This will change the sequence for the specified (vh, vb, type) to ATCGATCG.