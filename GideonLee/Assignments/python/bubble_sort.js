// Bubble Sort

var array = [1, 8, 5, 3, 7, 6, 2, 4];

function bubble_sort(arr) {
	for (var i = 0; i < arr.length; i++) {	
		for (var j = 0; j < arr.length-1; j++) {
			if (arr[j] > arr[j+1]) {
				var temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp; 
			}	
		}
	}
	return arr;
};

console.log(bubble_sort(array));