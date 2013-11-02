import sys, math, pygame

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        # Rotates the point around the X axis by the given angle in degrees. 
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        # Rotates the point around the Y axis by the given angle in degrees. 
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        # Rotates the point around the Z axis by the given angle in degrees.
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def project(self, win_width, win_height, fov, viewer_distance):
        # Transforms this 3D point to 2D using a perspective projection.
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()
 
        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Simulation of sphere 3d point rotation ")
 
        self.clock = pygame.time.Clock()
 
        self.vertices = [
            Point3D(0.0, 0.0, -2.0),
            Point3D(-0.128704656533, 0.550728457215, -1.91836734694),
            Point3D(-0.790274673388, 0.0432620492884, -1.83673469388),
            Point3D(-0.512377568264, -0.810608446701, -1.75510204082),
            Point3D(0.391988494862, -1.02266574605, -1.67346938776),
            Point3D(1.13155612234, -0.430855604661, -1.59183673469),
            Point3D(1.20110376397, 0.525959485134, -1.51020408163),
            Point3D(0.584250092602, 1.27194162711, -1.42857142857),
            Point3D(-0.377410027804, 1.42944660829, -1.34693877551),
            Point3D(-1.22808560264, 0.943825285251, -1.26530612245),
            Point3D(-1.61166511987, 0.0381137674029, -1.18367346939),
            Point3D(-1.39011590741, -0.923625358629, -1.10204081633),
            Point3D(-0.65776324442, -1.58937556752, -1.02040816327),
            Point3D(0.323445104608, -1.73611169161, -0.938775510204),
            Point3D(1.22866358657, -1.32502525013, -0.857142857143),
            Point3D(1.77634918365, -0.493120169041, -0.775510204082),
            Point3D(1.80678906019, 0.504030987314, -0.69387755102),
            Point3D(1.31714566162, 1.3748758093, -0.612244897959),
            Point3D(0.450717158503, 1.87491458168, -0.530612244898),
            Point3D(-0.550832483116, 1.86949215073, -0.448979591837),
            Point3D(-1.41640279526, 1.36339992231, -0.367346938776),
            Point3D(-1.91699525793, 0.493453673615, -0.285714285714),
            Point3D(-1.92276907278, -0.511184682855, -0.204081632653),
            Point3D(-1.43323673368, -1.38954622544, -0.122448979592),
            Point3D(-0.574949561432, -1.91514151678, -0.0408163265306),
            Point3D(0.431627401591, -1.95244252507, 0.0408163265306),
            Point3D(1.32773018452, -1.49068400559, 0.122448979592),
            Point3D(1.88132785497, -0.647268251436, 0.204081632653),
            Point3D(1.94642280993, 0.360285431166, 0.285714285714),
            Point3D(1.50244636496, 1.26795549882, 0.367346938776),
            Point3D(0.66350489215, 1.83253337874, 0.448979591837),
            Point3D(-0.34646648154, 1.89694797576, 0.530612244898),
            Point3D(-1.24892345749, 1.43713130307, 0.612244897959),
            Point3D(-1.78491702102, 0.576719318445, 0.69387755102),
            Point3D(-1.79076851392, -0.437872187868, 0.775510204082),
            Point3D(-1.25467536398, -1.3004214138, 0.857142857143),
            Point3D(-0.335108146978, -1.73389822979, 0.938775510204),
            Point3D(0.67149611853, -1.58362247494, 1.02040816327),
            Point3D(1.41435676995, -0.886059234168, 1.10204081633),
            Point3D(1.60794426184, 0.115898096128, 1.18367346939),
            Point3D(1.1548416936, 1.03215361222, 1.26530612245),
            Point3D(0.224897599792, 1.4612244881, 1.34693877551),
            Point3D(-0.760915613678, 1.17481534818, 1.42857142857),
            Point3D(-1.27975690278, 0.285492384513, 1.51020408163),
            Point3D(-0.984419002817, -0.704964564338, 1.59183673469),
            Point3D(-0.0214890090551, -1.09500613274, 1.67346938776),
            Point3D(0.828073683923, -0.483643257284, 1.75510204082),
            Point3D(0.574813313969, 0.544054517847, 1.83673469388),
            Point3D(-0.472049667393, 0.311505752295, 1.91836734694),
            Point3D(0.0, 0.0, 2.0)
        ]

        self.angleX, self.angleY, self.angleZ = 0, 0, 0
 
    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
 
            self.clock.tick(50)
            self.screen.fill((0,0,0))
 
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                x, y = int(p.x), int(p.y)
                self.screen.fill((255,255,255),(x,y,2,2))
 
            self.angleX += 1
            self.angleY += 1
            self.angleZ += 1
 
            pygame.display.flip()
 
if __name__ == "__main__":
    Simulation().run()
