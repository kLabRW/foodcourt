function addItemOrder(){
	//build an object of order data to submit.
	var data = {
		order: jQuery('#menu_order').val() };
	//make request, process response
	jQuery.post("/order/item/add/", data,
		function(response){
			// evaluate the "success" parameter
			if(response.success == "True"){
				// disable the submit button to prevent duplicates
				jQuery("#submit_order").attr('disabled','disabled');
			}
		}, "json");
}

function prepareDocument(){
	//code to prepare page here.
	jQuery("#submit_order").click(addItemOrder);
	jQuery("#left_grid").load(addItemOrder);
	//jQuery("#order_form").addclass('hidden');
	
}



jQuery(document).ready(prepareDocument);
