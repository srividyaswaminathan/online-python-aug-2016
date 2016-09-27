$(document).ready(function(){
	
	function display_result(data){
		var output = "<h1>";
		if (data.cod == 404){
			output += "Unrecognized city.</h1>";
		}
		else{
			output += data.name + "</h1>";
			output += "<h2>" + data.main.temp + "&deg;</h2>";
		}

		$("#result").html(output);
	}

	var api_key = '&APPID=dddaf915ffce0d65d8041cd554cdf203';
	var api_base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

	$('form').submit(function() {
        var url = api_base_url + $('#city').val() + "&units=imperial" + api_key;
        console.log(url);
        $.get(url, function(res) {
            display_result(res);
        }, 'json');
        
        return false;
    });

});