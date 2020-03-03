#!/usr/bin/env python
# coding: utf-8

import os
from io import BytesIO
from time import sleep
import pandas as pd
import win32clipboard
import win32com.client as win32
from PIL import Image # !pip install Pillow
from openpyxl import Workbook

def 클립보드로_이미지_복사하기(i):
    filepath = rf"G:\python_work\excel2hwp-master\imgs\{i}.png"
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:] # png 헤더부분 14글자까지
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# 엑셀파일 불러오기
excel = pd.read_excel("환경정보.xlsx")
print(excel.head())

# 엑셀 레코드 개수 확인하기
print('엑셀레코드 개수: ',len(excel))

# 한글 빈문서를 배경으로 불러오기
hwp= win32.Dispatch("HWPFrame.HwpObject")

# 한글 자동보안승인 요청
hwp.RegisterModule("FilePathCheckDLL","SecurityModule")

# 한글 파일 불러오기
# 한글파일을 불러올때는 절대경로로 불러와야 오류가 나오지 않는다
hwp.Open(r"G:\python_work\excel2hwp-master\환경정보리포팅.hwp", None, None)

# 한글파일에 누름틀 입력 기능으로 생성된 필드목록을 가져오기
# hwp.GetFieldList(0, None)
# 결과: 'site_no\x02id\x02x\x02y\x02dem\x02slope\x02aspect\x02forest\x02googlemap_id'

hwp.GetFieldList(1, None)
# 결과: 'site_no{{0}}\x02id{{0}}\x02x{{0}}\x02y{{0}}\x02dem{{0}}\x02slope{{0}}\x02aspect{{0}}\x02forest{{0}}\x02googlemap_id{{0}}'

# 위 결과에서 \x02를 기준으로 필드리스트를 가져오기
field_list =[i for i in hwp.GetFieldList(0, None).split("\02")]

#필드리스트 확인
field_list
# 결과: ['site_no', 'id', 'x', 'y', 'dem', 'slope', 'aspect', 'forest', 'googlemap_id']
# 엑셀의 필드목록과 일치한다.


# 한글 전체를 선택하기
hwp.Run("SelectAll")

# 선택한 내용을 복사하기
hwp.Run("Copy")

# 커서를 마지막 페이지로 이동
# hwp.MovePos(3, None, None) 


# 엑셀 레코드 개수만큼 복사한 한글내용을 붙여넣기
for i in range(len(excel)):
    hwp.Run("Paste")
    #hwp.MovePos(3, None, None)

hwp.MovePos(0, None, None)

#엑셀 레코드 개수마다 필드리스트에서 해당하는 필드의 내용에 맞게 한글 누름틀의 필드 값으로 입력하기
for page in range(len(excel)):
        for field in field_list:
                if(field != "googlemap_id"):
                        hwp.PutFieldText(f"{field}{{{{{page}}}}}", excel[field].iloc[page])

                elif(page == 0):   

                        클립보드로_이미지_복사하기(excel[field].iloc[page][-1])
                        hwp.Run("MoveRight")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("Paste")
                        sleep(0.1)
                else:
                        클립보드로_이미지_복사하기(excel[field].iloc[page][-1])
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("MoveDown")
                        hwp.Run("Paste")
                        sleep(0.1)

        
# 처리한 결과를 다른이름으로 한글파일 저장
hwp.SaveAs(r"G:\python_work\excel2hwp-master\result1.hwp", "HWP", "HWP")

# 한글 API 종료후 메모리 해제하기
hwp.Quit()
hwp=None


# 최종결과 불러오기
# 한글 빈문서를 배경으로 불러오기
#hwp= win32.Dispatch("HWPFrame.HwpObject")
# 한글 자동보안승인 요청
#hwp.RegisterModule("FilePathCheckDLL","SecurityModule")
# 불러오기
#hwp.Open(r"C:\ecosdm\hwp_work\results.hwp", "HWP", "HWP")
