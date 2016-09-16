//Given array and an index into array, remove and return the array value at that index. 
//Do this without using built-in array methods except pop(). Think of PopFront(arr) as equivalent to RemoveAt(arr,0).

function return_value_at_index(array, idx) {
	if(array[idx]>array.length) {
		return null
	}
	var valToReturn = array[idx] 
	for (var i=idx; i<array.length; i++){
		array[i]= array[i+1]
	}
	array.length = array.length-1
	return valToReturn
}

console.log(return_value_at_index([2,4,5,7], 1))

//Swap positions of successive pairs of values of given array. If length is odd, do not change final element. 
//For [1,2,3,4], return [2,1,4,3]. For [false,true,42], return [true,false,42].

function swap(arr){
	var x = arr.length;
	if((arr.length)%2!=0){
		x = x-1;
	}
	
	for(var i=0; i<x; i=i+2){
		var temp = arr[i];
		arr[i] = arr[i+1];			
		arr[i+1] = temp;			
	}	
	return arr
}	

console.log(swap([3,2,1,4]))
console.log(swap([3,2,4,5,1]))
//Sara is looking to hire an awesome web developer and has received applications from various sources. 
//Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together.
function remove_duplicates(arr){
	for(var i=0; i<arr.length; i++ ){
		if(arr[i]==arr[i+1]){
			arr.splice(i+1, 1)

		}
		
	}	
	return arr
}

console.log(remove_duplicates(["alpha", "alpha", "beta", "beta", "gamma"]))	


 
	