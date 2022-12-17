# import packages 
import numpy as np
import gpxpy
import gpxpy.gpx
from scipy.interpolate import interpn
import pandas as pd
import sys
import folium
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

# open file containing gps xml
gpx_file_name='Afternoon_Ride.gpx'
with open(gpx_file_name, 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# convert gpx file to route dictionary
route_info=[]
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            route_info.append({'latitude':point.latitude,'longitude':point.longitude,'elevation':point.elevation,'time':point.time})

# convert route dictionary to pandas DataFrame
route_df = pd.DataFrame(route_info)

# plot route DataFrame
plt.plot(route_df['longitude'],route_df['latitude'])
plt.show()