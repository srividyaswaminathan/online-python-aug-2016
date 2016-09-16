

function removeBlanks(str)
{
	newString = (str.split(" ")).join("");
	return newString;
}

function acronyms(str)
{
	array = (str.split(" "));
	newString = "";
	for (i = 0; i < array.length; i++)
	{
		newString = newString + array[i].charAt(0).toUpperCase();
	}
	return newString;
}

