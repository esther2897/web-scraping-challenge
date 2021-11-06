from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    new_news = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    new_news["news_title"] = soup.find("div", class_="content_title").get_text()
    new_news["news_p"] = soup.find("div", class_="article_teaser_body").get_text()
    new_news["featured_image_url"]  = (soup
    .find("div", {"class": "col-md-4"})
    .find("div", {"class": "list_image"})
    .find("img")
    .attrs['src']
    )
    # Quit the browser
    browser.quit()
    
    executable_path_two = {'executable_path': ChromeDriverManager().install()}
    browser_two = Browser('chrome', **executable_path, headless=False)
    
    url_two = "https://galaxyfacts-mars.com/"
    browser_two.visit(url_two)

    html_two = browser_two.html
    
    table = pd.read_html(html_two)[-1].to_html()
    browser.quit()

    new_news["table"] = str(table)

    hemisphere_image_urls = [{'title': 'Valles Marineris Hemisphere', 'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}, {'title': 'Cerberus Hemisphere', 'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'}, {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'}]
    new_news["images"] = hemisphere_image_urls
    return new_news

