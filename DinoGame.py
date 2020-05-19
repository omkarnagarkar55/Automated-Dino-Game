import pyautogui as p
from PIL import Image
import time
import pyscreenshot as ImageGrab

def hit(key):
    p.press(key)

def isCollide(data):
    for i in range(190, 210):
        for j in range(350, 445):
            if data[i, j] < 80:
                hit('down')
                return

    for i in range(210, 260):
        for j in range(465, 485):
            if data[i, j] < 100:
                hit("up")
                return

    return

if __name__=="__main__":
    time.sleep(3)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)

        for i in range(190, 210):
            for j in range(350, 445):
                data[i, j] = 77

        for i in range(210, 260):
            for j in range(465, 485):
                data[i, j] = 0

        image.show()
        break


