import folium
# Create map object
m = folium.Map(location=[45.503345, -73.570133], zoom_start=12)

# Global tooltip
tooltip = 'UNIQLO Montreal'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('UNIQLO.png')


folium.Marker([45.503228, -73.570102],
              popup='<strong>Uniqlo</strong>',
              tooltip=tooltip,
              icon=logoIcon).add_to(m)

m.save('map.html')