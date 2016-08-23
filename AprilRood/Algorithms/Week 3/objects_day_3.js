function mostRepeatedCharacter(str)
{
	letterList = [];
	maxLetter = 0;
	letterChk = "";

	for (i=0; i < str.length; i++)
	{
		if (letterList[str[i]])
		{
			letterList[str[i]] += 1;
			if (letterList[str[i]] > maxLetter)
			{
				maxLetter = letterList[str[i]];
				letterChk = str[i];
			}
		}else{
			letterList[str[i]] = 1;
		}
	}
	return  letterChk + " is used " + maxLetter.toString() + " times.";
}



