// Objects Day 2
//
// Zip Arrays into Map
// Associative arrays are sometimes called maps because a key (string) maps to a value.
// Given two arrays, create an associative array (map) containing keys of the first,
// and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true],
// return {"abc": 42, 3: "wassup", "yo": true}.
arr1 = ["abc", 3, "yo"];
arr2 = [42, "wassup", true];

function zipArraysIntoMap(arr_keys,arr_values) {
    var map = new Object();
    if(arr_keys.length != arr_values.length) {
        return console.log("The length of two arrays should be equal!");
    }
    for(var idx = 0; idx < arr_keys.length; idx++) {
        map[arr_keys[idx]] = arr_values[idx];
    }
    return map;
}

console.log(zipArraysIntoMap(arr1,arr2));
