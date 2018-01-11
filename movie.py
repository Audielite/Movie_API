import requests
import os

#os.environ['omdb_key'] = '4e1eae8c'

key = os.environ['omdb_key']
base_url = 'http://www.omdbapi.com/'
movie = input("What movie rating would you like to check? ")
params = {'apikey' : key, 't' : movie}
data = requests.get(base_url, params ).json()

print("Rating for that movie: ")
print(data['Ratings'][0]["Value"])
print("")
print("Some of the stars: ")
print(data ["Actors"])
