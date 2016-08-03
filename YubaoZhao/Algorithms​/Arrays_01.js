//Arrays Day 1

//Push Front
//Given array and an additional value, insert this value at the beginning of the array.

function pushFront(arr,val) {
    for(var i = arr.length; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[i] = val;
    return arr;
}

//Pop Front
//Given array, remove and return the value at the beginning of the array.
//Do this without using any built-in array methods except pop().

function popFront(arr) {
    var val = arr[0];
    for(var i = 1; i < arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.pop();
    return val;
}

//Insert At
//Given array, index, and additional value, insert the value into array at given index.
//You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).

function insertAt(arr,idx,val) {
    if(idx >= 0 && idx < arr.length) {
        for(var i = arr.length; i > idx; i--) {
            arr[i] = arr[i-1];
        }
        arr[idx] = val;
        return arr;
    }
    else {
        console.log("Wrong index number!");
        return;
    }
}
