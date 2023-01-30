import unittest

from src.geo_types import point, quad
from src.gmsh import gmsh_parser


class TestGMSH(unittest.TestCase):
    def test_quad_points(self):
        quad_parsed = gmsh_parser('./quad.msh')
        quad_parsed.parse()
        quad_points_real = [
            point(-1, -1, 0),
            point(1, -1, 0),
            point(1, 1, 0),
            point(-1, 1, 0),
            point(0, -1, 0),
            point(1, 0, 0),
            point(0, 1, 0),
            point(-1, 0, 0),
            point(0, 0, 0),
        ]
        quad_points_pred = quad_parsed.points
        self.assertEqual(
            len(quad_points_pred),
            len(quad_points_real),
            'Wrong number of points',
        )
        self.assertEqual(
            len(quad_points_pred),
            len(quad_points_real),
            'Problem in points',
        )

    def test_quad_elements(self):
        quad_parsed = gmsh_parser('./quad.msh')
        quad_parsed.parse()
        quad_elements_real = [
            quad(
                point(-1, -1, 0),
                point(0, -1, 1),
                point(0, 0, 0),
                point(-1, 0, 1),
            ),
            quad(
                point(-1, 1, 0),
                point(-1, 0, 0),
                point(0, 0, 0),
                point(0, 1, 0),
            ),
            quad(
                point(1, 0, 0),
                point(1, 1, 0),
                point(0, 1, 0),
                point(0, 0, 0),
            ),
            quad(
                point(0, -1, 0),
                point(1, -1, 0),
                point(1, 0, 0),
                point(0, 0, 0),
            ),
        ]
        quad_elements_pred = quad_parsed.quads
        self.assertEqual(
            len(quad_elements_pred),
            len(quad_elements_real),
            'Wrong number of elements',
        )
        self.assertEqual(
            len(quad_elements_pred),
            len(quad_elements_real),
            'Problem in elements',
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
