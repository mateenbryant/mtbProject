import React from "react";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { getParkSummaries } from '../api'
class Homepage extends React.Component {

    constructor(props) {
        super(props);
        this.state = { parkSummaries: {} };
        this.handleClick.bind(this);
    }

    handleClick = () => {
        this.props.setDetailVisibility(true);
    }

    render() {
        return (
            <div>
                {Object.entries(this.state.parkSummaries).map(([parkName, parkImgUrl]) => {
                    return (
                        <Card sx={{ maxWidth: 345 }}>
                            <CardMedia
                                component="img"
                                height="140"
                                image={parkImgUrl}
                                alt="green iguana"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div">

                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    {parkName}
                                </Typography>
                            </CardContent>
                            <CardActions>

                                <Button size="small" onClick={this.handleClick}>Learn More</Button>
                            </CardActions>
                        </Card>)
                })}
            </div>
        )
    }

    componentDidMount() {
        getParkSummaries().then(parkSummaries =>this.setState({ parkSummaries: parkSummaries }));
    }
}
export default Homepage;
