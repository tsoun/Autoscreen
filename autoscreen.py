from os import mkdir
import pyautogui
import datetime
from time import sleep
from PIL import Image, ImageChops, ImageStat
from pyautogui import failSafeCheck
import os

def take_screen(cpath):
    os.chdir(cpath)
    npath = "Screens/" + str(datetime.datetime.today().strftime('%Y-%m-%d'))
    if not os.path.exists(npath):
        os.mkdir(npath)
        os.chdir(npath)
        i = 1
    else:
        os.chdir(npath)
        i = len([name for name in os.listdir('.') if os.path.isfile(name)])

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
            if diff_ratio < 800:
                os.remove("screen" + str(i-1) + ".jpeg")
            print("Screen " + str(i) + " " + str(diff_ratio))
        i += 1
        if i == 600:
            break

def main():
    path = os.getcwd()
    for i in range(0,5):
        print("Screenshots begin in " + str(5-i) + "...")
        sleep(1)
    take_screen(path)

if __name__ == "__main__":
    main()