import pytest_playwright
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page #importing page class which will provide the fixtre of page in testbasic
from playwright.sync_api import *
import time
from playwright.sync_api import Playwright

@pytest.fixture
def login_page(page:Page):
    page.goto("https://rahulshettyacademy.com/LoginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio", name="Admin")
    time.sleep(3)
    page.get_by_role("combobox").select_option("Consultant")
    page.locator("#terms").check() #when giving hash, it locates the id. and check clicks the checkbox
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    
    return page

@pytest.fixture
def login_page_headed()->Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/LoginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("Learning@830$3mK2")
        page.get_by_role("radio", name="Admin")
        time.sleep(3)
        page.get_by_role("combobox").select_option("Consultant")
        page.locator("#terms").check() #when giving hash, it locates the id. and check clicks the checkbox
        page.get_by_role("link", name="terms and conditions")
        page.get_by_role("button", name="Sign In").click()
        yield page
        browser.close()
    

def test_valudationDynamicScript(login_page_headed : Page):
    screenshotPath = "D:/Personal/DevelopmentAnalysis/UdemyPlaywright/Playwright"
    iphoneproduct = login_page_headed.locator("app-card").filter(has_text="iphone X") #this goes like - go filter and find which card has the text iphone
    #filter condition is, in that component which is app-card, filter and find the card where text is iphone x.
    iphoneproduct.get_by_role("button").click()
    time.sleep(5)
    samsungProduct  = login_page_headed.locator("app-card").filter(has_text="Samsung Note 8")
    samsungProduct.get_by_role("button").click()
    
    blackberryProduct = login_page_headed.locator("app-card").filter(has_text="Blackberry")
    blackberryProduct.get_by_role("button").click()
    time.sleep(5)
    login_page_headed.get_by_text("Checkout").click()
    time.sleep(5)
    expect(login_page_headed.locator(".media-body")).to_have_count(3)
    login_page_headed.screenshot(path=screenshotPath+"/screenshot/checkout.png")
    
def test_handle_childwindow(page : Page):
    #if there is a child window, the current page object will not know about it, thus need to do it manually
    page.goto("https://rahulshettyacademy.com/LoginpagePractise/")
    
    with page.expect_popup() as newPage_info: #building a closure here in python where there is a chance a popum may trigger ie separate window or separate page. from this object retry to new page
        #this method get triggered when a new window gets opened. so it will check in everystep
        #it goes through all the steps and when it knows a new page is opened it will be captured in newPage_info automatically
        #new page items will be written in this block. once we go out, it ends there.
        page.locator(".blinkingText").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        #eliminate the left part of the text
        words = text.split("at") #0 -> Please email us , 1->mentor@rahulshettyacademy.com
        print(words[0])
        print(words[1])
        email_details = words[1].split(" ") #0-> mentor@rahulshetty.com and 1-> next text of it all. Better to strip it
        email = words[1].strip().split(" ")
        print(email_details[1])
        print(email)
        assert email_details[1] == "mentor@rahulshettyacademy.com"
        assert email == "mentor@rahulshettyacademy.com"
    
    
    