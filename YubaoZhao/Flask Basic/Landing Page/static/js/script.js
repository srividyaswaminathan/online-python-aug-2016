

$(document).ready(function(){
	console.log("hello!");
	$("img#yellow").hover(function(){
		$("span#yellow").toggle();
	});
	$("img#black").hover(function(){
		$("span#black").toggle();
	});
});