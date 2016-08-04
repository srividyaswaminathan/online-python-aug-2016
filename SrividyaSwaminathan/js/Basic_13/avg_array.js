//print average of array

function avg_array(arr){
	var avg = 0;
	var total = 0;
	for(var i=0; i<arr.length; i++){
		total = total + arr[i];
	}
	avg = total/arr.length
	console.log(total)
	console.log(avg)
}

avg_array([2,4,5,10])