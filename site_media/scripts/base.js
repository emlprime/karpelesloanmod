$(function(){
    // fix for target="_blank"
    $("a[@rel~='external']").click(function(){
	window.open($(this).attr("href"));
	return false;
    });
});