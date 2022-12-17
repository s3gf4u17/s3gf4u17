with open('exported.csv','r') as f:
    content=f.readlines()

c = [float(e[:-1].split(",")[1]) for e in content[1:]]
print(content)

line = [[c[0],c[1]],[c[2],c[3]]]

import folium

def draw_route(route: 'list[list[float]]'):
    fmap = folium.Map(location=[53.5, 22.5], zoom_start=7)
    folium.PolyLine(route, color="black").add_to(fmap)
    # for point in route:
    #     plotDot(point, fmap)
    return fmap

def plotDot(point, this_map):
    folium.CircleMarker(location=[point[0], point[1]], radius=0.1, weight=1.5, color="pink").add_to(this_map)

draw_route(line).save("index.html")