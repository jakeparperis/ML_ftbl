from selenium_config import driver, By, EC
import time
import re

base_url = "https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/saison_id/2015/transferfenster/alle/land_id//ausrichtung//spielerposition_id//altersklasse//leihe//plus/0/galerie/0/page/1"
pagination_xpath = "//*[@id='yw0']/div[2]/ul/li[12]/a"
pagination_CSS = 'a.tm-pagination__link[title*="Go to the last page"]'
driver.get(base_url)

def scrape_pages_num():
    try:
        elem = driver.find_element(By.CSS_SELECTOR, pagination_CSS)
        title = elem.get_attribute("title")
        match = re.search(r'page (\d+)', title)
        if match:
            pages = int(match.group(1))
            print(f"Pages : {pages}")
            return pages
        else:
            return 1
    except:
        print("no pages element")
    

def iterate_seasons_pages(seasons_start, seasons_end, base_url):
    current_season = seasons_start
    url = base_url

    for i in range(seasons_start, seasons_end):
        pages = scrape_pages_num()

        for j in range(1, pages):
            print(f"Page - {j}")
            url = url.replace(f"page/{j}", f"page/{j+1}")
            driver.get(url)
        
        
        url = url.replace(f"page/{pages}", f"page/1")

        url = url.replace(f"saison_id/20{i}", f"saison_id/20{i+1}")
        driver.get(url)

iterate_seasons_pages(15, 23, base_url)

time.sleep(5)
driver.quit()