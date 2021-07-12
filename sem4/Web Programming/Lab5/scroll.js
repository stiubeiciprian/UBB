$(document).ready(function() {

  $([document.documentElement, document.body]).animate(
    {scrollTop: $("#d4").offset().top},
     0
   );

    $(".desktop").click(function() {
      try {
        $([document.documentElement, document.body]).animate(
          {scrollTop: $(this).prev().offset().top},
           2000
         );
      } catch(error) {
        $([document.documentElement, document.body]).animate(
          {scrollTop: $("#d4").offset().top},
           2000
         );
      }

    });

});
