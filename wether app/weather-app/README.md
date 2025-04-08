# Weather App

This is a simple weather application built with Python and Flask. It allows users to fetch weather data for a specified city using an external weather API.

## Project Structure

```
weather-app
├── src
│   ├── app.py                # Entry point of the application
│   ├── services
│   │   └── weather_service.py # Contains the WeatherService class for fetching weather data
│   ├── utils
│   │   └── helpers.py        # Utility functions for formatting and logging
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables and configuration
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file. You will need to include your API key for the weather service.

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

3. To get the weather for a specific city, send a GET request to the `/weather` endpoint with the city name as a query parameter:
   ```
   http://127.0.0.1:5000/weather?city=London
   ```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.