$(function(){


var detail_list = $.get("http://0.0.0.0:3000/api/v1/content/details");

//var detail_list = [{"id": 1, "name": "First name"}, {"id": 2, "name": "Lastname"}];

for(x=0; x<detail_list.length; x++){
	
	var name = detail_list[x].name;
	var id = detail_list[x].id;
		
	$("div#checkboxes").append("<input id="+ id +" type='checkbox' name="+ name.replace(" ", "_") +">"+ detail_list[x].name  +"</input><br/>");

} 

$("#attribute-btn").click(function(){
   // var selected = [];
    $("#checkboxes input:checked").each(function(){

        //selected.push($(this).attr("name"))

	var attr_name = $(this).attr('name');
	var attr_id  = $(this).attr('id');
	
	$("#contact-btn").before("<label>"+ attr_name.replace("_"," ") +"</label>  <input type='text' name="+ attr_name +"><br/>");
	
	$(this).prop("checked", false);
    });	
	
    $("#contact-btn").show(); 

});

//Get all user inputs and submit
//Explore option of saving from view first
$("#contact-btn").click(function(){



});

});
