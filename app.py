# -*- coding: utf-8 -*-
from selenium import webdriver
from PIL import ImageEnhance
from PIL import Image
import pytesseract

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

# 開啟網頁
driver.get("https://www.uniair.com.tw/rwd/B2C/booking/ubk_search.aspx")

# 點擊關閉cookie提醒，避免影響下面點擊輸入資料
driver.find_element_by_xpath("//*[@id='btn_ViewPolicy']/span[1]").click()

## 處理驗證碼
# 全螢幕截圖
driver.save_screenshot('C:\\tmp\\captcha.png') 

# 找到認證碼圖片位置
element = driver.find_element_by_id('c_b2c_booking_ubk_search_cph_body_logincaptcha_CaptchaImage')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']

# 開啟存放認證碼圖片檔案，並且存放裁切好的認證碼圖片
img = Image.open('C:\\tmp\\captcha.png')
img = img.crop((left, top, right, bottom))
img.save('C:\\tmp\\captcha.png', 'png')

# 設定config 針對數字0-9進行辨認
config = '--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789'

# 設定pytesseract位置
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\useraccount\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
code = pytesseract.image_to_string(
    'C:\\tmp\\captcha.png', config=config)
# 列印出辨認後數字
print(code)
