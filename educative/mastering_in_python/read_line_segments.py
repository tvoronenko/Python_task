# Returning ID(s) of line segments lying only in II quadrant
def filter_line_segments(lines):
    return [ID for ID, (x1, y1), (x2, y2) in lines if ((x1 != 0 or x2 != 0) and (y1 != 0 or y2 != 0) and (x1 <=0 and y1 >=0 and x2 <=0 and y2 >=0))]

line_segment = [(1, (-2, 5), (-3, -8)), (2, (8, -3), (1, 4)) ,(3, (-2, 2), (-5, 5)),(4, (-7, 3), (-1, 8))]
print (filter_line_segments(line_segment))