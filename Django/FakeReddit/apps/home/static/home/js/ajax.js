// select   attach events
$("#content").keydown(function(event) {
    console.log(event.target.value);
})

$(document).ready(function() {
    alert("ready??")
    fetchStuff();
})
$('#sender').submit(function(event) {
    event.preventDefault();
    var data = $(this).serialize();
    console.log(data);
    // handle events
    $.ajax({
        url: "/ajax",
        method: "POST",
        data: data
    })
    .done(function(response) {
        $('#stuff').html(response);
    })
    $(this)[0].reset();
})
function fetchStuff() {
    $.ajax({
        url: "/ajax",
        method: "GET",
    })
    .done(function(response) {
        $('#stuff').html(response);
    })
}