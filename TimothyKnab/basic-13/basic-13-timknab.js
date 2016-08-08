
///////////////////////////////////////////////////////////////////////////
//																	
// 		Basic 13 Algorithm Challenge for Coding Dojo - August 2016 		
//
///////////////////////////////////////////////////////////////////////////
//
/////////////////////
//					
//  Instructions:  
//
/////////////////////
//
//		Step 1: Create an index.html file with a basic html5 frame.
// 		Step 2: Directly *above* the </body> tag of your document create: <script></script>
//		Step 3: Paste the entire algorithm code you want to see into action between the <script> and </script> tags.
// 		Step 4: Directly *beneath* the <body> tag of your document create: <div id='output' style='overflow-wrap: break-word;'></div> 
// 		Steo 5: Save the page and open it in your browser to see the output.
//
// 	Note: you may only run one of these functions at a time, as all use #output for their display.
// 	Thank you!
//
//
//
//
//
/////////////////////
//
//	Time Stamps:
//
/////////////////////
//
//		Attempt #1:  
//			Time: 2.75 Hours 
//			notes: first attempt, lots of hunting in past notes -- took me awhile longer than desired.
//			was trying to figure out how to append output to HTML, which led to some hiccups.
//
//
//
///////////////////////////////////////////////////////////////////////////












/////////////////////////////
//
//   #1. Print1To255()		Print 1 to 255
//
////////////////////////////









function Print1To255(){
	var number = []; 
	for (var i = 1; i <= 255; i++ ) { 
			number.push(i); 
		};
	return number; 
};

document.getElementById('output').innerHTML = Print1To255(); // runs my function and spits it out on the inner html of #output










/////////////////////////////
//
//   #2. PrintOdds1To255()		Print Odds 1 to 255
//
////////////////////////////










function PrintOdds1To255(){
	var number = []; 
	for (var i = 1; i <= 255; i++ ) {
		if ( i % 2 === 1 ) {  // note that modulus checks for *remainder*, not quotient, thus this checks if i is odd
			number.push(i);
		};
	};
	return number;
};
document.getElementById('output').innerHTML = PrintOdds1To255();












/////////////////////////////
//
//   #3. PrintIntsAndSum0To255()	Print Integers from 0 to 255, and with each integer print the sum so far
//
////////////////////////////









function PrintIntsAndSum0To255(){
	var number = [];
	var sum = 0; 

	for (var h = 0; h <= 255; h++) { // go through integers 0 to 255 and for *each* value:
		number.push(h);
		for (var i = 0; i < number.length; i++){ 
			sum = sum + number[i]; 
		}
		number.push(sum);
	};
	return number;
};
document.getElementById('output').innerHTML = PrintIntsAndSum0To255(); 











/////////////////////////////
//
//   #4. PrintArrayVals(arr)	Print all values in a given array
//
////////////////////////////










function PrintArrayVals(arr){	
	arr.toString();	// converts array values to a string
	return arr;	
};

var arr = [1,2,3,4,5];
document.getElementById('output').innerHTML = PrintArrayVals(arr);  












/////////////////////////////
//
//   #5. PrintMaxOfArray(arr)	  Print the largest element in a given array
//
////////////////////////////









function PrintMaxOfArray(arr){
	var max = arr[0]; // sets our max val to index[0] in our array to begin

	for (var i = 0; i < arr.length; i++){
		if (max < arr[i]) { 
			max = arr[i]; 
		};
	};
	return max;
};

var arr = [1,2,3,4,5,6,7,8,9,10];
document.getElementById('output').innterHTML = PrintMaxOfArray(arr);

	// QUESTION #1: Why won't this print to my innerHTML, #output? It does appear in console when I manually run the function. 

	// QUESTION #2: What exactly is the name for the object inside of the '()'? ie, the '(arr)'' in 'PrintMaxOfArray(arr)'? -- parameter











/////////////////////////////
//
//   #6. PrintAverageOfArray(arr)	  Analyze an array's values and print the average
//
////////////////////////////











