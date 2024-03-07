import requests

headers = {'Content-Type': 'application/ld+json'}

datadevice = '{    "id": "urn:test-device-2",    "type": "NetworkDevice",    "class": {        "type": "Property",        "value": "workstation"    },    "hostname": {        "type": "Property",        "value": "host1"    },    "HasInterfaces": {        "type": "Relationship",        "object": [            "urn:ngsi-ld:Floor:Test:SmartCitiesdomain:SmartBuildings:38vC2rMpPDpQ1cy52XqxrF",            "urn:ngsi-ld:Floor:Test:SmartCitiesdomain:SmartBuildings:0N3USWemr0KgB4UDlFuw2z",            "urn:ngsi-ld:Floor:Test:SmartCitiesdomain:SmartBuildings:0Jy7nvJPr4avJ7rEk394Tm",            "urn:ngsi-ld:Floor:Test:SmartCitiesdomain:SmartBuildings:1snjtpHWLBnQX6I36Y6QQU"        ]    },    "@context": ["https://raw.githubusercontent.com/Ale96Pa/data-model-security/main/DeviceInventory/context.json"]}'

response = requests.post('http://localhost:1026/ngsi-ld/v1/entities', headers=headers, data=data)

print(response.text)