from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'width', 'height'])
Line = namedtuple('Line', ['point', 'distance'])

def get_line_intersect(line1, line2):
    line = None

    line1, line2 = sorted(line1), sorted(line2)
    scenario1 = line1[0] <= line2[0] and line1[1] >= line2[0]
    scenario2 = line2[0] <= line1[0] and line2[1] >= line1[0]

    endpoints = [line1[1], line2[1]]

    if scenario1:
        line = Line(line2[0], min(x for x in endpoints if x >= line2[0]) - line2[0])
    elif scenario2:
        line = Line(line1[0], min(x for x in endpoints if x >= line1[0]) - line1[0])

    return line

def get_rectangle_intersect(r1, r2):
    ri = None
    line_x = get_line_intersect((r1.x, r1.x + r1.width), (r2.x, r2.x + r2.width))
    line_y = get_line_intersect((r1.y, r1.y + r1.height), (r2.y, r2.y + r2.height))

    if line_x and line_y:
        ri = Rectangle(line_x.point, line_y.point, line_x.distance, line_y.distance)

    return ri
    

if __name__ == "__main__":
    r1 = Rectangle(1, 0, 9, 7)
    r2 = Rectangle(4, 2, 2, 2)
    print('1 =>', get_rectangle_intersect(r1, r2))

    r1 = Rectangle(1, -1, 5, 4)
    r2 = Rectangle(2, 0, 8, 4)
    print('2 =>', get_rectangle_intersect(r1, r2))

    r1 = Rectangle(1, 0, 5, 4)
    r2 = Rectangle(3, 9, 4, 4)
    print('3 =>',get_rectangle_intersect(r1, r2))

    r1 = Rectangle(1, 0, 7, 4)
    r2 = Rectangle(1, 0, 4, -4)
    print('3 =>',get_rectangle_intersect(r1, r2))

    r1 = Rectangle(1, 0, 7, 4)
    r2 = Rectangle(1, 0, 7, 4)
    print('5 =>',get_rectangle_intersect(r1, r2))

    r1 = Rectangle(1, 0, 9, 6)
    r2 = Rectangle(1, 0, -8, -3)
    print('6 =>',get_rectangle_intersect(r1, r2))
