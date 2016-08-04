//given an array set negative values to zero

function set_negative(arr){
	for(var i=0; i<arr.length; i++){
		if(arr[i]<0){
			arr[i]=0;
		
	}
	}
	console.log(arr);
}

set_negative([-1,-5,6,7])