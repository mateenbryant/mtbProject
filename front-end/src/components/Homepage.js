import React from "react";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { getParkSummaries } from '../api'
import { alignProperty } from "@mui/material/styles/cssUtils";
class Homepage extends React.Component {

    constructor(props) {
        super(props);
        this.state = { listOfParkSummaries: [] };
        this.handleClick.bind(this);
    }

    handleClick = () => {
        this.props.setDetailVisibility(true);
    }

    render() {
        return (
            <div>
                {this.state.listOfParkSummaries.map(({ parkName, parkImg }) => {
                    return (
                        <Card sx={{ maxWidth: 345 }}>
                            <CardMedia
                                component="img"
                                height="140"
                                image={parkImg}
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
        this.setState({ listOfParkSummaries: getParkSummaries() })
    }
}
export default Homepage;
