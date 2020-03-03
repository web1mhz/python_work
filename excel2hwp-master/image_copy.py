import os
from io import BytesIO
from time import sleep

import pandas as pd

import win32clipboard
import win32com.client as win32
from PIL import Image # !pip install Pillow
from openpyxl import Workbook


def 클립보드로_이미지_복사하기(i):
    filepath = rf"C:\ecosdm\hwp_work\imgs\{i}.png"
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:] # png 헤더부분 14글자까지
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

spec = pd.read_excel("환경정보.xlsx")
print(spec.head())

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.RegisterModule("FilePathCheckDLL","SecurityModule")

hwp.Open(r"C:\ecosdm\hwp_work\image_copy.hwp", None, None)

for i in range(len(spec)):
    클립보드로_이미지_복사하기(i)
    hwp.Run("Paste")
    sleep(0.1)

    if i % 2 == 0:
        hwp.Run("TableAppendRow")        
    else:
        # hwp.Run("MoveDown")
        pass

    hwp.Run("TableRightCellAppend")

    if i % 2 == 0:
        hwp.Run("MoveUp")






# hwp.Quit()
# hwp=None
