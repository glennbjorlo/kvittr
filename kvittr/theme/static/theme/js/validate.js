

function validate() {

var regexp = /^[A-Za-zæøåÆØÅ0-9 _]{1,140}(\?)$/;

var errormessage = document.getElementById('errormessage');


	if(!regexp.test(kveetmessage.textareacomment.value)) {

	errormessage.innerHTML = 'Only numbers and letters allowed';
	return false;

	}

}
