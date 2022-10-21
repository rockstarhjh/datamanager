$('#comTable').DataTable( {
    serverSide: true,
    responsive: true,
    // "processing": true,
    ajax: {
        url: '/company/api/?format=datatables',
        // dataType:'json',
        // dataSrc:'',
        // dataSrc :'data',
        // dataSrc: function (res) {
        //     let data = res.data;
        //
        //     return data
        //     }
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

        // // 2번째 항목의 넓이를 100px로 설정
        // { targets: 1, width: 100 }
 ],
    columns: [
        { data: 'id' },
        { data: 'name' },
        { data: 'tel' },
        { data: 'fax' },
        { data: 'address' },
        { data: 'delivery' },
        { data: 'email' },
        { data: 'division' },
    ],
});

$(document).ready(function () {
    let table = $('#comTable').DataTable();

    $('#comTable tbody').on('click', 'tr', function () {
        let data = table.row(this).data().id;
        // alert(data);
        $.ajax({
            // type: 'GET',
            url: '/company/api/'+data+'/?format=json',
            dataType: "json",
            success: function(data) {
                if (data) {
                    // console.log(data.name)
                    // showComdata(data);
                    // window.location.href = data.redirect;
                } else {
                    // data.form contains the HTML for the replacement form
                    // $("#myform").replaceWith(data.form);
                }
    }

});
        window.location.href = '/company/' + data;
    });

    // document.getElementById ("delete").addEventListener ("click", Delete, false);

});
function Delete(str, eId){
    let id=document.getElementById(eId).value;
    if(confirm("삭제하시겠습니까?")){
   $.ajax({
       url: '/'+str+'/' + id + '/',
       type: 'delete',

       success: function (result) {
           if (result.status){
               // let url = '{% url company:com-list%}';
               // alert(url)
               alert('삭제되었습니다.')
               window.location.replace('/'+str)
           }
       },
       error: function (request) {
           // alert(data);
           alert("code:" + request.status);
       },
   })}}
$(function (){
    $("#deleteCom").click(function (){
        Delete("company","deleteCom");
    })
})
// $('#btn_toggle').click(function (){
//
//     alert("1");
//     $("#Toggle").toggle();
//
// })


// window.setTimeout(function() {
//     $(".alert-auto-dismissible").fadeTo(500, 0).slideUp(500, function(){
//         $(this).remove();
//     });
// }, 4000);


