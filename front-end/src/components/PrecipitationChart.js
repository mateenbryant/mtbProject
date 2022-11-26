import React from 'react';

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
import { Typography } from '@mui/material';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

function setupChartData(chartLabels, dataList) {
    const data = {
        labels: chartLabels,
        datasets: [{
            label: 'Daily Recorded Precipitation (in.)',
            data: dataList
        }]
    };

    const config = {
        responsive: true,
        backgroundColor: 'blue',
        plugins: {
            display: true,
            title: '',
        }
    };

    return {
        'data': data,
        'config': config
    };
};

export default function PrecipitationChart({ precipitationData }) {
    const labels = precipitationData.map((value, index) => {
        return index + 1;
    });

    var chartConfig = setupChartData(labels, precipitationData);

    return (
        <div>
            <br></br><Typography> 25 Day Recorded Precipitation </Typography>
            <Line className="Forecast-graph" options={chartConfig.config} data={chartConfig.data} />
        </div>

    );
}