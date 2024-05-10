from math import pi, cos, sin

import cv2
import numpy


def draw_lines(image, x1, y1, x2, y2, line_color, line_thickness=10):
    start_point = (x1, y1)
    end_point = (x2, y2)

    # Określ kolor i grubość linii
    color = line_color
    thickness = line_thickness

    line_length = numpy.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Narysuj linię na obrazie
    cv2.line(image, start_point, end_point, color, thickness)


def draw_parking_line(image, pivot, angle_deg, length, thickness,
                      color_line):
    const = pi / 2
    radians = -angle_deg * (pi / 180)
    height = image.shape[0]
    x2 = pivot[0] + length * cos(radians + const)
    y2 = pivot[1] + length * sin(radians + const)
    draw_lines(image, int(pivot[0]), height - (pivot[1]), int(x2), height - int(y2), color_line, thickness)
