import React from "react";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { getParkSummaries } from '../api'
import Grid from '@mui/material/Grid';

class Homepage extends React.Component {

    constructor(props) {
        super(props);
        this.state = { parkSummaries: {} };
        this.handleClick.bind(this);
    }

    handleClick = (parkName) => {
        this.props.setDetailVisibility(true, parkName);
    }

    render() {

        const styles = {
            margin: '2rem',
            textAlign: 'center',
        }

        const containerStyles = {
            justifyContent:"center"
        }

        return (
            <div>
                <Grid container style={containerStyles} spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
                    {Object.entries(this.state.parkSummaries).map(([parkName, parkImgUrl]) => {
                        return (
                            <Grid style={styles} item xs={8} sm={6} md={6}>
                                <Card >
                                    <CardMedia
                                        component="img"
                                        image={parkImgUrl}
                                        alt={parkName + ' Park Image'}/>
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="div">

                                        </Typography>
                                        <Typography variant="h5" color="text.secondary">
                                            {parkName}
                                        </Typography>
                                    </CardContent>
                                    <CardActions style={{alignItems: 'center', justifyContent: 'center'}}>
                                        <Button size="medium" variant="contained" onClick={e => this.handleClick(parkName)}>View Trail Conditions Forecast</Button>
                                    </CardActions>
                                </Card>
                            </Grid>)
                    })}
                </Grid>
            </div>
        )
    }

    componentDidMount() {
        getParkSummaries().then(parkSummaries => this.setState({ parkSummaries: parkSummaries }));
    }
}
export default Homepage;
