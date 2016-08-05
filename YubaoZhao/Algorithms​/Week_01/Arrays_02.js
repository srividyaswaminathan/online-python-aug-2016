//Arrays Day 2
//============
//Remove At
//Given array and an index into array, remove and return the array value at that
//index. Do this without using built-in array methods except pop().
//Think of PopFront(arr) as equivalent to RemoveAt(arr,0).
function removeAt(arr,index) {
    if(index < 0 || index >= arr.length) {
        console.log("Invalid index!");
        return;
    }
    for(var i = index; i < arr.length-1; i++) {
        arr[i] = arr[i+1];
    }
    arr.pop();
    return arr;
}

//Swap Array Pairs
//Swap positions of successive pairs of values of given array. If length is odd,
//do not change final element. For [1,2,3,4], return [2,1,4,3].
//For [false,true,42], return [true,false,42].
function swapArrayPairs(arr) {
    for(i = 0; i < arr.length-1; i += 2) {
        var temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
    }
    return arr;
}


//Array Remove Duplicates
//Sara is looking to hire an awesome web developer and has received applications
//from various sources. Her assistant alphabetized them but noticed some
//duplicates. Given a sorted array, remove duplicate values. Because array
//elements are already in order, all duplicate values will be grouped together.
function arrayRemoveDuplicates(arr) {
    var newarr = [];
    var item = arr[0];
    for(var i = 1; i <= arr.length; i++) {
        if(item != arr[i]) {
            newarr.push(item);
            item = arr[i];
        }
    }
    return newarr;
}
