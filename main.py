from gasp import *
import numpy as np

scale = 100
centerx, centery = 400, 300

points = np.array([

    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [0.5, 0.5, -0.5],
    [-0.5, 0.5, -0.5],

    [-0.5, -0.5, 0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, 0.5, 0.5]

])


def rotateX(angle):
    return np.array([[1, 0, 0],
                     [0, np.cos(angle), -np.sin(angle)],
                     [0, np.sin(angle), np.cos(angle)]
                     ])


def rotateY(angle):
    return np.array([[np.cos(angle), 0, np.sin(angle)],
                     [0, 1, 0],
                     [-np.sin(angle), 0, np.cos(angle)]
                     ])


def rotateZ(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                     [np.sin(angle), np.cos(angle), 0],
                     [0, 0, 1]
                     ])


def projection():
    return np.array([[1, 0, 0],
                     [0, 1, 0]])


def connect_points(i, j, projected_points):
    p1 = (projected_points[i][0]*scale+centerx, projected_points[i][1]*scale+centery)
    p2 = (projected_points[j][0]*scale+centerx, projected_points[j][1]*scale+centery)
    # p1 = (points[i][0], points[i][1])
    # p2 = (points[j][0], points[j][1])
    print(f"p1: {p1}\np2: {p2}")
    Line(p1, p2, color.WHITE)


def draw():
    begin_graphics(width=800, height=600, background=color.BLACK, title="Projection/Rotation")

    angle = 0

    projected_points = np.array([

        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],

        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]

    ], dtype=float)

    while angle < 20:

        print(f"---------------------------------CUBE---------------------------------")
        for i, point in enumerate(points):
            rotated = np.dot(rotateX(angle), point)
            rotated = np.dot(rotateY(angle), rotated)
            rotated = np.dot(rotateZ(angle), rotated)

            projected = np.dot(projection(), rotated)
            print(f"Projected Point {i + 1}: {projected}")

            projected_points[i] = [projected[0], projected[1]]
            

            Plot((scale * projected[0] + centerx, scale * projected[1] + centery), color.WHITE, size=3)

        connect_points(0, 1, projected_points)
        connect_points(0, 3, projected_points)
        connect_points(0, 4, projected_points)
        connect_points(1, 2, projected_points)
        connect_points(1, 5, projected_points)
        connect_points(2, 3, projected_points)
        connect_points(2, 6, projected_points)
        connect_points(3, 7, projected_points)
        connect_points(4, 5, projected_points)
        connect_points(4, 7, projected_points)
        connect_points(5, 6, projected_points)
        connect_points(6, 7, projected_points)
        
        
        


        print(projected_points)
        angle += 0.1
        clear_screen()

        time.sleep(0.05)

    end_graphics()


if __name__ == '__main__':
    try:
        draw()

    except KeyboardInterrupt:
        quit()

    except tkinter.TclError:
        quit()

    except AttributeError:
        quit()
