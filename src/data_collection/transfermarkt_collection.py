from selenium_config import driver, By
import time
import re

base_url = "https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/saison_id/{season}/transferfenster/alle/land_id//ausrichtung//spielerposition_id//altersklasse//leihe//plus/1/galerie/0/page/{page}"
pagination_xpath = "//*[@id='yw0']/div[2]/ul/li[12]/a"
pagination_CSS = 'a.tm-pagination__link[title*="Go to the last page"]'

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

def select_transfer_window(window):

def iterate_seasons_pages(seasons_start, seasons_end):
    for season in range(seasons_start, seasons_end + 1):
        driver.get(base_url.format(season=season, page=1))
        time.sleep(2)

        select_transfer_window("Summer transfers")
        pages = scrape_pages_num()
        for page in range(1, pages + 1):
            driver.get(base_url.format(season=season, page=page))
            time.sleep(2)

        select_transfer_window("Winter transfers")
        pages = scrape_pages_num()
        for page in range(1, pages + 1):
            driver.get(base_url.format(season=season, page=page))
            time.sleep(2)

iterate_seasons_pages(2015, 2023)

time.sleep(5)
driver.quit()