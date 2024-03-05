import requests

headers = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/Ale96Pa/data-model-security/main/DeviceInventory/context.json>; type="application/ld+json"',
}

response = requests.get('http://localhost:1026/ngsi-ld/v1/entities/?attrs=class', headers=headers)

print(response.text)