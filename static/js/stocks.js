$('#stocksTable').DataTable( {
    serverSide: true,
    responsive: true,
    order: [[1, 'desc']],
    destroy:true,
    // "processing": true,
    ajax: {
        url: '/stocks/api/?format=datatables',
    },
    columnDefs: [
        //1번재 항목 열을 숨김
        { targets: 0,
            visible : false},
        { targets: 11,
            visible : false},
        { targets: 1,
            createdCell:  function (td, cellData, rowData) {
               // console.log(rowData.id);
              $(td).attr('data-id',rowData.idstocks);
           } },

 ],
    columns: [
        { data: 'idstocks' },
        { data: 'date' },
        { data: 'category' },
        { data: 'p_name' },
        { data: 'company' },
        { data: 'in_field' },
        { data: 'out_field' },
        { data: 'return_field' },
        { data: 'lost_field' },
        { data: 'location' },
        { data: 'remark' },
        { data: 'idproducts', name : 'idproducts.idproducts' },
    ],
});
//재고 내역 테이블 클릭시 수정화면으로 이동
$(document).ready(function () {
    let table = $('#stocksTable').DataTable();

    $('#stocksTable tbody').on('click', 'tr', function () {
        let data = table.row(this).data().idstocks;
        // alert(table.row(this).data().idstocks);
        $.ajax({
            // type: 'GET',
            url: '/stocks/api/'+data+'/?format=json',
            dataType: "json",
        });
        window.location.href = '/stocks/' + data;
    });

});

//제품검색
$(function (){
    $('#btn_p_name').click(function (){
        let p_name= document.getElementById("id_p_name").value;
        // alert(com)
        $('#p_nameModal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            // pageLength: -1,
            ajax: {
                url: '/products/api/?p_name='+p_name+'&format=datatables',
            },
            columnDefs: [
                //1번재 항목 열을 숨김
                { targets: 0,
                    visible : false},
                { targets: 1,
                    createdCell:  function (td, cellData, rowData) {
                       // console.log(row,col);
                      $(td).attr('data-id',rowData.id);
                   } },
                // { targets: 3,
                //     visible : false},
                // { targets: 4,
                //     visible : false},
                // { targets: 5,
                //     visible : false},
                ],
            columns: [
                { data: 'idproducts' },
                { data: 'category' },
                { data: 'p_name' },
                // { data: 'fax' },
                // { data: 'address' },
                // { data: 'delivery' },
                // { data: 'email' },
                // { data: 'division' },
            ],
                        })
       ShowModal('Modal5');
})});
//모달 클릭시 값 폼에 넣고 모달 닫기
$('#p_nameModal').on('click', 'tbody tr', function (){
    let data = $('#p_nameModal').DataTable().row($(this)).data().idproducts;
    // alert(JSON.stringify(data));
    $.ajax({
            // type: 'GET',
            url: '/products/api/'+data+'/?format=json',
            dataType: "json",
            success: function(data) {
                // alert(data.name)
                $('#id_category').attr('value',data.category);
                $('#id_category').val(data.category);
                $('#id_p_name').attr('value',data.p_name);
                $('#id_p_name').val(data.p_name);
                $('#id_idproducts').val(data.idproducts);
            }
        });
    $('#Modal5').modal('hide')
})
//삭제
$(function (){
    $("#deleteStocks").click(function (){
        Delete("stocks","deleteStocks");
    })
})
