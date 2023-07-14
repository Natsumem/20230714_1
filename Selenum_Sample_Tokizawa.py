from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = "C:\data\etc\chromedriver.exe"

# 検索ワードを入力する
keyword = input("検索ワードを入力してください：")

# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)
 
 # Googleアクセス
 browser.get('https://www.google.com/')

 # サイト内検索ボックスのnameをセット
 search_box = browser.find_element(By.NAME, "q")

 # 入力した検索ワードをサイト内検索に出力
 search_box.send_keys(keyword)

 # 検索実行
 search_box.send_keys(Keys.RETURN)
