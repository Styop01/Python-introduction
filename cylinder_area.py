height = int(input("Write height of cylinder" ))
radius = int(input("Write radius of circle" ))
def cylinder_area(height, radius):
    import math   

    
    def circle_area(radius):
        circle = radius ** 2 * math.pi
        return circle
    print('Circle Area ---', circle_area(radius))


    def circumference(radius):
        length = 2 * radius * math.pi
        return length
    print('Circumference ---', circumference(radius))
    width = height
    length = circumference(radius)      
    

    def rectangle_area(length, width):
        rectangle = circumference(radius) * width
        return rectangle
    print('Rectangle Area ---', rectangle_area(length, width))    
    

    return print('Cylinder Area ---', rectangle_area(length, width) + 2 * circle_area(radius))
cylinder_area(height, radius)

