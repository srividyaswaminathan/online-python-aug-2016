// Strings Day 2

// Is Palindrome
// Create a function that returns a boolean indicating whether the string is a strict palindrome.
// For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization:
// if given "Dud" or "oho!", return false.

function isPalindrome(str) {
    for(var i = 0,j = str.length-1; i < j; i++,j--) {
        if(str[i] !== str[j]) {
            console.log("Not A Palindrome!");
            return false;
        }
        console.log("It's A Palindrome!");
        return true;
    }
}

// Next, ignore white space (spaces, tabs, returns), capitalization and punctuation.
function isPalindrome2(str) {
    var i = 0,j = str.length-1;
    var flag = false;
    str = str.toLowerCase()
    while(i < j) {
        if(str[i] < 'a' || str[i] > 'z') {
            i += 1;
            continue;
        }
        if(str[j] < 'a' || str[j] > 'z') {
            j -= 1;
            continue;
        }
        if(str[i] !== str[j]) {
            flag = false;
            break;
        }
        i += 1;
        j -= 1;
        flag = true;
    }
    if(flag) console.log("It's A Palindrome!");
    else console.log("Not A Palindrome!");
    return flag;
}
