//Create return an array with odd integers from 1-255.

function odd_int(arr){
	var new_arr = [];
	for(var i=1; i<256; i++){
		if(i%2!==0){
			new_arr.push(i) 
		}
	} 
	console.log(new_arr)
}
odd_int()
