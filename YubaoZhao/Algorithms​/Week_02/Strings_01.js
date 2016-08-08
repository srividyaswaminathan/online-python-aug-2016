// Strings Day 1

// Remove blanks
// Create a function that, given a string, returns a string without blanks.
// Given " play that Funky Music ", returns a string containing "playthatFunkyMusic".

function removeBlanks(str) {
    var newStr = "";
    var arr = str.split("");
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] != " ") newStr += arr[i];
    }
    return newStr;
}
// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".

function acronyms(str) {
    var newStr = "";
    var arr = str.split(" ");
    for(var i = 0; i < arr.length; i++) {
        var firstChar = (arr[i].split(""))[0];
        if(firstChar != undefined) {
            newStr += firstChar.toUpperCase();
        }
    }
    return newStr;
}
