// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var accountId = JSON.parse(document.getElementById('accountId').textContent);
let incomesPie = {
    'names': [],
    'values': [],
}

if(accountId) {
    var incomesChartPieURL = `/users/dashboard/incomes-chart-pie/${accountId}/`
} else {
    var incomesChartPieURL = `/users/dashboard/incomes-chart-pie/`
}

$.ajax({
    method: 'GET',
    url: incomesChartPieURL,
    success: function (response) {
        for (let i in response) {
            let key = Object.keys(response[i])[0]
            let value = Object.values(response[i])[0]
            incomesPie.names.push(key)
            incomesPie.values.push(value)
        }
        buildIncomesChartPie()
    }
})
function buildIncomesChartPie() {
    let ctx = document.getElementById("incomesPieChart");
    let myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: incomesPie.names,
            datasets: [{
                data: incomesPie.values,
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#e63900', '#7e98e7',
                '#4de6ad', '#85d4e0', '#ff6633', '#a9baef', '#a6f2d6', '#ade2eb', '#ffb399'],
                hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#b32d00', '#5376df',
                '#20df99', '#47bfd1', '#ff4000', '#7e98e7', '#79ecc2', '#85d4e0', '#ff8c66'],
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

let spendingsPie = {
    'names': [],
    'values': [],
}

if(accountId) {
    var spendingsChartPieURL = `/users/dashboard/spendings-chart-pie/${accountId}/`
} else {
    var spendingsChartPieURL = `/users/dashboard/spendings-chart-pie/`
}

$.ajax({
    method: 'GET',
    url: spendingsChartPieURL,
    success: function (response) {
        for (let i in response) {
            let key = Object.keys(response[i])[0]
            let value = Object.values(response[i])[0]
            spendingsPie.names.push(key)
            spendingsPie.values.push(value)
        }
        buildSpendingsChartPie()
    }
})
function buildSpendingsChartPie() {
    let ctx = document.getElementById("spendingsPieChart");
    let myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: spendingsPie.names,
            datasets: [{
                data: spendingsPie.values,
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#e63900', '#7e98e7',
                '#4de6ad', '#85d4e0', '#ff6633', '#a9baef'],
                hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#b32d00', '#5376df',
                '#20df99', '#47bfd1', '#ff4000', '#7e98e7'],
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
