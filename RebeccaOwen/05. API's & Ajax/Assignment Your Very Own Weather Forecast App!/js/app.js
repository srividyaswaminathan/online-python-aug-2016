/*
Pajama Programmer
Coding Dojo - July 5 Online Flex
07-September-2015
Python > API's & Ajax > Assignment: Your Very Own Weather Forecast App!
*/

$(document).ready(function() {

    $('form').submit(function() {

        var city = $('#city').val();

        var url = 'http://api.openweathermap.org/data/2.5/weather?q=' +city+'&units=imperial&APPID=386e0d3f54cc98472c2b5f640fa1ce23'
        console.log(url);


        $.get(url, function(data) {
            console.log(data);

            $('#city_chosen').html(data.name);
            $('#temp').html("Temperature: " + data.main.temp);

        }, 'json');

        return false;
    });
});



