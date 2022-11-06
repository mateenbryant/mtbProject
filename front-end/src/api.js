export function getForecastInfo() {
    return fetch('http://127.0.0.1:5000')
    .then((response) => response.json())
    .then((forecastInfoResponse) => {    
        const precipitationList = forecastInfoResponse.last_25_days_precipitation;
        var forecastDescriptions = forecastInfoResponse.forecast_descriptions;
        const trailCondition = forecastInfoResponse.trail_condition_description;
    
        return {
            "precipitationData" : precipitationList,
            "forecastDescriptions" : forecastDescriptions,
            "currentTrailCondition" : trailCondition
        };
    });
};

export function getParkSummaries() {
    return [{
        parkName: 'Massanutten',
        parkImg: 'https://mtbparks.com/images/2016-MASSANUTTEN/Massanutten_bike-park5.jpg'
    },
    {
        parkName: 'Bryce',
        parkImg : 'https://s14761.pcdn.co/wp-content/uploads/2016/01/Bryce-Mountain-Bike-Park-Virginia-25.jpg'
    }]
}

