/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
15-July-2016
Assignment: Sortable Ninja

This is the same as Assignment III: Ninja to Cat because sortable was already implemented then
*/

$(document).ready(function(){
    $('img').click(function() {
        var src = $(this).attr('src');
        var alt = $(this).attr('data-alt-src');
        //console.log(src, alt);
        $(this).attr('src', alt);
        $(this).attr('data-alt-src', src);
    });

    $("#dragDrop").sortable();
});

