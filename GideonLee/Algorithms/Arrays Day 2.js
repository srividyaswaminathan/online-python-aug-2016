// Arrays Day 2

// Remove At
// Given array and an index into array, remove and return the array value at that index. 
// Do this without using built-in array methods except pop(). Think of PopFront(arr) as 
// equivalent to RemoveAt(arr,0).

var arr = [1, 2, 3, 4, 5];
var index = 2;

function removeAt(arr, index) {
	for (var i = 0; i < arr.length; i++) {
		if (i < index) {
			continue; 
		}
		else {
			arr[i] = arr[i+1];
		}
	}
	arr.length = arr.length-1;  // arr.pop();
	return arr; 
};

console.log(removeAt(arr, index));



// Swap Array Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not 
// change final element. For [1,2,3,4], return [2,1,4,3]. For [false,true,42], return [true,false,42].

var oddList = [1, 2, true, false, 0];
var evenList = ['will', 'This', 'sense', 'make']; 

function swapArrayPairs(arr) {
	for (var i = 0; i < arr.length; i+=2) {
		if (arr[i] !== undefined && arr[i+1] !== undefined) {
			var temp = arr[i]; 
			arr[i] = arr[i+1]; 
			arr[i+1] = temp; 			
		}
	}
	return arr;
};

console.log(swapArrayPairs(evenList));
console.log(swapArrayPairs(oddList));

// Array Remove Duplicates
// Sara is looking to hire an awesome web developer and has received applications from various 
// sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, 
// remove duplicate values. Because array elements are already in order, all duplicate values 
// will be grouped together.

var orderedArray = ['Bob', 'Bob', 'Bob', 'Celina', 'Gideon', 'Gideon', 'Jill', 'Jill', 'Jill', 'Quas', 'Roberto', 'Robert'];

function removeDuplicates(arr) {
	var counter = 0; 
	while (counter < arr.length) {
		if (arr[counter] === arr[counter+1]) {
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

console.log(removeDuplicates(orderedArray));
