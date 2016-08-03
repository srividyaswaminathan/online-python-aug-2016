//Push Front

function push_front(){
	var arr = [2,3,4];
	for (var i=arr.length; i > 0; i -= 1) {
	arr[i] = arr[i-1];
	}
	arr[0] = 12;
	return arr;
	}

//Pop Front 
//Given array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function pop_front(){
	var arr = [2,3,4];
	arr.pop(4);
	for (var i=arr.length; i > 0; i-= 1) {
		arr[i] = arr[i-1];
	}
	arr[0] = 4;
	return arr;
}

//Insert At 
//Given array, index, and additional value, insert the value into array at given index. You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).

function insert_at(){
	var arr = [2,3,4,5,6,7];
	for (var i=arr.length; i>2; i-=1){
		arr[i]=arr[i-1];
	}
	arr[2]=12;
	return arr;
}