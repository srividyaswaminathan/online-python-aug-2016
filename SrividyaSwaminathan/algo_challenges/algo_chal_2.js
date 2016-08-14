//Given a numerical array, reverse the order of the values. The reversed array should have the same length, with existing elements moved to other indices so that the order of elements is reversed.

//BONUS: Don’t use a second array – move the values around within the array that you are given.
// using a temp array

function reverse(array){
	for(var i=0; i<array.length/2; i++){
		temp = array[i]
		array[i] = array[array.length-1-i]
		array[array.length-1-i] = temp
	}
	return array
}
console.log(reverse([2,3,4,5]))
//Array Min to Front Given an array of comparable values, move the lowest element to the array’s front, shifting backward elements that previously were ahead of it. Change [4,2,1,3,5] to [1,4,2,3,5]
function min_to_front(array){
	var min = array[0]
	for (var i=1; i<array.length; i++) {
		if (min>array[i]){
			min = array[i]
		}
	}
	temp = array[0]
	minimum_index = array.indexOf(min)
	array[0] = min 
	array[minimum_index] = temp
	return array
}

console.log(min_to_front([2,4,5,1]))