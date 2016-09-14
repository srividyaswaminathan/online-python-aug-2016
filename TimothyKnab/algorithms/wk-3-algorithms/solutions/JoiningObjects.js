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

        ]

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

]

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
]


function innerJoin() {
    // Create array to return
    var arrToReturn = [];

    // Loop over usersHaveBooks
    for (var recordIdx = 0; recordIdx < usersHaveBooks.length; recordIdx += 1) {
        // Creating miniArr that will hold record obj, userobj, and bookobj
        // initially just put the record obj we have access to inside
        var miniArr = [usersHaveBooks[recordIdx]] // miniArr = usersHaveBooks[0]

        // Find correct user object
        var correctUserObj = findById(usersHaveBooks[recordIdx].user_id, users)

        // Find correct book object
        var correctBookObj = findById(usersHaveBooks[recordIdx].book_id, books)

        // Put user obj in miniArr
        miniArr.push(correctUserObj)
            // Put book obj in miniArr
        miniArr.push(correctBookObj)

        // ALTERNATE CODE CAN TAKE PLACE OF EVERYTHING ABOVE
        // var miniArr = [usersHaveBooks[recordIdx],findById(usersHaveBooks[recordIdx].user_id, users),findById(usersHaveBooks[recordIdx].book_id, books)];

        // If we're here, miniArr is completed and we can add to arrToReturn
        arrToReturn.push(miniArr)
    }

    return arrToReturn
}

function findById(providedId, records) {
    // Use the id passed in to find the matching object in record
    for (var searchIdx = 0; searchIdx < records.length; searchIdx += 1) {
        if (records[searchIdx].id === providedId) {
            return records[searchIdx];
        }
    }
    // If we get here, no record with providedId as id property
    return {
        error: "No record found"
    }

}
