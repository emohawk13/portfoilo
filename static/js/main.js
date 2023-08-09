//main js

$(window).on('scroll', function() {
    var scrolled = $(window).scrollTop();

    // Adjusting background position
    $('.parallax-section').each(function() {
        var offset = $(this).offset().top;
        var distance = scrolled - offset;
        var backgroundPos = -(distance * 0.5) + 'px';
        $(this).css('backgroundPositionY', backgroundPos);
    });
    
    // Adjusting foreground position
    $('.foreground').each(function() {
        var offset = $(this).offset().top;
        var distance = scrolled - offset;
        var foregroundPos = (distance * 0.2) + 'px'; // Adjusting the factor (0.2) as per your desired effect
        $(this).css('top', foregroundPos);
    });
});
