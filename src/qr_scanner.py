import cv2
from PIL import Image
import numpy as np
import zbarlight
from KBHit import KBHit
import os


def scan(cap, kb,show_preview):
    try:
        # show_preview = determine_if_show_preview()
        print('-----------------------------------------')
        print("Put your QR code to the camera at about 5 cm away")
        print("Press q to quit without scanning.")
        print()
        # if show_preview:
        #     print('DISPLAY is ', os.environ['DISPLAY'])
        #     print('will show preview in Desktop')
        while True:
            # get the image
            if cap is None:
                cap = cv2.VideoCapture(0)
            cap_successful, img = cap.read()
            if not cap_successful:
                continue
            # cap.release() # flush buffer
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
                if c == 'q':
                    print(f"\nYou pressed '{c}' for Quit.")
                    return None, None
                if c == 's':
                    print('Saving')
                    cv2.imwrite('/src/cap_s.jpg', img)
                    return None, img
    finally:
        # print('Releasing all resources')
        # kb.set_normal_term()
        # cap.release()
        # cv2.destroyAllWindows()
        # print('Bye')
        pass


if __name__ == "__main__":
    qr_code, img = scan()
    print(type(qr_code))
    print('qr_code is ', qr_code)
    # print('image', img)

