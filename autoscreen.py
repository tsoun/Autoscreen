import pyautogui
import datetime
from time import sleep
from PIL import Image, ImageChops, ImageStat
from pyautogui import failSafeCheck
from os import remove

def take_screen():
    i = 10000
    while True:
        sleep(1)
        pyautogui.screenshot("screen" + str(i) + ".jpeg")
        if i > 1:
            try:
                im1 = Image.open("screen" + str(i-1) + ".jpeg")
                im2 = Image.open("screen" + str(i) + ".jpeg")
            except FileNotFoundError:
                continue
            diff = ImageChops.difference(im1, im2)
            stat = ImageStat.Stat(diff)
            diff_ratio = sum(stat.mean) / len(stat.mean) * 255
            if diff_ratio < 500:
                remove("screen" + str(i-1) + ".jpeg")
            print(diff_ratio)
        i += 1
        if i == 600:
            break

def main():
    take_screen()

if __name__ == "__main__":
    sleep(5)
    main()