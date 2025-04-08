from flask import Flask, jsonify, request
from services.weather_service import WeatherService

app = Flask(__name__)
weather_service = WeatherService()

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = weather_service.get_weather(city)
    if weather_data is None:
        return jsonify({'error': 'Could not fetch weather data'}), 500
    
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)