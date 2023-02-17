import cv2


def bcdecoder(path):
    img = cv2.imread(path)
    # img = cv2.resize(img, (300, 400))
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    bd = cv2.barcode.BarcodeDetector()
    retval, decoded_info, decoded_type, points = bd.detectAndDecode(img)
    ans = 0
    for i in decoded_info:
        if int(i) // 10**10 == 978:
            ans = i
    return ans
    # print(decoded_info)


# print(bcdecoder('IMG_4296.jpg'))
