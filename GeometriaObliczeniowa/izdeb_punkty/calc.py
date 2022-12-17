import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y



def get_polygon(file):
    my_txt = open(file, 'r')

    all_pts = my_txt.readlines()
    x = np.empty(len(all_pts))
    y = np.empty(len(all_pts))
    for i in range(len(all_pts)):
        line = all_pts[i]
        line_splited = line.split()
        x[i] = float(line_splited[0])
        y[i] = float(line_splited[1])

    my_txt.close()
    return np.column_stack((x, y))  # x = return[:, 0], y = return[:, 1]

def get_bbox(polygon_points):
    x = polygon_points[:, 0]
    y = polygon_points[:, 1]
    x_min = min(x)
    y_min = min(y)
    x_max = max(x)
    y_max = max(y)
    return {"x_min": x_min - 1, "y_min": y_min - 1, "x_max": x_max + 1, "y_max": y_max + 1}

def in_bbox(bbox, point):
    if point.x > bbox["x_min"] and point.x < bbox["x_max"] and point.y > bbox["y_min"] and point.y < bbox["y_max"]:
        return True
    else:
        return False

# polygon - object with points
# point - object wuth x and y
def in_polygon(polygon,point):
    bbox = get_bbox(polygon_points)
    # sprawdzenie czy w bboxie
    point_in_bbox = in_bbox(bbox, point)
    if not point_in_bbox:
        return False

    s = 0
    x = polygon_points[:, 0]
    y = polygon_points[:, 1]
    # sprawdzenie czy leży na wierzchołku
    for i in range(len(polygon_points)):
        if point.x == x[i] and point.y == y[i]:
            return True

    # sprawdzenie czy w środku
    for i in range(len(polygon_points)):
        if i != len(polygon_points) - 1:
            diff = angle(point, Point(x[i], y[i]), Point(x[i+1], y[i+1]))
            s += diff

    if 359.90 < s and s < 360.1:
        return True
    else:
        return False

def check_multiple_points(polygon_points, file):
    inside = 0
    all = 0
    with open(file, 'r') as f:
        for line in f:
            if line != '\n':
                current = line.split()
                x = float(current[0])
                y = float(current[1])
                if in_polygon(polygon_points, Point(x, y)):
                    inside += 1
                all += 1

    return inside, all

def plot(polygon_points, point):
    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot()

    x = polygon_points[:, 0]
    y = polygon_points[:, 1]

    ax.plot(y, x)
    ax.scatter(point.y, point.x)
    fig.show()

'''
a = get_polygon('Wielokat.txt')
a_bbox = get_bbox(a)
print('500.44, 400.70 in polygon:', in_polygon(a, Point(500.44, 400.70)), ' - should be False')
print('450.44, 237.99 in polygon:', in_polygon(a, Point(450.44, 237.99)), ' - should be False')
print('255, 196 in polygon:', in_polygon(a, Point(350, 350)), ' - should be True')
print('255, 196 in polygon:', in_polygon(a, Point(255, 196)), ' - should be True')
print('93 120.01 in polygon:', in_polygon(a, Point(93, 120.01)), ' - should be False')
print('250, 500 in polygon:', in_polygon(a, Point(250, 500)), ' - should be False')
print('220, 230 in polygon:', in_polygon(a, Point(220, 230)), ' - should be True')
print('400, 260 in polygon:', in_polygon(a, Point(400, 260)), ' - should be True')
print('260, 286.39 in polygon:', in_polygon(a, Point(260, 286.39)), ' - should be True')
print('90 115 in polygon:', in_polygon(a, Point(90, 115)), ' - should be False')
print('400, 390 in polygon:', in_polygon(a, Point(400, 390)), ' - should be True')
print('255, 196 in polygon:', in_polygon(a, Point(255, 196)), ' - should be True')
print('261, 196 in polygon:', in_polygon(a, Point(261, 196)), ' - should be False')
print('323.98  286.39 in polygon:', in_polygon(a, Point(323.98,  286.39)), ' - should be False')
print('260.00  240.00 in polygon:', in_polygon(a, Point(260.00,  240.00)), ' - should be True')
print('400,  286.39 in polygon:', in_polygon(a, Point(400,  286.39)), ' - should be True')
print('440.00,  397.600 in polygon:', in_polygon(a, Point(440,  397.6)), ' - should be True')
print('100,  400 in polygon:', in_polygon(a, Point(100,  400)), ' - should be False')
print('200 320 in polygon:', in_polygon(a, Point(200, 320)), ' - should be True')
print('250.0 500.0 in polygon:', in_polygon(a, Point(250.0, 500.0)), ' - should be False')
print('460.0 400.0 in polygon:', in_polygon(a, Point(460.0, 400.0)), ' - should be True')
print('450.0, 300.0 in polygon:', in_polygon(a, Point(450.0, 300.0)), ' - should be False')
print('250.0, 101.0 in polygon:', in_polygon(a, Point(250.0, 100.0)), ' - should be False')
print('323.98  286.39 in polygon:', in_polygon(a, Point(323.98,  286.39)), ' - should be True')
print('260,  120 in polygon:', in_polygon(a, Point(260,  120)), ' - should be True')
print(check_multiple_points(a, 'PunktyDoKontroli.txt'))
print(check_multiple_points(a, 'PunktyDoKontroli.txt'))
'''




