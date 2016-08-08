//Print 1-255
function printAll() {
	for (var i = 1; i <= 255; i++) {
		console.log(i);
	}
};

// printAll();


// Print all odd int 1-255
function printOdd() {
	for (var i = 1; i <= 255; i+=2) {
		console.log(i);
	}
};

// printOdd();


// Print integers from 0 to 255, and with each integer print the sum so far.
function printAndSum() {
	var sum = 0; 
	for (var i = 0; i <= 255; i++) {
		sum += i;
		console.log('Integer: ' + i + '. Current sum: ' + sum);
	}
};

// printAndSum();


// Iterate through a given array, printing each value.
var arr = [10, 11, 12, 13, 14, 15];

function iterateArray(arr) {
	for (var i = 0; i < arr.length; i++) {
		console.log(arr[i]);
	}
};

// iterateArray(arr);


// Find and Print Max, given an array, find and print its largest element.
function findMax(arr) {
	var max = arr[0];
	for (var i = 1; i < arr.length; i++) {
		if (max < arr[i]) {
			max = arr[i]; 
		}
	}
	return(max);
};

// console.log(findMax(arr));


// Get and Print Average
// Analyze an array’s values and print the average.
function printAverage(arr) {
	var sum = 0; 
	for (var i = 0; i < arr.length; i++) {
		sum += arr[i]; 
	}
	return sum/arr.length; 
};

// console.log(printAverage(arr));


// Array with Odds
// Create an array with all the odd integers between 1 and 255 (inclusive).
function createOdd() {
	var arr = [];
	for (var i = 1; i <= 255; i+=2) {
		arr.push(i);
	}
	return arr;
};

// console.log(createOdd(arr));


// Square the Values
// Square each value in a given array, returning that same array with changed values.
function squareValues(arr) {
	for (var i = 0; i < arr.length; i++) {
		arr[i] = arr[i] * arr[i]; 
	}
	return arr; 
};

// console.log(squareValues(arr));


// Greater than Y
// Given an array and a value Y, count and print the number of array values greater than Y.
function greaterThan(arr, y) {
	var count = 0; 
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] > y) {
			count++; 
			console.log(arr[i]);
		}
	}
	console.log('Number greater than ' + y + ' is: ' + count);
};

// greaterThan(arr, 12);


// Zero Out Negative Numbers
// Return the given array after setting any negative values to zero.
var arr = [-10, 1, 20, -5, 35, -2, 8];
function zeroNegatives(arr) {
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] < 0) {
			arr[i] = 0; 
		}
	}
	return arr; 
};

// console.log(zeroNegatives(arr));


// Max, Min, Average
// Given an array, print the max, min and average values for that array.
function findMaxMinAvg(arr) {
	var min = arr[0];
	var max = arr[0];
	var avg = 0; 
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
		else if (arr[i] > max) {
			max = arr[i]; 
		}
		avg += arr[i]; 
	}
	console.log('Min: ' + min);
	console.log('Max: ' + max);
	console.log('Avg: ' + avg/arr.length);
};

// findMaxMinAvg(arr);


// Shift Array Values
// Given an array, move all values forward by one index, dropping the first and leaving a 0 value at the end.
var arr = [50, 75, 100, 125, 150]; 
function shiftArrayValues(arr) {
	for (var i = 0; i < arr.length; i++) {
		arr[i] = arr[i+1]; 
	}
	arr[arr.length-1] = 0; 
	return arr;
};

// console.log(shiftArrayValues(arr));


// Swap String For Array Negative Values
// Given an array of numbers, replace any negative values with the string 'Dojo'.
var arr = [0, -1, 20, -5, -7, 30]; 
function dojoForNegatives(arr) {
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] < 0) {
			arr[i] = 'Dojo'
		}
	}
	return arr; 
};

// console.log(dojoForNegatives(arr));