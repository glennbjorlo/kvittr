//Scripts for giving thumbs up


$(document).ready(function(){
	$('#thumbup').click(function(event){
		event.preventDefault();
		$.ajax({
			url:$('#urlthumbup').val()
		})
		.done(function(data) {
			var thumbs_up_updated = data['thumbs_up'];
			$('.glyphicon-thumbs-up').html(thumbs_up_updated);
		});
	});
});
