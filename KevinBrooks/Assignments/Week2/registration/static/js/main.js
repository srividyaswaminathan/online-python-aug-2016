$(document).ready(function(){

	function display_form(type){
		if (type == 'ninja'){
			$("#div_ninja").css("display","block");
			$("#div_hacker").css("display","none");
			$("#regtype_ninja").attr("checked","true");
			$("#regtype_hacker").removeAttr("checked");
		}
		else{
			$("#div_ninja").css("display","none");
			$("#div_hacker").css("display","block");
			$("#regtype_ninja").removeAttr("checked");
			$("#regtype_hacker").attr("checked","true");
		}
	}

	$( '#birth_date' ).datepicker();
	$("#form_hacker").css("height","175px");
	display_form($("#sel_type").val().toLowerCase());
	

	$( '.reg_type' ).on('change', function(){
		display_form($(this).val().toLowerCase());
	})

});