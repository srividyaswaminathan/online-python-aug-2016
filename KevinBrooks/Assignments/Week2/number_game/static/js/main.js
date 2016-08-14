function validate_number()
{
	if (isNaN($("#txt_guess").val()))
	{
		$("#message").html("Invalid Number");
		return false;
	}
	return true;
}

$(document).ready(function(){

	
});