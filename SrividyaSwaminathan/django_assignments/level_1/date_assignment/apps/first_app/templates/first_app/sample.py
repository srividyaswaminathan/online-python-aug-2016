import random
import string
def random_word_generator(size, random_string = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(random_string) for _ in range(size))

print random_word_generator(13, string.ascii_uppercase + string.digits )	


	$(document).ready(function(){
					var attempt = 1;
					$('form.random_word').submit( function() {
						$.post($(this).attr('action'), $(this).serialize(), function(response) {
							var html_str = "Attempt#" + attempt + "<br/>";
							html_str +=response
							$('div#random').html(html_str);
						});
						attempt++;
						return false;
						//$(".show_attempt").html("<p>Random Word Generator: Attempt "+attempt+ " </p>" 
						
					})

				})