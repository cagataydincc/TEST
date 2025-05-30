import pytest
from playwright.sync_api import sync_playwright

def testlog():
  with sync_playwright() as p:
      browser = p.chromium.launch()
      page = browser.new_page()
      page.goto("https://demo.automationtesting.in/Index.html")
      print("Başarıyla giriş sağlandı.")




