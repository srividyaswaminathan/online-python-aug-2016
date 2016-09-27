$(document).ready(function(){
	
	function display_stats(data, img){
		var output = "<h1>" + data.name + "</h1>";
		output += img;
		output += "<p><b>Types</b></p>";
		output += "<ul>";
		for (i = 0; i < data.types.length; i++){
			output += "<li>" + data.types[i].name + "</li>";
		}
		output += "</ul>";
		output += "<p><b>Height</b></p>";
		output += "<p id='stat'>" + data.height + "</p>";
		output += "<p><b>Weight</b></p>";
		output += "<p id='stat'>" + data.weight + "</p>";

		$("#stats").html(output);
	}

	var output = '';
	for (i = 1; i < 152 ; i++){
		output += "<img src='http://pokeapi.co/media/img/{0}.png' alt='pokemon - {0}' id='{0}'>".split('{0}').join(String(i));
	}

	$("#imgs").html(output);

	$("img").on('click', function(){
		var id = $(this).attr('id')
		var img = "<img src='http://pokeapi.co/media/img/{0}.png' alt='pokemon - {0}' id='{0}'>".split('{0}').join(String(id));
		var api_query = "http://pokeapi.co/api/v1/pokemon/{0}/".replace('{0}', String(id));
		$.get(api_query, function(res){
			display_stats(res, img);
		}, "json");
	})

});