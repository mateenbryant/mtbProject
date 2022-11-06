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
            label: 'My first graph',

            data: dataList
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
            <br></br>Preciptation within the last 25 days.<br></br>
            <Line className="Forecast-graph" options={chartConfig.config} data={chartConfig.data} />
        </div>

    );
}