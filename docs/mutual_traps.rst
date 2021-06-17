.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mutual_traps
=======================================

You can download the script `here <https://github.com/mckwxp/oxDNA_UTILS/tree/master/new_scripts>`_.

Used for making mutual trap external force file.

Usage:

.. code:: python

   python mutual_traps.py monomer_conf_file monomer_top_file virt2nuc polymer_conf_file polymer_top_file

Args:
    - monomer_conf_file: monomer configuration file
    - monomer_top_file: monomer topology file
    - virt2nuc: virt2nuc file (can be generated from cadnano_interface.py with a cadnano json file)
    - polymer_conf_file: polymer configuration file
    - polymer_top_file: polymer topology file

Notes:
    You can change the :code:`pairs` variable at line 20 to select the pairs to apply traps as needed.
