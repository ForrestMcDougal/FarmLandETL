from census import Census

from config import api_key

c = Census(api_key, year=2017)

def census(zipcode):

    census_data = c.acs5.get(("NAME", 
                          "B19013_001E", 
                          "B01003_001E", 
                          "B01002_001E",
                          "B01002_002E",
                          "B01002_003E",
                          "B19301_001E",
                          "B17001_002E"), {'for': (f'zip code tabulation area: {zipcode}')})

    return census_data