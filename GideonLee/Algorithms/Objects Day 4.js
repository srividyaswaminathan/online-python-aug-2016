// Objects Day 4
// How many items?
// Given an object, return the number of items in the object. For example, given:
// {
//   name: "Charlie",
//   age: 29,
//   sayHello: function() {
//     console.log("Hello!")
//   }
// }
// Your function should return 3.

var obj = {
  name: "Charlie",
  age: 29,
  sayHello: function() {
    console.log("Hello!")
  },
  sayGoodBye: function() {
  	console.log('goodbye!')
  }
};

function countProperties(obj) {	
	var counter = 0; 
	for (var i in obj) {
		counter++; 
	}
	return counter; 
	// return Object.keys(obj).length;
};

console.log(countProperties(obj));


// Part II
// Instead of returning a single number, return another object with two key-value pairs,
// properties and methods. The value associated with properties should be a count of the
// initial object's non-function items. The value associated with methods should be a 
// count of the initial object's functions. Given the example object above, you'd return 
// the following:
// {
//   properties: 2,
//   methods: 1
// }

function countPropertiesMethods(obj) {
	var counterObj = {
		properties: 0,
		methods: 0
	}
	for (i in obj) {
		if (typeof(obj[i]) === 'function') {
			counterObj.methods += 1;
		}
		else {
			counterObj.properties += 1; 
		}
	}
	return counterObj;
};

console.log(countPropertiesMethods(obj));