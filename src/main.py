import cv2
from PIL import Image
import numpy as np
import zbarlight
from KBHit import KBHit
import os
import qr_scanner

cap = cv2.VideoCapture(0)

to_address, img = qr_scanner.scan(cap)
print('Scanned Address is ', to_address)