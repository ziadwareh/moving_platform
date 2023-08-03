# A script in order to use to compute the inertia of the links in the urdf files to add them as inertia parameters
#!/usr/bin/env python3
x = float(input("insert X: "))
y = float(input("insert Y: "))
z = float(input("insert Z: "))
m = float(input("insert Mass: "))
def compute_iniertia (a,b,m):
    result = (1/12)*m*((a*a)+(b*b))
    return result
if __name__ == '__main__':
    print("Ixx: ",compute_iniertia(y,z,m))
    print("Iyy: ",compute_iniertia(x,z,m))
    print("Izz: ",compute_iniertia(y,x,m))