function PrintAverageOfArray(arr){
	var avg = 0;

	for ( var i = 0; i < arr.length; i++){
		avg = avg + arr[i];
	}

	avg = avg / arr.length;
	return avg;
}

var arr = [1,2,3,4,5];
document.getElementById('output').innerHTML = PrintAverageOfArray(arr);

















/////////////////////////////
//
//   #7. ReturnOddsArray1To255()	  Create and return an array with odd integers from 1-255
//
////////////////////////////











function ReturnOddsArray1To255(){
	for ( var i = 1; i <= 255; i++ ){ 
		if ( i % 2 === 1 ) { 
			arr.push(i); 
		};
	};

	return arr; 
};

var arr = [];
document.getElementById('output').innerHTML = ReturnOddsArray1To255();












/////////////////////////////
//
//   #8. SquareArrayVals(arr)		Given an array, square each value in the array
//
////////////////////////////







function SquareArrayVals(arr){
	for (var i = 0; i < arr.length; i++){
		arr[i] = arr[i] * arr[i];
	};
	return arr;
};

var arr = [1,2,3,4,5];
document.getElementById('output').innerHTML = SquareArrayVals(arr);









/////////////////////////////
//
//   #9. ReturnArrayCountGreaterThanY(arr,y)		Given an array, return the count that is greater than Y
//
////////////////////////////








function ReturnArrayCountGreaterThanY(arr,y){
	var y = 1;
	var count = 0

	for ( var i = 0; i < arr.length; i++){
		if ( arr[i] > y ) {
			count = count + 1;
		}
	};
	return count;
};

var arr = [1,2,3,4,5];
document.getElementById('output').innerHTML = ReturnArrayCountGreaterThanY();










/////////////////////////////
//
//   #10. ZeroOutArrayNegativeVals(arr)		Given an array, set negative values to zero
//
////////////////////////////









function ZeroOutArrayNegativeVals(arr){
	for ( var i = 0; i < arr.length; i++){
		if( arr[i] < 0 ){
			arr[i] = 0;
		}
	};

	return arr;
};

var arr = [-1,0,1,2,3,4,5,-1];
document.getElementById('output').innerHTML = ZeroOutArrayNegativeVals();
















/////////////////////////////
//
//   #11. PrintMaxMinAverageArrayVals(arr)		Given an array, print max, min and average values
//
////////////////////////////



var i ="something"





function PrintMaxMinAverageArrayVals(arr){
	var max = arr[0];
	var min = arr[0];
	var avg = 0;

	for (var i = 0; i < arr.length; i++){
		if ( max < arr[i] ){
			max = arr[i];
		}
		if ( min > arr[i] ){
			min = arr[i];
		}
		avg = avg + arr[i];
	}

	avg = avg / arr.length;
	
	var arrNew = [max, min, avg];
	return arrNew;

}

var arr = [1,2,3,4,5,6,7,8,9,10];
document.getElementById('output').innerHTML = PrintMaxMinAverageArrayVals(arr)
// QUESTION #3 - Why can't I get this to print to my screen?













/////////////////////////////
//
//   #12. ShiftArrayValsLeft(arr)		Given an array, shift values forward by one, dropping the first value and leaving an extra '0' value at the end
//
////////////////////////////











function ShiftArrayValsLeft(arr){
	arr.shift(); // shifts array removing index[0]
	arr.push(0);  // adds extra 0 to the end of the array
	return arr;
};
var arr = [1,2,3,4,5];
document.getElementById('output').innerHTML = ShiftArrayValsLeft(arr);













/////////////////////////////
//
//   #13. SwapStringForArrayNegativeVals(arr)		Given an array, replace any negative values with 'Dojo' string
//
////////////////////////////











function SwapStringForArrayNegativeVals(arr){
	for (var i = 0; i < arr.length; i++){
		if ( arr[i] < 0 ){
			arr[i] = 'Dojo';
		}
	}
	return arr;
};

var arr = [-1,-2,0,1,2];
document.getElementById('output').innerHTML = SwapStringForArrayNegativeVals(arr);











