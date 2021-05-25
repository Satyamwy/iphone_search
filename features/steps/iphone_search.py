from behave import given, when, then
from behave.log_capture import capture



@given(u"the user is on the search page")
def user_on_search_page(context):
    context.web.open(r"https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=iphone&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000&otracker=categorytree")


@when(u"the user hit the url")
def user_hits_url(context):
    context.web.find_by_xpath("//*[@id="container"]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")


@then(u"fresults are found")
def results_are_displayed(context):
    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
        name=a.find('div', attrs={'class':'_4rR01T'})
        products.append(name.text) 
        
    elements = products.len
    assert len(elements) > 1
