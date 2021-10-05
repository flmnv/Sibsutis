# Вариант 16
# Nв = 2, Nя = 2, Nф = 4
# Метод парзеновского окна с фиксированным h
# T – треугольное
# Файл 4

import numpy
import pandas
import custom
from custom import Plane, Point


def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def triangle_kernel(r, h):
    return max(0, 1 - r/h)


def main():
    data = custom.get_data(
        file_name="data4"
    )
    plane = Plane()

    for element in data.values:
        plane.add_point(Point(element[0], element[1]/1000, element[2]))

    plane.show(
        point_size=3,
        scr_width=600,
        scr_height=600,
        frame_size=10,
        bg_color="#FFFFFF",
        frame_color="#FFFFFF"
    )


if __name__ == "__main__":
    main()
