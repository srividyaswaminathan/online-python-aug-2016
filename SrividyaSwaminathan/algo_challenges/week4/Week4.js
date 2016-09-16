
//###Balance Point
//Write a function that returns whether the given array has a balance point between indices, where one side’s sum is equal to the other’s. Example: `[1,2,3,4,10]` → `true` (between indices 3 & 4), 
//but `[1,2,4,2,1]` → `false`.


function balance_point(array){
for (var i=1; i<array.length; i++) {
	var left_sum=0;
	for (var j=0;j<i;j++) {
		left_sum += array[j];
	}

	var right_sum=0;
	for (var j=i;j<array.length;j++) {
		right_sum += array[j];
	}

	if (left_sum === right_sum) {
		return true;
	}

}

return false;
}
console.log(balance_point([1,2,3,4,10]))

//Balance Index
//Here, a balance point is *on* an index, not between indices. Return the balance index where sums are equal on either side (exclude its own value). 
//Return `-1` if none exist. Ex.: `[- 2,5,7,0,3]` → `2`, but `[9,9]` → `-1`.



function balance_index(array){
	var sum_to_left = 0
	for (var i=0; i<array.length; i++){
			sum_to_left += arr[i]
		}
		var sum_to_right = 0
		for (var j=0; j<array.length; j++){
			sum_to_right -= array[j]
			if (sum_to_right === sum_to_left) {
     			 return idx;
   				 }

   			 sum_to_left += array[i];
 		}
  
 		 return -1;
	}
		




//#Arrays II Day 2

//Flatten
//Flatten a given array, eliminating nested arrays and empty `[ ]` elements. Do not alter the array, but return a new array that retains the original order. 
//Example: given `[1, [2, 3], 4, [ ] ]`, return a new array `[1, 2, 3, 4]`.
function flatten(arr){
	var new_array = []
	for(var i=0; i<arr.length; i++){
		if (Array.isArray(arr[i])){

			for(var j=0; j<arr[i].length; j++){
				new_array.push(arr[i][j]);
			}
		}	
			else{
				new_array.push(arr[i]);
			} 
		
	}
	return new_array
}
console.log(flatten([1, [2, 3], 4, [ ] ]))

//Second-level challenge: Work 'in-place' in the given array (cannot create another). Alter order if needed. Ex.: `[1, [2, 3], 4, [ ] ]` you could change to `[1, 3, 4, 2]`.
//sThird-level challenge: Make your algorithm both **in-place** and **stable**. *Do you need a return value?*

function flatten_without_new_array(arr){
	var i =0;
	while(i<arr.length){
		console.log("here 1",i, arr.length);
		if (Array.isArray(arr[i])) {
			var arr_temp = arr.splice(i, 1)[0]
			for(var j=0; j<arr_temp.length; j++){
				arr.splice(i+j, 0, arr_temp[j])				
			}
			//i += arr_temp.length; (Work in place)

		}
		else{
			 i++;
		}
	}
	return arr;
}
console.log(flatten_without_new_array([1,[2,3],4]))
console.log("complete")
