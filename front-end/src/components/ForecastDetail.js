import React from 'react';
import '../ForecastDetail.css';


import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';


ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);


class ForecastDetail extends React.Component {

  render() {
    var x = new XMLHttpRequest();
    x.open("GET", "http://127.0.0.1:5000", false);
    x.send(null);
    var result = JSON.parse(x.responseText);
    const precipitation_list = result.last_25_days_precipitation;
    const trail_condition = result.trail_condition_description;
    const daily_forecast = result.forecast_descriptions;

    
  

    function create_jsx_line_tag(li_value, li_key_attribute) {
      return (<li key={li_key_attribute}>{li_value}</li>);
    }

    var new_list_of_jsx_expressions = precipitation_list.map((precipitationDataPoint, index) => {
      return create_jsx_line_tag(precipitationDataPoint, index)
    });


    const labels = precipitation_list.map((value, index) => {
      return index + 1;
    })
    console.log(labels);

    const data = {
      labels: labels,
      datasets: [{
        label: 'My first graph',

        data: precipitation_list
      }
      ]
    };

    const config = {
      responsive: true,
      backgroundColor: 'purple',
      plugins: {
        display: true,
        title: 'first chart',
      }
    };

    return (

      <div className="Forecast">

        <header className="Forecast-header">

          <h4 className="Forecast-park-name">
            Massanutten Downhill Park <br></br>
            {daily_forecast[0].detailedForecast} <br></br>
            <br></br>Preciptation within the last 25 days.<br></br>
            <Line className="Forecast-graph" options={config} data={data} />
          </h4>

          <h3 className="Forecast-trail-condition">{trail_condition}</h3>

          <a
            className="Forecast-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>

    );
  }
}

export default ForecastDetail;
