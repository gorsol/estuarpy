/* ************************************************************************** */
/* ** ToolTip *************************************************************** */
/* ************************************************************************** */
/* ** Made by Johan Mares for VLIZ on 06/02/2007                           ** */
/* ************************************************************************** */
/* ** Modifications: ******************************************************** */
/* ** 08/02/2007 : fixed bug in followMouseToolTip                         ** */
/* ************************************************************************** */

var ToolTipId = 'tooltipcontainer'; // if you change this, modify CSS
var ttOffsetX = 15;  // You need an offset, because otherwise in Firefox cons-
var ttOffsetY = 15;  // tantly mouseover and mouseout evenst will be triggered
var ttElm;
var ttVisible = false;
var ttBackupMouseMove; // Backup for main document's onmousemove event

/* ************************************************************************** */
/* ** FUNCTION createNewTT ************************************************** */
/* ************************************************************************** */
/* ** Creates ToolTip container (div) if it doesn't exist yet              ** */
/* ************************************************************************** */
/* ** Made by Johan Mares 06/02/2006                                       ** */
/* ************************************************************************** */
/* ** Modifications: ******************************************************** */
/* ** dd/mm/yyyy :                                                         ** */
/* ************************************************************************** */

function createNewToolTip(newid) {
	if(document.createElement){ 
		var el = document.createElement('div'); 
		el.id = newid;     
		with(el.style) { 
			display = 'none';
			position = 'absolute';
		} 
		el.innerHTML = '&nbsp;'; 
		document.body.appendChild(el); 
	} 
}

/* -------------------------------------------------------------------------- */

/* ************************************************************************** */
/* ** FUNCTION followMouseToolTip ******************************************* */
/* ************************************************************************** */
/* ** Gets the mousecoordinates (absolute). Only when tooltip is visible   ** */
/* ************************************************************************** */
/* ** Made by Johan Mares 06/02/2006                                       ** */
/* ************************************************************************** */
/* ** Modifications: ******************************************************** */
/* ** 08/02/2007 : Corrected IE bug mouse position when page > screen      ** */
/* ************************************************************************** */

function followMouseToolTip(ev) {
	if (ttVisible) {
		var pos;
		if (!ev) var ev = window.event;
		if (ev.pageX || ev.pageY) 	{
			pos = {x:ev.pageX, y:ev.pageY};
		}
		else if (ev.clientX || ev.clientY) 	{
			pos = {
				x:ev.clientX + document.body.scrollLeft + document.documentElement.scrollLeft,
				y:ev.clientY + document.body.scrollTop  + document.documentElement.scrollTop
				};
		} else {
			pos = {x:100, y:100};
		}
		ttElm.style.top = (pos.y + ttOffsetY) + 'px';
		ttElm.style.left = (pos.x + ttOffsetX) + 'px';
	}
}

/* -------------------------------------------------------------------------- */

/* ************************************************************************** */
/* ** FUNCTION showToolTip ************************************************** */
/* ************************************************************************** */
/* ** Call to show a tooltip with text and title. Only needs to be done    ** */
/* ** the first time on mousemove. This is the onmousemove eventhandler    ** */
/* ************************************************************************** */
/* ** Made by Johan Mares 06/02/2006                                       ** */
/* ************************************************************************** */
/* ** Modifications: ******************************************************** */
/* ** dd/mm/yyyy :                                                         ** */
/* ************************************************************************** */

function showToolTip(text, title){
	if (!ttVisible) {
		ttBackupMouseMove = document.onmousemove
		if (!document.getElementById(ToolTipId)) createNewToolTip(ToolTipId);
		ttElm = document.getElementById(ToolTipId);
		var tip = '<div>';
		if (typeof title != 'undefined' && title != '') {
			tip += '<h1>' + title + '</h1>';
		}
		tip += '<span>' + text + '</span></div>';
		ttElm.innerHTML = tip;
		ttElm.style.display = 'block';
		ttElm.style.left = -1000;
		ttVisible = true;
		document.onmousemove = followMouseToolTip;
	}
}

/* -------------------------------------------------------------------------- */

/* ************************************************************************** */
/* ** FUNCTION hideToolTip ************************************************** */
/* ************************************************************************** */
/* ** Hides ToolTip. Returns document.onmousemove to original eventhandler.** */
/* ************************************************************************** */
/* ** Made by Johan Mares 06/02/2006                                       ** */
/* ************************************************************************** */
/* ** Modifications: ******************************************************** */
/* ** dd/mm/yyyy :                                                         ** */
/* ************************************************************************** */

function hideToolTip() {
    document.getElementById(ToolTipId).style.display = 'none';
	ttVisible = false;
    document.onmousemove = ttBackupMouseMove;
	ttBackupMouseMove = null;
}

/* -------------------------------------------------------------------------- */