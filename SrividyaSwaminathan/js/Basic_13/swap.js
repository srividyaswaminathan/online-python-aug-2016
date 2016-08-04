//Given an array, replace negative values with &#39;Dojo&#39;.

function replace_negative(arr){
	for(var i=0; i<arr.length; i++){
		if(arr[i]<0){
			arr[i]="Dojo"
		}
	}
	console.log(arr)
}

replace_negative([2,3,-5,6,-10])