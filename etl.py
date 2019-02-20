import pymongo

import scrape_land

# initiate MongoDB databse with name `landDB`
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.landDB

# choose number of pages to scrape
pages_to_scrape = 50

for i in range(1, pages_to_scrape + 1):
    url = f'https://www.landsofamerica.com/United-States/farms/page-{i}'
    div_tops = scrape_land.get_all_land(url)
    for div_top in div_tops:
        land_info = scrape_land.scrape_land(div_top)

        db.farms.insert_one(land_info)
