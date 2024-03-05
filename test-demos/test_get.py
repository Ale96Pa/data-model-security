import requests

headers = {
    'Accept': 'application/ld+json',
}

params = {
    'type': 'GtfsAgency',
}

response = requests.get('http://localhost:1026/ngsi-ld/v1/entities', params=params, headers=headers)

print(response.content)