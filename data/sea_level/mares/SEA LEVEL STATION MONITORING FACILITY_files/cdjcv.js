ase_0="1.0.1";ase_1=navigator.userAgent.toLowerCase();ase_2=(ase_1.indexOf('gecko')!=-1&&ase_1.indexOf('safari')==-1);ase_3=(ase_1.indexOf('konqueror')!=-1);ase_4=(ase_1.indexOf('safari')!=-1);ase_5=(ase_1.indexOf('opera')!=-1);ase_6=(ase_1.indexOf('msie')!=-1&&!ase_5&&(ase_1.indexOf('webtv')==-1));ase_7=ase_6?-2:0;function ase_8(){return(new RegExp("msie ([0-9]{1,}[\.0-9]{0,})").exec(ase_1)!=null)?parseFloat(RegExp.$1):6.0;}
function ase_9(){return(new RegExp("firefox[\\/\\s](\\d+\\.\\d+)").exec(ase_1)!=null)?parseFloat(RegExp.$1):2.0;}
function ase_a(id){return document.getElementById?document.getElementById(id):document.all[id];}
function ase_b(e,la,lb,lc,ld){if(e&&(typeof(e[lc])!='undefined'))return e[lc];if(window.event)return window.event[la]+((document.documentElement&&document.documentElement[lb])||document.body[lb]);else return e[la]+window[ld];}
function ase_c(e){return ase_b(e,"clientX","scrollLeft","pageX","scrollX")+ase_7;}
function ase_d(e){return ase_b(e,"clientY","scrollTop","pageY","scrollY")+ase_7;}
function ase_e(e){if(ase_6&&window.event)return window.event.button;else return(e.which==3)?2:e.which;}
function ase_f(le,lf){return le?le[lf]+ase_f(le.offsetParent,lf):0;}
function ase_g(le,lf){if((!ase_5)&&le&&(le!=document.body)&&(le!=document.documentElement))return le[lf]+ase_g(le.parentNode,lf);else return 0;}
function ase_h(le){return ase_f(le,"offsetLeft")-ase_g(le,"scrollLeft")+(le.offsetWidth-le.clientWidth)/2;}
function ase_i(le){return ase_f(le,"offsetTop")-ase_g(le,"scrollTop")+(le.offsetHeight-le.clientHeight)/2;}
function ase_j(lg,lh){return lg+((lg.indexOf('?')!=-1)?'&':'?')+lh;}
function ase_k(li,lj,lk){var re=new RegExp(lj,'g');return li.replace(re,lk);}
function ase_l(lm){var ln=document.scripts;if(((!ln)||(!ln.length))&&document.getElementsByTagName)ln=document.getElementsByTagName("script");if(ln){for(var i=0;i<ln.length;++i){var lp=ln[i].src;if(!lp)continue;var lq=lp.indexOf(lm);if(lq!=-1)return lp.substring(0,lq);}
}
return "";}
function ase_m(lr,ls,lt){var lu=lr.indexOf(ls);var lv=lr.indexOf(lt);if((lu<0)||(lv<=lu))return '';else return lr.substring(lu+ls.length,lv);}
function ase_n(lr,lw){var lq=lr.indexOf(lw);return(lq>=0)?lr.substring(0,lq):lr;}
function ase_o(lr,lw){var lq=lr.indexOf(lw);return(lq>=0)?lr.substring(lq+1,lr.length):"";}
function ase_p(v){return ase_k(ase_k(v,'&','&amp;'),'"','&#34;');}
function ase_q(n){n.onload=n.onerror='';n.src='javascript:;';var p=n.parentNode||n.parentElement;if(p&&p.removeChild)p.removeChild(n);else if(n.outerHTML)n.outerHTML='';}
function ase_r(f){var f2=frames[f.id];if(f2){var d2=f2.contentDocument||f2.document;if(d2)return d2.body.innerHTML;}
return null;}
function ase_AJAX_frame_loaded(f){if(f.lx1)return;var l31=ase_r(f);if(null!=l31)f.lh1(l31);ase_q(f);}
function ase_AJAX_frame_error(f){if(f.li1)f.li1(700,ase_r(f));ase_q(f);}
function ase_s(lg,l41,l51){var f=null;var l61="ase_AJAX_frame_"+(new Date().getTime());if(ase_6&&(ase_8()>=5.5)){document.body.insertAdjacentHTML('AfterBegin',"<IFRAME SRC='javascript:;' NAME='"+l61+"' ID='"+l61+"' style='display:none' onload='ase_AJAX_frame_loaded(this)' onerror='ase_AJAX_frame_error(this)'></IFRAME>");f=ase_a(l61);}
if(!f){if(l51)l51(600,"Cannot create IFRAME '"+l61+"'");return null;}
var f2=frames[f.id];var d2=f2.contentDocument||f2.document;f.lx1=true;d2.open();d2.write('<html><body><form name="ase_form" method="'+((lg.length<1000)?'get':'post')+'" action="'+ase_p(ase_n(lg,"?"))+'">');var l71=ase_o(lg,"?").split("&");for(var i=0;i<l71.length;++i){d2.write('<input type="hidden" name="'+ase_p(ase_n(l71[i],"="))+'" value="'+ase_p(unescape(ase_o(l71[i],"=")))+'">');}
d2.write('</form></body></html>');d2.close();f.lx1=false;f.lh1=l41;f.li1=l51;d2.forms['ase_form'].submit();return{'abort':function(){ase_q(f);}};}
function ase_t(){if(typeof XMLHttpRequest!='undefined')return new XMLHttpRequest();
/*@cc_on
@if(@_jscript_version>=5)
try{return new ActiveXObject("Msxml2.XMLHTTP");}catch(e){}
try{return new ActiveXObject("Microsoft.XMLHTTP");}catch(e){}
@end
@*/
}
function ase_u(lg,l41,l51){var r=ase_t();if(r){r.onreadystatechange=function(){if(r.readyState==4){var status=-9999;eval("try { status = r.status; } catch(e) {}");if(status==-9999)return;if((r.status==200)||(r.status==304))l41(r.responseText);else if(l51)l51(r.status,r.responseText);window.setTimeout(function(){r.onreadystatechange=function(){};r.abort();},1);}
}
if((lg.length<1000)||(ase_5&&!r.setRequestHeader)){r.open('GET',lg,true);r.send(null);}
else {r.open('POST',ase_n(lg,"?"),true);r.setRequestHeader("Content-Type","application/x-www-form-urlencoded");r.send(ase_o(lg,"?"));}
return r;}
return ase_s(lg,l41,l51);}
function _jcv(v){this.lr=v.id;v.lc2=v.useMap;this.lp1=v.style.cursor;this.lr1(v);this.lo={};var la1=v.id+"_JsChartViewerState";this.lu1=ase_a(la1);if(!this.lu1){var p=v.parentNode||v.parentElement;if(p&&p.insertBefore){var s=this.lu1=document.createElement("HIDDEN");s.id=s.name=la1;s.value=this.la1();p.insertBefore(s,v);}
else if(v.insertAdjacentHTML){v.insertAdjacentHTML("AfterEnd","<HIDDEN id='"+la1+"' name='"+la1+"'>");this.lu1=ase_a(la1);if(this.lu1)this.lu1.value=this.la1();else this.lu1={"name":la1,"id":la1,"value":this.la1()};}
}
else this.decodeState(this.lu1.value);this.ls1();if(!ase_6)this.l11(this.lw1());if(this.ln)this.partialUpdate();}
_jcvp=_jcv.prototype;_jcv.l22=function(ld1){var le1=window.cdjcv_path;if(typeof le1=="undefined")le1=ase_l("cdjcv.js");else if((le1.length>0)&&("/=".indexOf(le1.charAt(le1.length-1))==-1))le1+='/';return le1+ld1;}
_jcv.Horizontal=0;_jcv.Vertical=1;_jcv.HorizontalVertical=2;_jcv.Default=0;_jcv.Scroll=2;_jcv.ZoomIn=3;_jcv.ZoomOut=4;_jcv.msgContainer='<div style="font-family:Verdana;font-size:8pt;font-weight:bold;padding:3 8 3 8;border:1pt solid #000000;background-color:#FFCCCC;color:#000000">%msg</div>';_jcv.okButton='<center>[<a href="javascript:%closeScript"> OK </a>]</center>';_jcv.xButton='[<a href="javascript:%closeScript"> X </a>]';_jcv.shortErrorMsg='Error %errCode accessing server'+_jcv.okButton;_jcv.serverErrorMsg=_jcv.xButton+'<div style="font-family:Arial; font-weight:bold; font-size:15pt;">Error %errCode accessing server</div><hr>%errMsg';_jcv.updatingMsg='<div style="padding:0 8 0 6;background-color:#FFFFCC;color:#000000;border:1px solid #000000"><table><tr><td><img src="'+_jcv.l22('wait.gif')+'"></td><td style="font-size:8pt;font-weight:bold;font-family:Verdana">Updating</td></tr></table></div>';_jcv.lj1=new Array("l0","l1","l2","l3","l4","l5","l6","l7","l8","l9","la","lb","lc","ld","le","lf","lg","lh","li","lj","lk","ll","lm","ln","lo","lp","lq");_jcv.get=function(id){var imgObj=ase_a(id);if(!imgObj)return null;if(!imgObj._jcv)imgObj._jcv=new _jcv(imgObj);return imgObj._jcv;}
_jcvp.getId=function(){return this.lr;}
_jcvp.lt1=function(){return ase_a(this.lr);}
_jcvp.lr1=function(){this.lt1().ly=function(e,id){var lg1;if(!this._jcv.lm1)lg1=this._jcv["onImg"+id](e);if(this["_jcvOn"+id+"Chain"])lg1=this["_jcvOn"+id+"Chain"](e);return lg1;};this.lt1()._jcvOnMouseMoveChain=this.lt1().onmousemove;this.lt1()._jcvOnMouseUpChain=this.lt1().onmouseup;this.lt1()._jcvOnMouseDownChain=this.lt1().onmousedown;var lh1=this.lr;this.lt1().onmousemove=function(e){return ase_a(lh1).ly(e,"MouseMove");}
this.lt1().onmousedown=function(e){return ase_a(lh1).ly(e,"MouseDown");}
this.lt1().onmouseup=function(e){return ase_a(lh1).ly(e,"MouseUp");}
}
_jcvp.lq2=function(x){return x-ase_h(this.lt1());}
_jcvp.lr2=function(y){return y-ase_i(this.lt1());}
_jcvp.lp2=function(w){return w;}
_jcvp.lo2=function(h){return h;}
_jcvp.lm2=function(x){return x+ase_h(this.lt1());}
_jcvp.ln2=function(y){return y+ase_i(this.lt1());}
_jcvp.ll2=function(w){return w;}
_jcvp.lk2=function(h){return h;}
_jcvp.setCustomAttr=function(k,v){this.lo[k]=v;this.le2();}
_jcvp.getCustomAttr=function(k){return this.lo[k];}
_jcvp.l4=0;_jcvp.l5=0;_jcvp.l6=1;_jcvp.l7=1;_jcvp.setViewPortLeft=function(x){this.l4=x;this.le2();}
_jcvp.getViewPortLeft=function(){return this.l4;}
_jcvp.setViewPortTop=function(y){this.l5=y;this.le2();}
_jcvp.getViewPortTop=function(){return this.l5;}
_jcvp.setViewPortWidth=function(w){this.l6=w;this.le2();}
_jcvp.getViewPortWidth=function(){return this.l6;}
_jcvp.setViewPortHeight=function(h){this.l7=h;this.le2();}
_jcvp.getViewPortHeight=function(){return this.l7;}
_jcvp.l0=-1;_jcvp.l1=-1;_jcvp.l2=-1;_jcvp.l3=-1;_jcvp.l01=function(x,y){x=this.lq2(x);y=this.lr2(y);return(this.l0<=x)&&(x<=this.l0+this.l2)&&(this.l1<=y)&&(y<=this.l1+this.l3);}
_jcvp.msgBox=function(ln1,lo1){var m=this.l21;if(!m&&ln1){var d=document;if(d.body.insertAdjacentHTML){var lr1='msg_'+this.lr;d.body.insertAdjacentHTML("BeforeEnd","<DIV ID='"+lr1+"' style='position:absolute;visibility:hidden;'></DIV>");m=ase_a(lr1);}
else if(d.createElement){m=d.createElement("DIV");m.style.position='absolute';m.style.visibility='hidden';d.body.appendChild(m);}
if(m)this.l21=m;}
if(m){window.clearTimeout(m.l31);var s=m.style;if(ln1){if(lo1)m.l31=window.setTimeout(function(){s.visibility='hidden';},Math.abs(lo1));if(lo1<0)ln1+=_jcv.okButton;if(ln1.substring(0,4).toLowerCase()!="<div")ln1=ase_k(_jcv.msgContainer,'%msg',ln1);var ls1="_jcv.get('"+this.lr+"').msgBox();";m.innerHTML=ase_k(ln1,'%closeScript',ls1);s.visibility='visible';s.left=this.lm2(Math.max(0,this.l0+(this.l2-m.offsetWidth)/2))+"px";s.top=this.ln2(Math.max(0,this.l1+(this.l3-m.offsetHeight)/2))+"px";}
else {s.visibility='hidden';}
}
}
_jcvp.l8=2;_jcvp.l9="#000000";_jcvp.setSelectionBorderWidth=function(w){this.l8=w;this.le2();}
_jcvp.getSelectionBorderWidth=function(){return this.l8;}
_jcvp.setSelectionBorderColor=function(c){this.l9=c;this.le2();}
_jcvp.getSelectionBorderColor=function(){return this.l9;}
_jcvp.lq1=function(){_jcv.l92=this.l62("_jcv_leftLine");_jcv.la2=this.l62("_jcv_rightLine");_jcv.l72=this.l62("_jcv_topLine");_jcv.l82=this.l62("_jcv_bottomLine");}
function _jcvp_false_function(){return false;}
_jcvp.l62=function(id){var d=document;if(d.body.insertAdjacentHTML){d.body.insertAdjacentHTML("BeforeEnd","<DIV ID='"+id+"' style='position:absolute;visibility:hidden;background-color:#000000;width:1px;height:1px;'><IMG WIDTH='1' HEIGHT='1'></DIV>");var lg1=ase_a(id);if(ase_6&&(ase_8()<5.5))lg1.onmousemove=_jcvp_false_function;return lg1;}
else if(d.createElement){var lg1=d.createElement("DIV");var s=lg1.style;s.position="absolute";s.visibility="hidden";s.backgroundColor="#000000";s.width="1px";s.height="1px";d.body.appendChild(lg1);return lg1;}
}
_jcvp.lk1=function(x,y,lu1,lv1){if(!_jcv.l92)this.lq1();if(!_jcv.l92)return;var lw1=_jcv.l92.style;var lx1=_jcv.la2.style;var ly1=_jcv.l72.style;var lz1=_jcv.l82.style;lw1.left=ly1.left=lz1.left=x+"px";lw1.top=lx1.top=ly1.top=y+"px";ly1.width=lz1.width=lu1+"px";lz1.top=(y+lv1-this.l8+1)+"px";lw1.height=lx1.height=lv1+"px";lx1.left=(x+lu1-this.l8+1)+"px";lw1.width=lx1.width=ly1.height=lz1.height=this.l8+"px";lw1.backgroundColor=lx1.backgroundColor=ly1.backgroundColor=lz1.backgroundColor=this.l9;}
_jcvp.ll1=function(b){if(b&&!_jcv.l72)this.lq1();if(ase_6&&_jcv.l72&&(ase_8()<5.5)){_jcv.l92.onmouseup=_jcv.la2.onmouseup=_jcv.l72.onmouseup=_jcv.l82.onmouseup=this.lt1().onmouseup;}
if(_jcv.l72)_jcv.l92.style.visibility=_jcv.la2.style.visibility=_jcv.l72.style.visibility=_jcv.l82.style.visibility=b?"visible":"hidden";}
_jcvp.la=_jcv.Default;_jcvp.lb=_jcv.Horizontal;_jcvp.lc=_jcv.Horizontal;_jcvp.ld=2;_jcvp.le=0.5;_jcvp.lf=0.01;_jcvp.lg=1;_jcvp.lh=0.01;_jcvp.li=1;_jcvp.getMouseUsage=function(){return this.la;}
_jcvp.setMouseUsage=function(l12){this.la=l12;if(ase_2&&(ase_9()<2))this.lf2();this.le2();}
_jcvp.lf2=function(){var a=this.lb2;if(a){switch(this.la){case _jcv.ZoomIn:a.href="javascript://ZoomIn";break;case _jcv.ZoomOut:a.href="javascript://ZoomOut";break;default:a.removeAttribute("href");}
}
}
_jcvp.getScrollDirection=function(){return this.lb;}
_jcvp.setScrollDirection=function(l32){this.lb=l32;this.le2();}
_jcvp.getZoomDirection=function(){return this.lc;}
_jcvp.setZoomDirection=function(l32){this.lc=l32;this.le2();}
_jcvp.getZoomInRatio=function(){return this.ld;}
_jcvp.setZoomInRatio=function(l42){if(l42>0)this.ld=l42;this.le2();}
_jcvp.getZoomOutRatio=function(){return this.le;}
_jcvp.setZoomOutRatio=function(l42){if(l42>0)this.le=l42;this.le2();}
_jcvp.getZoomInWidthLimit=function(){return this.lf;}
_jcvp.setZoomInWidthLimit=function(l42){this.lf=l42;this.le2();}
_jcvp.getZoomOutWidthLimit=function(){return this.lg;}
_jcvp.setZoomOutWidthLimit=function(l42){this.lg=l42;this.le2();}
_jcvp.getZoomInHeightLimit=function(){return this.lh;}
_jcvp.setZoomInHeightLimit=function(l42){this.lh=l42;this.le2();}
_jcvp.getZoomOutHeightLimit=function(){return this.li;}
_jcvp.setZoomOutHeightLimit=function(l42){this.li=l42;this.le2();}
_jcvp.lb1=function(){return((this.lc!=_jcv.Vertical)&&(this.l6>this.lf))||((this.lc!=_jcv.Horizontal)&&(this.l7>this.lh));}
_jcvp.lc1=function(){return((this.lc!=_jcv.Vertical)&&(this.l6<this.lg))||((this.lc!=_jcv.Horizontal)&&(this.l7<this.li));}
_jcvp.ls2=-1;_jcvp.lt2=-1;_jcvp.lj=5;_jcvp.getMinimumDrag=function(){return this.lj;}
_jcvp.setMinimumDrag=function(l52){this.lj=l52;this.le2();}
_jcvp.l41=function(e,d){var l62=Math.abs(ase_c(e)-this.ls2);var l72=Math.abs(ase_d(e)-this.lt2);switch(d){case _jcv.Horizontal:return l62>=this.lj;case _jcv.Vertical:return l72>=this.lj;default:return(l62>=this.lj)||(l72>=this.lj);}
}
_jcvp.onImgMouseDown=function(e){if(this.l01(ase_c(e),ase_d(e))&&(ase_e(e)==1)){if(e&&e.preventDefault&&(this.la!=_jcv.Default))e.preventDefault();this.ld2(true);this.ls(e);}
}
_jcvp.onImgMouseMove=function(e){if(this.l12&&window.event&&(ase_e(e)!=1)){this.ld2(false);this.l02=false;this.ll1(false);}
this.lz1=this.l12||this.l01(ase_c(e),ase_d(e));if(this.lz1){this.lu(e);if(this.l12){if((this.la!=_jcv.Default)&&this.lt1().useMap)this.lt1().useMap=null;this.lt(e);}
}
this.l11(this.lz(e));return this.la==_jcv.Default;}
_jcvp.onImgMouseUp=function(e){if(this.l12&&(ase_e(e)==1)){this.ld2(false);this.lv(e);}
}
_jcvp.ld2=function(b){var imgObj=this.lt1();if(b){if(((this.la==_jcv.ZoomIn)||(this.la==_jcv.ZoomOut))&&imgObj.useMap)imgObj.useMap=null;}
else {if(imgObj.useMap!=imgObj.lc2)imgObj.useMap=imgObj.lc2;}
if(!ase_6){if(b){if(!window._jcvOnMouseUpChain)window._jcvOnMouseUpChain=window.onmouseup;if(!window._jcvOnMouseMoveChain)window._jcvOnMouseMoveChain=window.onmousemove;window.onmouseup=imgObj.onmouseup;window.onmousemove=imgObj.onmousemove;}
else {window.onmouseup=window._jcvOnMouseUpChain;window.onmousemove=window._jcvOnMouseMoveChain;window._jcvOnMouseUpChain=null;window._jcvOnMouseMoveChain=null;}
}
this.l12=b;}
_jcvp.setZoomInCursor=function(l82){this.lk=l82;this.le2();}
_jcvp.getZoomInCursor=function(){return this.lk;}
_jcvp.setZoomOutCursor=function(l82){this.ll=l82;this.le2();}
_jcvp.getZoomOutCursor=function(){return this.ll;}
_jcvp.setNoZoomCursor=function(l82){this.lq=l82;this.le2();}
_jcvp.getNoZoomCursor=function(){return this.lq;}
_jcvp.setScrollCursor=function(l82){this.lm=l82;this.le2();}
_jcvp.getScrollCursor=function(){return this.lm;}
_jcvp.lw1=function(){if(ase_6&&(ase_8()<6.0))return "";switch(this.la){case _jcv.ZoomIn:if(this.lb1()){if(this.lk)return this.lk;else return ase_2?"-moz-zoom-in":"url('"+_jcv.l22('zoomin.cur')+"')";}
else {if(this.lq)return this.lq;else return ase_2?"default":"url('"+_jcv.l22('nozoom.cur')+"')";}
case _jcv.ZoomOut:if(this.lc1()){if(this.ll)return this.ll;else return ase_2?"-moz-zoom-out":"url('"+_jcv.l22('zoomout.cur')+"')";}
else {if(this.lq)return this.lq;else return ase_2?"default":"url('"+_jcv.l22('nozoom.cur')+"')";}
default:return "";}
}
_jcvp.lz=function(e){if(this.lm1)return "wait";if(this.l02){if(this.lm)return this.lm;switch(this.lb){case _jcv.Horizontal:return(ase_c(e)>=this.ls2)?"e-resize":"w-resize";case _jcv.Vertical:return(ase_d(e)>=this.lt2)?"s-resize":"n-resize";default:return "move";}
}
if(this.lz1)return this.lw1();else return "";}
_jcvp.l11=function(l92){if(l92!=this.lp1){this.lp1=l92;this.lt1().style.cursor=new String(l92);}
}
_jcvp.ls=function(e){this.ls2=ase_c(e);this.lt2=ase_d(e);}
_jcvp.lu=function(e){}
_jcvp.lt=function(e){var eX=ase_c(e);var eY=ase_d(e);if(this.la==_jcv.ZoomIn){var d=this.lc;var lc2=this.lb1()&&this.l41(e,d);if(lc2){var ld2=Math.min(eX,this.ls2);var le2=Math.min(eY,this.lt2);var l62=Math.abs(eX-this.ls2);var l72=Math.abs(eY-this.lt2);switch(d){case _jcv.Horizontal:this.lk1(ld2,this.ln2(this.l1),l62,this.lk2(this.l3));break;case _jcv.Vertical:this.lk1(this.lm2(this.l0),le2,this.ll2(this.l2),l72);break;default:this.lk1(ld2,le2,l62,l72);break;}
}
this.ll1(lc2);}
else if(this.la==_jcv.Scroll){var d=this.lb;if(this.l02||this.l41(e,d)){this.l02=true;var lf2=(d==_jcv.Vertical)?0:(eX-this.ls2);var lg2=(d==_jcv.Horizontal)?0:(eY-this.lt2);if((lf2<0)&&(this.l4+this.l6-this.l6*this.lp2(lf2)/this.l2>1))lf2=Math.min(0,(this.l4+this.l6-1)*this.l2/this.l6);if((lf2>0)&&(this.l6*this.lp2(lf2)/this.l2>this.l4))lf2=Math.max(0,this.l4*this.l2/this.l6);if((lg2<0)&&(this.l5+this.l7-this.l7*this.lo2(lg2)/this.l3>1))lg2=Math.min(0,(this.l5+this.l7-1)*this.l3/this.l7);if((lg2>0)&&(this.l7*this.lp2(lg2)/this.l3>this.l5))lg2=Math.max(0,this.l5*this.l3/this.l7);this.lk1(this.lm2(this.l0)+lf2,this.ln2(this.l1)+lg2,this.ll2(this.l2),this.lk2(this.l3));this.ll1(true);}
}
}
_jcvp.lv=function(e){this.ll1(false);switch(this.la){case _jcv.ZoomIn:if(this.lb1()){if(this.l41(e,this.lc))this.le1(e);else this.lg1(e,this.ld);}
break;case _jcv.ZoomOut:if(this.lc1())this.lg1(e,this.le);break;default:if(this.l02)this.lf1(e);break;}
this.l02=false;}
_jcvp.lg1=function(e,lh2){var eX=ase_c(e);var eY=ase_d(e);var li2=this.l6/lh2;var lj2=this.l7/lh2;this.l71(this.lc,(this.lq2(eX)-this.l0)*this.l6/this.l2-li2/2,li2,(this.lr2(eY)-this.l1)*this.l7/this.l3-lj2/2,lj2);}
_jcvp.lf1=function(e){var eX=ase_c(e);var eY=ase_d(e);this.l71(this.lb,this.l6*this.lp2(this.ls2-eX)/this.l2,this.l6,this.l7*this.lo2(this.lt2-eY)/this.l3,this.l7);}
_jcvp.le1=function(e){var eX=ase_c(e);var eY=ase_d(e);var li2=this.l6*this.lp2(Math.abs(this.ls2-eX))/this.l2;var lj2=this.l7*this.lo2(Math.abs(this.lt2-eY))/this.l3;this.l71(this.lc,this.l6*(this.lq2(Math.min(this.ls2,eX))-this.l0)/this.l2,li2,this.l7*(this.lr2(Math.min(this.lt2,eY))-this.l1)/this.l3,lj2);}
_jcvp.l71=function(d,lk2,ll2,lm2,ln2){var lo2=this.l4;var lp2=this.l5;var li2=this.l6;var lj2=this.l7;if((((ll2<this.l6)&&(this.l6<this.lf))||(d==_jcv.Vertical))&&(((ln2<this.l7)&&(this.l7<this.lh))||(d==_jcv.Horizontal)))return;if(d!=_jcv.Vertical){if(ll2!=this.l6){li2=Math.max(this.lf,Math.min(ll2,this.lg));lk2-=(li2-ll2)/2;}
lo2=Math.max(0,Math.min(this.l4+lk2,1-li2));}
if(d!=_jcv.Horizontal){if(ln2!=this.l7){lj2=Math.max(this.lh,Math.min(ln2,this.li));lm2-=(lj2-ln2)/2;}
lp2=Math.max(0,Math.min(this.l5+lm2,1-lj2));}
if((lo2!=this.l4)||(lp2!=this.l5)||(li2!=this.l6)||(lj2!=this.l7)){this.lh2=this.l4;this.li2=this.l5;this.lj2=this.l6;this.lg2=this.l7;this.l4=lo2;this.l5=lp2;this.l6=li2;this.l7=lj2;this.lp=1;this.le2();this.applyHandlers("viewportchanged");if(this.onViewPortChanged&&(this.lo1("viewportchanged").length==0))this.onViewPortChanged();this.lp=0;}
}
_jcvp.lo1=function(lq2){var id=(lq2+"events").toLowerCase();if(!this[id])this[id]=[];return this[id];}
_jcvp.attachHandler=function(lq2,f){var a=this.lo1(lq2);a[a.length]=f;return lq2+":"+(a.length-1);}
_jcvp.detachHandler=function(lr2){var ab=lr2.split(':');var a=this.lo1(ab[0]);a[parseInt(ab[1])]=null;}
_jcvp.applyHandlers=function(lq2){var lg1=false;var a=this.lo1(lq2);for(var i=0;i<a.length;++i){this.lu2=a[i];if(this.lu2!=null)lg1|=this.lu2();}
this.lu2=null;return lg1;}
_jcvp.partialUpdate=function(){if(this.lm1)return;_jcv.ld1(this.lt1());this.applyHandlers("preupdate");this.ln=1;this.le2();var lt2=this.updatingMsg;if(!lt2)lt2=_jcv.updatingMsg;if(lt2&&(lt2!="none"))this.msgBox(lt2);var lg=ase_j(ase_a(this.lr+"_callBackURL").value,"cdPartialUpdate="+this.lr+"&cdCacheDefeat="+(new Date().getTime())+"&"+this.lu1.name+"="+ase_k(escape(this.lu1.value),'\\+','%2B'));var lu2=this;this.lm1=true;ase_u(lg,function(t){lu2.l42(t)},function(lw2,lx2){lu2.lx(lw2,lx2);});}
_jcvp.l42=function(lr){var ly2=ase_m(lr,"<!--CD_SCRIPT "," CD_SCRIPT-->");if(ly2){var lz2=ase_m(lr,"<!--CD_MAP "," CD_MAP-->");var imgObj=this.lt1();var imgBuffer=this.l61=(this.doubleBuffering)?new Image():imgObj;if(imgObj.useMap)imgObj.useMap=null;imgObj.loadImageMap=function(){window.setTimeout(function(){_jcv.putMap(imgObj,lz2);},100);};imgBuffer.onload=function(){imgObj._jcv.onPartialLoad(true);}
imgBuffer.onerror=imgBuffer.onabort=function(ln1){imgObj._jcv.lx(999,"Error loading image '"+this.src+"'["+ln1+"]");}
var l13=window.onerror;window.onerror=function(ln1){imgObj._jcv.lx(801,"Error interpretating partial update result ["+ln1+"] <div style='margin:20px;background:#dddddd'><xmp>"+ly2+"</xmp></div>")};eval(ly2);window.onerror=l13;if(ase_2)this.le2();}
else this.lx(800,"Partial update returns invalid data <div style='margin:20px;background:#dddddd'><xmp>"+lr+"</xmp></div>");}
_jcvp.lw=function(l23){var imgObj=this.lt1();var imgBuffer=this.l61;if(imgBuffer)imgBuffer.onerror=imgBuffer.onabort=imgBuffer.onload='';imgObj.onUpdateCompleted='';this.lm1=false;if(l23){this.lh2=this.l4;this.lg2=this.l7;this.li2=this.l5;this.lj2=this.l6;if(imgObj!=imgBuffer){imgObj.src=imgBuffer.src;imgObj.style.width=imgBuffer.style.width;imgObj.style.height=imgBuffer.style.height;}
imgObj.loadImageMap();}
else {imgObj.useMap=imgObj.lc2;if(this.lj2||this.lg2){this.l4=this.lh2;this.l7=this.lg2;this.l5=this.li2;this.l6=this.lj2;this.le2();}
}
imgObj.loadImageMap='';}
_jcvp.onPartialLoad=function(l23){if(this.lt1().onUpdateCompleted)this.lt1().onUpdateCompleted();else this.msgBox();this.lw(l23);this.applyHandlers("postupdate");}
_jcvp.lx=function(lw2,lx2){this.lw(false);this.msgBox();this.errCode=lw2;this.errMsg=lx2;if(!this.applyHandlers("updateerror")){var l33=this.serverErrorMsg;if(!l33)l33=_jcv.serverErrorMsg;if(l33&&(l33!="none"))this.msgBox(ase_k(ase_k(l33,'%errCode',lw2),'%errMsg',lx2));}
this.errCode=null;this.errMsg=null;}
_jcvp.streamUpdate=function(l43){var l53=new Date().getTime();if(!l43)l43=60;var l63=this.l52;if(l63){if(l43*1000>=l53-l63.l51)return false;l63.src=null;l63.onerror=l63.onabort=l63.onload=null;}
if(!this.l32)this.l32=this.lt1().src;this.l52=l63=new Image();l63.l51=l53;var lu2=this;l63.onload=function(){var imgObj=lu2.lt1();if(imgObj.useMap)imgObj.useMap=null;var b=lu2.l52;if(imgObj!=b)imgObj.src=b.src;b.onabort();}
l63.onerror=l63.onabort=function(){var b=lu2.l52;if(b)b.onload=b.onabort=b.onerror=null;lu2.l52=null;}
l63.src=ase_j(this.l32,"cdDirectStream="+this.lr+"&cdCacheDefeat="+l53);return true;}
_jcvp.l91=function(a,v){return a+((typeof v!="number")?"**":"*")+v;}
_jcvp.l81=function(av){var lq=av.indexOf("*");if(lq==-1)return null;var a=av.substring(0,lq);var v=av.substring(lq+1,av.length);if(v.charAt(0)=="*")v=v.substring(1,v.length);else v=parseFloat(v);return{"attr":a,"value":v};}
_jcvp.la1=function(){var lg1="";for(var i=0;i<_jcv.lj1.length;++i){var a=_jcv.lj1[i];var v=null;if((a=="lo")&&this.lo){for(var lf in this.lo)v=((v==null)?"":v+"\x1f")+this.l91(lf,this.lo[lf]);}
else v=this[a];if((typeof v!="undefined")&&(null!=v))lg1+=(lg1?"\x1e":"")+this.l91(i,v);}
return lg1;}
_jcvp.decodeState=function(s){var l71=s.split("\x1e");for(var i=0;i<l71.length;++i){var av=this.l81(l71[i]);if(!av)continue;var a=_jcv.lj1[parseInt(av.attr)];if(a=="lo"){var l83=av.value.split("\x1f");for(var i2=0;i2<l83.length;++i2){var la3=this.l81(l83[i2]);if(!la3)continue;this.lo[la3.attr]=la3.value;}
}
else this[a]=av.value;}
this.lp=0;}
_jcvp.le2=function(){if(this.lu1)this.lu1.value=this.la1();}
_jcvp.ls1=function(){if(!ase_6){var imgObj=this.lt1();var m=_jcv.ln1(imgObj);if(m){m.onmousedown=imgObj.onmousedown;m.onmousemove=imgObj.onmousemove;if(ase_2&&(ase_9()<2)&&document.createElement){var a=this.lb2=document.createElement("AREA");a.coords=""+this.l0+","+this.l1+","+(this.l0+this.l2)+","+(this.l1+this.l3);a.shape="rect";a.onclick="return false;";m.appendChild(a);m.ly1=a;this.lf2();}
}
}
}
_jcv.ln1=function(imgObj){var lb3=imgObj.lc2;if(!lb3)lb3=imgObj.useMap;if(!lb3)return null;var lq=lb3.indexOf('#');if(lq>=0)lb3=lb3.substring(lq+1);return ase_a(lb3);}
_jcv.loadMap=function(imgObj,lg){if(!imgObj.lc2)imgObj.lc2=imgObj.useMap;_jcv.ld1(imgObj);imgObj.lv1=ase_u(lg,function(t){_jcv.putMap(imgObj,ase_m(t,"<!--CD_MAP "," CD_MAP-->"));},function(lw2,lx2){_jcv.onLoadMapError(lw2,lx2);}
);}
_jcv.loadPendingMap=function(){if(!window._jcvPendingMap)return;for(var a in window._jcvPendingMap){var le=ase_a(a);if(le){var lg=window._jcvPendingMap[a];window._jcvPendingMap[a]=null;if(lg)_jcv.loadMap(le,lg);}
}
}
_jcv.ld1=function(imgObj){if(imgObj.lv1){imgObj.lv1.abort();imgObj.lv1=null;}
}
_jcv.onLoadMapError=function(lw2,lx2){}
_jcv.putMap=function(imgObj,lc3){var m=_jcv.ln1(imgObj);if(!m&&lc3){var lb3='map_'+imgObj.id;imgObj.useMap=imgObj.lc2='#'+lb3;var d=document;if(d.body.insertAdjacentHTML){d.body.insertAdjacentHTML("BeforeEnd","<MAP ID='"+lb3+"'></MAP>");m=ase_a(lb3);}
else if(d.createElement){m=d.createElement("MAP");m.id=m.name=lb3;d.body.appendChild(m);}
if(imgObj._jcv)imgObj._jcv.ls1();}
if(m){m.innerHTML=lc3;if(m.ly1)m.appendChild(m.ly1);if(imgObj.useMap!=imgObj.lc2)imgObj.useMap=imgObj.lc2;}
imgObj.lv1=null;}
_jcv.canSupportPartialUpdate=function(){return((ase_6&&(ase_8()>=5.5))||window.XMLHttpRequest||ase_t());}
_jcv.getVersion=function(){return ase_0;}
JsChartViewer=_jcv;_jcv.loadPendingMap();