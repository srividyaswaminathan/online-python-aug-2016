// The following are soulutions to the Basic 13 challenge for Coding Dojo August 2016

printOddsTo255 = function(){
	for (var i = 1; i<= 255;i++){
		if (i % 2 != 0){
			console.log(i)
		}
	}
};

print1To255 = function(){
	for (var i = 1;i <= 255; i++){
		console.log(i);
	}
};

printIntsAndSum0To255 = function(){
	var count = 0;
	for (var i =0;i <= 255; i++){
		count += i;
		console.log("Sum:" + count + " " + "Integer:" + i);
	}
};

printArrayVals = function (arr){
	for (var i = 0; i < arr.length; i++){
		console.log(arr[i]);
	}
};

PrintMaxOfArray = function(arr){
	var count = 0;
	for (var i = 0; i <= arr.length; i++){
		if (arr[i] > count){
			count = arr[i];
		}	
	}
  console.log(count);
};

PrintAverageOfArray = function(arr){
var count = 0;
for (var i = 0;i < arr.length; i++){
    count += arr[i];
    }
    console.log(count / arr.length);
}

ReturnOddsArray1To255 = function(){
	var arr = []
	for (var i = 1;i <= 255; i++){
  	if (i % 2 != 0){
    arr.push(i);
    }
  }
  console.log(arr)
}


SquareArrayVals= function(arr){
	for (var i = 0;i < arr.length; i++){
		arr[i] = arr[i]*arr[i];
	}
	console.log(arr);
}

ReturnArrayCountGreaterThanY = function(arr, y){
	var count = 0;
	for (var i =0;i < arr.length; i++){
		if (arr[i] > y){
			count += 1;
		}
	}
  console.log(count);
}

ZeroOutArrayNegativeVals= function(arr){
	for (var i =0;i < arr.length; i++){
		if (arr[i] < 0){
			arr[i] = 0;
		}
	}
  console.log(arr);
}

SwapStringForArrayNegativeVals = function(arr){
	for (var i = 0;i < arr.length; i++){
		if (arr[i] < 0){
			arr[i] = "Dojo";
		}
	}
	debug(arr)
}

ShiftArrayValsLeft = function(arr){
	arr.shift();
	arr.push(0);
}