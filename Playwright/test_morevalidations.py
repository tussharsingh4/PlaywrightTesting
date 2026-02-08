import pytest_playwright
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page #importing page class which will provide the fixtre of page in testbasic
from playwright.sync_api import *
import time
from playwright.sync_api import Playwright



def test_uiChecks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, devtools=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        page.get_by_placeholder("Hide/Show Example").fill("Tere se jyada pata hai mereko")
        time.sleep(2)
        
def test_handle_Alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        #alert boxes
        #need to create event to handle the events. just like testing the window, we have to create a method to handle it
        page.on("dialog", lambda dialog:dialog.dismiss()) #this takes two argument, which has event. So giving a lambda function where if there is a dialog, it will accept it. labmda helps to create anonymous function which needs to name or triggering.
        #the above code says that when it appears, just accept it.
        page.locator("#name").fill("Tusshar kumar")
        time.sleep(3)
        page.locator("#alertbtn").click()
        time.sleep(2)
        page.locator("#confirmbtn").click()
        time.sleep(5)
        
        
def test_alert_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #alert boxes
    #need to create event to handle the events. just like testing the window, we have to create a method to handle it
    page.on("dialog", lambda dialog:dialog.accept()) #this takes two argument, which has event. So giving a lambda function where if there is a dialog, it will accept it. labmda helps to create anonymous function which needs to name or triggering.
    #the above code says that when it appears, just accept it.
    page.locator("#name").fill("Tusshar kumar")
    time.sleep(3)
    page.locator("#alertbtn").click()
    time.sleep(2)
    page.locator("#confirmbtn").click()
    time.sleep(5)


def test_handle_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe") #this is to locate the frame in the page
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")
    
def test_table_values(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #eheck the price of a particular thing from the table.
    #-identify the price columns
    #-Iterate over list
    #check which index we are getting the price
    #each columns has a ta th, so with the tagname, we can write a css
    for i in range(page.locator("th").count()): #this will iterate 3 time
        if page.locator("th").nth(i).filter(has_text="Price").count()>0: #iteraring through each header of the table. nth helps with the index
        #at 0th index, the value on th is veg, so will go to index 2
            priceColValue = i
            print(f"Index of price column value is {priceColValue}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice") #from the six locators of tr, I just applied the filter on that. capture it in rice row
    rice_price = rice_row.locator("td").nth(priceColValue) #this here will work as the locator object here will only check in the ricerow row. so in that row only the values will be checked
    expect(rice_price).to_have_text("37")

def test_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    time.sleep(2) 
    page.get_by_role("link", name="Top").click()