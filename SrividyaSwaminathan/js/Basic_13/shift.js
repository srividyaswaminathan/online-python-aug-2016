//Given an array, shift values forward by one, dropping  and leaving an extra 0 value at the end.

function shift_forward(arr){
	for(var i=0; i<arr.length-1; i++){
		
		arr[i]= arr[i+1];
		
	}
	arr[arr.length-1] = 0
    console.log(arr)
}

shift_forward([2,4,5,6])

