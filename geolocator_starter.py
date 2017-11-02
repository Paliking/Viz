import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

# zdroj: https://www.kaggle.com/steamengine/d/saurograndi/airplane-crashes-since-1908/crash-sites-visualized-civilian-and-military
from geopy.geocoders import Nominatim
import time

import csv

geolocator = Nominatim()


with open('inputs/geo_coors1000.csv', 'a', newline='') as csvfile:
    g = csv.writer(csvfile, delimiter=',')
    for i, locat in df['Location'][4944:].iteritems():
        time.sleep(1)
        geo_obj = geolocator.geocode(locat, timeout=15)
        print(i, geo_obj)
        if geo_obj is not None:
            row = [i, geo_obj.latitude, geo_obj.longitude]
        else:
            row = [i, '', '']
        g.writerow(row)
