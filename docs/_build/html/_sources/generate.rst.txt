.. oxDNA_UTILS documentation master file, created by
   sphinx-quickstart on Fri Nov 22 08:42:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

generate
=======================================
Generates oxDNA configuration and topology files.

Usage: 

.. code:: python

   python generate.py filename box_side

Args:
    - filename: path to text file with a format described below
    - box_side: length of box side

Reads a text file with the following format:

- Each line contains the sequence for a single strand (A,C,T,G). The nucleotides can be specified by (case insensitive) letter (A, C, G, T), random (X), strong (S) and weak (W).
- Options: DOUBLE, CIRCULAR, DOUBLE CIRCULAR

Example:
    - Two ssDNA (single stranded DNA):

        ATATATA

        GCGCGCG
    - Two strands, one double stranded, the other single stranded:

        DOUBLE AGGGCT

        CCTGTA
    - One dsDNA that frays only on one side:

        DOUBLE SSXXXXXXWW
    - One dsDNA that frays very little but has TATA in the middle:

        DOUBLE SSXXXXTATAXXXXSS
    - Two strands, one double stranded circular, the other single stranded circular:

        DOUBLE CIRCULAR AGAGGTAGGAGGATTTGCTTGAGCTTCGAGAGCTTCGAGATTCGATCAGGGCT

        CIRCULAR CCTGTAAGGAGATCGGAGAGATTCGAGAGGATCTGAGAGCTTAGCT
