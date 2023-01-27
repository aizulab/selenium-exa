import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

options = webdriver.ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントインすると画面が表示されない）
# options.add_argument("--headless")
driver: WebDriver = webdriver.Remote(
    command_executor="http://host.docker.internal:4444/wd/hub", options=options
)
driver.implicitly_wait(10)
try:
    # aizulabのお知らせページにアクセス
    driver.get("https://www.aizulab.com")

    # moreをクリック
    driver.find_element(
        By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/section[3]/div/a"
    ).click()

    # お知らせの日付の要素をxpathで取得（条件に合致するものすべて）
    news = driver.find_elements(
        By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/div[2]/div/time"
    )

    for item in news:
        # 日付の要素から相対パスを使用して本文を取得
        body = item.find_element(By.XPATH, "../div/p")
        print(item.text)
        print(body.text)

except Exception as e:
    print(traceback.format_exc())
finally:
    driver.quit()
