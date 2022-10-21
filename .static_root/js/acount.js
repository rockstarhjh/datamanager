//데이터 테이블 api 합 구하기 위해 임포트 시켜야하는 코드
jQuery.fn.dataTable.Api.register( 'sum()', function ( ) {
    return this.flatten().reduce( function ( a, b ) {
        if ( typeof a === 'string' ) {
            a = a.replace(/[^\d.-]/g, '') * 1;
        }
        if ( typeof b === 'string' ) {
            b = b.replace(/[^\d.-]/g, '') * 1;
        }

        return a + b;
    }, 0 );
} );

//페이지 준비시 1주일치 거래내역 표시
$(document).ready(function (){
    const today = new Date();
    const day = today.getDate();
    const edate = today.toISOString().substring(0,10);
    const sdate = new Date(new Date().setDate(day - 7)).toISOString().substring(0,10);
    // let year = today.getFullYear(); // 년도
    // let month = today.getMonth() + 1;  // 월
    // let edate = d.toISOString().substring(0,10);  // 날짜
    // let sdate = ago1w.toISOString().substring(0,10);
    // alert(edate);
    // alert(sdate);
    // let day = today.getDay();  // 요일
    $('#acoTable').DataTable( {
        serverSide: true,
        responsive: true,
        // paging: true,
        processing: true,
        order: [[0, 'desc']],
        pageLength:25,
        destroy:true,
        select:true,
        ajax: {
            url: '/acount/api/?date_after='+sdate+'&date_before='+edate+'&format=datatables',
        },
        columnDefs: [
            { targets: 0,
                visible : false},
            { targets: 1,
                createdCell:  function (td, cellData, rowData) {
                   // console.log(row,col);
                  $(td).attr('data-id',rowData.id);
               } },
            { targets: 6,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 7,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 8,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 9,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 11,
                render: $.fn.dataTable.render.number(',', '.', '')},
        ],
        columns: [
            { data: 'id' },
            { data: 'date' },
            { data: 'company' },
            { data: 'product' },
            { data: 'count' },
            { data: 'unit' },
            { data: 'price' },
            { data: 'sumprice' },
            { data: 'tax' },
            { data: 'totalprice' },
            { data: 'inoutcompany' },
            { data: 'incomeprice' },
            { data: 'division' },
            { data: 'paymethod' },
            { data: 'remark' },
        ],
        // drawCallback: function () {
        //     let api = this.api();
        //     let sum = api.column( 9, {search:'applied'} ).data().sum();
        //     // let sum = $('#acoTable').DataTable().column(9).data()
        //     // alert(JSON.stringify(sum))
        // },
        // $('#total').html(sum);
    });

    $('#acoTable tbody').on('dblclick', 'tr', function () {
        let table = $('#acoTable').DataTable();
        // alert(JSON.stringify(table));
        let data = table.row(this).data().id;
        // alert(JSON.stringify(table.row(this).data()));
        $.ajax({
            // type: 'GET',
            url: '/acount/api/'+data+'/?format=json',
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
        window.location.href = '/acount/' + data;
    });

})

//조건 검색
$("#search").click(function (){
    let sdate = $("#searchStartDate").val();
    let edate = $("#searchEndDate").val();
    let com = $("#searchCom").val();
    let product = $("#searchProduct").val();
    let division = $("#searchdivision").val();
    let sum1 = 0;
    let sum2 = 0;
    if (!sdate && !edate && !com && !product &&!division){
        alert("조건을 입력하고 검색하세요. 아니면 데이터가 너무 많아 오래걸립니다.")
        return
    }
    // alert(sdate+edate+com+product+division);
    $('#acoTable').DataTable({
        serverSide: true,
        responsive: true,
        // paging: false,
        processing: true,
        order: [[0, 'desc']],
        // pageLength:25,
        destroy:true,
        select:true,
        ajax: {
            url: '/acount/api/?date_after='+sdate+'&date_before='+edate+'&company='+com+'&product='+product+'&division='+division+'&format=datatables',
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
            { targets: 6,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 7,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 8,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 9,
                render: $.fn.dataTable.render.number(',', '.', '')},
            { targets: 11,
                render: $.fn.dataTable.render.number(',', '.', '')},

            // // 2번째 항목의 넓이를 100px로 설정
            // { targets: 1, width: 100 }
         ],
        columns: [
            { data: 'id' },
            { data: 'date' },
            { data: 'company' },
            { data: 'product' },
            { data: 'count' },
            { data: 'unit' },
            { data: 'price' },
            { data: 'sumprice' },
            { data: 'tax' },
            { data: 'totalprice' },
            { data: 'inoutcompany' },
            { data: 'incomeprice' },
            { data: 'division' },
            { data: 'paymethod' },
            { data: 'remark' },
        ],
        drawCallback: function () {
            let table = $('#acoTable').DataTable();

            table.rows().every( function ( rowIdx, tableLoop, rowLoop ) {
               let data = this.data();
               if(data.division ==="매출"|| data.division ==="매입반품"){
                   sum1 = sum1 + data.totalprice
               }
               if(data.division ==="매입"|| data.division ==="매출반품"){
                   sum2 = sum2 + data.totalprice
               }
            } );
            //전체 합
            let api = this.api();
            $( api.column( 1 ).footer() ).html('Total');
            $( api.column( 2 ).footer() ).html('');
            $( api.column( 3 ).footer() ).html('');
            $( api.column( 4 ).footer() ).html(addComma(api.column( 4, {search:'applied'} ).data().sum()));
            $( api.column( 5 ).footer() ).html('');
            $( api.column( 6 ).footer() ).html(addComma(api.column( 6, {search:'applied'} ).data().sum()));
            $( api.column( 7 ).footer() ).html(addComma(api.column( 7, {search:'applied'} ).data().sum()));
            $( api.column( 8 ).footer() ).html(addComma(api.column( 8, {search:'applied'} ).data().sum()));
            $( api.column( 9 ).footer() ).html(addComma(api.column( 9, {search:'applied'} ).data().sum()));
            $( api.column( 10 ).footer() ).html('');
            $( api.column( 11 ).footer() ).html(addComma(api.column( 11, {search:'applied'} ).data().sum()));
            $( api.column( 12 ).footer() ).html('');
            $( api.column( 13 ).footer() ).html('');
            $( api.column( 14 ).footer() ).html('');
            // $( api.table().footer() ).html(
            //     api.column( 11, {search:'applied'} ).data().sum()
            //   );
            // let sum = api.column( 11, {search:'applied'} ).data().sum();
            // let sum = $('#acoTable').DataTable().column(9).data()
            // alert(JSON.stringify(sum))
            let sum3 = addComma(sum1-sum2);
            sum1 = addComma(sum1);
            sum2 = addComma(sum2);
            $('#tableName').text('조건검색 거래 내역');
            $('#outsum').text('매출 금액 : '+ sum1 +'원');
            $('#insum').text('매입 금액 : '+ sum2 +'원');
            $('#totalsum').text('순이익 금액 : '+ sum3 +'원');
            sum1=0;
            sum2=0;
            sum3=0;
        },
    });
})
$(function (){
	$("#btn_toggle").click(function (){
  	$("#Toggle").toggle();
  });
});

//메세지 출력 시간
window.setTimeout(function() {
    $(".alert-auto-dismissible").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 4000);


//datepicker 한글표시
 $.datepicker.setDefaults({
  dateFormat: 'yy-mm-dd',
  prevText: '이전 달',
  nextText: '다음 달',
  monthNames: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  monthNamesShort: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  dayNames: ['일', '월', '화', '수', '목', '금', '토'],
  dayNamesShort: ['일', '월', '화', '수', '목', '금', '토'],
  dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
  showMonthAfterYear: true,
  yearSuffix: '년'
});
//datepicker 실행
$(function () {
  $('.datepicker').datepicker();
});
function ShowModal(str){
   $('#'+str).modal('show');
}
////폼검색
//거래내역검색
$(function (){
    $('#btn_trans_list').click(function (){
        let com= document.getElementById("id_company").value;
        let product= document.getElementById("id_product").value;
        // alert(com)
        $('#trans_list_modal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            order: [[1, 'desc']],
            // pageLength: -1,
            ajax: {
                url: '/acount/api/?company='+com+'&product='+product+'&format=datatables',
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
                { data: 'date' },
                { data: 'company' },
                { data: 'product' },
                { data: 'count' },
                { data: 'unit' },
                { data: 'price' },
                { data: 'division' },
            ],
                        })
       ShowModal('Modal_list');
})});
$('#trans_list_modal').on('click', 'tbody tr', function (){
    let data = $('#trans_list_modal').DataTable().row($(this)).data().id;
    // alert(data);
    $.ajax({
            // type: 'GET',
            url: '/acount/api/'+data+'/?format=json',
            dataType: "json",
            success: function(data) {
                // alert(data.name)
                $('#id_date').attr('value',data['date']);
                $('#id_date').val(data['date']);
                $('#id_company').attr('value',data['company']);
                $('#id_company').val(data['company']);
                $('#id_product').attr('value',data['product']);
                $('#id_product').val(data['product']);
                $('#id_count').attr('value',data['count']);
                $('#id_count').val(data['count']);
                $('#id_unit').attr('value',data['unit']);
                $('#id_unit').val(data['unit']);
                $('#id_price').attr('value',data['price']);
                $('#id_price').val(data['price']);
                $('#id_sumprice').attr('value',data['sumprice']);
                $('#id_sumprice').val(data['sumprice']);
                $('#id_tax').attr('value',data['tax']);
                $('#id_tax').val(data['tax']);
                $('#id_totalprice').attr('value',data['totalprice']);
                $('#id_totalprice').val(data['totalprice']);
                $('#id_inoutcompany').attr('value',data['inoutcompany']);
                $('#id_inoutcompany').val(data['inoutcompany']);
                $('#id_division').attr('value',data['division']);
                $('#id_division').val(data['division']);
                $('#id_paymethod').attr('value',data['paymethod']);
                $('#id_paymethod').val(data['paymethod']);
                $('#id_remark').attr('value',data['remark']);
                $('#id_remark').val(data['remark']);
            }
        });
    $('#Modal_list').modal('hide')
})
//회사이름 검색
$(function (){
    $('#btn_com').click(function (){
        let com= document.getElementById("id_company").value;
        // alert(com)
        $('#comModal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            // pageLength: -1,
            ajax: {
                url: '/company/api/?company='+com+'&format=datatables',
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
                { data: 'comnum' },
                // { data: 'fax' },
                // { data: 'address' },
                // { data: 'delivery' },
                // { data: 'email' },
                // { data: 'division' },
            ],
                        })
       ShowModal('Modal1');
})});
$('#comModal').on('click', 'tbody tr', function (){
    let data = $('#comModal').DataTable().row($(this)).data().id;
    // alert(data);
    $.ajax({
            // type: 'GET',
            url: '/company/api/'+data+'/?format=json',
            dataType: "json",
            success: function(data) {
                // alert(data.name)
                $('#id_company').attr('value',data.name);
                $('#id_company').val(data.name);
            }
        });
    $('#Modal1').modal('hide')
})
//제품검색
$(function (){
    $('#btn_product').click(function (){
        let product= document.getElementById("id_product").value;
        $('#productModal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            pageLength: -1,
            ajax: {
                url: '/acount/api/?format=datatables&product='+product,
                dataSrc: function(d) {
                    let products =[]
                    return d.data.filter(function(row) {
                     if (!~products.indexOf(row['product'])) {
                       products.push(row['product']);
                       return row;
                     }
                    })
                }
            },
            // drawCallback:function(){
            //         alert('1')
            //         let a = table.column(0).data().unique();
            //         alert(JSON.stringify(a));
            //     },
            columns: [
                // { data: 'id' },
                { data: 'product' },
            ],
                        })
       ShowModal('Modal2');
})});
$('#productModal').on('click', 'tbody tr', function (){
    let data = $('#productModal').DataTable().row($(this)).data();
    // alert(data['product']);
    $('#id_product').attr('value',data['product']);
    $('#id_product').val(data['product']);
    $('#Modal2').modal('hide')
})

