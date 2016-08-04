// Arrays Day 3

// Reverse array
// 	Given a numerical array, reverse the order of the values. The reversed array should 
// 	have the same length, with existing elements moved to other indices so that the order 
// 	of elements is reversed.
// 		BONUS: Don’t use a second array – move the values around within the array that you are given.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function reverseArray(arr) {
	end = arr.length-1; 
	for (var i = 0; i < arr.length/2; i++) {
		var temp = arr[i];
		arr[i] = arr[end];
		arr[end] = temp; 
		end--; 
	}
	return arr;
};

console.log('The starting array is: (' + arr + ')');
console.log('The new reversed array: (' + reverseArray(arr) + ')');


// Array Min to Front
// 	Given an array of comparable values, move the lowest element to the array’s front, shifting
// 	backward elements that previously were ahead of it. Change [4,2,1,3,5] to [1,4,2,3,5].

arr = [3, 7, 10, 2, 9, 2, 6, 4, 5];

function minToFront(arr) {
	var min = arr[0];
	var index = 0;
	//Find the lowest value
	for (var i = 1; i < arr.length; i++) {
		if (min > arr[i]) {
			min = arr[i];
			index = i; 
		}
	}
	//Shift everything up one space starting from the lowerest value
	for (var i = index; i > 0; i--) {
		arr[i] = arr[i-1];
	}
	//Reassign the first value the lowest value
	arr[0] = min; 
	return arr; 
};

console.log('The starting array is: (' + arr + ')');
console.log('After pushing the min to the front: (' + minToFront(arr) + ')');