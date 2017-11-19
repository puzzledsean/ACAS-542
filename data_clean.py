# import
# keep columns that are relevant

import pandas as pd
import numpy as np

usecols=['time','icao24','lat','lon','velocity','heading','vertrate','onground','alert','baroaltitude','lastposupdate','lastcontact']
df = pd.read_csv('states_2017-08-28-00.csv/states_2017-08-28-00.csv', usecols=usecols)
df = df.sort_values(['icao24','time'])

import math
import geopy
import geopy.distance

def compute_distance(point_1, point_2):
    '''    
    Parameters:
        - point_1 -> list in order of [lat,long, alt]
        - point_2 -> list in order of [lat,long, alt]
        
    Returns:
        Distance between two points in km using geopy
    '''    
    p1 = geopy.point.Point(point_1)
    p2 = geopy.point.Point(point_2)

    return geopy.distance.vincenty(p1, p2).km


# generating NMAC data
def gen_NMAC():
    # get rows that were in an NMAC
    NMAC_icao = df[df['alert'] == True]
    # get rows that were in an NMAC and have readily available data (i.e. remove rows with NaN for lat long etc)
    cleaned_NMAC_icao = NMAC_icao.dropna()
    unique_NMAC_icao = cleaned_NMAC_icao.icao24.unique()
    

    print('There are {} unique potential NMAC icao planes'.format(len(unique_NMAC_icao)))
    count = 0
    
    # ultimate final NMAC csv dataframe
    df_final = pd.DataFrame()
 
    NMAC_id = 0
    # for each unique icao
    for name in unique_NMAC_icao:
        # print stats
        print('Iterated through {} icao planes so far...'.format(count))
        count += 1
        # get rows where icao == name (boolean vector)
        selector = cleaned_NMAC_icao['icao24'] == name
        current_icao = cleaned_NMAC_icao[selector]

        second_counter = 0
        for second_name in unique_NMAC_icao:
            #if count == 3:
            #    print('second counter {}'.format(second_counter))
            #    second_counter += 1
            second_selector = cleaned_NMAC_icao['icao24'] == second_name
            second_icao = cleaned_NMAC_icao[second_selector]

            if name == second_name:
                continue

            incremented_NMAC_id = False
            for index, row in current_icao.iterrows():
                for index2, row2 in second_icao.iterrows():
                    lat_1 = row['lat']
                    lon_1 = row['lon']
                    alt_1 = row['baroaltitude']

                    lat_2 = row2['lat']
                    lon_2 = row2['lon']
                    alt_2 = row2['baroaltitude']

                    point_1 = [lat_1, lon_1, alt_1]
                    point_2 = [lat_2, lon_2, alt_2]

                    dist = compute_distance(point_1, point_2)

                    if dist < 200 and row['time'] == row2['time']:
                        if not incremented_NMAC_id:
                            NMAC_id += 1
                            incremented_NMAC_id = True
                        
                        NMAC_row = pd.DataFrame({
                            'NMAC_id': [NMAC_id],
                            'time_1': [row['time']], #first plane
                            'icao24_1':[row['icao24']],
                            'lat_1':[row['lat']],
                            'lon_1':[row['lon']],
                            'velocity_1':[row['velocity']],
                            'heading_1':[row['heading']],
                            'vertrate_1':[row['vertrate']],
                            'onground_1':[row['onground']],
                            'alert_1':[row['alert']],
                            'baroaltitude_1':[row['baroaltitude']],
                            'lastposupdate_1':[row['lastposupdate']],
                            'lastcontact_1':[row['lastcontact']],
                            'time_2': [row2['time']], #second plane
                            'icao24_2':[row2['icao24']],
                            'lat_2':[row2['lat']],
                            'lon_2':[row2['lon']],
                            'velocity_2':[row2['velocity']],
                            'heading_2':[row2['heading']],
                            'vertrate_2':[row2['vertrate']],
                            'onground_2':[row2['onground']],
                            'alert_2':[row2['alert']],
                            'baroaltitude_2':[row2['baroaltitude']],
                            'lastposupdate_2':[row2['lastposupdate']],
                            'lastcontact_2':[row2['lastcontact']],
                            })
                        # add to data frame
                        df_final = df_final.append(NMAC_row)

    # write to csv file
    df_final.to_csv("NMAC.csv", index=False)
    print('Saved files')

gen_NMAC()
