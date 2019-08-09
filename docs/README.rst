GridPY
======

GridPy is a python module for mapping coordinates into squares and rectangles.
A major feature is the ability to use diagonal coordinates on square grids

Purpose
-------

This module is for those who need to index over a grid. 
Often such sequencing is useful for classic games involving 
a square grid such as chess or connect-four.

Use
---

Flat coordinates are array indices.
They can be converted to matrix and diagonal coordinates.
Matrix coordinates :math: `$(i,j)$` denote the :math: `$i$` th row and 
:math: `j` th column of the matrix

flat to matrix
--------------

.. image :: ../matrix.png
    :height: 512
    :width: 512
    :alt: image missing
    :align: center
    :scale: 50

flat to diagonal
----------------

.. image :: ../diagonal.png
    :height: 512
    :width: 512
    :alt: image missing
    :align: center
    :scale: 50

Future updates
--------------

Future updates to this module may include flips and rotations 
for matrix coordinates, and diagonal coordinates for rectangles.