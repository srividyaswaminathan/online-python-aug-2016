// Arrays II Day 1
// Balance Point
// Write a function that returns whether the given array has a balance point between indices,
// where one side’s sum is equal to the other’s. Example: [1,2,3,4,10] → true (between indices 3 & 4), but [1,2,4,2,1] → false.
function balancePoint(arr) {
    var balance = false,
        totalSum = 0,
        leftSum = 0;
    for(var i = 0; i < arr.length; i++) {
        totalSum += arr[i];
    }
    for(var idx = 0; idx < arr.length-1; idx++) {
        leftSum += arr[idx];
        if(leftSum == totalSum - leftSum) {
            balance = true;
            console.log("Balance Point is between indices [%d] & [%d]", idx, idx+1);
            break;
        }
    }
    return balance;
}
// Balance Index
// Here, a balance point is on an index, not between indices. Return the balance index
// where sums are equal on either side (exclude its own value). Return -1 if none exist. Ex.: [- 2,5,7,0,3] → 2, but [9,9] → -1.
function balanceIndex(arr) {
    var balance = -1;
    var totalSum = 0,
        leftSum = 0;
    for(var i = 0; i <arr.length; i++) {
        totalSum += arr[i];
    }
    for(var idx = 1; idx < arr.length-1; idx++) {
        leftSum += arr[idx-1];
        if(leftSum == totalSum-leftSum-arr[idx]) {
            balance = idx;
            console.log("Balance Index is [%d]", idx);
            break;
        }
    }
    return balance;
}
