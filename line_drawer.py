from math import pi, cos, sin

import cv2
import numpy


def draw_line_on_frame(image, x1: int, y1: int, x2: int, y2: int, thickness: int,
                       rgb: tuple[int, int, int]):

    color = (rgb[2], rgb[1], rgb[0])
    cv2.line(image, (x1, y1), (x2, y2), color, thickness)


def draw_parking_line(image, pivot: tuple[any, any], angle_deg, length, thickness: int, rgb: tuple[int, int, int]):
    x2, y2 = get_line_end_point(pivot, angle_deg, length)
    height = image.shape[0]
    draw_line_on_frame(image, int(pivot[0]), height - (pivot[1]), int(x2), height - int(y2), thickness, rgb)

def get_line_end_point(pivot: tuple[any, any], angle_deg, length):
    const = pi / 2
    radians = -angle_deg * (pi / 180)
    x2 = pivot[0] + length * cos(radians + const)
    y2 = pivot[1] + length * sin(radians + const)
    return x2, y2

def check_if_intersect(line_begin, line_end, box_top_left, box_bottom_right):
    (x_min, y_min), (x_max, y_max) = box_top_left, box_bottom_right
    top_b, top_e = (x_min, y_max), (x_max, y_max)
    left_b, left_e = (x_min, y_min), (x_max, y_max)
    bottom_b, bottom_e = (x_min, y_min), (x_max, y_min)
    right_b, right_e = (x_max, y_min), (x_max, y_max)

    tmp = intersect(line_begin, line_end, top_b, top_e)
    if tmp is not None:
        return True
    tmp = intersect(line_begin, line_end, left_b, left_e)
    if tmp is not None:
        return True
    tmp = intersect(line_begin, line_end, right_b, right_e)
    if tmp is not None:
        return True
    tmp = intersect(line_begin, line_end, bottom_b, bottom_e)
    if tmp is not None:
        return True

    return False


def intersect(p1, p2, p3, p4):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)