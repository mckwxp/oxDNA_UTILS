.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

modify_topology
=======================================

You can download the script `here <https://github.com/mckwxp/oxDNA_UTILS/tree/master/new_scripts>`_.

Primarily used for changing sequences to poly-T in an origami and prints out the new topology file. 
Can also be used to change sequences for other parts, but set_seq scripts should be better.

Usage:

.. code:: python

   python modify_topology.py conf_file top_file virt2nuc seq_file

Args:
    - conf_file: configuration file
    - top_file: topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)
    - seq_file: file containing which base to change (details described below)

Notes:
    An example seq_file is shown below:

    T: 0-25,70-71,stap 0-6,296-297,stap 8-23,392-393,stap 24-25,232-233,stap

    This will change all the nucleotides for the specified (vh, vb, type) to T. vh and vb stands for virtual base index and virtual helix index in cadnano, and type is either stap (staple) or scaf (scaffold).
