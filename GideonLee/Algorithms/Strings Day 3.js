// Book Index
// Martin is writing his opus: a book of algorithm challenges, set as 
// lyrics to a suite of baroque fugues. He knows that some of those 
// fugueing challenges will be less popular than others, so he needs a 
// book index. Given a sorted array of pages, produce a book index string.
//  Consecutive pages should form ranges separated by a dash. 
//  For [1,3,4,5,7,8,10], return the string "1, 3-5, 7-8, 10".

function bookIndex(arr) {
 	var indexString = ''; 
 	var consecutive = false; 
 	for (var i = 0; i < arr.length; i++) {
 		if (consecutive === false) {
 			indexString += arr[i]; 
 		}	
 		if (arr[i+1] === arr[i]+1) {
 			consecutive = true;
 			continue; 
 		}
 		else if (consecutive === true && arr[i] !== arr[i]+1) {
 			consecutive = false;
 			indexString += '-' + arr[i];
 		}
 		if (i !== arr.length-1) {
 			indexString += ', ';
 		} 
   	}
 	return indexString; 
 };

var arr = [1, 3, 4, 5, 7, 8, 10]
console.log(bookIndex(arr));