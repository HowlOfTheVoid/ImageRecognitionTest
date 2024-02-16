'''
Created on Sep 24, 2023

@author: EnderWolf
'''

import cv2
import numpy as np

def __main__():
    captcha_image = cv2.imread('models\\mirrorcaptcha.png', cv2.IMREAD_UNCHANGED)
    dragon_image = cv2.imread('models\\mirrorW.png', cv2.IMREAD_UNCHANGED)
    
    edited_dragon_image = cv2.resize(dragon_image, (60, 60))
    
    grey_d = cv2.cvtColor(edited_dragon_image, cv2.COLOR_BGR2GRAY)
    grey_cap = cv2.cvtColor(captcha_image, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(grey_cap, grey_d, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    print(max_loc)
    print(max_val)
    
    w = edited_dragon_image.shape[1]
    h = edited_dragon_image.shape[0]
    
    cv2.rectangle(captcha_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (255, 0, 0), 2)
    
    cv2.imshow('Result', captcha_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    __main__()