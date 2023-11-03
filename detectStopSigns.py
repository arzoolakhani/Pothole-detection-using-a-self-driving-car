import cv2
import numpy as np
import argparse
import time

def meanSquareError(img1, img2):
    assert img1.shape == img2.shape, "Images must be the same shape."
    error = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    error = error / float(img1.shape[0] * img1.shape[1] * img1.shape[2])
    return error

def compareImages(img1, img2):
    return 1 / meanSquareError(img1, img2)

def pyramid(image, scale=1.5, minSize=30, maxSize=1000):
    yield image
    while True:
        w = int(image.shape[1] / scale)
        image = cv2.resize(image, (w, w))
        if image.shape[0] < minSize or image.shape[1] < minSize:
            break
        if image.shape[0] > maxSize or image.shape[1] > maxSize:
            continue
        yield image

def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[1]])




target_image = cv2.imread("StopSign1.jpg")
target_image = cv2.resize(target_image, (500, 500))
prototype_img = cv2.imread("stopPrototype.png")

max_similarity = -1
max_box = (0, 0, 0, 0)

t0 = time.time()

for p in pyramid(prototype_img, minSize=50, maxSize=target_image.shape[0]):
    for (x, y, window) in sliding_window(target_image, stepSize=2, windowSize=p.shape):
        if window.shape[0] != p.shape[0] or window.shape[1] != p.shape[1]:
            continue

        temp_similarity = compareImages(p, window)
        if temp_similarity > max_similarity:
            max_similarity = temp_similarity
            max_box = (x, y, p.shape[0], p.shape[1])

t1 = time.time()

print("Execution time: " + str(t1 - t0))
print(max_similarity)
print(max_box)

buffer_size = 5
(x, y, w, h) = max_box

cv2.rectangle(target_image, (x - buffer_size//2, y - buffer_size//2), (x + w + buffer_size//2, y + h + buffer_size//2), (0, 255, 0), 2)

cv2.imshow('image', target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
