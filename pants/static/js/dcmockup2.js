var pants = [
		{
		"Brand": "Levi's",
		"Style": "514",
		"Waist": "Same Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant0.jpg'></img>",
		},
		{
		"Brand": "Banana Republic",
		"Style": "Slim Fit",
		"Waist": "Same Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant1.jpg'></img>",
		},	
		{
		"Brand": "Gap",
		"Style": "Relaxed Fit",
		"Waist": "Same Waist",
		"Cuff": "Looser at Ankle",
		"Image": "<img src='pant2.jpg'></img>",
		},
		{
		"Brand": "Old navy",
		"Style": "Urban Slim",
		"Waist": "Looser Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant3.jpg'></img>",
		},
		{
		"Brand": "Dockers",
		"Style": "Slim Fit",
		"Waist": "Looser Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant4.jpg'></img>",
		},
		{
		"Brand": "Wings + Horns",
		"Style": "Slim Fit",
		"Waist": "Looser Waist",
		"Cuff": "Looser at Ankle",
		"Image": "<img src='pant5.jpg'></img>",
		},
		{
		"Brand": "Penny Stock",
		"Style": "Relaxed Fit",
		"Waist": "Tighter Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant6.jpg'></img>",
		},
		{
		"Brand": "Beta Unit",
		"Style": "Urban Slim",
		"Waist": "Tighter Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant7.jpg'></img>",
		},
		{
		"Brand": "Dunderdon",
		"Style": "Slim Fit",
		"Waist": "Tighter Waist",
		"Cuff": "Looser at Ankle",
		"Image": "<img src='pant8.jpg'></img>",
		},
		{
		"Brand": "Obey",
		"Style": "Slim Fit",
		"Waist": "Tighter Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant9.jpg'></img>",
		},
		{
		"Brand": "Woolrich",
		"Style": "Relaxed Fit",
		"Waist": "Same Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant10.jpg'></img>",
		},
		{
		"Brand": "Rogue Territory",
		"Style": "Urban Slim",
		"Waist": "Looser Waist",
		"Cuff": "Tighter at Ankle",
		"Image": "<img src='pant11.jpg'></img>",
		},
		{
		"Brand": "Left Field",
		"Style": "Slim Fit",
		"Waist": "Tighter Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant12.jpg'></img>",
		},
		{
		"Brand": "Apolis",
		"Style": "Slim Fit",
		"Waist": "Same Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant13.jpg'></img>",
		},
		{
		"Brand": "Insight",
		"Style": "Relaxed Fit",
		"Waist": "Looser Waist",
		"Cuff": "Same at Ankle",
		"Image": "<img src='pant14.jpg'></img>",
		},
		{
		"Brand": "Kill City",
		"Style": "Urban Slm",
		"Waist": "Looser Waist",
		"Cuff": "Looser at Ankle",
		"Image": "<img src='pant15.jpg'></img>",
		},
]

$(document).ready(function() {
	$("li[name='cuff8']").click(function () {
     cuff8();
   });
  	$("li[name='cuff9']").click(function () {
     cuff9();
  	 });
   	$("li[name='waist32']").click(function() {
   	 waist32();
   });	
   	$("li[name='waist33']").click(function() {
   	 waist33();
   });	
});

function cuff8() {
	var cuffcount=6
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[0].Image;
		a+= '<li><b>' + pants[0].Brand + '</b></li>';
		a+= '<li>'+pants[0].Style + '</li>';
		a+= '<li onclick="waist32cuff8()">'+pants[0].Waist + '</li>';
		a+= '<li id="selected">'+pants[0].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[3].Image;
		a+= '<li><b>' + pants[3].Brand + '</b></li>';
		a+= '<li>'+pants[3].Style + '</li>';
		a+= '<li onclick="waist33cuff8()">'+pants[3].Waist + '</li>';
		a+= '<li id="selected">'+pants[3].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==2) {
		a+= '<div id="item">';
		a+= pants[6].Image;
		a+= '<li><b>' + pants[6].Brand + '</b></li>';
		a+= '<li>'+pants[6].Style + '</li>';
		a+= '<li onclick="waist31cuff8()">'+pants[6].Waist + '</li>';
		a+= '<li id="selected">'+pants[6].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==3) {
		a+= '<div id="item">';
		a+= pants[9].Image;
		a+= '<li><b>' + pants[9].Brand + '</b></li>';
		a+= '<li>'+pants[9].Style + '</li>';
		a+= '<li onclick="waist31cuff8()">'+pants[9].Waist + '</li>';
		a+= '<li id="selected">'+pants[9].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==4) {
		a+= '<div id="item">';
		a+= pants[10].Image;
		a+= '<li><b>' + pants[10].Brand + '</b></li>';
		a+= '<li>'+pants[10].Style + '</li>';
		a+= '<li onclick="waist32cuff8()">'+pants[10].Waist + '</li>';
		a+= '<li id="selected">'+pants[10].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==5) {
		a+= '<div id="item">';
		a+= pants[11].Image;
		a+= '<li><b>' + pants[11].Brand + '</b></li>';
		a+= '<li>'+pants[11].Style + '</li>';
		a+= '<li onclick="waist33cuff8()">'+pants[11].Waist + '</li>';
		a+= '<li id="selected">'+pants[11].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
	}
}

