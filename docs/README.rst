======
GridPY
======

:Author: Thomas Vandeven

Overview
--------
GridPy is a python module for mapping coordinates into squares and rectangles.
A major feature is the ability to use diagonal coordinates on square grids.
Full documentation is available here.

Purpose
-------
This module is for those who need to index over a grid.
Often such sequencing is useful for classic games involving
a square grid such as chess or connect-four.

Use
---

Flat coordinates are regular array indices.
They can be converted to matrix and diagonal coordinates.

Matrix coordinates *( i, j )* denote the *i*th row and
*j* th column of the matrix. Rows are typically written
left to right and rows written top to bottom.

Diagonal coordinates for square arrays map *( a, b )* to the *a*th diagonal
and the *b* th element of that diagonal.
Diagonal lines travel up and to the right starting at the top left corner.

flat to matrix 2d
~~~~~~~~~~~~~~~~~

.. image :: ../matrix.png
    :height: 512
    :width: 512
    :alt: image missing
    :align: center
    :scale: 50

**Code Example:**

>>>[ flat_to_matrix2d(4, i) for i in range(4*4) ]

[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3),
(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]

flat to diagonal
~~~~~~~~~~~~~~~~

.. image :: ../diagonal.png
    :height: 512
    :width: 512
    :alt: image missing
    :align: center
    :scale: 50

**Code Example:**

>>>[ flat_to_diagonal(4, i) for i in range(4*4) ]

[(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1),
(3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (6, 0)]

Future updates
--------------
Future updates to this module may include flips and rotations
for matrix coordinates, and diagonal coordinates for rectangles.
