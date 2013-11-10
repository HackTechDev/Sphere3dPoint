#!/usr/bin/python

import sys, math, pygame

# Generate all points of a sphere
# n = Number of points
#
# Ellipsoid axis lengths : r1, r2, r3

def generateSphere3dPoints(n, r1, r2, r3):
    
    vertices = []

    # Index
    k = 0.0
    phi1 = 0.0
    phi = 0.0
    thete = 0.0
    h = 0.0
    x = 0.0
    y = 0.0
    z = 0.0

    # Default radius
    R = 2.0

    # True radius
    r = 2.0  

    r = R

    vertices.append(Point3D(0.0, 0.0, -1.0 * r3))

    for k in range(2, n):
        h = -1.0 + 2.0 * ( k - 1.0 ) / ( n - 1.0 );
        
        theta = math.acos ( h )

        if theta < 0.0 or theta > math.pi: 
            print "Error"
            sys.exit() 

        phi = phi1 + 3.6 / ( math.sqrt ( n * ( 1 - h * h ) ) )

        phi = math.fmod ( phi, 2.0 * math.pi )

        phi1 = phi

        x = math.cos ( phi ) * math.sin ( theta )
        y = math.sin ( phi ) * math.sin ( theta )
        # z = cos ( theta ) 
        # But z==h, so:
        z = h

        vertices.append(Point3D(r1 * x, r2 * y, r3 * z))
 
    vertices.append(Point3D(0.0, 0.0, 1.0 * r3))

    return vertices

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
    
        self.numberVertice = 300 

        self.r1 = 2.0
        self.r2 = 2.0
        self.r3 = 2.0

        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)

        self.angleX, self.angleY, self.angleZ = 0, 0, 0
 
    def run(self):

        angleX = 0
        angleY = 0
        angleZ = 0

        sizePoint = 4

        font = pygame.font.Font(os.path.join('data', 'freesansbold.ttf'), 25)

        backFace = False

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:
                        sys.exit()
                    if event.key == pygame.K_a:
                        angleX = -1
                    if event.key == pygame.K_z:
                        angleX = 0
                    if event.key == pygame.K_e:
                        angleX = 1

                    elif event.key == pygame.K_q:
                        angleY = -1
                    elif event.key == pygame.K_s:
                        angleY = 0
                    elif event.key == pygame.K_d:
                        angleY = 1

                    elif event.key == pygame.K_w:
                        angleZ = -1
                    elif event.key == pygame.K_x:
                        angleZ = 0
                    elif event.key == pygame.K_c:
                        angleZ = 1

                    elif event.key == pygame.K_r:
                        self.r1 += -0.1
                        if self.r1 <= 0.1:
                            self.r1 = 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)
                    elif event.key == pygame.K_t:
                        self.r1 += 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)

                    elif event.key == pygame.K_f:
                        self.r2 += -0.1
                        if self.r2 <= 0.1:
                            self.r2 = 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)
                    elif event.key == pygame.K_g:
                        self.r2 += 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)

                    elif event.key == pygame.K_v:
                        self.r3 += -0.1
                        if self.r3 <= 0.1:
                            self.r3 = 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)
                    elif event.key == pygame.K_b:
                        self.r3 += 0.1
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)

                    elif event.key == pygame.K_DOWN:
                        self.numberVertice -= 10
                        if self.numberVertice <= 0:
                            self.numberVertice = 10
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)
                    elif event.key == pygame.K_UP:
                        self.numberVertice += 10
                        self.vertices = generateSphere3dPoints(self.numberVertice, self.r1, self.r2, self.r3)

                    elif event.key == pygame.K_n:
                        if backFace == True:
                            backFace = False
                        else:
                            backFace = True

            self.clock.tick(50)
            self.screen.fill((0, 0, 0))
 
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                x, y = int(p.x), int(p.y)

                # -0.75 is the limit behind the sphere
                if r.z < -0.75:
                    self.screen.fill((255, 0, 0), (x, y, sizePoint, sizePoint))
                else:
                    if backFace == True:
                        self.screen.fill((0, 0, 0), (x, y, sizePoint, sizePoint))
                    else:
                        self.screen.fill((255, 255, 255), (x, y, sizePoint, sizePoint))
 
            self.angleX += angleX
            self.angleY += angleY
            self.angleZ += angleZ

            sizeText = font.render("Size sphere: x=" + str(self.r1) + " y=" + str(self.r2) + " z=" + str(self.r3), True, ( 255, 0, 0))
            self.screen.blit(sizeText, [10, 10])

            rotationText = font.render("Angle rotation direction: x=" + str(angleX) + " y=" + str(angleY) + " z=" + str(angleZ), True, ( 0, 255, 0))
            self.screen.blit(rotationText, [10, 30])

            pointText = font.render("# of 3d points: " + str(self.numberVertice), True, ( 0, 0, 255))
            self.screen.blit(pointText, [10, 50])

            pygame.display.flip()
 
if __name__ == "__main__":
    Simulation().run()
