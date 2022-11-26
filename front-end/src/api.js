export function getForecastInfo(location) {
    return fetch(process.env.REACT_APP_BACKEND_API_HOSTNAME + '/locations/forecast-detail/' + location)
    .then((response) => response.json())
    .then((forecastInfoResponse) => {    

        const precipitationList = forecastInfoResponse.last_25_days_precipitation;
        var forecastDescriptions = forecastInfoResponse.forecast_descriptions;
        const trailCondition = forecastInfoResponse.trail_conditions_descriptions;
    
        return {
            "precipitationData" : precipitationList,
            "forecastDescriptions" : forecastDescriptions,
            "currentTrailCondition" : trailCondition
        };
    });
};

export function getParkSummaries() {
    return fetch(process.env.REACT_APP_BACKEND_API_HOSTNAME + '/locations').then(response => response.json())
}

