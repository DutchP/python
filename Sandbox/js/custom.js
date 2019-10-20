function generateData(){
    $.post("generate").done(function(data){
        $("#placeholder").html("<ul data-role='listview' data-inset='true'>"+data+"</ul>");
    })
}
function regenerateData(){
		$.post("regenerate").done(function(data){
				$("#placeholder").html("<h1>andere data</h1><ul data-role='listview' data-inset='true'>"+data+"</ul>");
		})

}
/*$(document).on("pagecreate","#answer",(function(e){*/
		/*generateData()	*/
/*})*/