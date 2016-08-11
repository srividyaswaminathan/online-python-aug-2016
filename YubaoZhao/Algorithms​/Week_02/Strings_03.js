// Strings Day 3

// Book Index
// Martin is writing his opus: a book of algorithm challenges, set as lyrics to a
// suite of baroque fugues. He knows that some of those fugueing challenges will be
// less popular than others, so he needs a book index.Given a sorted array of pages,
// produce a book index string. Consecutive pages should form ranges separated by a dash.
// For [1,3,4,5,7,8,10], return the string "1, 3-5, 7-8, 10".

function bookIndex(arr) {
    var str = "",
        flag = 0;
    for(var i = 0; i < arr.length-1; i++) {
        if(arr[i+1] - arr[i] == 1) {
            if(flag) continue;
            str += arr[i] + "-";
            flag = 1;
        }
        else {
            str += arr[i] + ", ";
            flag = 0;
        }
    }
    str += arr[i];
    return console.log(str);
}
