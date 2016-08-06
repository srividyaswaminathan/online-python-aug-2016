//given an array square each value in an array

function square(arr){
	var new_arr = [];
	for(var i=0; i<arr.length; i++){
		new_arr.push(arr[i]*arr[i]);
	}
	console.log(new_arr);
}

square([4,5,6,7])
