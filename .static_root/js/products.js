$('#productsTable').DataTable( {
    serverSide: true,
    responsive: true,
    // order: [[1, 'desc']],
    destroy:true,
    // "processing": true,
    // paging : false,
    ajax: {
        url: '/products/api/?format=datatables',
    },
    columnDefs: [
        //1번재 항목 열을 숨김
        { targets: 0,
            visible : false},
        { targets: 1,
            createdCell:  function (td, cellData, rowData) {
               // console.log(rowData.id);
              $(td).attr('data-id',rowData.idproducts);
           } },
        { targets: 3,
            searchable : false},
        { targets: 4,
            searchable : false},
        { targets: 5,
            searchable : false},

 ],
    columns: [
        { data: 'idproducts'},
        { data: 'category' },
        { data: 'p_name' },
        { data: 'office_stock' },
        { data: 'warehouse_stock' },
        { data: 'total_stock' },
    ],
});