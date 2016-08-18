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
    var counterOfprop = 0,
        counterOfMeth = 0,
        count = {};
    for(var item in obj) {
        if(typeof(obj[item]) == "function") {
            counterOfMeth += 1;
        }
        else {
            counterOfprop += 1;
        }
    }
    count['properties'] = counterOfprop;
    count['methods'] = counterOfMeth;
    return count;
}

console.log(numberOfPropertiesAndMethods(obj));
