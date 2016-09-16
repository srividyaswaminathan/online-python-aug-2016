/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
07-September-2015
Python > API's & Ajax > Assignment: What's that Pokemon? Build Your Own Pokedex
*/

$(document).ready(function(){
    for (i=1; i<152; i++)
    {
        var img = '<img id="' +i+ '"  src='+"http://pokeapi.co/media/img/" + i+ ".png" +'>';
        $("#pokemon").append(img);
    }

    $('img').click(function(event){

        var url = 'http://pokeapi.co/api/v2/pokemon/'+$(this).attr('id');
        $.get(url, function(data) {
            //console.log(data);
            var html = "<h1>" + data.name + "</h1>";
            for(var sprite in data.sprites) {
                if (data.sprites[sprite] != null)
                {
                    html += '<img src="'+data.sprites[sprite]+'" alt="'+sprite+'">';
                }
            }
            html += "<h3>Types</h3>";
            html += "<ul>"
            for(var i = 0; i < data.types.length; i++) {
                html += "<li>" + data.types[i].type.name + "</li>";
            }
            html += "</ul>";
            html += "<h3>Height</h3>";
            html += "<p>" + data.height + "</p>";
            html += "<h3>Weight</h3>";
            html += "<p>" + data.weight + "</p>";
            //console.log(html);
            $('#pokedex').html(html);
        }, 'json');
    })
});



