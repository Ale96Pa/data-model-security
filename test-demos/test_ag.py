import requests

headers = {'Content-Type': 'application/ld+json'}

def test_post():
    dataag = ''
    datadevice = ''
    datavuln = ''
    datamitigation = ''

    responseag = requests.post('http://localhost:1026/ngsi-ld/v1/entities', headers=headers, data=dataag)
    print(responseag.text)

    responsedevice = requests.post('http://localhost:1026/ngsi-ld/v1/entities', headers=headers, data=datadevice)
    print(responsedevice.text)

    responsevuln = requests.post('http://localhost:1026/ngsi-ld/v1/entities', headers=headers, data=datavuln)
    print(responsevuln.text)

    responsemitigation = requests.post('http://localhost:1026/ngsi-ld/v1/entities', headers=headers, data=datamitigation)
    print(responsemitigation.text)

def test_get():
    print()

if __name__=="__main__":
    test_post()