import matplotlib.pyplot as plt


class base_parser(object):
    def __init__(self, filetype=None):
        self.filetype = filetype
        self.points = []
        self.tris = []
        self.quads = []

    def get_filename(self):
        return self.filename

    def get_filetype(self):
        return self.filetype

    def get_points(self):
        return self.points

    def get_tris(self):
        return self.tris

    def get_quads(self):
        return self.quads

    def show_info(self):

        n_points = len(self.points)
        n_tris = len(self.tris)
        n_quads = len(self.quads)
        print('-----------------------------------')
        print('Showing info about cross-section...')
        print(f'Number of points: {n_points}')
        print(f'Number of triangles: {n_tris}')
        print(f'Number of quads: {n_quads}')

    def show_2d(self):
        # draw tri elements
        for tri in self.tris:
            x = [tri.p1.x, tri.p2.x, tri.p3.x]
            y = [tri.p1.y, tri.p2.y, tri.p3.y]
            plt.fill(x, y, facecolor='blue', edgecolor='purple', linewidth=2)
        # draw quad elements
        for quad in self.quads:
            x = [quad.p1.x, quad.p2.x, quad.p3.x, quad.p4.x]
            y = [quad.p1.y, quad.p2.y, quad.p3.y, quad.p4.y]
            plt.fill(x, y, facecolor='blue', edgecolor='purple', linewidth=2)

        plt.show()
