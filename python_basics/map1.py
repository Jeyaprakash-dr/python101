import folium
import pandas

data = pandas.read_csv("../Webmap_datasources/Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elevate = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """
Volcano Information:<br>
<a href="https://www.google.com/search?q=%%22%s%22" target="_blank">%s</a><br>
Height: %s m
"""

map1 = folium.Map(location=[38.58, -99.20], zoom_start=5, tiles="OpenStreetMap", attr="Mapbox Data Attribution")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elevate):
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=str(el) + " m", fill_color=color_producer(el),
                                      color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 100000000
                             else 'orange' if 100000000 <= x['properties']['POP2005'] < 900000000 else 'red'}))

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())

map1.save("Map1.html")
