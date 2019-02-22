import pandas as pd
import numpy as np

#-----Column descriptions---------
# POPPT - population of zip in specific county
# ZPOP - zip code population
# ZHU - zip housing unit count 
# HUPT - housing unit count of zip in specific county
# ZOPOPPCT - percent of total zip pop for portion of zip in that county 
# COPOP - population in that county
# COPOPPCT - percept of total county pop wihtin that zip code
# ZAREA - area of zipcode
# ZAREALAND - land area of zipcode
# COHU - county housing units
# COAREA - area of county
# COAREALAND - land area of county


df = pd.read_csv('https://query.data.world/s/d4svu353zh227c66s7tix7gav44gkz')

#Pass zipcode and dataframe to return list of dictionaries of info for particular zipcode
def getZipCounty(zipcode,the_df):
    
    the_df.rename(columns={'ZCTA5':'Zipcode'}, inplace=True)

    the_df.set_index("Zipcode")

    dict_list = []
    zip_data = the_df.loc[zipcode]
    
    for row_index,row in zip_data.iterrows():
        
        dict_list.append(dict(row))
    
    return dict_list
    
