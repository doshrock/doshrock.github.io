/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

(function($) {
    "use strict"; // Start of use strict

    // Smooth scroll for same-page "#section" links - requires jQuery Easing plugin.
    // Other hrefs ("/#about", "/index-en", external) keep the browser's default navigation.
    $('a.page-scroll').on('click', function(event) {
        var href = $(this).attr('href');
        if (!href || href.charAt(0) !== '#') {
            return;
        }
        var target = document.getElementById(href.slice(1));
        if (!target) {
            return;
        }
        $('html, body').stop().animate({
            scrollTop: ($(target).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

})(jQuery); // End of use strict
