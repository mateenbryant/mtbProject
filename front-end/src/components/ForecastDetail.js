import React from 'react';
import '../ForecastDetail.css';
import { getForecastInfo } from '../api';
import PrecipitationChart from './PrecipitationChart';
import Typography from '@mui/material/Typography';
import WeatherForecast from './WeatherForecast';
import Card from '@mui/material/Card';
import { CardContent } from '@mui/material';


class ForecastDetail extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      precipitationData: [],
      forecastDescriptions: [],
      currentTrailCondition: ""
    }
  }

  render() {
    return (
      <div className="Forecast-detail">
        <Typography variant="h3" style={{ marginTop: '5rem' }} className="Forecast-park-name">
          {this.props.parkName} Downhill Bike Park
        </Typography>

        <Typography variant="h6" className="Forecast-park-name">
          Trail Conditions and Weather Forecast
        </Typography>

        <br />
        <Typography>Near Term Weather Forecast</Typography>
        {this.state.forecastDescriptions.map(forecastDescription =>
          <WeatherForecast sx={{maxWidth: 360}} forecastDescription={forecastDescription} />
        )}

        <PrecipitationChart sx={{maxWidth: 360}} precipitationData={this.state.precipitationData} />
        <br />
        <Card>
          <CardContent sx={{maxWidth: 360}}>
            <Typography variant="h6" className="Forecast-trail-condition">Computed Trail Conditions Report: </Typography>
            <Typography>{this.state.currentTrailCondition}</Typography>
          </CardContent>
        </Card>
        <br />
      </div>
    );
  }

  componentDidMount() {
    getForecastInfo(this.props.parkName).then(forecastInfo => this.setState(forecastInfo));
  }
}

export default ForecastDetail;
