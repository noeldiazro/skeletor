from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://localhost:8000')
assert 'Django' in browser.title

browser.quit()
