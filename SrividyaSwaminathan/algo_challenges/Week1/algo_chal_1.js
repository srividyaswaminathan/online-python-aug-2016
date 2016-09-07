//Given array and an additional value, insert this value at the beginning of the array.
function insert_val(arr, val){
 	for(var i=arr.length; i>0; i--){
 		arr[i] = arr[i-1];
 	}
	arr[0]= val
	return arr
}
console.log(insert_val([2,4,5,6],1))

//Given array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().
function remove_val(array){
	var value_to_return = array[0]
	for(var i=0; i<array.length;i++) {
		array[i] = array[i+1]
	}
	array.length = array.length-1
	return value_to_return
}
console.log(remove_val([2,3,4,5]))
//Given array, index, and additional value, insert the value into array at given index. You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).

function insert_at_index(array, idx, val){
	for(var i=array.length; i<idx; i--){
		array[i] =array[i-1]
	}
	array[idx] = val
	return array
}
console.log(insert_at_index([2,3,4,5], 2, 5))