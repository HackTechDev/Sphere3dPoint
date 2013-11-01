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
            Point3D(0.000000, 0.000000, -2.000000),
            Point3D(-0.166587, 0.710597, -1.862069),
            Point3D(-1.012619, 0.044180, -1.724138),
            Point3D(-0.621385, -1.047773, -1.586207),
            Point3D(0.559582, -1.260700, -1.448276),
            Point3D(1.450833, -0.421997, -1.310345),
            Point3D(1.399479, 0.816643, -1.172414),
            Point3D(0.464131, 1.647552, -1.034483),
            Point3D(-0.794793, 1.601405, -0.896552),
            Point3D(-1.704637, 0.720213, -0.758621),
            Point3D(-1.820958, -0.546676, -0.620690),
            Point3D(-1.098854, -1.599833, -0.482759),
            Point3D(0.128769, -1.965836, -0.344828),
            Point3D(1.320974, -1.487354, -0.206897),
            Point3D(1.963995, -0.371438, -0.068966),
            Point3D(1.781404, 0.906557, 0.068966),
            Point3D(0.845943, 1.800437, 0.206897),
            Point3D(-0.445324, 1.919057, 0.344828),
            Point3D(-1.526717, 1.198366, 0.482759),
            Point3D(-1.900609, -0.049278, 0.620690),
            Point3D(-1.371205, -1.242695, 0.758621),
            Point3D(-0.177126, -1.778994, 0.896552),
            Point3D(1.061239, -1.342988, 1.034483),
            Point3D(1.613651, -0.146885, 1.172414),
            Point3D(1.074986, 1.061792, 1.310345),
            Point3D(-0.221743, 1.361369, 1.448276),
            Point3D(-1.152353, 0.395005, 1.586207),
            Point3D(-0.575742, -0.834188, 1.724138),
            Point3D(0.679454, -0.266535, 1.862069),
            Point3D(0.000000, 0.000000, 2.000000)
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
