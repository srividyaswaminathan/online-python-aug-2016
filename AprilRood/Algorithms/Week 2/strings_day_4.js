function parensValid(str)
{
	parenCount = 0;
	for (i=0; i < str.length; i++)
	{
		if (str[i] == "(")
		{
			parenCount = parenCount + 1;
		}
		if (str[i] == ")")
		{
			parenCount = parenCount - 1;
		}
		if (parenCount < 0)
		{
			return false;
		}
	}

	if (parenCount % 2 == 0)
	{
		return true
	}else{
		return false
	}
}

