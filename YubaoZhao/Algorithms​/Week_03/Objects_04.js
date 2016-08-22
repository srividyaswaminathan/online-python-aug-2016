// PART I:How many items?
// Given an object, return the number of items in the object.
obj = {
  name: "Charlie",
  age: 29,
  sayHello: function() {
    console.log("Hello!")
  }
};

function numberOfItems(obj) {
    var counter = 0;
    for(var item in obj) {
        counter += 1;
    }
    return counter;
}
console.log("The given object:",obj);
console.log("The number of items in the object:",numberOfItems(obj));

// Part II
// Instead of returning a single number, return another object with two key-value pairs, properties and methods.
// The value associated with properties should be a count of the initial object's non-function items.
// The value associated with methods should be a count of the initial object's functions.
function numberOfPropertiesAndMethods(obj) {
    var  counterObj = {
             properties : 0,
             methods : 0
        };
    for(var item in obj) {
        if(typeof(obj[item]) == "function") {
            counterObj['methods'] += 1;
        }
        else {
            counterObj['properties'] += 1;
        }
    }
    return counterObj;
}

console.log(numberOfPropertiesAndMethods(obj));
