// -----------------------------------------------------------------------
// Copyright ...
// blahblah  ...
// -----------------------------------------------------------------------


function cropID(IDin)
{
    var ind = IDin.indexOf(':');
    if (ind < 0) return IDin;
    return IDin.substring(0, ind);
}

function generateConceptLevel (presserdepth) {
    var Container = document.getElementById("AbsContainerContainer");
    
    var outerDiv = document.createElement('div');
    outerDiv.setAttribute('class', 'absContainer');
    var leftArrow = document.createElement('img');
    leftArrow.setAttribute('class', 'conceptArrow Left');
    leftArrow.setAttribute('src', 'img/arrow6.png');
    leftArrow.setAttribute('data-depth', presserdepth+1);
    addArrowListener2(leftArrow, 'L');

    var div = document.createElement('div');
    div.setAttribute('class', 'abstractionLevel');
    var movingDiv = document.createElement('div');
    movingDiv.setAttribute('class', 'movingAbsLevel');

    var rightArrow = document.createElement('img');
    rightArrow.setAttribute('class', 'conceptArrow Right');
    rightArrow.setAttribute('src', 'img/arrow6.png');
    rightArrow.setAttribute('data-depth', presserdepth+1);
    addArrowListener2(rightArrow, 'R');

    Container.appendChild(outerDiv);
    div.appendChild(movingDiv);
    outerDiv.appendChild(leftArrow);
    outerDiv.appendChild(div);
    outerDiv.appendChild(rightArrow);

    return movingDiv;
}


function fillDivWithButtons(div, depth, idlist, textlist) {
    for (i = 0; i < idlist.length; i++) {
	if (textlist.length < i) {
	    break;
	}
	var b = document.createElement('a');
	b.setAttribute('class', 'conceptButton');
	b.setAttribute('data-depth', depth);
	b.setAttribute('href', '#');
	b.setAttribute('id', idlist[i]);
	b.setAttribute('onclick', "requestProba(this.id, this.getAttribute('data-depth'))");
	b.innerHTML = textlist[i];
	div.appendChild(b);
    }
}

function removeConceptLines(presserdepth) {
    console.log("deleting... " + presserdepth);
    var Container = document.getElementById("AbsContainerContainer");
    while (Container.children.length > presserdepth+1) {
	Container.removeChild(Container.children[Container.children.length-1]);
    }
}

function requestProba(sentID, depth)
{
    // crop the ID (removing :2, :3 etc from the end):
    var rawID = sentID;
    sentID = cropID(sentID);
    depth = parseInt(depth);

    // sending the request to the server:
    const Http = new XMLHttpRequest();
    const url='http://127.0.0.1:15400';
    var params = "id=" + sentID;
    Http.open("GET", url + "?" + params);
    Http.overrideMimeType("text/html");
    Http.send();

    // the reaction to the response:
    Http.onreadystatechange = (e) => {
	if(Http.status == 200) {
	    if(Http.readyState == 0 || Http.readyState == 4) {
		var childstr = Http.responseText;
		childstr = childstr.replace("[", '');
		childstr = childstr.replace("]", '');
		childstr = childstr.replace(/'/g, '');
		childstr = childstr.replace(/ /g, '');
		// creating a list of IDs from the response text:
		var children = childstr.split(",");
		// alert("Children: '" + children + "'");

		removeConceptLines(depth);

		var pressed = document.getElementById(rawID);
		var parent = pressed.parentElement;

		for(var i = 0; i < parent.children.length; i++) {
		    parent.children[i].style.textDecoration = "initial";
		    console.log(parent.children[i]);
		}		

		pressed.style.textDecoration = "underline";
		
		if(children[0] == "") return;
		
		// creating the next absContainer:
		var div = generateConceptLevel(depth);
		
		// filling the abscontainer with the proper buttons:
		fillDivWithButtons(div, depth+1, children, children);
		
		
	    }
	}
    }
}

// --------------------------------------------------------------------
// Adding the events:

var elements;
var doAnimation=false;
var animated = undefined;
var startloc=undefined;
var starttime=-1;
var direction = undefined;

function step(timestamp) {
    /*console.log(timestamp);*/
    if (!doAnimation) return;
    if (starttime == -1) starttime = timestamp;
    var progress = timestamp - starttime;
    var currentloc;
    if(direction == "R")
	currentloc = startloc + (progress / 10)*1.8;
    else currentloc = startloc - (progress / 10)*1.8;
    animated.style.transform = 'translateX(' + currentloc + 'px)';
    if(doAnimation == true) {
	window.requestAnimationFrame(step);
    }
}

function addArrowListener2(arrow, dir) {
    var depth = arrow.getAttribute("data-depth");
    console.log("The depth I got: " + depth);
    arrow.addEventListener
    ("mouseover",
     function(){
	 if(doAnimation == true) return;
	 var cont = document.getElementById("AbsContainerContainer");
	 var cL = cont.children.item(depth);
	 for (var i = 0; i < cL.children.length; i++) {
	     if (cL.children[i].className == "abstractionLevel")
		 animated = cL.children[i];
	 }
	 animated = animated.children[0];
	 startloc = animated.style.transform;
	 if(startloc == '') startloc = 0;
	 else startloc = parseInt(startloc.substring(11, startloc.length -3));
	 /*console.log("'"+startloc + "'  " + typeof startloc);*/
	 doAnimation = true;
	 direction = dir;
	 window.requestAnimationFrame(step);
     } 
    );
    arrow.addEventListener
    ("mouseleave",
     function(){/*clearInterval(repeater);*/
	 doAnimation = false;
	 animated = undefined;
	 starttime = -1;
     } 
    );
    
}

//***************************************************************************
// code that adds the animation event handler:

elements = document.getElementsByClassName("conceptArrow Right");
for(var i = 0; i < elements.length; i++) {
    var arrow = elements[i];
    addArrowListener2(arrow, 'R');
}

elements = document.getElementsByClassName("conceptArrow Left");
for(var i = 0; i < elements.length; i++) {
    var arrow = elements[i];
    addArrowListener2(arrow, 'L');
}
