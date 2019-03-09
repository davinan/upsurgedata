import populartimes
import json
api_key = "AIzaSyDQkNQQGP6HF-WbW0OmUTqbHtOF8TnTBJo"
place_id = "ChIJp0eq6HsE9YgRtDmGa4gATak" #"55 Ivan Allen Jr Blvd NW, Atlanta, GA 30308"
# response = populartimes.get_id(api_key, place_id)
def load_data(file_name, from_file):
    response = populartimes.get(api_key, ["restaurants", "clubs"], (33.765060, -84.389950), (33.769040, -84.374520))
    geojson = format(response)
    return geojson

def save_data(data):
    file_name = "data.geojson"
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

def format(data):
    geojson = {}
    geojson["type"] = "FeatureCollection"
    geojson["features"] = []
    for place in data:
        for week_day in place["populartimes"]:
            for i in range(0, 8):
                geo_data = { "type": "Feature", "properties": { "id": place["id"], "mag": week_day["data"][i], "time": i}, "geometry": { "type": "Point", "coordinates": [place["coordinates"]["lat"], place["coordinates"]["lng"], 0.0 ] } }
                geojson["features"].append(geo_data)
    return geojson

data = load_data("data.geojson", True)

save_data(data);
print(data)
