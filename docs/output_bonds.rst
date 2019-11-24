.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

output_bonds
=======================================

Prints out all interactions in the system.

Usage:

.. code:: python

   python output_bonds.py input_file trajectory_file [confid]

Args:
    - input_file: path to input file used for simulation
    - trajectory_file: path to trajectory file generated from simulation
    - confid: configuration id in the trajectory (defaults to 0, i.e. the first configuration)

Notes:
    This script is only suitable for analysing a few configurations in a trajectory. 
    
    If you want to analyse the whole trajectory, you should use the DNAnalysis program directly.
    It can be found in the same place as the oxDNA executable.