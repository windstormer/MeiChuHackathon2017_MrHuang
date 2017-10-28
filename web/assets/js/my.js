function TypeId(){
	if(document.getElementById("typeid").value=="type chat id")
		document.getElementById("typeid").value="";
}

function authenticate(){
	var id = document.getElementById("typeid").value;
	var ip,mac;
	if (id.length!=0 && id!=document.getElementById("typeid").defaultValue)
	{
		alert('redirecting!!');
		result = findGetParameter();
		for (var para in result){
			// alert(result[para]['key']+","+result[para]['value']);
			if(result[para]['key']=="ip")
				{
					ip = result[para]['value'];
				}
			if(result[para]['key']=="mac")
				mac = result[para]['value'];
		}
		myAjax(id,ip,mac);
		window.location = "http://lms.nthu.edu.tw/?token=9487";
	}else
		alert('Please type id!!');
	
}
function Enterdetect(e){
    if (!e) e = window.event;
    var keyCode = e.keyCode || e.which;
    if (keyCode == '13'){
      authenticate();
      return false;
    }
  }

function findGetParameter()
{
	var dict = [],tmp = {};
	window.location.search.substr(1).split("&").forEach(function(item){
		tmp = item.split("=");
		dict.push();

dict.push({
    key:   tmp[0],
    value: tmp[1]
});
	});
	return dict;
}

function myAjax(id,ip,mac) {
	$.ajax({
		type: "POST",
		url: '../../ajax.php',
		data:{id:id,ip:ip,mac:mac},
		success:function(html) {
             //alert("success");
         }

     });
}