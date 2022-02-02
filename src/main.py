import os
from datetime import datetime

import cv2
from PIL import Image
import numpy as np
import zbarlight
from KBHit import KBHit

import qr_scanner
import wallet

def release_resources(cap,kb):
    print("Releasing resources...",end='')
    kb.set_normal_term()
    if not cap is None:
        cap.release()
    cv2.destroyAllWindows()
    print(" Done.\nBye")
def determine_if_show_preview():
    if os.environ['DISPLAY']:
        print("It seems you are using a monitor / in VNC mode.")
        return True
    else:
        print("It seems you are running in headless mode.")
        return False

def main():
    print('Initializing camera')
    cap = cv2.VideoCapture(0)
    print('Inialising keyboard')
    kb = KBHit()
    show_preview = determine_if_show_preview()
    print()
     # infinite loop
    while True:
        to_address, img = qr_scanner.scan(cap,kb,show_preview)
        if to_address is None:
            release_resources(cap,kb)
            return
        print('Yes! Successfully scanned an address: ', to_address)

        # now we have an adress, enter another infi loop for user to confirm
        
        now = datetime.now()
        send_amt_in_eth = float(f"0.0000{now.hour:02d}{now.minute:02d}")
        print(f'Now it is UTC time {now}.')
        print(f'Do you want to send some Ether: {send_amt_in_eth:.8f} eth to the address above? [Yes/No/Quit]')
        while True:
            if kb.kbhit():
                c = kb.getch()
                if c=='y' or c=='Y':
                    print(f"\nYou pressed '{c}' for Yes. Preparing to send...")
                    wallet.send_ether(to_address,send_amt_in_eth)
                    cap = None
                    break
                elif c=='N' or c=='n':
                    print(f"\nYou pressed '{c}' for No. OK. Let's scan again.")
                    cap = None
                    break
                elif c=='Q' or c=='q':
                    print(f"\nYou pressed '{c}' for Quit.")
                    release_resources(cap,kb)
                    return
                    break
                
    release_resources(cap,kb)

if __name__ == "__main__":
    main()