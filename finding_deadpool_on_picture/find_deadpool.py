from PIL import Image
import cv2
import numpy as np

picture = "One_img4.png"

deadpool = cv2.imread("wynik.png")
deadpool = cv2.cvtColor(deadpool, cv2.COLOR_BGR2HSV)
image = cv2.imread(picture)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
for ch, col in enumerate(color):
    histdeadpool = cv2.calcHist([deadpool], [ch], None, [256], [0, 255])
    histimage = cv2.calcHist([image], [ch], None, [256], [0, 255])
    cv2.normalize(histdeadpool, histdeadpool, 0, 255, cv2.NORM_MINMAX)
    cv2.normalize(histimage, histimage, 0, 255, cv2.NORM_MINMAX)
    best = cv2.compareHist(histdeadpool, histimage, cv2.HISTCMP_CORREL)

print(best)

heightImage = np.size(image, 0)
widthImage = np.size(image, 1)
heightDeadpool = np.size(deadpool, 0)
widthDeadpool = np.size(deadpool, 1)

#print(widthDeadpool, heightDeadpool)

for i in range(0, widthImage - widthDeadpool, 5):
    for j in range(0, heightImage - heightDeadpool, 5):
        box = (i, j, i + widthDeadpool, j + heightDeadpool)
        image_cropped = image[j:j + widthDeadpool, i:i + heightDeadpool]
        for ch, col in enumerate(color):
            histcropped = cv2.calcHist([image_cropped], [ch], None, [256], [0, 255])
        new = cv2.compareHist(histcropped, histdeadpool, cv2.HISTCMP_CORREL)
        # print(new)
        if new > best:
            best = new
            ibest = i
            jbest = j

print(best)
#print(ibest)
#print(jbest)

image = Image.open(picture)
bestbox = (ibest, jbest, ibest + widthDeadpool, jbest + heightDeadpool)
#print(bestbox)
image = image.crop(bestbox)
image.show()
