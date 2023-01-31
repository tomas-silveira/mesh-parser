import numpy as np

from .baseparser import base_parser
from .geo_types import point, quad, tri

TRI = 2
QUAD = 3


class gmsh_parser(base_parser):
    def __init__(self, filename):
        """GMSH parser

        Implementation of a parser for GMSH .msh files
        NOTE: .msh files must be version>=4

        Args:
            filename (string): name of gmsh .msh file
        """
        self.filename = filename
        super().__init__('gmsh')

    def _process_line(self, line):
        line = line.replace('\n', '')
        items = line.split(' ')
        return items

    def _parse_nodes(self, lines):
        # Start Nodes
        n = 0
        while n < len(lines):
            items = self._process_line(lines[n])
            if len(items) == 3:
                # Add nodes
                x = np.float64(items[0])
                y = np.float64(items[1])
                z = np.float64(items[2])
                self.points.append(point(x, y, z))

            # End Nodes
            if len(items) == 1 and items[0] == '$EndNodes':
                n = len(lines)

            n += 1

    def _parse_elements(self, lines):
        # Start Elements
        n = 2
        while n < len(lines):
            items = self._process_line(lines[n])
            if len(items) == 1 and items[0] == '$EndElements':
                # End Elements
                n = len(lines)
            else:
                # Add elements
                elem_type = int(items[2])
                ini_ix = n + 1
                end_ix = (
                    n + 1 + int(items[3])
                )   # item[3] refers to the curr #elements
                for line in lines[ini_ix:end_ix]:
                    items = self._process_line(line)
                    if elem_type == TRI:
                        e1 = self.points[int(items[1]) - 1]
                        e2 = self.points[int(items[2]) - 1]
                        e3 = self.points[int(items[3]) - 1]
                        self.tris.append(tri(e1, e2, e3))
                    if elem_type == QUAD:
                        e1 = self.points[int(items[1]) - 1]
                        e2 = self.points[int(items[2]) - 1]
                        e3 = self.points[int(items[3]) - 1]
                        e4 = self.points[int(items[4]) - 1]
                        self.quads.append(quad(e1, e2, e3, e4))

                n = end_ix

    def parse(self):

        mesh_file = open(self.filename, 'r')
        lines = mesh_file.readlines()
        n = 0
        while n < len(lines):
            items = self._process_line(lines[n])
            if len(items) == 1 and items[0] == '$Nodes':
                self._parse_nodes(lines[n:])
            elif len(items) == 1 and items[0] == '$Elements':
                self._parse_elements(lines[n:])

            n += 1

        mesh_file.close()
