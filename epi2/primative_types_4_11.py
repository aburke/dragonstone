from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'width', 'height'])
Line = namedtuple('Line', ['point', 'distance'])

def get_line_intersect(line1, line2):
    line = None

    line1, line2 = sorted(line1), sorted(line2)

    p1 = max(line1[0], line2[0])
    p2 = min(line1[1], line2[1])

    if p2 >= p1:
        line = Line(p1, p2 - p1)

    return line

def get_rectangle_intersect(r1, r2):
    ri = None
    line_x = get_line_intersect((r1.x, r1.x + r1.width), (r2.x, r2.x + r2.width))
    line_y = get_line_intersect((r1.y, r1.y + r1.height), (r2.y, r2.y + r2.height))

    if line_x and line_y:
        ri = Rectangle(line_x.point, line_y.point, line_x.distance, line_y.distance)

    return ri
