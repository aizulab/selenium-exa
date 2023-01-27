# スクリプト例

**スクリプトの書き方**

```python
try:
    # seleniumのスクリプトを書く

except Exception as e:
    print(traceback.format_exc())
finally:
    driver.quit()
```

## 要素の取得
```python
driver.get(MAKESHOP_URL)

# idで要素を取得しテキストを入力
driver.find_element(By.NAME, "id").send_keys("LOGINID")
# XPATHで要素を取得しクリック
driver.find_element(By.XPATH, "//fieldset[@id='loginForm']/a").click()
# セレクト要素を取得しプルダウンを選択
Select(driver.find_element(By.ID, "menu_csv")).select_by_value("yamato")
```

## ブラウザに接続
```python
# ドライバーを作成
options = webdriver.ChromeOptions()
driver: WebDriver = webdriver.Remote(command_executor=SELENIUM_URL, options=options)

# ページに接続
dirver.get("https://example.com")

# windowを閉じる
driver.close()

# 接続を閉じる
driver.quit()
```

## iframeへの切り替え
```python
# 切り替え
driver.switch_to.frame(driver.find_element(By.NAME, "topframe"))

# 戻る
driver.switch_to.default_content()
```
