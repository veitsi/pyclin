$(document).ready(function(){
    
    $(".top-button")
        .mouseover(function() {
            $(this).addClass("gray");    
        })
        .mouseout(function() {
            $(this).removeClass("gray");
        })
        
    $(".header button")
        .mouseover(function() {
            $(this).addClass("hover-button");
        })
        .mouseout(function() {
            $(this).removeClass("hover-button");
        })
        

	//Switch the "Open" and "Close" state per click then slide up/down (depending on open/close state)
	$(".toggle_trigger").click(function()
    {
		$(this).next().toggle();
	});


});