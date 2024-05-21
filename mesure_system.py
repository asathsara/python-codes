# Functions

# In Python, you need to define the functions before you call them.
def cube_area(cube_length):
    area = round(6 * (cube_length ** 2), 2)
    print('______________\n')
    print(f'Cube length = {cube_length}\n')
    print(f'Cube surface area = {area}\n')
    print('______________\n')

def cube_volume(cube_length):
    volume = round(cube_length ** 3, 2)
    print('______________\n')
    print(f'Cube length = {cube_length}\n')
    print(f'Cube volume = {volume}\n')
    print('______________\n')

def cuboid_area(length, breadth, height):
    area = round(2 * (length * breadth + breadth * height + height * length), 2)
    print('______________\n')
    print(f'Cuboid dimensions (length, breadth, height) = ({length}, {breadth}, {height})\n')
    print(f'Cuboid surface area = {area}\n')
    print('______________\n')

def cuboid_volume(length, breadth, height):
    volume = round(length * breadth * height, 2)
    print('______________\n')
    print(f'Cuboid dimensions (length, breadth, height) = ({length}, {breadth}, {height})\n')
    print(f'Cuboid volume = {volume}\n')
    print('______________\n')

def sphere_area(radius):
    area = round(4 * 3.14159 * (radius ** 2), 2)
    print('______________\n')
    print(f'Sphere radius = {radius}\n')
    print(f'Sphere surface area = {area}\n')
    print('______________\n')

def sphere_volume(radius):
    volume = round((4/3) * 3.14159 * (radius ** 3), 2)
    print('______________\n')
    print(f'Sphere radius = {radius}\n')
    print(f'Sphere volume = {volume}\n')
    print('______________\n')

def cylinder_area(radius, height):
    area = round(2 * 3.14159 * radius * (radius + height), 2)
    print('______________\n')
    print(f'Cylinder radius = {radius}, height = {height}\n')
    print(f'Cylinder surface area = {area}\n')
    print('______________\n')

def cylinder_volume(radius, height):
    volume = round(3.14159 * (radius ** 2) * height, 2)
    print('______________\n')
    print(f'Cylinder radius = {radius}, height = {height}\n')
    print(f'Cylinder volume = {volume}\n')
    print('______________\n')

def cone_area(radius, height):
    slant_height = (radius ** 2 + height ** 2) ** 0.5
    area = round(3.14159 * radius * (radius + slant_height), 2)
    print('______________\n')
    print(f'Cone radius = {radius}, height = {height}\n')
    print(f'Cone surface area = {area}\n')
    print('______________\n')

def cone_volume(radius, height):
    volume = round((1/3) * 3.14159 * (radius ** 2) * height, 2)
    print('______________\n')
    print(f'Cone radius = {radius}, height = {height}\n')
    print(f'Cone volume = {volume}\n')
    print('______________\n')

def thank_you_message():
    print('\n............ \n')
    print('Thanks for Submitting data \n')
    print('............\n')
    # End of user inputs

print('............ \n')
print('Mesure System 2024 \n')
print('............\n')

print("1. Volume")
print("2. Area \n")

# This is code that user input their first selection. That means user selects Volume or Area
mesure_way = int(input('Enter the number for your selection:- '))

print('\n1. Cube')
print('2. Cuboid')
print('3. Sphere')
print('4. Cylinder')
print('5. Cone\n')

# Selecting shape
mesure_shape = int(input('Enter the number for your selection:- '))
print('')

# Get user input details for shapes to calculate
if mesure_shape == 1:
    cube_length = float(input('Enter length of cube: '))

    thank_you_message()

    if mesure_way == 1:
        cube_volume(cube_length)
    else:
        cube_area(cube_length)

elif mesure_shape == 2:
    cuboid_length = float(input('Enter length of cuboid: '))
    cuboid_breadth = float(input('Enter breadth of cuboid: '))
    cuboid_height = float(input('Enter height of cuboid: '))

    thank_you_message()

    if mesure_way == 1:
        cuboid_volume(cuboid_length, cuboid_breadth, cuboid_height)
    else:
        cuboid_area(cuboid_length, cuboid_breadth, cuboid_height)

elif mesure_shape == 3:
    sphere_radius = float(input('Enter radius of sphere: '))

    thank_you_message()

    if mesure_way == 1:
        sphere_volume(sphere_radius)
    else:
        sphere_area(sphere_radius)

elif mesure_shape == 4:
    cylinder_radius = float(input('Enter radius of cylinder: '))
    cylinder_height = float(input('Enter height of cylinder: '))

    thank_you_message()

    if mesure_way == 1:
        cylinder_volume(cylinder_radius, cylinder_height)
    else:
        cylinder_area(cylinder_radius, cylinder_height)

elif mesure_shape == 5:
    cone_radius = float(input('Enter radius of cone: '))
    cone_height = float(input('Enter height of cone: '))

    thank_you_message()

    if mesure_way == 1:
        cone_volume(cone_radius, cone_height)
    else:
        cone_area(cone_radius, cone_height)
