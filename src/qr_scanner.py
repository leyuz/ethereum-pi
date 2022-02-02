import cv2
from PIL import Image
import numpy as np
import zbarlight
from KBHit import KBHit
import os

def determine_if_show_preview():
    if os.environ['DISPLAY']:
        return True
    else:
        return False


def scan(cap):
    print('Inialising keyboard')
    kb = KBHit()
    print('Initializing camera')
    # cap = cv2.VideoCapture(0)
    print('Initialization done.')
    try:
        show_preview = determine_if_show_preview()

        if show_preview:
            print('DISPLAY is ', os.environ['DISPLAY'])
            print('will show preview')
        while True:
            # get the image
            _, img = cap.read()
            real_img = Image.fromarray(np.uint8(img)).convert('L')

            qr_code = zbarlight.scan_codes(['qrcode'], real_img)
            if show_preview:
                cv2.imshow("code detector", img)
                if(cv2.waitKey(1) == ord("s")):
                    cv2.imwrite('/src/cap_s_cv2.jpg', img)
                    return qr_code[0].decode('ascii'), img

            if(qr_code is not None):
                cv2.imwrite('/src/cap_qr.jpg', img)
                return qr_code[0].decode('ascii'), img
            # display the image preview

            if kb.kbhit():
                c = kb.getch()
                if ord(c) == 27:  # ESC
                    return None, None
                if c == 's':
                    print('Saving')
                    cv2.imwrite('/src/cap_s.jpg', img)
                    return None, img
                print(c)
    finally:
        # print('Releasing all resources')
        kb.set_normal_term()
        cap.release()
        cv2.destroyAllWindows()
        # print('Bye')


if __name__ == "__main__":
    qr_code, img = scan()
    print(type(qr_code))
    print('qr_code is ', qr_code)
    # print('image', img)

