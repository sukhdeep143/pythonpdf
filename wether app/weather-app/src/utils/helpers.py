def format_weather_data(data):
    if not data or 'main' not in data:
        return "No weather data available."

    city = data.get('name', 'Unknown City')
    temperature = data['main'].get('temp', 'N/A')
    weather_description = data['weather'][0].get('description', 'No description available.')

    formatted_data = f"Weather in {city}:\nTemperature: {temperature}°C\nDescription: {weather_description.capitalize()}"
    return formatted_data

def log_error(message):
    with open('error.log', 'a') as f:
        f.write(f"ERROR: {message}\n")