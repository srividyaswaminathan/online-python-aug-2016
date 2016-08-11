// Parens Valid
// Create a function that, given an input string str, returns a 
// boolean whether parentheses in str are valid. Valid sets of 
// parentheses always open before they close, for example. For 
// "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: 
// not every parenthesis is closed. Given "N(0)t )0(k", return false.

var str = "()(0-)(1(2)3)4";

function parensValid(str) {
	var arr = []; 
	var parens = 0; 
	for (var i = 0; i < str.length; i++) {
		if (str[i] === '(' || str[i] === ')') {
			arr.push(str[i]);
		}
	}
	if (arr[0] === ')') {
		return false;
	}
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] === '(') {
			parens++; 
		}
		else if (arr[i] === ')') {
			parens--;
		}
	}
	if (parens === 0) {
		return true;
	}		
	return false; 
};

console.log(parensValid(str));