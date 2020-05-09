import hyperlpr
import cv2.cv2 as cv2
# image = cv2.imread("demo.jpg")
# print("processing")
# res = hyperlpr.HyperLPR_plate_recognition(image)
# print(res)
# print("finish")


def recognition(img):
    try:
        res = []
        rawres = hyperlpr.HyperLPR_plate_recognition(img)
        for i in rawres:
            if (i[1] > 0.5):
                res.append(i[0])
        return res
    except Exception as e:
        print(e)


# print(recognition(image))
