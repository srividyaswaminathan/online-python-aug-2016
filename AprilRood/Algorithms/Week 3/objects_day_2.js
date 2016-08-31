function zipArrayIntoMap(array1, array2)
{
	newarray = [];
	for (i = 0; i < array1.length; i++)
	{
		newarray[array1[i]] = array2[i];
	}
	return newarray;
}


