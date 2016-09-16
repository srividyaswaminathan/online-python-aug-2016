// Flatten
// Flatten a given array, eliminating nested arrays and empty [ ] elements.
// Do not alter the array, but return a new array that retains the original order.
// Example: given [1, [2, 3], 4, [ ] ], return a new array [1, 2, 3, 4].
function flattenArray(arr) {
    var newarr = [];
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] instanceof Array) {
            for(var j = 0; j < arr[i].length; j++) {
                newarr.push(arr[i][j]);
            }
        }
        else {
            newarr.push(arr[i]);
        }
    }
    return newarr;
}

// Second-level challenge: Work 'in-place' in the given array (cannot create another).
// Alter order if needed. Ex.: [1, [2, 3], 4, [ ] ] you could change to [1, 3, 4, 2].
// Third-level challenge: Make your algorithm both in-place and stable. Do you need a return value?
function flattenArray2(arr) {
    var oldLength = arr.length,
        newLength = arr.length;
    for(var i = 0; i < oldLength; i++) {
        if(arr[i] instanceof Array) {
            for(var j = 0; j < arr[i].length; j++) {
                arr[newLength] = arr[i][j];
                newLength += 1;
            }
        }
        else {
            arr[newLength] = arr[i];
            newLength += 1;
        }
    }
    for(var i = 0, j = oldLength; j < newLength; i++, j++) {
        arr[i] = arr[j];
    }
    arr.length = newLength - oldLength;
    return arr;
}
