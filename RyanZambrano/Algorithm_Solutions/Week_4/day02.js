a = [1, [2, 3], 4, [5, [6, 7], 8], 9]


x = -1
function flatten(arr) {
	for (var i = 0; i < arr.length; i++) {
		if (arr[i].constructor === Array) {
			flatten(arr[i]);
		}
		else { // need a way to add to the original arr without affecting the function
			// x++
			// console.log(x)
			console.log(arr[i])
			// arr[x] = arr[i]
		}
	}
}


flatten(a); 
console.log(a);