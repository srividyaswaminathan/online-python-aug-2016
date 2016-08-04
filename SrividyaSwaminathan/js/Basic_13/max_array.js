//print max of array

function max(arr){
	var max = 0;
	for(i=0; i<arr.length; i++){
		if(arr[i]>max){
			max = arr[i]
		} 
	}
	console.log(max)
}

max([1,2,3,4])
max([23,37,7456])