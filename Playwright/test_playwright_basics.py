#fixtures are something to seupt and recieve data
import pytest_playwright
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page #importing page class which will provide the fixtre of page in testbasic
from playwright.sync_api import *
import time
from playwright.sync_api import Playwright


def test_playwrightBasics(page): #playwright is a fixture name. global fixture
   page.goto("https://www.google.com/")


def test_coreLocators(playwright):
   browser = playwright.chromium.launch(headless=False)
   page = browser.new_page()
   page.goto("https://rahulshettyacademy.com/LoginpagePractise/")
   page.get_by_label("Username:").fill("rahulshettyacademy")
   page.get_by_label("Password:").fill("Learning@830$3mK2")
   page.get_by_role("radio", name="Admin")
   time.sleep(3)
   page.get_by_role("combobox").select_option("Consultant")
   page.locator("#terms").check() #when giving hash, it locates the id. and check clicks the checkbox
   page.get_by_role("link", name="terms and conditions")
   page.get_by_role("button", name="Sign In").click() #we can add additional attributes in get by role method
   time.sleep(5)
   
def test_wrong_credentials(playwright : Playwright):
   browser = playwright.chromium.launch(headless=False)
   page = browser.new_page()
   page.goto("https://rahulshettyacademy.com/LoginpagePractise/")
   page.get_by_label("Username:").fill("rahulshettyacademy")
   page.get_by_label("Password:").fill("notlearn@830$3mK2")
   page.get_by_role("radio", name="Admin")
   time.sleep(3)
   page.get_by_role("combobox").select_option("Consultant")
   page.locator("#terms").check() #when giving hash, it locates the id. and check clicks the checkbox
   page.get_by_role("link", name="terms and conditions")
   page.get_by_role("button", name="Sign In").click() #we can add additional attributes in get by role method
   expect(page.get_by_text("Incorrect  username/password.")).to_be_visible() #expecting the component to be visible. PLaywright applies auto wait.
   

   
   
   
   
   
   
    

    