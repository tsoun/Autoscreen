import pyautogui
import datetime
from time import sleep
from PIL import Image, ImageChops, ImageStat
import os

def take_screen(cpath):
    lim = 0
    os.chdir(cpath)
    npath = "Screens/" + str(datetime.datetime.today().strftime('%Y-%m-%d'))
    if not os.path.exists(npath):
        os.makedirs(npath)
        os.chdir(npath)
        i = 1
    else:
        os.chdir(npath)
        i = 10000 

    im1 = pyautogui.screenshot()
    sleep(0.5)
    im2 = pyautogui.screenshot()
    
    while True:
        sleep(1)
        try:
            im1 = im2
        except FileNotFoundError:
            i += 1
            continue
        im2 = pyautogui.screenshot()
        if i > 1:
            diff = ImageChops.difference(im1, im2)
            stat = ImageStat.Stat(diff)
            diff_ratio = sum(stat.mean) / len(stat.mean) * 255
            if diff_ratio < 700:
                print("Thrown in the garbage screen" + str(i-1) + ".jpeg due to insignificant change.")
            else:
                im2.save("screen" + str(i) + ".jpeg")
                print("Saved screen" + str(i) + ".jpeg.")
            print("Screen " + str(i) + " " + str(diff_ratio))
        i += 1
        lim += 1
        if lim == 7500:
            break

def main():
    path = os.getcwd()

    print("""

 ______     __  __     ______   ______     ______     ______     ______     ______     ______     __   __    
/\  __ \   /\ \/\ \   /\__  _\ /\  __ \   /\  ___\   /\  ___\   /\  == \   /\  ___\   /\  ___\   /\ "-.\ \   
\ \  __ \  \ \ \_\ \  \/_/\ \/ \ \ \/\ \  \ \___  \  \ \ \____  \ \  __<   \ \  __\   \ \  __\   \ \ \-.  \  
 \ \_\ \_\  \ \_____\    \ \_\  \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\\"\_\ 
  \/_/\/_/   \/_____/     \/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_____/   \/_/ \/_/ by tsoun
                                                                                                             
""")
    sleep(2)
    print("You will find the screenshots at the sudirectory .../autoscreen/Screens/. The garbage screenshots will be thrown\n*aggressively* in my virtual trash can. Have fun.")
    input("Press any key to start screenshoting...\n")
    
    for i in range(0,5):
        print("Screenshots begin in " + str(5-i) + "...")
        sleep(1)
    take_screen(path)

if __name__ == "__main__":
    main()
