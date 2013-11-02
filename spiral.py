import sys, math

# Number of points
n = 100 

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
R = 2

# True radius
r = 2.0  

# ellipsoid axis lengths
r1 = 0.0
r2 = 0.0
r3 = 0.0

r = R
r1 = r2 = r3 = r

print "Point3D(0.0, 0.0, " + str(-1.0 * r3) + "),"

for k in range(2, n):
    h = -1.0 + 2.0 * ( k - 1.0 ) / ( n - 1.0 );
    
    theta = math.acos ( h )

    
    #print "k: " + str(k) + " h: " + str(h) + " n: " + str(n) + " theta: " + str(theta)    

    if theta < 0 or  theta > math.pi: 
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

    print "Point3D(" + str(r1 * x) + ", " + str(r2 * y) + ", " + str(r3 * z) + "),"   

print "Point3D(0.0, 0.0, " + str(1.0 * r3) + ")"

