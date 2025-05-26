import cv2
import numpy as np
img = cv2.imread("frutas.jpg")
kernel = np.ones((7, 7), np.uint8)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def leer(archivo):
    dicty = {}
    with open(archivo, "r") as f:
        for linea in f:
            clave, valor = linea.strip().split(":")  # (hsv, 45)
            dicty[clave.strip()] = int(valor.strip())
    return dicty


valores = leer("datos.txt")
while True:

    lower = np.array([valores["hmin"], valores["smin"], valores["vmin"]])
    upper = np.array([valores["hmax"], valores["smax"], valores["vmax"]])
    mask = cv2.inRange(hsv, lower, upper)
    dilatacion = cv2.dilate(mask, kernel, iterations=6)
    erode = cv2.erode(dilatacion, kernel, iterations=6)
    img2 = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    img3 = cv2.bitwise_and(img, img2, mask=erode)
    x, y, w, h = cv2.boundingRect(erode)
    # si quieres el centro pone x+(round(w/2))
    cv2.rectangle(img3, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("w", erode)
    cv2.imshow("ww", img3)
    k = cv2.waitKey(1)

    if k == ord('g'):
        break
cv2.destroyAllWindows()
