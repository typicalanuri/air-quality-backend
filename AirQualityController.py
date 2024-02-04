from flask import Flask, request
from service.QualityService import getQualityByCity
from requests.exceptions import HTTPError

app = Flask(__name__)

@app.route('/quality', methods=['GET'])
def air_quality_request():
    userinput = request.get_json()
    city = userinput['city']
    print(city)
    try:
        airQuality = getQualityByCity(city)
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as exception:
        print(f'Exception occured: {exception}')
    else:
        return airQuality

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)