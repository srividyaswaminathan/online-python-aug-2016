$(document).ready(function(){
	var languages = ['c#','Python','Javascript', 'C++', 'Other'];
	var locations = ['Seattle', 'San Francisco', 'World-Online', 'Other'];
	var lang = $('#fav_lang').attr("value");
	var loc = $('#dojo_location').attr("value");

	for (i = 0; i < languages.length; i++){
		selected = lang == languages[i] ? "selected" : "";
		$('#fav_lang').append("<option value='" + languages[i] + "'" + selected + ">" + languages[i] + "</option>");	
	}
	
	for (i = 0; i < locations.length; i++){
		selected = loc == locations[i] ? "selected" : "";
		$('#dojo_location').append("<option value='" + locations[i] + "'" + selected + ">" + locations[i] + "</option>");	
	}

});