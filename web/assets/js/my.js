function TypeId(){
	document.getElementById("typeid").value="";
}

function authenticate(){
	var id = document.getElementById("typeid").value;
	if (id.length==0)
		alert("fuck");
	else alert("great");
	alert(findGetParameter());
	myAjax(id);
}

function findGetParameter()
{
	var result = [],tmp = {};
	window.location.search.substr(1).split("&").forEach(function(item){
		tmp = item.split("=");
		result.push(tmp[1]);
	});
	return result;
}

function myAjax(id) {
      $.ajax({
           type: "POST",
           url: '../../ajax.php',
           data:{id:id,ip:"0.0.0.0",mac:"12:34:56:78"},
           success:function(html) {
             alert("success");
           }

      });
 }