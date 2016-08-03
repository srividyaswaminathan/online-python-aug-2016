##The Basic 13

Completed in 25 minutes.

###Print 1-255   
> Print all the integers from 1 to 255.     
    
    function print1To255() {   
        for(var i = 1; i < 256; i++) {
            console.log(i);
        }      
    }

###Print Odds 1-255
> Print all odd integers from 1 to 255.

    function printOdds1To255() {
        for(var i = 1; i <256; i++) {
            if( i % 2 !== 0 ) {
                console.log(i);
            }
        }
    }

###Print Ints and Sum 0-255   
> Print integers from 0 to 255, and with each integer print the `sum` so far.   

    function printIntsAndSum0To255() {
        var sum = 0;
        for(var i = 0; i < 256; i++) {
            sum += i;
            console.log(“Integer:” + i + “ Sum:” + sum);
       }
    }


###Iterate and Print Array
> Iterate through a given array, printing each value.

    function printArrayVals(arr) {
        for(var i = 0; i < arr.length; i++) {
            console.log(arr[i]);
        }
    }

###Find and Print Max
> Given an array, find and print its largest element.

    function printMaxOfArray(arr) {
        var max = arr[0];
        for(var i = 1; i < arr.length; i++) {
            if( arr[i] >max ) max = arr[i];
        }
        console.log(max);
    }

###Get and Print Average
> Analyze an array’s values and print the average.

    function printAverageOfArray(arr) {
        var avg = 0;
        var sum = 0;
        for(var i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        avg = sum / arr.length;
        console.log(avg);
    }
    
###Array with Odds
> Create an array with all the odd integers between 1 and 255 (inclusive).

    function returnOddsArray1To255() {
        var arr = [ ];
        for(var i = 1; i <256; i++) {
            if( i % 2 !== 0) arr.push(i);
        }
    } 

###Square the Values
> Square each value in a given array, returning that same array with changed values.

    function squareArrayVals(arr) {
        for(var i = 0; i < arr.length; i++) {
            arr[i] *= arr[i];
        }
        return arr;
    }

###Greater than Y
> Given an array and a value `Y`, count and print the number of array values greater than `Y`.

    function returnArrayCountGreaterThanY(arr,y) {
        var count = 0;
        for(var i = 0; i < arr.length; i++) {
            if( arr[i] > y ) count++;
        }
        return count;
    }

###Zero Out Negative Numbers
> Return the given array after setting any negative values to zero.

    function zeroOutArrayNegativeVals(arr) {
        for(var i = 0; i < arr.length; i++) {
            if( arr[i] < 0 ) arr[i] = 0;
        }
        return arr;
    }   

###Max, Min, Average
> Given an array, print the `max`, `min` and `average` values for that array.

    function printMaxMinAverageArrayVals(arr) {
        var max = arr[0];
        var min = arr[0];
        var sum = arr[0];
        var avg = 0;
        for(var i = 1; i < arr.length; i++) {
            if(arr[i] > max) max = arr[i];
            if(arr[i] < min) min = arr[i];
            sum += arr[i]; }
        avg = sum / arr.length;
        console.log(“Max:”+max+” Min:”+min+” Average:”+avg);
    }

###Shift Array Values
> Given an array, move all values forward by one index, dropping the first and leaving a `0` value at the end.

    function shiftArrayValsLeft(arr) {
        for(var i = 1; i < arr.length; i++) { 
            arr[i-1] = arr[i];
        }
        arr[i-1] = 0;
        return arr;
    }

###Swap String For Array Negative Values
> Given an array of numbers, replace any negative values with the string `'Dojo'`.

    function swapStringForArrayNegativeVals(arr) {
        for(var i = 0; i < arr.length; i++) {
            if( arr[i] < 0 ) arr[i] = “Dojo”;
        }
        return arr;
    }
