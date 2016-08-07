
///////////////////////////////////////////////////////////////////////////
//																	
// 		Arrays Day 1 - Coding Dojo - August 2016 		
//
///////////////////////////////////////////////////////////////////////////
//
/////////////////////
//					
//  Instructions:  
//
/////////////////////
//
//		To see the following JS code in your browser, follow these easy 5 steps:
//		Step 1: Create a basic HTML page and save it as .html.
// 		Step 2: Directly *above* the closing </body> tag of your document create: <script></script>
//		Step 3: Paste the entire algorithm code you want to see into action between the <script> and </script> tags.
// 		Step 4: Directly *beneath* the opening <body> tag of your document create: <div id='output' style='overflow-wrap: break-word;'></div> 
// 		Step 5: Save the page as .html and open it in your browser to see the output.
//
// 	Note: you may only run one of these functions at a time, as all use #output for their display.
// 	Thank you!
//
/////////////////////
//
//	Assignment Notes:
//
/////////////////////
//
// 	From your work with the Basic 13 challenges, we assume that you already know how to read from numerical arrays, 
//	and that you can easily create JavaScript functions to get the minimum or maximum value, the sum of all values 
//	in the array, or the average of all values in the array. If this is not the case, definitely review those 
//	implementations before continuing to today’s challenges.
//
///////////////////////////////////////////////////////////////////////////// 

// Here are the challenges for today:







/////////////////////////////
//
//   #1. pushFront()	Given array and an additional value, insert this value at the beginning of the array.
//
////////////////////////////


function pushFront(){
	var stagesOfLife = ['Early Adulthood', 'Middle Adulthood', 'Late Adulthood', 'Old Age'];
	stagesOfLife.unshift('Childhood','Adolescence'); // .unshift() function places new items at the *beginning* of an array
	return stagesOfLife;
};


document.getElementById('output').innerHTML = pushFront();




		// ** OFFICIAL ANSWER **
		// Note: the vars 'arr' and 'value' can be anything, instead in your example where you defined them strictly.
		// this function goes through the array length, 
		function pushFront(arr, value) {
		    // Start from the end of the array, pushing everything back by one
		    for (var i = arr.length; i > 0; i -= 1) {
		        arr[i] = arr[i - 1];
		    }
		    // Now we can set the new value to position 0
		    arr[0] = value;
		    return arr;
		}















/////////////////////////////
//
//   #2. popFront()	Given array, remove and return the value at the beginning of the array. 
//		 Do this without using any built-in array methods except pop().
//
////////////////////////////


function popFront(){
	var arr = ['Blue', 'Green', 'Red', 'Orange'];
	var firstItem = arr[0];
	arr.pop(0);  // I thought that the '0' here indicates an index value, but it does not appear to -- how can I use pop() to remove a specific position? Everything online said if you want to remove and return the value of the first index place, then use shift() -- but not desired in this exercise.
	return arr;
};


document.getElementById('output').innerHTML = popFront();



		
		// ** OFFICIAL ANSWER **
		// note that pop() was never used
		function popFront(arr) {
	    // Store the first value in the array in a variable
	    // Iterate through the array, pushing every value forward
	    // Shorten the array by 1
	    // Return the stored value

	    var valToReturn = arr[0];

	    for (var i = 0; i < arr.length; i += 1) {
	        arr[i] = arr[i + 1];
	    }

	    arr.length = arr.length - 1;

	    return valToReturn;
		}















/////////////////////////////
//
//   #3. insertAt()		Given array, index, and additional value, insert the value into array at given index. 
// 						You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).
//
////////////////////////////


function insertAt(){
	var arr = [1,2,3,5,6,7];
	// splice(position, numberOfItemsToRemove, item)
	arr.splice(3, 0, 4); // this should insert the number '4' in arr[2]
	return arr;
};


document.getElementById('output').innerHTML = insertAt();



		/* OFFICIAL ANSWER */
		function insertAt(arr, idx, value) {
		    // Iterate from end of array, shifting values to the right, until reaching the idx
		    // Replace arr[idx] with value
		    for (var i = arr.length; i > idx; i -= 1) {
		        arr[i] = arr[i - 1];
		    }
		    arr[idx] = value;
		    return arr;
		}






