$(document).ready(function(){
    $("#header").load("/../templates/header.html", function() {
        document.getElementById("header").classList.add("show");
    })
})
