import cv2
import line_drawer
import video_handler

if __name__ == '__main__':
    video_handler.frameCapture('./assets/2024-02-08_08-35-59-front.mp4')

    # image = cv2.imread('./assets/test.jpeg')
    # line_drawer.draw_lines(image, 100, 110, 150, 700, (0, 0, 255))
    # line_drawer.draw_lines(image, 150, 700, 500, 500, (0, 0, 255))

    # line_drawer.draw_parking_line(image, (0, 0), 30, 500, 10, (255, 0, 255))
    # line_drawer.draw_parking_line(image, (image.shape[1], 0), -30, 500, 10, (255, 0, 255))

    # cv2.imshow('Pic with line', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


