# features/steps/web_steps.py

from behave import then
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

@then('I should not see the text "{text}"')
def step_impl(context, text):
    assert text not in driver.page_source, f"Unexpected text '{text}' found in page source"
