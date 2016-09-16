a = [1,2,3,4,10];
b = [1,2,3,2,1];
c = [-2,5,7,0,3];
d = [9,9]

function balancePoint(arr) {
	// console.log(arr)
	for (var i = arr.length - 1; i >= 0; i--) {
		var left = 0;
		var right = 0;

		for (var j = arr.length - 1; j >= 0; j--) {
			if (j <= i) {
				left += arr[j];
			}
			else if (j > i) {
				right += arr[j];
			}
		}
		if (left == right) {
			return true
			// tests 
			// return console.log(true)
			// console.log('i: '+i)
			// console.log('L: '+left)
			// console.log('R: '+right)
			// console.log('-----')
		}			
	}
	return false
	// tests
	// return console.log(false)
	// console.log('i: '+i)
	// console.log('L: '+left)
	// console.log('R: '+right)
	// console.log('-----')
}

function balanceIndex(arr) {
	// console.log(arr)
	for (var i = arr.length - 1; i >= 0; i--) {
		var left = 0;
		var right = 0;

		for (var j = arr.length - 1; j >= 0; j--) {
			if (j < i) {
				left += arr[j];
			}
			else if (j > i) {
				right += arr[j];
			}
		}
		if (left == right) {
			return i
			// test
			// return console.log('i: '+i)
		}
	} 
	return -1
	// test
	// return console.log('-1')
}
balancePoint(a);
balancePoint(b);
balanceIndex(c);
balanceIndex(d);