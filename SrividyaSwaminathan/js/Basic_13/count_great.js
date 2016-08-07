//Given an array, return the count that is greater than Y.

function count_greater(arr, y){
	var count = 0;
	for(var i=0; i<arr.length; i++){
		if(arr[i]>y){
			count = count+1
		}
	}
	console.log(count)
}

count_greater([23,5,4,3],7)