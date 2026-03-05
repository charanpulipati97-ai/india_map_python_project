import folium

# Create a map centered on India
india_map = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

# Data for some states
states = [
    {
        "state": "Andhra Pradesh",
        "capital": "Amaravati",
        "food": "Pulihora",
        "culture": "Kuchipudi dance and Telugu traditions",
        "lat": 15.9129,
        "lon": 79.7400
    },
    {
        "state": "Telangana",
        "capital": "Hyderabad",
        "food": "Hyderabadi Biryani",
        "culture": "Bathukamma festival and Deccan heritage",
        "lat": 18.1124,
        "lon": 79.0193
    },
    {
        "state": "Tamil Nadu",
        "capital": "Chennai",
        "food": "Dosa",
        "culture": "Bharatanatyam dance and Dravidian temples",
        "lat": 11.1271,
        "lon": 78.6569
    },
    {
        "state": "Karnataka",
        "capital": "Bengaluru",
        "food": "Bisi Bele Bath",
        "culture": "Yakshagana folk theatre",
        "lat": 15.3173,
        "lon": 75.7139
    },
    {
        "state": "Maharashtra",
        "capital": "Mumbai",
        "food": "Vada Pav",
        "culture": "Lavani dance and Marathi traditions",
        "lat": 19.7515,
        "lon": 75.7139
    }
]

# Add markers
for s in states:
    popup_text = f"""
    <b>State:</b> {s['state']}<br>
    <b>Capital:</b> {s['capital']}<br>
    <b>Famous Food:</b> {s['food']}<br>
    <b>Culture:</b> {s['culture']}
    """

    folium.Marker(
        location=[s["lat"], s["lon"]],
        popup=popup_text,
        tooltip=s["state"]
    ).add_to(india_map)

# Save map
india_map.save("india_states_map.html")