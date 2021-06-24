.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to oxDNA UTILS documentation!
=======================================

.. toctree::
   :caption: Contents:
   :hidden:
       
   Tutorial
   generate
   ligation
   modify_topology
   mutual_traps
   output_bonds
   pulling_force
   set_seq_strand
   set_seq_vh_vb

Tutorial
========
:doc:`Tutorial`

Scripts
========

+-----------------------+---------------------------------------------------+
|:doc:`generate`        | Generates oxDNA configuration and topology files. |
+-----------------------+---------------------------------------------------+
|:doc:`ligation`        | Ligates two strands in an origami.                |
+-----------------------+---------------------------------------------------+
|:doc:`modify_topology` | Changes sequences to poly-T in an origami.        |
+-----------------------+---------------------------------------------------+
|:doc:`mutual_traps`    | Makes a mutual trap external force file.          |
+-----------------------+---------------------------------------------------+
|:doc:`output_bonds`    | Prints out all interactions in the system.        |
+-----------------------+---------------------------------------------------+
|:doc:`pulling_force`   | Makes a pulling external force file.              |
+-----------------------+---------------------------------------------------+
|:doc:`set_seq_strand`  | Changes sequences of whole strands in an origami. |
+-----------------------+---------------------------------------------------+
|:doc:`set_seq_vh_vb`   | Changes sequences in an origami, e.g. sticky ends.|
+-----------------------+---------------------------------------------------+

Modules
=======
.. autosummary::
   :toctree:

   base
   generators
   origami_utils
   readers

Index
==================

:ref:`genindex`

.. * :ref:`modindex`
.. * :ref:`search`
