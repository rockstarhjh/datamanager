$('#priceTable').DataTable( {
    serverSide: true,
    responsive: true,
    // order: [[1, 'desc']],
    destroy:true,
    // "processing": true,
    // paging : false,
    ajax: {
        url: '/price/api/?format=datatables',
    },
    columnDefs: [
        //1번재 항목 열을 숨김
        { targets: 0,
            visible : false},
        { targets: 1,
            createdCell:  function (td, cellData, rowData) {
               // console.log(rowData.id);
              $(td).attr('data-id',rowData.idprice);
           } },
        { targets: 3,
                render: $.fn.dataTable.render.number(',', '.', '')},
        { targets: 5,
                render: $.fn.dataTable.render.number(',', '.', '')},
        { targets: 7,
            searchable : false},
     ],
    columns: [
        { data: 'idprice'},
        { data: 'category'},
        { data: 'p_name'},
        { data: 'buyprice' },
        { data: 'renew_bp_date' },
        { data: 'sellprice' },
        { data: 'renew_sp_date' },
        { data: 'price_rate' },
        { data: 'remark' },
    ],
});
$(document).ready(function () {
    let table = $('#priceTable').DataTable();

    $('#priceTable tbody').on('click', 'tr', function () {
        let data = table.row(this).data().idprice;
        // alert(table.row(this).data().idstocks);
        $.ajax({
            // type: 'GET',
            url: '/price/api/'+data+'/?format=json',
            dataType: "json",
        });
        window.location.href = '/price/' + data;
    });

});

//삭제
$(function (){
    $("#deletePrice").click(function (){
        Delete("price","deletePrice");
    })
})