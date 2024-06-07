from math import pi, cos, sin

import cv2
import numpy


def draw_line_on_frame(image, x1: int, y1: int, x2: int, y2: int, thickness: int,
                       rgb: tuple[int, int, int]):

    color = (rgb[2], rgb[1], rgb[0])
    cv2.line(image, (x1, y1), (x2, y2), color, thickness)


def draw_parking_line(image, pivot: tuple[any, any], angle_deg, length, thickness: int, rgb: tuple[int, int, int]):
    const = pi/2
    radians = -angle_deg * (pi / 180)
    height = image.shape[0]
    x2 = pivot[0] + length * cos(radians + const)
    y2 = pivot[1] + length * sin(radians + const)
    draw_line_on_frame(image, int(pivot[0]), height - (pivot[1]), int(x2), height - int(y2), thickness, rgb)