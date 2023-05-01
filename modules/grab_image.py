import config
import modules.read_image as read_image

import os
import numpy as np
import cv2
import keyboard
import pyautogui
import time
from PIL import ImageGrab


def screen_capture(image_directory):
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Freeze the screen and convert it to grayscale
    screenshot = ImageGrab.grab()
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    
    # Show the frozen screen to the user
    cv2.namedWindow('Select Area', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Select Area', screen_width, screen_height)
    cv2.setWindowProperty('Select Area', cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow('Select Area', screenshot_gray)

    # Wait for the user to select an area
    rect = cv2.selectROI('Select Area', screenshot_gray, False)
    cv2.destroyAllWindows()

    # Extract the selected area
    cropped_screenshot = screenshot.crop((rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3]))

    # Save the screenshot
    save_screenshot(cropped_screenshot, image_directory)

def save_screenshot(cropped_screenshot, image_directory):
    file_name = "screenshot_{}.png".format(time.strftime("%Y%m%d-%H%M%S"))
    cropped_screenshot.save(os.path.join(image_directory, file_name))
    read_image.read_image(os.path.join(image_directory, file_name))

def grab_image(image_directory):
    # Wait for the hotkey combination to be pressed
    if all(keyboard.is_pressed(key) for key in config.HOTKEY_KEYS):
        screen_capture(image_directory)
        # Avoid multiple captures due to keypress delay
        time.sleep(1) 