function balancePoint(array)
{
	totalSum = 0;
	for (i = 0; i < array.length; i++)
	{
		totalSum = totalSum + array[i];
	}
	reverseSum = 0;
	for (i = 1; i <array.length; i++)
	{
		reverseSum = reverseSum + array[array.length - i]
		if (reverseSum == totalSum-reverseSum)
			{
				return true;
			} 
	}
	return false;
} 


function balanceIndex(array)
{
	totalSum = 0;
	for (i = 0; i < array.length; i++)
	{
		totalSum = totalSum + array[i];
	}
	leftCount = array[0];
	rightCount = totalSum - leftCount;
	for (i = 1; i < array.length; i++)
	{
		if (leftCount == (rightCount - array[i]))
		{
			return i;
		} else {
			leftCount = leftCount + array[i];
			rightCount = totalSum - leftCount;
		}
	}
	return -1;
} 


