import requests

def getQualityByCity(city):
    print("city={}".format(city))
    response = requests.get(
        'https://api.ambeedata.com/latest/by-city',
        params={'city': '{}'.format(city)},
        headers={'x-api-key': '52c35f0842d81e18c2787025d67ca26cd6600d7ed3491bb6953c76aad9297227', 'Accept-Language':'English'}
        )
    if response.status_code == 200:
        print("Success")
        json_response = response.json()
        print(json_response)
    else:
        print("Request is not successful")
        json_response = None
    return json_response