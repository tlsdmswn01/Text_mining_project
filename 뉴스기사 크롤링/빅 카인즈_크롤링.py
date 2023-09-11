#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import pyautogui
import pyperclip #한글 입력을 하기 위해서
import cv2 # 이미지 해상도 조절
import pandas as pd


# In[10]:


get_ipython().system('pip  install openpyxl')


# In[2]:


time.sleep(4)
print(pyautogui.position()) # 마우스 위치를 알려주는
#Point(x=1188, y=301) 창 너비


# In[11]:


df=pd.read_excel('상장법인목록.xlsx')


# In[13]:


cor_list=df['회사명']


# In[5]:


def imgClick(filename,t):
    '''
    filename에 'test.png'와 같이 이미지 파일을 입력하면 클릭 하고, t초를 대기하는 함수
    '''
    imgfile= pyautogui.locateOnScreen(filename,confidence=0.9) # 내가 입력한 이미지와 같은 화면을 반환해라
    center=pyautogui.center(imgfile) # 중앙값
    pyautogui.moveTo(center)# 중간으로마우스로 이동해라
    pyautogui.click(center)
    time.sleep(t)


# In[6]:


def scroll(line):
    '''
    아래로 스크로 : -
    위로 스크롤: +
    '''
    time.sleep(0.5)
    pyautogui.scroll(line)
    time.sleep(0.5)
    
    
    


# In[14]:


keywords=['{} AND ({})'.format(i,i) for i in cor_list] #제목에 상장기업 이름이 포함된 기사들만 가져오기
date='2023-01-01'


# In[79]:


time.sleep(1)

for keyword in keywords:
    
    #1. 검색어 창을 입력해서 클릭해라
    imgClick('search_bar.png',0.2)
    pyautogui.hotkey('ctrl','a') #hotkey 단축키
    pyautogui.press('delete')
    pyperclip.copy(keyword)
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey()
    
    pyautogui.moveTo(1110, 400)
    pyautogui.click()
    time.sleep(1)

    #1. 기간 설정 입력해서 클릭해라
    pyautogui.moveTo(438, 730)
    pyautogui.click()

    pyautogui.hotkey('ctrl','a') #hotkey 단축키
    pyautogui.press('delete')
    pyperclip.copy(date)
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey()
    
    scroll(-100)
    pyautogui.moveTo(989, 790)
    pyautogui.click()
    
    #2. 스크롤을 내려서 엑셀 다운로드 버튼 누르기
    for i in range(1,5):
        scroll(-600)
    scroll(40)
    pyautogui.moveTo(577, 228)
    pyautogui.click()
    scroll(-10000)
    scroll(20)
    pyautogui.click(x=1100, y=230,interval=0.5)
    pyautogui.click(x=711, y=238,interval=0.5)

