from flask import Flask, render_template
import folium
import os

app = Flask(__name__)


@app.route("/")
def open_street_map():
    # this map using stamen toner
    # define which map to use
    map = folium.Map(
        location=[45.92736, 14.972],
        zoom_start=10
    )

    # DEFINE CUSTOM ICONS FOR MARKERS

    # Markers
    folium.Marker(
        location=[46.08153163502347, 15.286592112099468],
        icon=folium.features.CustomIcon('router.png', icon_size=(50,50)),
        popup='<h3>Lisca</h3>'
    ).add_to(map),
   
    folium.Marker(
        location=[46.109650149268795, 14.053135018812508],
        popup="<b>Ermanovec</b>",
        tooltip="Click Here!",
        icon=folium.features.CustomIcon('router.png', icon_size=(50,50)),
    ).add_to(map),

    folium.Marker(
        location=[45.89481472629865, 14.07749366269257],
        popup="<b>javornik</b>",
        tooltip="Click Here!",
        icon=folium.features.CustomIcon('router.png', icon_size=(50,50))
    ).add_to(map),

    #folium.PolyLine(povezava, tooltip="Coast").add_to(map)
    
    #folium.PolyLine(povezava2, tooltip="Coast").add_to(map)
    
#     header = map.get_root().header.render()
#    overlay = os.path.join('data', 'overlay.json')

    iframe= map._repr_html_()

    return render_template('index.html', iframe=iframe)
    
    
@app.route("/test")
def test():
    map=folium.Map(
        location=[45.92736, 14.972],
        zoom_start=10
        )
    # adding data from JSON 
    folium.GeoJson('data.json', name='cambridge',popup=folium.GeoJsonPopup(fields=['Lokacija','IP'])).add_to(map)
    iframe=map._repr_html_()
    
    return render_template('index.html', iframe=iframe)
#    return map._repr_html_()

#    povezava = [(46.109650149268795, 14.053135018812508),(46.08153163502347, 15.286592112099468),]
#    povezava2 = [(45.89481472629865, 14.07749366269257), (46.109650149268795, 14.053135018812508),]
if __name__ == "__main__":
    app.run(debug=False)
