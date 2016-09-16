// Objects Day 3
// Most Repeated Character
// Given a string, return the character that's used most 
// often, along with the number of times it's repeated.

var str = 'acbabddbc';

function mostRepeated(str) {
	var obj = {}; 
	var counter;  
	var frequency = 1;
	var character = str[0];
	for (var i = 0; i < str.length; i++) {
		counter = 1;
		for (var j = i+1; j < str.length; j++) {
			if (str[i] === str[j]) {
				counter++
			}
		}
		if (counter > frequency) {
			frequency = counter; 
			character = str[i];
		}
	}
	return 'Character: ' + character + '. It comes up: ' + frequency;
};

console.log(mostRepeated(str));