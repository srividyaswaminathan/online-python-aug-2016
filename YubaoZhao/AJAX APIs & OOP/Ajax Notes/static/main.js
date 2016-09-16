$(document).ready(function() {
// Add notes...
    $('form').submit(function() {
        console.log("Form data:", $(this).serialize());
        var title = $(this).children('input').val();
        if(title.replace(/\s/g, '')) {
            var url = "/notes/create";
            $.post(url, $(this).serialize(), function(res) {
                // console.log(res);
                $('div#notes').html(res);
            });
        }
        else {
            console.log("No title input...");
        }
        $(this).children('input').val("");
        return false;
    });
// Delete notes..
    $('div#notes').on('click', 'b', function() {
        if (confirm("Confirm Delete?")) {
            var id = $(this).attr('id');
            console.log("Delete ID:", id);
            var url = "/notes/" + id + "/delete";
            console.log("URL:", url);
            $.get(url, function(res) {
                // console.log(res);
                $('div#notes').html(res);
            });
        }
        else return false;
    });
// Update notes...
    var oldValue = "";
    var newValue = "";
    var item = "";
    $('div#notes').on('focus', 'input, textarea', function() {
        item = $(this).attr('name');
        // console.log("Focus:",item);
        if($(this).attr('name') === 'title') {
            $(this).css("border-bottom","1px solid silver");
        }
        oldValue = $(this).val();
        // console.log("Old %s value: %s",$(this).attr('name'), oldValue);
    });
    $('div#notes').on('blur', 'input, textarea', function() {
        if($(this).attr('name') === 'title') {
            $(this).css("border-bottom","none");
        }
        item = $(this).attr('name');
        // console.log("Blur:",item);
        newValue = $(this).val();
        // console.log("New %s value: %s",$(this).attr('name'), newValue);
        if(newValue !== oldValue) {
            var id = $(this).parent().attr('id');
            if($(this).val().replace(/\s/g, '')) {
                var data = $(this).parent('form').serialize();
                var url = "/notes/" + id + "/update";
                $.post(url, data, function(res) {
                    $('div#notes').html(res);
                });
            }
            else {
                // console.log("No %s input...", item);
                $(this).val(oldValue);
            }
        }
        else console.log("No changes.No update.");
    });
});
