// Strings Day 1

// Remove blanks
// Create a function that, given a string, returns a string without blanks.
// Given " play that Funky Music ", returns a string containing "playthatFunkyMusic".

function removeBlanks(str) {
    var newStr = "";
    for(var i = 0; i < str.length; i++) {
        if(str[i] !== " ") {
            newStr += str[i];
        }
    }
    return newStr;
}

function removeBlanks2(str) {
    return newstr = str.split(" ").join("");
}
// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".

function acronyms(str) {
    var newStr = "";
    var flag = 1;
    if(var i = 0; i < str.length; i++) {
        if(str[i] === " ") {
            flag = 1;
            continue;
        }
        if(flag) {
            flag = 0;
            newStr += str[i].toUpperCase();
        }
    }
    return newStr;
}
