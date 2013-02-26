jQuery(document).ready(function() {
	$("#login_form").ajaxForm({
		success: function(response) {
			$("#login_form tbody").html(response);
		},
		error: function() {
			location.reload();
		}
	});


	$("#collect_form").ajaxForm();
	$("#collect_form a").click(function(e) {
		e.preventDefault();
		$("#collect_form").submit();
	});

	// var search_form = $("#search_form");
	// search_form.ajaxForm(function(response) {
	// 	$("#search_form tbody").html(response);
	// 	bind_search_form_selects();
	// });
	// bind_search_form_selects();
	// function bind_search_form_selects() {
	// 	$("#search_form select").change(function() {
	// 		search_form.submit();
	// 	});
	// }

	// $('#open_collection_link').click(function(e) {
	// 	e.preventDefault();
	// 	show_collect_win();
	// });
});