$('#v_moneyTable').DataTable( {
    serverSide: true,
    responsive: true,
    order: [[1, 'desc']],
    destroy:true,
    // "processing": true,
    ajax: {
        url: '/v_money/api/?format=datatables',
        // success : function (response){
        //     alert(JSON.stringify(response))
        // }
    },
    columnDefs: [
        //1번재 항목 열을 숨김
        { targets: 0,
            visible : false},
        { targets: 1,
            createdCell:  function (td, cellData, rowData) {
               // console.log(rowData.id_v_money);
              $(td).attr('data-id',rowData.id_v_money);
           } },
        { targets: 2,
                render: $.fn.dataTable.render.number(',', '.', '')},
        { targets: 3,
                render: $.fn.dataTable.render.number(',', '.', '')},

 ],
    columns: [
        { data: 'id_v_money' },
        { data: 'date' },
        { data: 'deposit' },
        { data: 'expense' },
        { data: 'remark' },
    ],
});
//시재금 내역 테이블 클릭시 수정화면으로 이동
$(document).ready(function () {
    let table = $('#v_moneyTable').DataTable();

    $('#v_moneyTable tbody').on('click', 'tr', function () {
        let data = table.row(this).data().id_v_money;
        // alert(table.row(this).data().idstocks);
        $.ajax({
            // type: 'GET',
            url: '/v_money/api/'+data+'/?format=json',
            dataType: "json",
        });
        window.location.href = '/v_money/' + data;
    });

});

//삭제
$(function (){
    $("#deleteVMoney").click(function (){
        Delete("v_money","deleteVMoney");
    })
})
