from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Initialization of variables

driver = webdriver.Chrome(r"C:\Users\{user}\Downloads\chromedriver_win32\chromedriver.exe")
products=[] 
prices=[] 
ratings=[] 



# Getting the url

driver.get(r"https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=iphone&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000&otracker=categorytree")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')




# Extraction and saving

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    
    
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('span', attrs={'class':'_2_R_DZ'})
    
    
    if not name:
        products.append("NA")
    else:
        products.append(name.text)    

    if not price:
        price.append("NA")
    else:
        prices.append(price.text)                
    
    if not rating:
        ratings.append("NA")
    else:
        ratings.append(rating.text)    
   
   
   
# Csv formation

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')