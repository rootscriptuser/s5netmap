import folium
import os
import json

# Create map object
m = folium.Map(location=[46.0660877,14.4496992], zoom_start=12)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('router.png', icon_size=(50, 50))

# Vega data
#vis = os.path.join('data', 'vis.json')

# Geojson Data
#overlay = os.path.join('data', 'overlay.json')

# Create markers
folium.Marker([46.0660877,14.449699],
    popup='<strong>Location One</strong>',
    tooltip=tooltip).add_to(m)

# Circle marker
folium.CircleMarker(
    location=[46.066470, 14.449110],
    radius=50,
    popup='My Birthplace',
    color='#428bca',
    fill=True,
    fill_color='#428bca').add_to(m)

# Geojson overlay
#folium.GeoJson(overlay, name='cambridge').add_to(m)

# Generate map
m.save('map.html')
