import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from behave import *


# "Constants"

driver = webdriver.Chrome(r"C:\Users\UTKARSH GITIKANSH\Downloads\chromedriver_win32\chromedriver.exe")
products=[] 
API = 'https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=iphone&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000&otracker=categorytree'


# Whens

@when('the API is queried with')
def step_impl(context):
    driver.get(r"https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=iphone&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000&otracker=categorytree")
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    context.response = soup

# Thens

@then('the response contains results')
def step_impl(context, phrase):
    for a in context.response.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
        name=a.find('div', attrs={'class':'_4rR01T'})
        if not name:
         products.append("NA")
        else:
         products.append(name.text)
         print(name)    
        
    assert count == products.length

