// Is Palindrome

// Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered
// palindromes, because (if we ignore spaces, punctuation and capitalization) the letters
// are the same from back to front. Create a function that returns a boolean indicating 
// whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do 
// not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
var str1 = 'a x a';
function isStrictPalindrome(str) {
	for (var i = 0; i < str.length/2; i++) {
		if (str[i] !== str[str.length-1-i]) {
			return false; 
		}
	}
	return true;
};

if (isStrictPalindrome(str1)) {
	console.log('"' + str1 + '"' + ' is a strict palidrome.');
}
else {
	console.log('"' + str1 + '"' + ' is not a strict palidrome.');
}


// 	Next, ignore white space (spaces, tabs, returns), capitalization and punctuation.
var str2 = '....K-L?a-g,_g Al,,,,,,,****-k'
function isPalidrome(str) {
	str = str.toLowerCase().replace(/[\W_]+/g, '');
	for (var i = 0; i < str.length/2; i++) {
		if (str[i] !== str[str.length-1-i]) {
			return false; 
		}
	}
	return true; 
};

if (isPalidrome(str2) === true) {
	console.log('"' + str2 + '"' + ' is a loose palidrome.');
}
else {
	console.log('"' + str2 + '"' + ' is not a loose palidrome.');
}
