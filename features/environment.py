from selenium.webdriver import Firefox


def before_feature(context, feature):
    context.browser = Firefox()


def after_feature(context, feature):
    context.browser.quit()
