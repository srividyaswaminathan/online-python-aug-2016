// Joining objects
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
  }
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
  }
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
  }
];

function innerJoin(users,books,usersHaveBooks) {
    var array = [];
    for(var i = 0; i < usersHaveBooks.length; i++) {
        array[i] = [];
        for(var j = 0; j < users.length; j++) {
            if(users[j].id ==  usersHaveBooks[i].user_id) {
                array[i].push(users[j]);
                break;
            }
        }
        for(var k = 0; k < books.length; k++) {
            if(books[k].id == usersHaveBooks[i].book_id) {
                array[i].push(books[k]);
                break;
            }
        }
        array[i].push(usersHaveBooks[i]);
    }
    return array;
};

console.log(innerJoin(users,books,usersHaveBooks));



// object = {
//   id:1,
//   user_id:2,
//   book_id:2,
//   created_at:'2012-12-31 23:59:59',
//   updated_at:'2012-12-31 23:59:59'
// }
// function leftJoin(object,users,books,usersHaveBooks) {
//     if(object['book_title'] != undefined) return books;
//     if(object['first_name'] != undefined) return users;
//     if(object['user_id'] != undefined) return usersHaveBooks;
//     return console.log("Nothing!");
// };
//
// console.log(leftJoin(object,users,books,usersHaveBooks));
