$("#happy_btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#happy_hour").offset().top
    }, 1000);
});
$("#drink_btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#drinks").offset().top
    }, 1001);
});
$("#app_btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#apps").offset().top
    }, 1002);
});
$("#entree_btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#entrees").offset().top
    }, 1003);
});
$("#dessert_btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#desserts").offset().top
    }, 1004);
});