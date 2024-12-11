# A dictionary containing mock weather data for demonstration purposes
weather_data = {
    "Nairobi": {"Temperature": 25, "Humidity": 60, "Description": "Sunny"},
    "Dubai": {"Temperature": 40, "Humidity": 20, "Description": "Hot and Dry"},
    "New York": {"Temperature": 15, "Humidity": 50, "Description": "Cloudy"},
    "London": {"Temperature": 10, "Humidity": 80, "Description": "Rainy"},
    "Tokyo": {"Temperature": 20, "Humidity": 70, "Description": "Partly Cloudy"}
}

def get_weather(city):
    # Check if the city exists in the mock database
    city_weather = weather_data.get(city.title())
    if city_weather:
        return city_weather
    else:
        return "Weather data for this city is not available."

def main():
    print("Welcome to the Offline Weather Application!")
    while True:
        # Ask the user for a city
        city = input("\nEnter the city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Thank you for using the Weather Application. Goodbye!")
            break

        # Get and display the weather data
        weather = get_weather(city)
        if isinstance(weather, dict):
            print("\nWeather Information:")
            for key, value in weather.items():
                print(f"{key}: {value}")
        else:
            print(weather)

# Run the application
if __name__ == "__main__":
    main()
