import requests
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; ResearchBot/1.0)"
}

tmarkt_url = "https://www.transfermarkt.com/"

def get_robots_txt(url):
    robots_url = urljoin(url, 'robots.txt')
    response = requests.get(robots_url, headers=headers)
    if response.status_code == 200:
        print(url)
        print()
        print(response.text)
        print()
    elif response.status_code == 403:
        print(url + ' - failed to fetch data - ' + str(response.status_code))
    else:
        print(url + ' - unexpected status code - ' + str(response.status_code))

get_robots_txt(tmarkt_url)