$(function (){
    $('#btn_price').click(function (){
        let com= document.getElementById("id_company").value;
        let product= document.getElementById("id_product").value;
        $('#priceModal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            order: [[0, 'desc']],
            // pageLength: -1,
            ajax: {
                url: '/acount/api/?company='+com+'&product='+product+'&format=datatables',
            },
            columnDefs: [
                { targets: 3 , render: $.fn.dataTable.render.number( ',' ) }],
    		// { targets: 3 , render: $.fn.dataTable.render.number( ',' , '.' , 0 , '' , '원' ) }],

            columns: [
                { data: 'date' },
                { data: 'company' },
                { data: 'product' },
                { data: 'price' },
            ],
                        })
       ShowModal('Modal3');
})});
$('#priceModal').on('click', 'tbody tr', function (){
    let data = $('#priceModal').DataTable().row($(this)).data();
    // alert(data['product']);
    $('#id_price').attr('value',data['price']);
    $('#id_price').val(data['price']);
    $('#Modal3').modal('hide');
    CalPrice();
})
//매입처/매출처 검색
$(function (){
    $('#btn_inoutcompany').click(function (){
        let com= document.getElementById("id_company").value;
        if (!com){
            alert('먼저 거래처를 입력해주세요');
                return;
        }
        let product= document.getElementById("id_product").value;
        let com2= document.getElementById("id_inoutcompany").value;
        let division= document.getElementById("id_division").value;
        if(com2==='자사'){
            $('#inoutComModal').DataTable({
            serverSide: true,
            responsive: true,
            searching: false,
            destroy: true,
            order: [[0, 'desc']],
            // pageLength: -1,
            ajax: {
                url: '/acount/api/?&product='+product+'&inoutcompany='+com2+'&format=datatables',
            },
            columnDefs: [
                { targets: 3 , render: $.fn.dataTable.render.number( ',' ) }],
    		// { targets: 3 , render: $.fn.dataTable.render.number( ',' , '.' , 0 , '' , '원' ) }],

            columns: [
                { data: 'date' },
                { data: 'inoutcompany' },
                { data: 'product' },
                { data: 'incomeprice' },
            ],
                        })
        } else {
             if(division ==='매입'||division==='매입반품'){
                    division = '매출';
                } else{
                    division = '매입'
                }
            $('#inoutComModal').DataTable({
                serverSide: true,
                responsive: true,
                searching: false,
                destroy: true,
                order: [[0, 'desc']],
                // pageLength: -1,
                ajax: {
                    url: '/acount/api/?division=' + division + '&product=' + product + '&format=datatables',
                },
                columnDefs: [
                    {targets: 3, render: $.fn.dataTable.render.number(',')}],
                // { targets: 3 , render: $.fn.dataTable.render.number( ',' , '.' , 0 , '' , '원' ) }],

                columns: [
                    {data: 'date'},
                    {data: 'company'},
                    {data: 'product'},
                    {data: 'price'},
                ],
            })
        }
       ShowModal('Modal4');
})});
$('#inoutComModal').on('click', 'tbody tr', function (){
    let data = $('#inoutComModal').DataTable().row($(this)).data();
    if(data['company']) {
        $('#id_inoutcompany').attr('value', data['company']);
        $('#id_inoutcompany').val(data['company']);
        $('#id_incomeprice').attr('value', data['price']);
        $('#id_incomeprice').val(data['price']);
        $('#Modal4').modal('hide');
    } else{
        $('#id_inoutcompany').attr('value', data['inoutcompany']);
        $('#id_inoutcompany').val(data['inoutcompany']);
        $('#id_incomeprice').attr('value', data['incomeprice']);
        $('#id_incomeprice').val(data['incomeprice']);
        $('#Modal4').modal('hide');
    }
})

