var timer;
var count=0;
function show_option()
{
		 change_year();
}
var load_finish=1;

function change_year()
{
	if(load_finish==0)//not finish loading previus yet
	{
		alert("Loading Please Wait......");
		return 0;
	}
	load_finish=0;
	clearInterval(timer);
	document.getElementById("loading").innerHTML='';
	year=document.getElementById("year").value;
	year=parseInt(year)+2000;
	console.log(year);
	path="/view/?year="+year;
	window.history.pushState("object", "Title", path);
//	window.history.replaceState("object", "Title", "/new-path2");
	time=15;
timer=setInterval(set_timer,1000)
document.getElementById("year_load").style.display="block";
function set_timer(){
	
	
if(time>0)
{
	document.getElementById("year_load").innerHTML='getting graphs of year '+year+' in '+time+' seconds';
	time--;
}
else if (time>-10)
{
	document.getElementById("year_load").innerHTML='Please Patientgetting graphs of year '+year+' in Few seconds';
	time--;
}
else
{
	document.getElementById("year_load").innerHTML='Please Wait its can be an error this page is get reloading';
	location.reload();
}

}

	document.getElementById("year_load").style.display="block";
get_new_data(year);	

}




function get_new_data(year)
{

	 var xmlhttp = new XMLHttpRequest();
        
		xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
				clearInterval(timer);
//				document.getElementById("year_load"),innerHTML=str;
				document.getElementById("year_load").style.display="none";
                //document.getElementById("loading").innerHTML='';
				document.getElementById("loading").innerHTML = this.responseText;
				load_finish=1;
				
            }
        };
        xmlhttp.open("GET", "/view/?year=" + year, true);
        xmlhttp.send();
}
// document.getElementsByTagName("tr")[1].style.color='white';
// document.getElementsByTagName("tr")[1].style.backgroundColor='gray';
