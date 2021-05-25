from behave import use_fixture
from fixtures import browser_chrome

def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context)