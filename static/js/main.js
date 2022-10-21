const color1 = "102, 0, 204"
const color2 = "255, 102, 102"
const color3 = "0, 204, 0"
$.ajax({
    method : "GET",
    url : "/",
    success : function (response) {
        let r_label = response.data.revenue_label;
        let r_value = response.data.revenue_value;
        // let r_header = response.data.r_header;
        let p_label = response.data.purchase_label;
        let p_value = response.data.purchase_value;
        // let p_header = response.data.p_header;
        let n_label = response.data.net_label;
        let n_value = response.data.net_value;
        let n_header = response.data.net_header;
        const ctx = document.getElementById('accountChart').getContext('2d');
        const ctx2 = document.getElementById('accountChart2').getContext('2d');
        const ctx3 = document.getElementById('netChart').getContext('2d');
        drawChart(ctx, r_label, r_value, color1);
        drawChart(ctx2, p_label, p_value, color2);
        drawChart(ctx3, n_label, n_value, color3);
        // $("#accountHeader").html('<i class="fas fa-chart-bar me-1"></i>'+r_header);
        $("#netHeader").html('<i class="fas fa-chart-bar me-1"></i>'+n_header);
    }
})



function drawChart(ctx, label, value, color){
    const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label,
        datasets: [{
            // label:
            data: value,
            backgroundColor: [
                'rgba('+color+', 0.2)',
                // 'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)',
                // 'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba('+color+', 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            // title : {
            //     display :true,
            //     text: header,
            //     padding: {
            //         top:10,
            //         bottom:30
            //     }
            // },
            legend: {
              display: false
            }
        },
        scales: {
            x: {
                grid: {
                  display: false
                }
            },
            y: {
                ticks: {callback : function(label,index,array) {
                    return label/10000+'만원'}},
                // stepSize: 10000,
                beginAtZero: true,
                grid : {display: false},
            }
        }
    }
})
}
// const ctx = document.getElementById('accountChart').getContext('2d');
// const myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });