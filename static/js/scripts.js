(function ($) {
    "use strict";
    // data-background (for background image)
	$("[data-background]").each(function() {
	    $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
	});
    
    // carousel
    $('.top-categories-carousel').owlCarousel({
        loop: true,
        margin: 50,
        items: 4,
        autoplay: true,
        nav: false,
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        dots: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false,
                autoplay: true,
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });
    
    // carousel
    $('.brand-carousel').owlCarousel({
        loop: true,
        margin: 30,
        items: 5,
        autoplay: true,
        nav: false,
        navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
        dots: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false,
                autoplay: true,
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
    
    // Countdown
    $("[data-countdown]").each(function () {
        var $this = $(this),
            finalDate = $(this).data("countdown");
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="cdown day">%-D <p>Days</p></span> <span class="cdown hour">%-H <p>Hours</p></span> <span class="cdown minutes">%M <p>Mins</p></span> <span class="cdown second">%S <p>Sec</p></span>'));
        });
    });
    
   $('.offers-carousel').slick({
       slidesToShow: 1,
       slidesToScroll: 1,
       arrows: false,
       asNavFor: '.offers-carousel-thumbnail',
       dots: false,
       // dotsClass:'slick-modified-dots',
   });
   $('.offers-carousel-thumbnail').slick({
       slidesToShow: 2,
       slidesToScroll: 1,
       asNavFor: '.offers-carousel',
       dots: true,
       centerMode: false,
       focusOnSelect: true,
       arrows: false,
       vertical: true,
       verticalSwiping: true,
       dots: false,
   });
    
    $('.review-carousel').slick({
       slidesToShow: 1,
       slidesToScroll: 1,
       arrows: false,
       asNavFor: '.review-carousel-thumbnail',
       dots: false,
       // dotsClass:'slick-modified-dots',
   });
   $('.review-carousel-thumbnail').slick({
       slidesToShow: 3,
       slidesToScroll: 1,
       asNavFor: '.review-carousel',
       dots: true,
       centerMode: true,
       focusOnSelect: true,
       arrows: false,
       dots: false,
   });
    

    new WOW().init();

    /*---background image---*/
    function dataBackgroundImage() {
        $('[data-bgimg]').each(function () {
            var bgImgUrl = $(this).data('bgimg');
            $(this).css({
                'background-image': 'url(' + bgImgUrl + ')', // + meaning concat
            });
        });
    }

    $(window).on('load', function () {
        dataBackgroundImage();
    });

    /*---stickey menu---*/
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 100) {
            $(".sticky-header").removeClass("sticky");
        } else {
            $(".sticky-header").addClass("sticky");
        }
    });

    $('.modal').on('shown.bs.modal', function (e) {
        $('.product_navactive').resize();
    })

    /*--- Video Popup---*/
    $('.video_popup').magnificPopup({
        type: 'iframe',
        removalDelay: 300,
        mainClass: 'mfp-fade'
    });

    /*---Photo Popup---*/
    $('.port_popup').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });


    /*--- niceSelect---*/
    $('.select_option').niceSelect();

//    /*---portfolio Isotope activation---*/
//    $('.portfolio_gallery').imagesLoaded(function () {
//
//        var $grid = $('.portfolio_gallery').isotope({
//            itemSelector: '.gird_item',
//            percentPosition: true,
//            masonry: {
//                columnWidth: '.gird_item'
//            }
//        });
//
//        /*---ilter items on button click---*/
//        $('.portfolio_button').on('click', 'button', function () {
//            var filterValue = $(this).attr('data-filter');
//            $grid.isotope({
//                filter: filterValue
//            });
//
//            $(this).siblings('.active').removeClass('active');
//            $(this).addClass('active');
//        });
//
//    });

        // isotop massonry
        $('.grid').imagesLoaded(function() {
            // init Isotope
            var $grid = $('.grid').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry: {
                    // use outer width of grid-sizer for columnWidth
                    columnWidth: 1,
                }
            });
            // filter items on button click
            $('.button-group').on('click', 'button', function() {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({
                    filter: filterValue
                });
            });
        });
        //for isotop massonry menu active class
        $('.button-group > button').on('click', function(event) {
            $(this).siblings('.active').removeClass('active');
            $(this).addClass('active');
            event.preventDefault();
        });
    
    
    /*---categories slideToggle---*/
    $(".categories-title").on("click", function() {
        $(this).toggleClass('active');
        $('.categories-menu-toggle').slideToggle('medium');
    }); 

})(jQuery);