$( document ).ready( function() {
    $( '#id_count, #id_price' ).on("property-change  change keyup paste input", function() {
      CalPrice();
    } );
} );
function CalPrice(){
  let a = $( '#id_count' ).val();
  let b = $( '#id_price' ).val();
  let ab = a * b;
  $('#id_sumprice').val(ab)
  // $('#id_price').text(Number(b).toLocaleString('ko-KR'));
  // $('#id_sumprice').text(Number(ab).toLocaleString('ko-KR'));
  // $('#id_sumprice').val(addComma2('#id_sumprice', ab));

  $('#id_tax').val(ab*0.1);

  $('#id_totalprice').val(Math.round(ab*1.1));
  // alert(addComma2('#id_sumprice', ab))
  //   alert(ab)
}
//삭제
$(function (){
    $("#deleteAco").click(function (){
        Delete("acount","deleteAco");
    })
})

//거래명세서
$("#transaction").click(function (){
    let data = $("#acoTable").DataTable().rows({ selected: true }).data();
    // alert(JSON.stringify(data))
    // alert(data.length)
    // alert(data[0]['company'])
    for(let i=0; i<data.length; i++){
        if(data[0]['company'] !==data[i]['company'] ){
            alert('다른거래처들을 선택했습니다.');
            return;
        }
    }
    $.ajax({
        url : '/company/api/?company='+data[0]['company'],
        // type : 'POST',
        dataType: "json",
        // data : data,
        success : function (response, status, xhr){
            // alert(response.results[0].name)
            // alert(data[0]['company'])
            // alert(response.results)
            // alert(response.results[0].id)
            let comData;
            if (!response.results||response.results.length ===0){
                // alert(data[0]['company']);
                comData = data[0]['company'];
            }else{
                comData = response.results;
            }

            // alert(JSON.stringify(data))
            let url = '/acount/transaction/';
            post(url, data, comData);
        }
            // window.location.href = 'http://127.0.0.1:8000/acount/transaction/'
    })
})
//ajax로 폼 post
/* https://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit */
function post(path, acoData, comData, method='post') {

  // The rest of this code assumes you are not using a library.
  // It can be made less verbose if you use one.
  const form = document.createElement('form');
  form.method = method;
  form.action = path;
  let sumpricesum = 0;
  let taxsum = 0;
  let totalpricesum;
  // alert(csrf)
    //csrf 토큰 문제 해결
   let csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
      csrfInput.name = 'csrfmiddlewaretoken';
      csrfInput.value = csrf;
      form.appendChild(csrfInput)
  // form.appendChild(csrfInput)
  //   alert(comData)
    if (typeof comData === 'object') {
        // alert('1')
        $.each(comData[0], function (key, value) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = 'com_' + key;
            hiddenField.value = value;
            form.appendChild(hiddenField);
            // console.log('키 : '+key + ', 값 :' + value);
        });
    }else{
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = 'com_name';
        hiddenField.value = comData;
        form.appendChild(hiddenField);
    }

    for (let i=0; i<acoData.length; i++){
        $.each(acoData[i], function (key, value){
            const hiddenField2 = document.createElement('input');
            hiddenField2.type = 'hidden';
            hiddenField2.name = 'aco_'+key;
            hiddenField2.value = value;
            form.appendChild(hiddenField2);
            if (key==='sumprice'){
                sumpricesum = sumpricesum + value;
            }
            if(key ==='tax'){
                taxsum = taxsum+ value;
            }
            // console.log('키 : '+key + ', 값 :' + value);
        })
    }
    totalpricesum = sumpricesum + taxsum;
    const hiddenField3 = document.createElement('input');
    hiddenField3.type = 'hidden';
    hiddenField3.name = 'aco_sumpricesum';
    hiddenField3.value = sumpricesum;
    form.appendChild(hiddenField3);
    const hiddenField4 = document.createElement('input');
    hiddenField4.type = 'hidden';
    hiddenField4.name = 'aco_taxsum';
    hiddenField4.value = taxsum;
    form.appendChild(hiddenField4);
    const hiddenField5 = document.createElement('input');
    hiddenField5.type = 'hidden';
    hiddenField5.name = 'aco_totalpricesum';
    hiddenField5.value = totalpricesum;
    form.appendChild(hiddenField5);
    // alert(sumpricesum+':'+taxsum+':'+totalpricesum);
    document.body.appendChild(form);

  // for (const key in params) {
  //   if (params.hasOwnProperty(key)) {
  //     const hiddenField = document.createElement('input');
  //     hiddenField.type = 'hidden';
  //     hiddenField.name = key;
  //     hiddenField.value = params[key];
  //
  //     form.appendChild(hiddenField);
  //   }
  // }

  // document.body.appendChild(form);
  form.submit();
}
//천단위 콤마 펑션
   function addComma(value){
        value = value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        return value;
    }
