with open('exported3.csv','r') as f:
    content=f.readlines()

import math

content=content[1:]
content = [cont.split(',') for cont in content]
content = [[float(cont[9])/math.pi*180,float(cont[10])/math.pi*180] for cont in content]

import folium

def draw_route(route: 'list[list[float]]'):
    fmap = folium.Map(location=[53.5, 22.5], zoom_start=7)
    folium.PolyLine(route, color="black").add_to(fmap)
    # for point in route:
    #     plotDot(point, fmap)
    return fmap

def plotDot(point, this_map):
    folium.CircleMarker(location=[point[0], point[1]], radius=0.1, weight=1.5, color="pink").add_to(this_map)

draw_route(content).save("index.html")