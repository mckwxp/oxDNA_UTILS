.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ligation
=======================================

Ligates two strands in an origami and prints out the new configuration and topology file.

Usage:

.. code:: python

   python ligation.py conf_file top_file virt2nuc ligate_file

Args:
    - conf_file: configuration file
    - top_file: topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)
    - ligate_file: file containing which nucleotide to ligate (details described below)

Notes:
    This script works for multiple ligations in a single structure, but none of the ligations should be performed on the same strand, otherwise the script does not give correct results.

    If you want to connect the 5' end nucleotide of strand 1 to the 3' end nucleotide of strand 2, you should put the former nucleotide before the latter nucleotide in the ligate_file. Otherwise, the script will throw a warning.

    An example ligate_file is shown below:

    1 16 stap 0 39 scaf

    1 31 scaf 1 31 stap

    This ligates the staple nucleotide at (vh, vb) = (1, 16) to the scaffold nucleotide at (vh, vb) = (0, 39), as well as the scaffold nucleotide at (vh, vb) = (1, 31) to the staple nucleotide at (1, 31). 

