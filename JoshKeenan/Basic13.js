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

ReturnOddsArray1To255 = function(arr){
	for (var i = 1;i <= 255; i++){
  	if (arr[i] % 2 != 0){
    console.log(arr[i]);
    }
  }
}

