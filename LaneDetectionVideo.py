import cv2
import numpy as np

def region_of_interest(image):
    height, width = image.shape[:2]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]], np.int32)
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def detect_lane(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 15)
    return line_image

cap = cv2.VideoCapture('test2.mp4')  # Replace with the path to your video file

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    lane_image = np.copy(frame)

    canny_result = detect_lane(lane_image)
    masked_image = region_of_interest(canny_result)
    lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    line_image = display_lines(lane_image, lines)

    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

    cv2.imshow("Lane Detection", combo_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()