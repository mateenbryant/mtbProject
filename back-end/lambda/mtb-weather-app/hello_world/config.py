from dataclasses import dataclass

@dataclass
class LocationToApiArgsMap:
    forecast_grid_location : str
    historical_precipitation_url_path : str

@dataclass
class AppConfig:
    locations: dict[str, LocationToApiArgsMap]
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
        'massanutten' : LocationToApiArgsMap(forecast_grid_location='LWX/40,42', historical_precipitation_url_path='weather-massanutten-virginia/va281/past.php'),
        'bryce' : LocationToApiArgsMap(forecast_grid_location='LWX/37,60', historical_precipitation_url_path='weather-basye-virginia/22810/past.php'),
        'snowshoe': LocationToApiArgsMap(forecast_grid_location='RLX/119,75', historical_precipitation_url_path='weather-snowshoe-west-virginia/26209/past.php')
    },
    forecast_api_url="https://api.weather.gov/gridpoints/{grid_value}/forecast",
    precipitation_data_source_url="https://www.localconditions.com/{historical_precipitation_url_path}"
)

def get_locations_list():
    return list(app_config.locations.keys())
