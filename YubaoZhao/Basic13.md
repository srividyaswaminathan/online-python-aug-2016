##The Basic 13

Completing in 25 minutes.

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

###Iterate and Print Array
> Iterate through a given array, printing each value.

###Find and Print Max
> Given an array, find and print its largest element.

###Get and Print Average
> Analyze an array’s values and print the average.

###Array with Odds
> Create an array with all the odd integers between 1 and 255 (inclusive).

###Square the Values
> Square each value in a given array, returning that same array with changed values.

###Greater than Y
> Given an array and a value `Y`, count and print the number of array values greater than `Y`.

###Zero Out Negative Numbers
> Return the given array after setting any negative values to zero.

###Max, Min, Average
> Given an array, print the `max`, `min` and `average` values for that array.

###Shift Array Values
> Given an array, move all values forward by one index, dropping the first and leaving a `0` value at the end.

###Swap String For Array Negative Values
> Given an array of numbers, replace any negative values with the string `'Dojo'`.
