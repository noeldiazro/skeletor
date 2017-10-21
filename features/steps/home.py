from behave import given, when, then


@when('home page is requested')
def request_home_page(context):
    context.browser.get('http://localhost:8000')


@then('page title contains "{page_title}"')
def assert_page_title_contains(context, page_title):
    context.test.assertIn('Home', context.browser.title)
