// Write a function innerJoin that uses the three provided arrays to 
// return a new array, where each element is also an array containing 
// three objects, one each pulled from users, books and usersHaveBooks. 
// Here's the catch: The user object's id property must match the 
// user_id property of the usersHaveBooks object, and the book object's 
// id property must match the book_id property of the usersHaveBooks object.

var users = [
	{ 
		id: 1,
		first_name: 'Johnny',
		last_name: 'Rotten',
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id: 2,
		first_name: 'Amy',
		last_name: 'Brown',
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id: 3,
		first_name: 'Alice',
		last_name: 'Roh',
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
]; 

var usersHaveBooks = [
	{
		id:1,
		user_id:1,
		book_id:1,
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id:1,
		user_id:1,
		book_id:2,
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id:1,
		user_id:1,
		book_id:3,
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id:1,
		user_id:2,
		book_id:2,
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
];

var books = [
	{
		id: 1,
		book_title: 'Grapes of Wrath',
		book_subject: 'The hard life during the depression',
		created_at:'2012-12-31 23:59:59',
		updated_at:'2012-12-31 23:59:59'
	},
	{
		id: 2,
		book_title: 'Metamorphosis',
		book_subject: 'The degradation of humanity, reflected in a single man',
		created_at:'2015-01-12 23:59:59',
		updated_at:'2015-01-12 23:59:59'
	},
	{
		id: 3,
		book_title: 'The Coming Plague',
		book_subject: 'Infectious diseases',
		created_at:'2015-01-12 23:59:59',
		updated_at:'2015-01-12 23:59:59'
	},
];

function innerJoin() {
	var arr = [];
	for (var i = 0; i < usersHaveBooks.length; i++) {
		//Push into the main array, an array for each element in user books
		arr.push([usersHaveBooks[i]]);
		for (var j = 0; j < users.length; j++) {
			//If the arr finds a match for the users ...
			if (arr[i][0]['user_id'] === users[j]['id']) {
				for (var k = 0; k < books.length; k++) {
					// ... it'll look for its book match and push both user and book to the array. 
					if (arr[i][0]['book_id'] === books[k]['id']) {
						arr[i].push(users[j]);
						arr[i].push(books[k]);
					}
				}
			}
		}
	}
	return arr; 
};

// console.log(innerJoin(usersHaveBooks, users, books));


// Write a function called leftJoin that accepts three arrays. All the 
// objects in whichever array is passed as the first argument should be 
// represented in the final output array.

function leftJoin(arr1, arr2, arr3) {

};