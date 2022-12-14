import React from 'react';
import './App.css';
import Homepage from './components/Homepage';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ForecastDetail from './components/ForecastDetail';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.setDetailVisibility.bind(this);
    this.handleBackButtonClick.bind(this);
    this.state = { forecastDetailsAreVisible: false };
  }

  setDetailVisibility = (detailVisibility, parkName) => {
    this.setState({
      forecastDetailsAreVisible: detailVisibility,
      currentSelectedParkName: parkName
    });
  }

  handleBackButtonClick = () => {
    this.setState({ forecastDetailsAreVisible : false });
  }

  render() {
    let componentToRender;

    if (this.state.forecastDetailsAreVisible) {
      componentToRender = <ForecastDetail parkName={this.state.currentSelectedParkName}/>;
    } else {
      componentToRender = <Homepage setDetailVisibility={this.setDetailVisibility} />;

    }

    return (
      <div className="App">
        <Box sx={{ flexGrow: 1 }}>
          <AppBar position="static">
            <Toolbar>
              {this.state.forecastDetailsAreVisible &&
                <IconButton
                  onClick={this.handleBackButtonClick}
                  size="large"
                  edge="start"
                  color="inherit"
                  aria-label="menu"
                  sx={{ mr: 2 }}>
                  <ArrowBackIcon />
                </IconButton>}

              <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                Weather for MTB Parks in VA/WV
              </Typography>
            </Toolbar>
          </AppBar>
        </Box>
        {componentToRender}
      </div>

    );
  }
}

export default App;
