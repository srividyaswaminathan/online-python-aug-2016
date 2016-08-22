function isPalindromeStrict(str)
{
	palindrome = false;
	chkLen = str.length - 1;
	for (i = 0; i < ((str.length)/2); i++)
	{
		if (str[i] == str[chkLen - i])
		{
			palindrome = true;
		}else{
			return false;
		}
	}
	return palindrome;
}

function isPalindrome(str)
{
	palindrome = false;
	newstr = (str.replace(/[\W]/g,"")).toUpperCase();
	chkLen = newstr.length - 1;
	for (i = 0; i < ((newstr.length)/2); i++)
	{
		if (newstr[i] == newstr[chkLen - i])
		{
			palindrome = true;
		}else{
			return false;
		}
	}
	return palindrome;
}

