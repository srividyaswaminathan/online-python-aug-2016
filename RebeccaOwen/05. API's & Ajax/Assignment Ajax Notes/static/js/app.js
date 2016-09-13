/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-September-2015
Python > API's & Ajax > Assignment: Ajax Notes
*/

$(document).ready(function(){

    $('body').on('submit', 'form', function(){

        if ($(this)[0].name === 'new')
        {
            //console.log($(this)[0].name);
             $.post('/notes/create', $(this).serialize(), function(res) {
                $('#notes').html(res);
            });

            return false;
        }
        if ($(this)[0].name === 'update')
        {
            //console.log($(this)[0].name);
            var note_id = $(this).closest('div').attr('class').split(' ')[1];
            //console.log(note_id, $(this).serialize());

            $.post('/notes/'+note_id+'/update', $(this).serialize(), function(res) {
                $('#notes').html(res);
            });
            return false;
        }

    });

    $('body').on("click", 'a', function(){
        var href = $(this)[0].href;
        $.get(href, function(res) {
            $('#notes').html(res);
        });
        return false;
    });

    $('body').on("focusin", 'textarea', function(){
        //console.log($(this).closest('div').find('.updateBtn').attr('class', 'updateBtn'));
        $(this).closest('div').find('.updateBtn').attr('class', 'updateBtn')
    });

});
