
// function
(function($){

  $.fn.loopBg = function(options){
      var self = this;
      var color_index = 0;

      var settings = {
          colors: Array('#f00', '#0f0', '#00f'),
          duration: 50000
      }
      var opts = $.extend({},settings,options);

    $.fn.recurseAnim = function(){
        $(self).animate({ backgroundColor: opts.colors[color_index] }, opts.duration,
            function() {
                if( color_index+1 == opts.colors.length){
                    color_index = 0;
                } else {
                    ++color_index;
                }
                $.fn.recurseAnim();
            }
        );
    };
    $.fn.recurseAnim();

    return this;
}

})(jQuery);

// usage
$(function(){
  $("body").loopBg(
      {
          colors: Array('#077bf4', '#fedf01'),
          duration: 5000
      }
  );
});
