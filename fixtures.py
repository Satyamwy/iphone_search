from selenium import webdriver
# from web_driver.web import Web



def browser_chrome(context, timeout=30, **kwargs):
    browser = webdriver.Chrome(r"C:\Users\{user}\Downloads\chromedriver_win32\chromedriver.exe")
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()