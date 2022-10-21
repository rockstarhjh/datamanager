$(document).ready(function() {

			//datepicker 한국어로 사용하기 위한 언어설정
			$.datepicker.setDefaults($.datepicker.regional['ko']);

			// Datepicker
			$(".datepicker").datepicker({
				showButtonPanel: true,
				dateFormat: "yy-mm-dd",
				onClose : function ( selectedDate ) {

					let eleId = $(this).attr("id");
					let optionName = "";

					if(eleId.indexOf("StartDate") > 0) {
						eleId = eleId.replace("StartDate", "EndDate");
						optionName = "minDate";
					} else {
						eleId = eleId.replace("EndDate", "StartDate");
						optionName = "maxDate";
					}

					$("#"+eleId).datepicker( "option", optionName, selectedDate );
					$(".searchDate").find(".chkbox2").removeClass("on");
				}
			});

			//시작일.
			/*$('#searchStartDate').datepicker("option","onClose", function( selectedDate ) {
				// 시작일 datepicker가 닫힐때
				// 종료일의 선택할수있는 최소 날짜(minDate)를 선택한 시작일로 지정
				$("#searchEndDate").datepicker( "option", "minDate", selectedDate );
				$(".searchDate").find(".chkbox2").removeClass("on");
			});
			*/

			//종료일.
			/*$('#searchEndDate').datepicker("option","onClose", function( selectedDate ) {
				// 종료일 datepicker가 닫힐때
				// 시작일의 선택할수있는 최대 날짜(maxDate)를 선택한 종료일로 지정
				$("#searchStartDate").datepicker( "option", "maxDate", selectedDate );
				$(".searchDate").find(".chkbox2").removeClass("on");
			});
			*/

			$(".dateclick").dateclick();	// DateClick
			$(".searchDate").schDate();		// searchDate

		});

		// Search Date
		jQuery.fn.schDate = function(){
			let $obj = $(this);
			let $chk = $obj.find("input[type=radio]");
			$chk.click(function(){
				$('input:not(:checked)').parent(".chkbox2").removeClass("on");
				$('input:checked').parent(".chkbox2").addClass("on");
			});
		};

		// DateClick
		jQuery.fn.dateclick = function(){
			let $obj = $(this);
			$obj.click(function(){
				$(this).parent().find("input").focus();
			});
		}


		function setSearchDate(start){

			let num = start.substring(0,1);
			let str = start.substring(1,2);

			let today = new Date();

			//var year = today.getFullYear();
			//var month = today.getMonth() + 1;
			//var day = today.getDate();

			let endDate = $.datepicker.formatDate('yy-mm-dd', today);
			$('#searchEndDate').val(endDate);

			if(str == 'd'){
				today.setDate(today.getDate() - num);
			}else if (str == 'w'){
				today.setDate(today.getDate() - (num*7));
			}else if (str == 'm'){
				today.setMonth(today.getMonth() - num);
				today.setDate(today.getDate() + 1);
			}else if (str =='y'){
				today.setFullYear(today.getFullYear()-num)
				today.setMonth(today.getMonth());
				today.setDate(today.getDate());
			}

			let startDate = $.datepicker.formatDate('yy-mm-dd', today);
			$('#searchStartDate').val(startDate);

			// 종료일은 시작일 이전 날짜 선택하지 못하도록 비활성화
			$("#searchEndDate").datepicker( "option", "minDate", startDate );

			// 시작일은 종료일 이후 날짜 선택하지 못하도록 비활성화
			$("#searchStartDate").datepicker( "option", "maxDate", endDate );

		}
