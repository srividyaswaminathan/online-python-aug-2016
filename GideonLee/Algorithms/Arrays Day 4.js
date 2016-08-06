// Arrays Day 4

// Skyline Heights
// From lovely Burbank you have a breathtaking view of the 
// Los Angeles skyline. Let’s say you are given an array with 
// heights of consecutive buildings, starting closest to you 
// and extending directly away. Array [-1,7,3] would represent 
// three buildings: first is actually out of view below street 
// level, behind it is second at 7 stories high, third is 3 
// stories high (hidden behind the 7-story). You are situated 
// at street level. Return array containing heights of buildings
//  you can see, in order. Given [1,-1,7,3] return [1,7].

a = [1, -1, 7, 3]; 

function visibleBuildings(arr) {
	var vision = 0; 
	var remove = 0;
	var visible = [];
	for (var i = 0; i < arr.length; i++) {
		if (vision < arr[i]) {
			visible.push(arr[i]);
			vision = arr[i];
		}
	}
	return visible; 
};

console.log(visibleBuildings(a));

// Filter Range
// Alan is good at breaking secret codes. One tool is to eliminate
// numbers he knows are outside a certain specific range. Given
// array and values min and max, remove array values between min 
// and max. Work in-place: return the array you are given, with 
// values in original order. No built-in array functions.

var a = [0, 1, 10, 11, 2, 4, 12, 3, 15, 7, 8, 13, 14, 9]; 

function breakSecret(arr, min, max) {
	var counter = 0; 
	while(counter < arr.length) {
		if (arr[counter] >= min && arr[counter] <= max) {
			for (var i = counter; i < arr.length; i++) {
				arr[i] = arr[i+1];
			}
			arr.length = arr.length-1;
		}	
		else {
			counter++;
		}
	}	
	return arr;
};

//Get rid of all the digits between 10 and 15. 
console.log(breakSecret(a, 10, 15));