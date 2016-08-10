$(document).ready(function(){

	var title = $(document).attr('title');
	var description = $("meta[name='description']").attr("content");
	$(".main_paragraph").html(title + " : " + description);



});