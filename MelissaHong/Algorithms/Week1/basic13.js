//This took me about an hour to complete

//Print 1 to 255 integers
function get_array(){
var arr=[];
for (var i=1; i<=255; i++){
	arr.push(i);
}
return arr;
}

//Print Odds 1 to 255
function get_odds(){
	var arr=[];
	for (var i=1; i<=255; i++){
		if (i%2===1){
			arr.push(i);
		}
	}
	return arr;
}

//PrintIntsAndSum0to255()
function intsandsum(){
	var arr=[];
	var sum=0;
	for (var i=0; i<=255; i++){
			arr.push(i);
			sum+=i;
			console.log(sum);
		}
	console.log(arr);
	}

//Print Array Vals
function vals(arr){
	for (var index = 0; index < arr.length; index++){
		console.log("array[", index,"] is equal to", arr[index]);
	}
}

//Print Max Array
function findMax(arr){
	var max=0;
	for (var i=0; i<arr.length; i++){
		if (arr[i]>max){
			max=arr[i];
		}
	}
	console.log(max);
}

//Print Avg Array
function findAvg(arr){
	var sum=0;
	for (var i=0; i<arr.length; i++){
		sum+=arr[i];
	}
	var avg=sum/arr.length;
	console.log(avg);
}

//Return Odds 1 to 255
function returnOdds(){
	var arr=[];
	for (var i=1; i<=255; i++){
		if(i%2===1){
		arr.push(i);
		}
	}
	console.log(arr);
}

//Square value of array #s
function squareArray(arr){
	for (var i=0; i<arr.length; i++){
		arr[i]=arr[i]*arr[i];
	}
	return(arr);
}

//Return array count greater than Y (arr, y)
function greaterThanY(arr. Y){
	var Y=0;
	var count=0;
	for (var i=0; i<arr.length; i++){
		if (arr[i]>Y){
			count++
		}
	}
	return count;
}

//Set neg values to zero of an array
function zeroNeg(arr){
	for (var i=0; i<arr.length; i++){
		if (arr[i]<0){
			arr[i]=0;
		}
	}
	return arr;
}

//Max Min Avg values
function maxMinAvg(arr){
	var max=arr[0];
	var min=arr[0];
	var sum=arr[0];
	for (var i=0; i<arr.length;i++){
		if (arr[i]>max){
			max=arr[i];
		}
		if (arr[i]<min){
			min=arr[i];
		}
		sum+=arr[i];
		var avg=sum/arr.length;
	}
	var maxminavg=[max, min, avg];
	return maxminavg;
}

//Shift the array by 1, with index 0 at the end

function shiftOne(arr){
	for (var i=0; i<arr.length; i++){
		arr[i]=arr[i+1];
	}
	arr[arr.length-1]=0;
	}
	return arr;
}


//Replace neg values to dojo
function negDojo(arr){
	for (var i=0; i<arr.length; i++){
		if (arr[i]<0){
			arr[i]='dojo';
		}
	}
	return arr;
}
