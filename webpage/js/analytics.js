var data = [{
    x: 10,
    y: 20
}, {
    x: 15,
    y: 10
}]
var ctx = document.getElementById('myChart').getContext('2d');
var stackedLine = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
        scales: {
            yAxes: [{
                stacked: true
            }]
        }
    }
});

