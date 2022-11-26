from dataclasses import dataclass

@dataclass
class LocationData:
    forecast_grid_location : str
    historical_precipitation_url_path : str
    image_url : str

@dataclass
class AppConfig:
    locations: dict[str, LocationData]
    forecast_api_url: str
    precipitation_data_source_url: str

    def get_forecast_api_url_for_location(self, location):
        location_grid_value = self.locations[location].forecast_grid_location
        return self.forecast_api_url.format(grid_value=location_grid_value)

    def get_precipitation_data_url_for_location(self, location):
        precipitation_url_path = self.locations[location].historical_precipitation_url_path
        return self.precipitation_data_source_url.format(historical_precipitation_url_path=precipitation_url_path)

app_config = AppConfig(
    locations= {
        'Massanutten' : LocationData(forecast_grid_location='LWX/40,42', historical_precipitation_url_path='weather-massanutten-virginia/va281/past.php', image_url='https://mtbparks.com/images/2016-MASSANUTTEN/Massanutten_bike-park5.jpg'),
        'Bryce' : LocationData(forecast_grid_location='LWX/37,60', historical_precipitation_url_path='weather-basye-virginia/22810/past.php', image_url='https://s14761.pcdn.co/wp-content/uploads/2016/01/Bryce-Mountain-Bike-Park-Virginia-25.jpg'),
        'Snowshoe': LocationData(forecast_grid_location='RLX/119,75', historical_precipitation_url_path='weather-snowshoe-west-virginia/26209/past.php', image_url='https://www.snowshoemtn.com/-/media/snowshoe/summer/2400x1350/2022bikeparkseasonpass.jpg?rev=2a4332ab4f62417b95e316cde05193fc?h=1012&w=1800&hash=0DFE8400D69A11B92FEF950661CFC85B')
    },
    forecast_api_url="https://api.weather.gov/gridpoints/{grid_value}/forecast",
    precipitation_data_source_url="https://www.localconditions.com/{historical_precipitation_url_path}"
    
)

def get_locations_with_image_urls():
    location_data_dict = app_config.locations
    location_image_url_dict = {}
    for location_key, location_data in location_data_dict.items():
        location_image_url_dict[location_key] = location_data.image_url

    return location_image_url_dict
