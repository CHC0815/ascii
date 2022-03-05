import cv2
import numpy as np


def main():
    vid = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    thickness = 1
    color = (255, 255, 255)
    width = 1000
    height = 1000
    blanc_image = np.zeros((width, height, 3), np.uint8)
    w = int(width / 10)
    h = int(height / 10)
    char_offset = 2
    offset = 0
    # density = " "*char_offset + "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/…\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    density = " "*char_offset + "Ñ@#W$9876543210?!abc;:+=-,._ "
    length = len(density)
    gray = True

    while True:
        ret, frame = vid.read()
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(grayscale, (w, h), interpolation=cv2.INTER_LINEAR)
        resized = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)

        image = blanc_image.copy()
        for i in range(h-1):
            for j in range(w-1):
                intensity = resized_gray[i][j] + offset
                char = density[int(intensity / 255 * (length-1))]
                if gray:
                    col = color
                else:
                    col = (int(resized[i][j][0]), int(resized[i][j][1]), int(resized[i][j][2]))
                cv2.putText(image, char, (10 * j, 10 * i + 10), font, font_scale, col, thickness, cv2.LINE_AA)

        cv2.imshow('ASCII', image)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()