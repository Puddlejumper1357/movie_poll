var myButton=function(me){
	var form=me.parentNode;
	var slider=form.querySelector('input');
	var value=slider.value;
}
var mySlider=function(me){
	var image=document.getElementById( me.getAttribute("related-image-id"))
	image.src="/static/polls/Images/"+me.value+"s.JPG";
}

