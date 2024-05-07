import cv2


def draw_lines(image, x1, y1, x2, y2, line_color, line_thickness=10):
    start_point = (x1, y1)
    end_point = (x2, y2)

    # Określ kolor i grubość linii
    color = line_color
    thickness = line_thickness

    # Narysuj linię na obrazie
    cv2.line(image, start_point, end_point, color, thickness)

