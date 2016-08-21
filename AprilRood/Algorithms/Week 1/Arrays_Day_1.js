function pushFront(array1, value){

	array1.unshift(value);
	return array1;

}

function popFront(array1)
{
	newarray = [];
	value = array1[0];
	for (i = 0; i < array1.length; i++)
	{
		if (i > 0) {
			newarray[i-1] = array1[i] 
		}
	}
	return value;
}

function insertAt(array1, index, value)
{
	array1.splice(index, 0, value);
	return array1;
}


