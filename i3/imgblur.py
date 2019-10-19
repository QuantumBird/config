import cv2
import sys

img = cv2.imread(sys.argv[1])
pmg = img
times = 10
for _ in range(times):
    pmg = cv2.GaussianBlur(pmg, ksize=(9, 9), sigmaX=0, sigmaY=0)
cv2.imwrite(sys.argv[2], pmg)

