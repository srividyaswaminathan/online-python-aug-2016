$(document).ready(function(){
	
	$('form').on('submit', function(){
		$('#result').html('');
		$('#wait').css('display', 'block');	
		$.post('/directions', $(this).serialize(), function(data) {
              console.log(data);
              if (data.status != "INVALID_REQUEST"){
                var output = '<h4>Directions from {0} to {1}</h4>';
                output = output.replace('{0}', data.routes[0].legs[0].start_address);
                output = output.replace('{1}', data.routes[0].legs[0].end_address);  

                for (i=0; i < data.routes[0].legs[0].steps.length; i++){
                  output += '<p>' + data.routes[0].legs[0].steps[i].html_instructions + '</p>';  
                }
                
              }
              else{
                output = "<h4>Could not find address.</h4>" 
              }
              
              
              $('#result').html(output);

          },'json');
		return false;
	})

	$(document).ajaxStop(function () {
		  	$('#wait').css('display', 'none');	
  	});

});