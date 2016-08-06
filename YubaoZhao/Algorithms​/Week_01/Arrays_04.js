// Arrays Day 4
// =============

// Skyline Heights
// From lovely Burbank you have a breathtaking view of the Los Angeles skyline.
// Let’s say you are given an array with heights of consecutive buildings,
// starting closest to you and extending directly away. Array [-1,7,3] would
// represent three buildings: first is actually out of view below street level,
// behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story).
// You are situated at street level. Return array containing heights of buildings
// you can see, in order. Given [1,-1,7,3] return [1,7].
function skylineHeights(arr) {
    var max = 0;
    var newarr = [];
    for(var i = 0; i < arr.length; i++) {
        if(max < arr[i]) {
            max = arr[i];
            newarr.push(arr[i]);
        }
    }
    return newarr;
}

// Filter Range
// Alan is good at breaking secret codes. One tool is to eliminate numbers he knows
// are outside a certain specific range. Given array and values min and max, remove
// array values between min and max. Work in-place: return the array you are given,
// with values in original order. No built-in array functions.

function filterRange(arr,min,max) {
    if(min > max) {
        console.log("Invalid min&max values!");
        return;
    }
    else {
        for(var i = arr.length-1; i >= 0; i--) {
            if(arr[i] >= min && arr[i] <= max) {
                for(var j = i; j < arr.length-1; j++)
                    arr[j] = arr[j+1];
                arr.pop();
            }
        }
        return arr;
    }
}
