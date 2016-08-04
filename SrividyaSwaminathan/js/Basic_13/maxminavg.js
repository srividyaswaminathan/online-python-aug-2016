//Given an array, print max, min and average values.

function max_min_avg(arr){
	var sum = 0;
	var sort = arr.sort(function(a, b){return a-b});
	console.log(sort);
	 max = arr[arr.length-1]
	 min = arr[0]
	for(var i=0; i<arr.length; i++){
		sum = sum+ arr[i];
	}
	avg = sum/arr.length
	console.log("average value in this array is", avg)
	console.log("maximum value in this array is", max)
	console.log("average value in this array is", min)
}

max_min_avg([2, 5, 7,14])