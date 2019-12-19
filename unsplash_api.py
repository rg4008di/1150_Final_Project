# access key (unsplash) e73fdc2f4eff1bbeb0ec4505b7cc355b6572b434a09f410702383be7536129aa
import requests
from PIL import Image
from io import BytesIO

url = 'https://api.unsplash.com/photos/random/'

query = 'tacos'

client_id = 'e73fdc2f4eff1bbeb0ec4505b7cc355b6572b434a09f410702383be7536129aa'

query_params = {'client_id': client_id, 'query': query}

response = requests.get(url, params=query_params).json()



img.show()


