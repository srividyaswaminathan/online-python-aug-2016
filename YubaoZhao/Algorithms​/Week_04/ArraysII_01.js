// Arrays II Day 1
// Balance Point
// Write a function that returns whether the given array has a balance point between indices,
// where one side’s sum is equal to the other’s. Example: [1,2,3,4,10] → true (between indices 3 & 4), but [1,2,4,2,1] → false.
function balancePoint(arr) {
    var balance = false;
    for(var idx = 1; idx < arr.length; idx++) {
        var leftSum = 0,
            rightSum = 0;
        for(var i = 0; i < idx; i++) {
            leftSum += arr[i];
        }
        for(var j = idx; j < arr.length; j++) {
            rightSum += arr[j];
        }
        if(leftSum == rightSum) {
            balance = true;
            console.log("Balance Point is between indices [%d] & [%d]", idx-1, idx);
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
    for(var idx = 1; idx <arr.length-1; idx++) {
        var leftSum = 0,
            rightSum = 0;
        for(var i = 0; i < idx; i++) {
            leftSum += arr[i];
        }
        for(var j = idx+1; j < arr.length; j++) {
            rightSum += arr[j];
        }
        if(leftSum == rightSum) {
            balance = idx;
            console.log("Balance Index is [%d]", idx);
            break;
        }
    }
    return balance;
}
