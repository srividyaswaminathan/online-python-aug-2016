$(document).ready(function(){
	$('p:nth-child(2)').hover(function(){
		$('#message').show();
	}, function(){
		$('#message').hide();
	});
});