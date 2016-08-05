//Arrays Day 3
//=================

//Reverse array
//Given a numerical array, reverse the order of the values. The reversed array
// should have the same length, with existing elements moved to other indices
//so that the order of elements is reversed.
//BONUS: Don’t use a second array – move the values around within the array
//that you are given.

function reverseArray(arr) {
    var temp;
    for(var i = 0,j = arr.length-1; i < j ; i++,j--) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}


//Array Min to Front
//Given an array of comparable values, move the lowest element to the array’s
//front, shifting backward elements that previously were ahead of it.
//Change [4,2,1,3,5] to [1,4,2,3,5].

function arrayMinToFront(arr) {
    var minIdx,temp;
    var min = arr[0];
    for(var i = 1; i < arr.length; i++) {
        if(min > arr[i]) {
            min = arr[i];
            minIdx = i;
        }
    }
    temp = arr[minIdx];
    for(i = minIdx; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = temp;
    return arr;
}
