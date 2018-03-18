$(document).ready(function() {
    $('.btn-hello').click(function() {
        $.getJSON('_hello', {
            name: 'world'
        }, function(data) {
            $('#hello').text(data);
        });
    });
})
