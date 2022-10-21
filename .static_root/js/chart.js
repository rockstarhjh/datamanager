const color = "43, 43, 243";
const ctx = document.getElementById('drawChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            // label:
            data: [],
            backgroundColor: [
                'rgba('+color+', 0.2)',
            ],
            borderColor: [
                'rgba('+color+', 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
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
                beginAtZero: true,
                grid : {display: false},
            }
        }
    }
})
// myChart.
$("#searchChart").click(function (){
    let year = $("#year").val();
    let year_gap = $("#year_gap").val();
    let month = $("#month").val();
    let month_gap = $("#month_gap").val();
    let division = $("#chartDivision").val();
    let date;
    let gap;
    let date_division;
    if (!division){alert("구분을 선택하세요"); return;}
    if (!year && !month){
        alert("조건을 입력하고 검색하세요.");
        return
    }
    if (year && month){
        alert("조건을 하나만 입력하세요.");
        return
    }
    if (year && !month){
        if (!year_gap){year_gap=6}
        date = year;
        gap = year_gap-1;
        date_division = "year";
    }else {
        if (!month_gap){month_gap=6}
        date = month
        gap = month_gap-1
        date_division = "month";
    }
    $.ajax({
        method : "POST",
        url : "/chart/",
        data : {'date': date, 'gap': gap, 'division': division, 'date_division': date_division},
        success : function (response) {
            // alert('1');
            let label = response.data.label;
            let value = response.data.value;
            let header = response.data.header;
            // checkChart(label,value);
            drawChart(label, value);
            $("#searchHeader").html('<i class="fas fa-chart-bar me-1"></i>'+header);
            // $("#netHeader").html('<i class="fas fa-chart-bar me-1"></i>'+n_header);
    }
})
})
function drawChart(label,value){
    // let chartStatus = Chart.getChart("drawChart"); // <canvas> id
    // if (chartStatus) {
    //     chartStatus.destroy();
    //     // alert('1')
    // }
    myChart.data.labels=label;
    myChart.data = {
        labels : label,
        datasets: [{
            data: value,
            backgroundColor: [
                'rgba('+color+', 0.6)',
            ],
            borderColor: [
                'rgba('+color+', 1)',
            ],
            borderWidth: 1
        }]
    }
    myChart.options ={
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
                    return label/1000000+'백만원'}},
                // stepSize: 10000,
                beginAtZero: true,
                grid : {display: false},
            }
        }
    }
    myChart.update();
}

