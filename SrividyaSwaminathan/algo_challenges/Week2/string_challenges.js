//Strings are arrays of characters (more accurately, you can read individual characters the same way you read specific values in a numerical array, and these individual values are strings of length 1).
//However, you cannot write individual characters in a string in this same way. Once a string is defined, individual characters can be referenced by [ ] but not changed. Strings are immutable: 
//they can be completely replaced in their entirety, but not changed piecewise. To manipulate string characters, you must split the string to an array, make individual changes, then join it.
//For the following, feel free to use any of the following built-in functions (not required though!): split, join, concat (look up how to use them in the MDN Documentation).
//Remove blanks

//CHALLENGE 1:
//Create a function that, given a string, returns a string without blanks. Given " play that Funky Music ", returns a string containing "playthatFunkyMusic".

// \s is the regex for white spaces /g is the replacement for the white spaces globally. 
function remove_space(str){
	var new_str = str.replace(/\s/g,'');
	return new_str
}
console.log(remove_space("play that Funky Music"))

//Acronyms
//Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch - gotta pay yer way. ", 
//return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN". The built-in toUpperCase method might be useful here...

function acronym(str){
	var sub_str = str.split(" ")
	var abbr = ""
	for (var i=0; i<sub_str.length;i++ ){		
		var first_letter = sub_str[i][0].toUpperCase();
		// console.log("before append", abbr);
		abbr = abbr+first_letter
		// console.log("after append", abbr);	
	}
	return abbr
}
console.log(acronym("Live from New York, it's Saturday Night!"))

//CHALLENGE2
// Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered palindromes, because (if we ignore spaces, punctuation and capitalization) the letters are 
// the same from back to front. Create a function that returns a boolean indicating whether the string is a strict palindrome. For "a x a" or "racecar", return true. 
// Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
// Next, ignore white space (spaces, tabs, returns), capitalization and punctuation.

function strict_palindrome(str){
	for (var i= str.length-1; i>=str.length/2; i--){
		var given_string = str.toLowerCase()
		console.log(given_string)
		if (given_string[i] != given_string[given_string.length-1-i]){
			return false
		}
	}
	return true	
}


console.log(strict_palindrome("rac e car!"))

function palindrome(str){
	var removeChar = str.replace(/[^A-Za-z0-9]/g, "").toLowerCase()
	console.log("after replacing", removeChar)
	var checkPalindrome = removeChar.split('').reverse().join('')
	console.log("after reversing", checkPalindrome)
	if(removeChar === checkPalindrome){
		return true
	}
	return false
}

console.log(strict_palindrome("Dud!!"))

//CHALLENGE3
//Martin is writing his opus: a book of algorithm challenges, set as lyrics to a suite of baroque fugues. He knows that some of those fugueing challenges will be less popular than others, 
//so he needs a book index. Given a sorted array of pages, produce a book index string. Consecutive pages should form ranges separated by a dash. For [1,3,4,5,7,8,10], return the string "1, 3-5, 7-8, 10".

function book_index(arr) {
	var range_of_pages = [], rstart, rend
	for(var i=0; i<arr.length; i++){
		rstart= arr[i]
		rend = rstart
		while(arr[i+1] - arr[i] ==1){
			rend = arr[i+1]
			i++
		}
		range_of_pages.push(rstart == rend ? rstart+'' : rstart + '-' + rend);
	}
	return range_of_pages.toString()
}

console.log(book_index([1,3,4,5,6,7,8,10]))

//CHALLENGE4
//Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. 
//Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false.

function valid_parentheses(str){
	var count_parantheses = 0;
	for (var i=0; i<str.length; i++){
		if(str[i] == "("){
			count_parantheses+=1
		}
		if(str[i] == ")"){
			count_parantheses -=1
		}
		if (count_parantheses<0){
		return false
	}
}
	return count_parantheses===0	 
	
}	

console.log(valid_parentheses("(3(p)p(3)rs"))