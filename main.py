import cv2
import line_drawer

if __name__ == '__main__':
    image = cv2.imread('test.jpeg')
    line_drawer.draw_lines(image, 100, 110, 150, 700, (0, 0, 255))
    line_drawer.draw_lines(image, 150, 700, 500, 500, (0, 0, 255))

    cv2.imshow('Pic with line', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