function cuff9() {
	var cuffcount=6
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[1].Image;
		a+= '<li><b>' + pants[1].Brand + '</b></li>';
		a+= '<li>'+pants[1].Style + '</li>';
		a+= '<li onclick="waist32cuff9()">'+pants[1].Waist + '</li>';
		a+= '<li id="selected">'+pants[1].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[4].Image;
		a+= '<li><b>' + pants[4].Brand + '</b></li>';
		a+= '<li>'+pants[4].Style + '</li>';
		a+= '<li onclick="waist33cuff9()">'+pants[4].Waist + '</li>';
		a+= '<li id="selected">'+pants[4].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==2) {
		a+= '<div id="item">';
		a+= pants[7].Image;
		a+= '<li><b>' + pants[7].Brand + '</b></li>';
		a+= '<li>'+pants[7].Style + '</li>';
		a+= '<li>'+pants[7].Waist + '</li>';
		a+= '<li id="selected">'+pants[7].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==3) {
		a+= '<div id="item">';
		a+= pants[12].Image;
		a+= '<li><b>' + pants[12].Brand + '</b></li>';
		a+= '<li>'+pants[12].Style + '</li>';
		a+= '<li>'+pants[12].Waist + '</li>';
		a+= '<li id="selected">'+pants[12].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==4) {
		a+= '<div id="item">';
		a+= pants[13].Image;
		a+= '<li><b>' + pants[13].Brand + '</b></li>';
		a+= '<li>'+pants[13].Style + '</li>';
		a+= '<li onclick="waist32cuff9()">'+pants[13].Waist + '</li>';
		a+= '<li id="selected">'+pants[13].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==5) {
		a+= '<div id="item">';
		a+= pants[14].Image;
		a+= '<li><b>' + pants[14].Brand + '</b></li>';
		a+= '<li>'+pants[14].Style + '</li>';
		a+= '<li onclick="waist33cuff9()">'+pants[14].Waist + '</li>';
		a+= '<li id="selected">'+pants[14].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
	}
}

function waist32() {
	var cuffcount=5
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[0].Image;
		a+= '<li><b>' + pants[0].Brand + '</b></li>';
		a+= '<li>'+pants[0].Style + '</li>';
		a+= '<li id="selected">'+pants[0].Waist + '</li>';
		a+= '<li onclick="waist32cuff8()">'+pants[0].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[1].Image;
		a+= '<li><b>' + pants[1].Brand + '</b></li>';
		a+= '<li>'+pants[1].Style + '</li>';
		a+= '<li id="selected">'+pants[1].Waist + '</li>';
		a+= '<li onclick="waist32cuff9()">'+pants[1].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==2) {
		a+= '<div id="item">';
		a+= pants[2].Image;
		a+= '<li><b>' + pants[2].Brand + '</b></li>';
		a+= '<li>'+pants[2].Style + '</li>';
		a+= '<li id="selected">'+pants[2].Waist + '</li>';
		a+= '<li onclick="waist32cuff10()">'+pants[2].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==3) {
		a+= '<div id="item">';
		a+= pants[10].Image;
		a+= '<li><b>' + pants[10].Brand + '</b></li>';
		a+= '<li>'+pants[10].Style + '</li>';
		a+= '<li id="selected">'+pants[10].Waist + '</li>';
		a+= '<li onclick="waist32cuff8()">'+pants[10].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==4) {
		a+= '<div id="item">';
		a+= pants[13].Image;
		a+= '<li><b>' + pants[13].Brand + '</b></li>';
		a+= '<li>'+pants[13].Style + '</li>';
		a+= '<li id="selected">'+pants[13].Waist + '</li>';
		a+= '<li onclick="waist32cuff9()">'+pants[13].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
	}
}

