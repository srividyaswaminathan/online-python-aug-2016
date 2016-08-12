// Parens Valid

// Create a function that, given an input string str, returns a boolean whether
// parentheses in str are valid. Valid sets of parentheses always open before they close,
// for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed.
// Given "N(0)t )0(k", return false.

function parensValid(str) {
    var firOpenIdx = 0,
        lasOpenIdx = 0,
        firCloseIdx = 0,
        lasCloseIdx = 0,
        openNum = 0,
        closeNum = 0;
        for(var i = 0; i < str.length; i++) {
            if(str[i] == "(") {
                if(openNum == 0) {
                    firOpenIdx = i;
                    lasOpenIdx = i;
                }
                else lasOpenIdx = i;
                openNum += 1;
            }
            if(str[i] == ")") {
                if(closeNum == 0) {
                    firCloseIdx = i;
                    lasCloseIdx = i;
                }
                else lasCloseIdx = i;
                closeNum += 1;
            }
            // console.log("Idx:%d, firOpenIdx:%d, lasOpenIdx:%d, firCloseIdx:%d, lasCloseIdx:%d, openNum:%d, closeNum:%d",i,firOpenIdx,lasOpenIdx,firCloseIdx,lasCloseIdx,openNum,closeNum);
            if(firOpenIdx > firCloseIdx && firCloseIdx != 0) return false;
        }
        if(lasOpenIdx < lasCloseIdx && openNum == closeNum) return true;
        else return false;
}


function parensValid2(str) {
    var parensNum = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] == "(") {
            parensNum += 1
        }
        if (str[i] == ")") {
            parensNum -= 1;
        }
        if (parensNum < 0) {
            return false;
        }
    }
    return (parensNum == 0);
}
