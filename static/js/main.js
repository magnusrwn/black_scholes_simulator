/* Setting placeholder for table */
const placeholderData = [{
    type: "surface",
  x: [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ],

  y: [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ],

  z: [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ],
    colorscale: "Greys"
}];
Plotly.newPlot("dataTable", placeholderData, {})

function updateTable(data){
    const {time_plot, price_plot, c_plot, s} = data;
    const GRAPH_DATA = [{
        type: "surface",
        x: price_plot,
        y: time_plot,
        z: c_plot,
        colorscale: "Viridis"
    }];
    const layout = {
        title: 'Option Price Surface',
        autosize: true,
        margin: {
            l: 50,
            r: 50,
            b: 50,
            t: 50,
            pad: 4
        },
        scene: {
            xaxis: {
                title: 'Stock Price (S)',
                titlefont: { size: 14, color: '#333' },
                tickfont: { size: 12 }
            },
            yaxis: {
                title: 'Time to Expiry (T)',
                titlefont: { size: 14, color: '#333' },
                tickfont: { size: 12 }
            },
            zaxis: {
                title: 'Call Option Price (C)',
                titlefont: { size: 14, color: '#333' },
                tickfont: { size: 12 }
            }
        },
        paper_bgcolor: '#f8f9fa',
        plot_bgcolor: '#ffffff',
        font: {
            family: 'Arial, sans-serif',
            size: 12,
            color: '#333'
        }
    };
    Plotly.react('dataTable', GRAPH_DATA, layout);
}

/* Event lister */
$('#variableInputForm').on("submit", async function(event) {
    console.log("hello")
    /* Prevent the reload of page */
    event.preventDefault();

    const formData = new FormData(event.target);
    const response = await fetch("/calc", {
        method: "POST",
        body: formData,
    });
    const data = await response.json();
    updateTable(data);
})