function waist33() {
	var cuffcount=6
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[3].Image;
		a+= '<li><b>' + pants[3].Brand + '</b></li>';
		a+= '<li>'+pants[3].Style + '</li>';
		a+= '<li id="selected">'+pants[3].Waist + '</li>';
		a+= '<li onclick="waist33cuff8()">'+pants[3].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[4].Image;
		a+= '<li><b>' + pants[4].Brand + '</b></li>';
		a+= '<li>'+pants[4].Style + '</li>';
		a+= '<li id="selected">'+pants[4].Waist + '</li>';
		a+= '<li onclick="waist33cuff9()">'+pants[4].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==2) {
		a+= '<div id="item">';
		a+= pants[5].Image;
		a+= '<li><b>' + pants[5].Brand + '</b></li>';
		a+= '<li>'+pants[5].Style + '</li>';
		a+= '<li id="selected">'+pants[5].Waist + '</li>';
		a+= '<li onclick="waist33cuff10()">'+pants[5].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==3) {
		a+= '<div id="item">';
		a+= pants[11].Image;
		a+= '<li><b>' + pants[11].Brand + '</b></li>';
		a+= '<li>'+pants[11].Style + '</li>';
		a+= '<li id="selected">'+pants[11].Waist + '</li>';
		a+= '<li onclick="waist33cuff8()">'+pants[11].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==4) {
		a+= '<div id="item">';
		a+= pants[14].Image;
		a+= '<li><b>' + pants[14].Brand + '</b></li>';
		a+= '<li>'+pants[14].Style + '</li>';
		a+= '<li id="selected">'+pants[14].Waist + '</li>';
		a+= '<li onclick="waist33cuff9()">'+pants[14].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==5) {
		a+= '<div id="item">';
		a+= pants[15].Image;
		a+= '<li><b>' + pants[15].Brand + '</b></li>';
		a+= '<li>'+pants[15].Style + '</li>';
		a+= '<li id="selected">'+pants[15].Waist + '</li>';
		a+= '<li onclick="waist33cuff10()">'+pants[15].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
	}
}
function waist31cuff8() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[6].Image;
		a+= '<li><b>' + pants[6].Brand + '</b></li>';
		a+= '<li>'+pants[6].Style + '</li>';
		a+= '<li id="selected">'+pants[6].Waist + '</li>';
		a+= '<li id="selected">'+pants[6].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[9].Image;
		a+= '<li><b>' + pants[9].Brand + '</b></li>';
		a+= '<li>'+pants[9].Style + '</li>';
		a+= '<li id="selected">'+pants[9].Waist + '</li>';
		a+= '<li id="selected">'+pants[9].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		
	}
}

function waist32cuff8() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[0].Image;
		a+= '<li>`<b>' + pants[0].Brand + '</b></li>';
		a+= '<li>'+pants[0].Style + '</li>';
		a+= '<li id="selected">'+pants[0].Waist + '</li>';
		a+= '<li id="selected">'+pants[0].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[10].Image;
		a+= '<li><b>' + pants[10].Brand + '</b></li>';
		a+= '<li>'+pants[10].Style + '</li>';
		a+= '<li id="selected">'+pants[10].Waist + '</li>';
		a+= '<li id="selected">'+pants[10].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		
	}
}

function waist32cuff9() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[1].Image;
		a+= '<li><b>' + pants[1].Brand + '</b></li>';
		a+= '<li>'+pants[1].Style + '</li>';
		a+= '<li id="selected">'+pants[1].Waist + '</li>';
		a+= '<li id="selected">'+pants[1].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[13].Image;
		a+= '<li><b>' + pants[13].Brand + '</b></li>';
		a+= '<li>'+pants[13].Style + '</li>';
		a+= '<li id="selected">'+pants[13].Waist + '</li>';
		a+= '<li id="selected">'+pants[13].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}
	}
}

function waist32cuff10() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[2].Image;
		a+= '<li><b>' + pants[2].Brand + '</b></li>';
		a+= '<li>'+pants[2].Style + '</li>';
		a+= '<li id="selected">'+pants[2].Waist + '</li>';
		a+= '<li id="selected">'+pants[2].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}		
	}
}

function waist33cuff8() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[3].Image;
		a+= '<li><b>' + pants[3].Brand + '</b></li>';
		a+= '<li>'+pants[3].Style + '</li>';
		a+= '<li id="selected">'+pants[3].Waist + '</li>';
		a+= '<li id="selected">'+pants[3].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}	
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[11].Image;
		a+= '<li><b>' + pants[11].Brand + '</b></li>';
		a+= '<li>'+pants[11].Style + '</li>';
		a+= '<li id="selected">'+pants[11].Waist + '</li>';
		a+= '<li id="selected">'+pants[11].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}	
	}
}

function waist33cuff9() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[4].Image;
		a+= '<li><b>' + pants[4].Brand + '</b></li>';
		a+= '<li>'+pants[4].Style + '</li>';
		a+= '<li id="selected">'+pants[4].Waist + '</li>';
		a+= '<li id="selected">'+pants[4].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}	
		else if (i==1) {
		a+= '<div id="item">';
		a+= pants[14].Image;
		a+= '<li><b>' + pants[14].Brand + '</b></li>';
		a+= '<li>'+pants[14].Style + '</li>';
		a+= '<li id="selected">'+pants[14].Waist + '</li>';
		a+= '<li id="selected">'+pants[14].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}	
	}
}

function waist33cuff10() {
	var cuffcount=2
	var a= ''
	for (i=0; i<cuffcount; i++) {
		if (i==0) {
		a+= '<div id="item">';
		a+= pants[5].Image;
		a+= '<li><b>' + pants[5].Brand + '</b></li>';
		a+= '<li>'+pants[5].Style + '</li>';
		a+= '<li id="selected">'+pants[5].Waist + '</li>';
		a+= '<li id="selected">'+pants[5].Cuff+'</li></div>';
		document.getElementById('resultpants').innerHTML = a;	
		}	
	}
}

