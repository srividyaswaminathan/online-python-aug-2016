$(document).ready(function(){
	
	$('form').on('submit', function(){
		$('#result').html('');
		$('#wait').css('display', 'block');	
		$.post('/movie', $(this).serialize(), function(data) {
            	if (data.resultCount > 0){
            		output = "<video controls src='" +
                               data.results[0].previewUrl +
                               "'></video>";
                    $('#result').html(output);
            	}
            	else{
            		$('#result').html("<h3>Artist Not Found.</h3>")
            	}

          },'json');
		return false;
	})

	$(document).ajaxStop(function () {
		console.log('done')
      	$('#wait').css('display', 'none');	
  	});

});