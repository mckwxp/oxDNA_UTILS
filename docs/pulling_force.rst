.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pulling_force
=======================================

You can download the script `here <https://github.com/mckwxp/oxDNA_UTILS/tree/master/new_scripts>`_.

Used for making pulling external force file.

Usage:

.. code:: python

   python pulling_force.py conf_file top_file virt2nuc

Args:
    - conf_file: configuration file
    - top_file: topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)

Notes:
    You can change the variables in lines 63-68 to select the nucleotides to apply traps as needed.
