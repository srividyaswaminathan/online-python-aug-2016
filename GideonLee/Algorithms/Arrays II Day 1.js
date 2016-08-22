// Arrays II Day 1
// Balance Point

// Write a function that returns whether the given array has a balance point 
// between indices, where one side’s sum is equal to the other’s. Example: 
// [1,2,3,4,10] → true (between indices 3 & 4), but [1,2,4,2,1] → false.

function balancePoint(arr) {
	var frontCounter = 0;
	var endCounter = arr.length-1;
	
	var frontSum = arr[frontCounter];
	var endSum = arr[endCounter];

	while (frontCounter < endCounter) {
		//If they are matching and right next to each other in the array. 
		if (frontSum === endSum && frontCounter === endCounter-1) {
			return true; 
		}
		//Increment the lower of the two sums and move that index.
		else {
			if (frontSum <= endSum) {
				frontCounter++; 
				frontSum += arr[frontCounter];
			}
			else {
				endCounter--; 
				endSum += arr[endCounter];
			}
		}
	}
	return false; 
};

var arr = [1, 2, 3, 4, 10];
console.log(balancePoint(arr));


// Balance Index
// Here, a balance point is on an index, not between indices. Return the 
// balance index where sums are equal on either side (exclude its own value). 
// Return -1 if none exist. Ex.: [- 2,5,7,0,3] → 2, but [9,9] → -1.

function balanceIndex(arr) {
	var frontCounter = 0;
	var endCounter = arr.length-1;

	var frontSum = arr[frontCounter];
	var endSum = arr[endCounter];

	while (frontCounter < endCounter) {
		if (frontSum === endSum && frontCounter != endCounter-1) {
			return endCounter-1; 
		}
		else {
			if (frontSum <= endSum) {
				frontCounter++;
				frontSum += arr[frontCounter]; 
			}
			else {
				endCounter--;
				endSum += arr[endCounter];
			}			
		}
	}
	return false; 
};

var arr = [9, 9];
console.log(balanceIndex(arr));