import requests
from bs4 import BeautifulSoup


def get_all_land(url):
    """
    Gets all of the land listings on current page of landsofamerica.com

    Arguments:
        url {string} -- webpage to be scaped from landsofamerica.com

    Returns:
        BeautifulSoup -- all listings on current page
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    div_tops = soup.body.find_all('div', class_='contentTop')

    return div_tops


def scrape_land(div_top):
    """[summary]

    Arguments:
        div_top {BeautifulSoup} -- land listing

    Returns:
        dict -- all info from land listing
    """
    rstats = div_top.find('div', class_='rstats')
    price = rstats.find('span', class_='price').text
    price = float(price.replace('$', '').replace(',', ''))
    size = rstats.find('span', class_='size').text
    size = float(size.split(' ')[0])
    address = div_top.find(itemprop='streetAddress').text
    locality = div_top.find(itemprop='addressLocality').text
    address_region = div_top.find(itemprop='addressRegion').text
    postal_code = div_top.find(itemprop='postalCode').text
    postal_code = int(postal_code)
    county = div_top.find('span', class_='county').text.split('- ')[1].strip()

    land_info = {
        'price': price,
        'acres': size,
        'address': address,
        'locality': locality,
        'address_region': address_region,
        'postal_code': postal_code,
        'county': county,
    }

    return land_info
