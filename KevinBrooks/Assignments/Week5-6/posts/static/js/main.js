$(document).ready(function(){
	
	function display_posts(){
		$.get('/posts/get', function(data){

			var output = '';
			for (i=0; i < data.length; i++)
			{
				output += "<p>" + data[i].description + "</p>";
			}

			$('#posts').html(output);

		}, 'json')
	}

	$('form').submit(function(){
		
		$.post('/posts/create', $(this).serialize(), function(res) {
            	
          });

		display_posts();

		return false;
	})

	display_posts();

});