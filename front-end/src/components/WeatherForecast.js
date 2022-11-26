import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';

export default function WeatherForecast({forecastDescription}) {
  return (
    <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      <ListItem alignItems="flex-start">
        <ListItemAvatar>
          <Avatar alt={forecastDescription.shortForecast} src={forecastDescription.icon} />
        </ListItemAvatar>
        <ListItemText
          primary={forecastDescription.name}
          secondary={
            <React.Fragment>
              <Typography
                sx={{ display: 'inline' }}
                component="span"
                variant="body2"
                color="text.primary"
              >
              {forecastDescription.temperature + forecastDescription.temperatureUnit + ' - ' + forecastDescription.detailedForecast}
              </Typography>
            </React.Fragment>
          }
        />
      </ListItem>
    </List>
  );
}