/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
14-July-2016
Assignment: Contact Card
*/

$(document).ready(function(){
    $('form').submit(function() {

        //convert form data into an array
        var input = $(this).serialize().split('&');

        //Build Name
        var name = '<span>' + decodeURIComponent(input[0].split('=')[1]).toUpperCase() + '</span>';
        name += decodeURIComponent(input[1].split('=')[1]).toUpperCase();

        //Description
        var data = decodeURIComponent(input[2].split('=')[1]);

        //Build HTML for Card
        var card = '<article data-alt-p="'+data+'"><h1>'+name+'</h1><p>Click for description!</p></article>';

        //Append Card to website
        $('#cards').append(card);
        return false;
    });

    $(document).on('click', 'article', function(){
        var p_tag = "";
        var p_alt = "";

        //toggle name
        $(this).children('h1').toggle();

        //toggle p tag
        p_tag = $(this).children('p').text();
        p_alt = $(this).attr('data-alt-p');

        $(this).children('p').text(p_alt);
        $(this).attr('data-alt-p', p_tag);
        event.stopPropagation();
    });

});



