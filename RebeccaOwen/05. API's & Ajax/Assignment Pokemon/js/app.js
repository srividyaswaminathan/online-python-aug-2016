/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
06-September-2015
Python >API's & Ajaz > Assignment: Pokemon
*/

$(document).ready(function(){
    for (i=1; i<152; i++)
    {
        var img = '<img src='+"http://pokeapi.co/media/img/" + i+ ".png" +'>';
        $("#pokemon").append(img);
    }
});



