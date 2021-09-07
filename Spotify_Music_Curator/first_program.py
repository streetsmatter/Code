import requests


#SETTINGS
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQCYTm-lS1z1vWep5pobgM7WIx-quNGoVcJXRZmrdm7acGHQCmJWPl_0gCmaK88i-e96X8UoHPPNIkakvoLS-J_7irnWwA4XaaGB06k6BJp8E9roTnd26gqxmUMoRnCIV_b3f-S92YK4wduTJ76g4J7gn908eatBUz_GOxywRdhDXJR0V-s"
user_id =  "streetsmatter"

# OUR FILTERS 
limit = 30
market = "US"
seed_genre1 = "hip hop"
valence = .9
uris = []
seed_artists='4LEiUm1SRbFMgfqnQTwUbQ'
seed_tracks = '7bzzC7QIfflM9eEj2aqaYX' 

# PERFORM THE QUERY

query = f'{endpoint_url}limit={limit}&market={market}&seed_genre1={seed_genre1}&valence={valence}'
query += f'&seed_artists={seed_artists}'
query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1} \"{j['name']}\" by {j['artists'][0]['name']}")

# CREATE A NEW PLAYLIST

import requests
import json 

token = "BQC8VTJc35zzZ09qmXARcKZf6TEmK76JYCbq-t6n3RQES7Ee-4HJdX8QOyjz9r9CP7kcvRsFZokcaAdS28DHTe3pt1A3hpKPNLokrK2NqyKCAyDmauQne6CUGxEpeB7pF9HN7BfTW13b3XHSb1Mbz3aJFJicrewl0uEm1vnf3RJ5LHjxuyE"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Music like Bon Iver and Fleet Foxes but Hip hop",
          "description": "My first programmatic playlist, yooo!",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})


url = response.json()['external_urls']['spotify']
print(response.status_code)


# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
token = "BQAkCfYj_q98Abcc5i9RUsBh_pduWk_ldFi70echxX7Kc_FUbj9U--QcyvwAmeIMlO-CUbGCZgYwQ1CrvIXAXrfW4sxLw7JxwVWDNvaMdEeuvyVpfft2UW4cQ8ogm3kUCNBZKqEgGoeOTKKXpn-6rrWla-iWuHFCLMT8wIHlWJ6AOsgQl-I"
request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')
