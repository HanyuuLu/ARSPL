import hyperlpr
import cv2.cv2 as cv2


def recognition(img):
    try:
        res = []
        rawres = hyperlpr.HyperLPR_plate_recognition(img)
        for i in rawres:
            if (i[1] > 0.8):
                res.append(i[0])
        return res
    except Exception as e:
        print(e)
