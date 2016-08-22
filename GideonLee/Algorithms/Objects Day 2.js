// Zip Arrays into Map

// Associative arrays are sometimes called maps because a key
// (string) maps to a value. Given two arrays, create an associative 
// array (map) containing keys of the first, and values of the second. 
// For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], 
// return {"abc": 42, 3: "wassup", "yo": true}.

var arr1 = ["abc", 3, "yo"];
var arr2 = [42, "wassup", true];

function zipToMap(arr1, arr2) {
	var map = {};
	var key; 
	for (var i = 0; i < arr1.length; i++) {
		key = arr1[i];
		map[key] = arr2[i];
	}
	return map;
}

console.log(zipToMap(arr1, arr2));