
//Challenge Day2
// Zip Arrays into Map
// Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, 
//and values of the second. For `arr1 = ["abc", 3, "yo"]` and `arr2 = [42, "wassup", true]`, return `{"abc": 42, 3: "wassup", "yo": true}`.
function zip_arrays(arr1, arr2){
	var object = {};
	for(var i=0; i<arr1.length; i++){
		object[arr1[i]] = arr2[i]
	}
	return object
}
console.log(zip_arrays(["abc", 3, "yo"], [42, "wassup", true]))

//Challenge Day 3
//Most Repeated Character Given a string, return the character that's used most often, along with the number of times it's repeated.
function repeated_character(word){
	var charObj = {};
	var maxChar = {
						times: 0,
						letter: 0
					}
	for (var i=0; i<word.length; i++){
		if (word[i] in charObj){
			charObj[word[i]] += 1
		}
		else {
			charObj[word[i]] = 1
		}
	if(charObj[word[i]] > maxChar.times){
			maxChar.times = charObj[word[i]]
			maxChar.letter = word[i]
		}	
	}
	return maxChar
}
console.log(repeated_character("xxxwwdxesxer"))

//challenge day 4 
//How many items? 
//Given an object, return the number of items in the object. For example, given:
//{
//name: "Charlie",
//  age: 29,
//  sayHello: function() {
 //   console.log("Hello!")
 // }
//}
//Your function should return 3.
function count_property(obj){
	var count = 0;
	for (var property in obj){
		if(obj.hasOwnProperty(property)){
			count +=1
		}
	}
	return count

}

console.log(count_property({
  name: "Charlie",
  age: 29,
  sayHello: function() {
    console.log("Hello!")
  }
}))


//Instead of returning a single number, return another object with two key-value pairs, properties and methods. The value associated with properties should be a count of the initial object's non-function items.
// The value associated with methods should be a count of the initial object's functions. Given the example object above, you'd return the following:
// {   properties: 2,   methods: 1 }

function count_property_method(obj){
	var countObj = {
		methods: 0,
		property: 0
	}
	for(key in obj){
		if (typeof obj[key]==="function"){
			countObj.methods += 1
		}
		else {
			countObj.property +=1
		}
	}	
	return countObj
}

console.log(count_property_method({
  name: "Charlie",
  age: 29,
  sayHello: function() {
    console.log("Hello!")
  }
}))