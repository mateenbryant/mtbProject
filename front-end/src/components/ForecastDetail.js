import React from 'react';
import '../ForecastDetail.css';
import { getForecastInfo } from '../api';
import PrecipitationChart from './PrecipitationChart';

class ForecastDetail extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      precipitationData : [],
      forecastDescriptions : [],
      parkName : "",
      currentTrailCondition: ""
    }
  }

  render() {

    return (
      <div className="Forecast-detail">
        <h4 className="Forecast-park-name">
          Massanutten Downhill Park <br></br>

          {this.state.forecastDescriptions.map(forecastDescriptions => 
            <h5> {forecastDescriptions.detailedForecast} </h5>
          )}
            <br></br>
        </h4>

        <PrecipitationChart precipitationData={this.state.precipitationData} />

        <h3 className="Forecast-trail-condition">{this.state.currentTrailCondition}</h3>
      </div>
    );
  }

  componentDidMount() {
    getForecastInfo().then(forecastInfo => this.setState(forecastInfo));
  }
}

export default ForecastDetail;
