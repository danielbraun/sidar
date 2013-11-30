function displayLoginBox() {
	var display = document.getElementById("login").style.display;
	if(display == "none") showLoginBox();
	if(display == "block") hideLoginBox();
}

function showLoginBox() {
	document.getElementById("login").style.display = "block";
	document.getElementById("personal_page_link").style.display = "none";
}

function hideLoginBox() {
	document.getElementById("login").style.display = "none";
	document.getElementById("personal_page_link").style.display = "block";
}


//_ open collect window

function show_collect_win(url) {
	// if(url == "" || url == "undefined") url = "showcollect.php?pos=gd";
	if(!url) {
		throw("no url entered!");
	}
	var _left = 0;
	var _top = 200;
	var _x = 0;
	var _y = _top + 70;
	var _width = 630;
	var _height = screen.height - _top - 80;
	var _scroll = "yes";
	var _status = "yes";

	window.open(url, 'collect_php', 'width=' + _width + ',height=' + _height + ',left=' + _left + ',top=' + _top + ',screenX=' + _x + ',screenY=' + _y + ',scrollbars=' + _scroll + ',status=' + _status).focus();
}


// feedback

function displayFeedbackBox() {
	var display = document.getElementById("feedback").style.display;
	if(display == "none") showFeedbackBox();
	if(display == "block") hideFeedbackBox();
}

function showFeedbackBox() {
	document.getElementById("feedback").style.display = "block";
	document.getElementById("feedback_link").style.display = "none";
}

function hideFeedbackBox() {
	document.getElementById("feedback").style.display = "none";
	document.getElementById("feedback_link").style.display = "block";
}