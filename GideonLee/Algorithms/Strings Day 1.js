// Remove blanks
// Create a function that, given a string, returns a string without blanks. 
// Given " play that Funky Music ", returns a string containing "playthatFunkyMusic".
var string = ' play that Funky Music '; 

//Using Regular Expressions
function removeBlanks1(str){
	return str.replace(/\s/g, '');
};

console.log(removeBlanks1(string));

//Using for loops
function removeBlanks2(str) {
	var newStrArr = [];
	var newStr = ''; 
	for (var i = 0; i < str.length; i++) {
		if (str[i] !== ' ') {
			newStrArr.push(str[i]);
		}
	}
	for (var i = 0; i < newStrArr.length; i++) {
		newStr += newStrArr[i];
	}
	return newStr;
};

console.log(removeBlanks2(string));



// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". Given 
// "Live from New York, it's Saturday Night!", return "LFNYISN". The built-in toUpperCase method might be useful here...
var string1 = "Live from New York, It's Saturday Night!";
var string2 = " there's no free lunch - gotta pay yer way. ";

function acronym(str){
	str = str.toUpperCase();
	var arr = [];
	var isBlank = false; 
	for (var i = 0; i < str.length; i++) {
		if (isBlank === false && str[i] !== ' ') {
			arr.push(str[i]);
			isBlank = true; 
		}
		else if (str[i] === ' ') {
			isBlank = false;
		}
	}
	var acrStr = '';
	for (var i = 0; i < arr.length; i++) {
		acrStr += arr[i];
	}
	return acrStr;
};

console.log(acronym(string1));
console.log(acronym(string2));