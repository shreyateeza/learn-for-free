import json
import requests
import numpy as np
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth

credentials = json.loads(open('credentials.json').read())
authentication = HTTPBasicAuth(credentials['username'], credentials['password'])

data = requests.get('https://api.github.com/users/' + credentials['username'] + '/learn-for-free/contributors', auth = authentication)
data = data.json()

print("Information about user {}:\n".format(credentials['username']))
print("Name: {}".format(data['name']))

contributors_info = []
for contributor in data:
    combined = []
    combined.append(data['name'])
    combined.append(data['login'])
    contributors_info.append(combined)

contributors_df = pd.DataFrame(contributors_info, columns = ['Name', 'Username'])
contributors_df.to_csv('contributors_info.csv', index = False)
print("Saved contributors list to contributors_info.csv")






