.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tutorial
=======================================
Before you use any scripts or modules, please put this line in your .bashrc file, and put in the path to your oxDNA UTILS:

.. code:: python
   export PYTHONPATH="$PYTHONPATH:/path/to/your/oxDNA/UTILS/"

Remember to do 
.. code:: python
   . ~/.bashrc

To use the scripts, simply follow the instructions given in their respective documentation pages.

To use the modules, here is an example code:

.. code:: python

   import origami_utils as oru
   import readers

   # Read the configuration file 'prova.conf' and topology file 'prova.top'
   l = readers.LorenzoReader('prova.conf', 'prova.top')

   # Get a base.System object from the reader
   s = l.get_system()

   # Initialise an Origami object from the System
   # The 'virt2nuc' file can be generated from cadnano_interface.py with a cadnano json file
   o = oru.Origami(system = s, cad2cuda_file = 'virt2nuc')

   """All code below are optional"""

   """
   If you need to know which nucleotides are interacting with which...
   Note: you don't have to run this unless you want to use class methods which require this list.
   """
   # Get a list of interactions between nucleotides
   # 'input' is a normal simulation input file, but it's only for the DNAnalysis program and it won't run a simulation
   o.get_h_bond_list('input')

   """
   If you want to get the oxDNA nucleotide index from the virtual helix and virtual base in cadnano...
   """
   vh = 1       # virtual helix index (just an example)
   vb = 2       # virtual base index (just an example)
   scaf_id = o.get_nucleotides(vh, vb, type = "scaf")   # get the scaffold nucleotide id 
   stap_id = o.get_nucleotides(vh, vb, type = "stap")   # get the staple nucleotide id
