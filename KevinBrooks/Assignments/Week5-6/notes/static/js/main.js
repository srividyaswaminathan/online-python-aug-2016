$(document).ready(function(){
	

	function display_notes(){
		$.get('/notes/get', function(data){

			var note = " <div class='note_container'> \
                <h3>Note_Title</h3> \
                <form id='{{ note_id }}' action='/' class='del_form' method='post'> \
                    <input class='delete' type='submit' value='delete'> \
                </form> \
                <div class='note'> \
                    Note_Data \
                </div> \
                <form action='/' method='post' class='post_note' > \
                    <textarea id='{{ note_id }}' name='note_text' rows='10' cols='39'>Note_Data</textarea> \
                </form> \
            </div> \
			";

			var output = '';
			var full_output = '';
			for (i=0; i < data.length; i++)
			{
				output = note;
				output = output.replace("{{ note_id }}", data[i].id);
				output = output.replace("{{ note_id }}", data[i].id);
				output = output.replace("Note_Title", data[i].title);
				output = output.replace("Note_Data", data[i].description);
				output = output.replace("Note_Data", data[i].description);
				
				full_output += output;
			}

			$('#notes').html(full_output);

		}, 'json')
	}


	$(document).on("click", "div", function(){
		if ($(this).attr("class") == "note"){
			$(this).siblings(".post_note").css("display", "inline-block");
			$(this).css("display", "none");
		}
	})

	$(document).on("focusout", "textarea", function(){
		var id = $(this).attr("id");
		var note = $(this).val();
		update_note(id, note);

		display_notes();
		//$(this).parent().siblings(".note").css("display", "inline-block");	
		//$(this).parent().css("display", "none");
	})

	$(document).on('submit', 'form', function(){
		console.log('deleteing');
		if ($(this).attr("id") == "new_note"){
			$.post('/notes/create', $(this).serialize(), function(res) {
            	
          });	
		}
		else if ($(this).attr("class") == "del_form"){
			var elem_id = $(this).attr("id");
			console.log('/notes/' + elem_id + '/delete');
			$.post('/notes/' + elem_id + '/delete', '', function(res) {
            	
          });	
		}
		
		display_notes();

		return false;
	})

	function update_note(id, note){
		var serialized = "id=" + id + "&note=" + note;
		$.post('/notes/post', serialized, function(res) {
            	
          });	
	}


	display_notes();

});