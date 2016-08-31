function bookIndex(array)
{
	newStr = [];
	listStart = array[0];
	for (i = 0; i < array.length; i++)
	{
		if (array[i+1] != array[i] + 1)
		{
			if (array[i] == listStart)
			{
				newStr.push(array[i])
				listStart = array[i+1]
			}else{
				newStr.push(listStart + "-" + array[i])
				listStart = array[i+1]
			}
		}
	}
	return newStr	
}
