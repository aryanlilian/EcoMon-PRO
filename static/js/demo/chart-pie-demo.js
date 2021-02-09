// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var incomes_pie = {
    'names': [],
    'values': [],
}
var incomesChartPieURL = '/users/dashboard/incomes-chart-pie'

$.ajax({
    method: 'GET',
    url: incomesChartPieURL,
    success: function (response) {
        for (var i in response) {
            var key = Object.keys(response[i])[0]
            var value = Object.values(response[i])[0]
            incomes_pie.names.push(key)
            incomes_pie.values.push(value)
        }
        buildIncomesChartPie()
    }
})
function buildIncomesChartPie() {
    var ctx = document.getElementById("incomesPieChart");
    var myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: incomes_pie.names,
            datasets: [{
                data: incomes_pie.values,
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
                hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
                hoverBorderColor: "rgba(234, 236, 244, 1)",
            }],
        },
        options: {
            maintainAspectRatio: false,
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                borderColor: '#dddfeb',
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10,
            },
            legend: {
                display: false
            },
            cutoutPercentage: 80,
        },
    });
}


        // Set new default font family and font color to mimic Bootstrap's default styling
        Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
        Chart.defaults.global.defaultFontColor = '#858796';

        // Pie Chart Example
        var spendings_pie = {
            'names': [],
            'values': [],
        }
        var spendingsChartPieURL = '/users/dashboard/spendings-chart-pie'

        $.ajax({
            method: 'GET',
            url: spendingsChartPieURL,
            success: function (response) {
                for (var i in response) {
                    var key = Object.keys(response[i])[0]
                    var value = Object.values(response[i])[0]
                    spendings_pie.names.push(key)
                    spendings_pie.values.push(value)
                }
                buildSpendingsChartPie()
            }
        })
        function buildSpendingsChartPie() {
            var ctx = document.getElementById("spendingsPieChart");
            var myPieChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: spendings_pie.names,
                    datasets: [{
                        data: spendings_pie.values,
                        backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
                        hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
                        hoverBorderColor: "rgba(234, 236, 244, 1)",
                    }],
                },
                options: {
                    maintainAspectRatio: false,
                    tooltips: {
                        backgroundColor: "rgb(255,255,255)",
                        bodyFontColor: "#858796",
                        borderColor: '#dddfeb',
                        borderWidth: 1,
                        xPadding: 15,
                        yPadding: 15,
                        displayColors: false,
                        caretPadding: 10,
                    },
                    legend: {
                        display: false
                    },
                    cutoutPercentage: 80,
                },
            });
        }
