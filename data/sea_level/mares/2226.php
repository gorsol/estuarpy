
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">

<head>


<title>
Data and Station Information for IMHAMBANE II</title>

<link rel="shortcut icon" type="image/x-icon" href="/graphics/favicon.ico" >
<link rel="icon" href="/graphics/favicon.png" type="image/png">
<link rel="stylesheet" href="/style.css" type="text/css" media="screen" >
<link rel="stylesheet" href="/print.css" type="text/css" media="print" >

</head>

<body onload="onLoad()">

<div id="global">

<div id="header">

        <a href="#MainContent" class="hide" title="jump to main content">Jump to main content.</a>

  <a href="/"><img class="top_logo" src="/graphics/psmsl_header.gif" alt="Permanent Service for Mean Sea Level (PSMSL) logo"></a>


</div>
<div id="TopMenuBar">
<ul id="level1Nav">
 

<li><a href="/about_us/" title="About Us" ><span class="TopMenu"> &nbsp;&nbsp;&nbsp;About Us&nbsp;&nbsp;&nbsp;</span></a></li>
<li><a href="/data/" title="Data" ><span class="TopMenu">&nbsp;&nbsp;&nbsp;Data&nbsp;&nbsp;&nbsp;</span></a></li>
<li><a href="/products/ " title="Products"><span class="TopMenu">&nbsp;&nbsp;&nbsp;Products&nbsp;&nbsp;&nbsp;</span></a></li>
<li><a href="/gloss/ " title="GLOSS"><span class="TopMenu">&nbsp;&nbsp;&nbsp;GLOSS&nbsp;&nbsp;&nbsp;</span></a></li>
<li><a href="/train_and_info/ " title="Training and Information" ><span class="TopMenu">&nbsp;&nbsp;&nbsp;Training&nbsp;&nbsp;&nbsp;</span></a></li>
<!--<li><a href="/train_and_info/ " title="Training and Information" ><span class="TopMenu">&nbsp;&nbsp;&nbsp;Training &amp; Information&nbsp;&nbsp;&nbsp;</span></a></li>-->
<li><a href="/links/ " title="Links" ><span class="TopMenu">&nbsp;&nbsp;&nbsp;Links&nbsp;&nbsp;&nbsp;</span></a></li>
 

</ul>
	</div>	
<div id="BreadCrumbs">

You are here: <a href="/">home > </a><a href="/data/">data > </a><a href="/data/obtaining/">obtaining > </a><a href="/data/obtaining/stations/">stations > </a> </div>
<div class="SideBar">
<h2 class="SideBarTitle"> Data </h2>
<ul class="SideBarNav1">
<li><a href="/data/obtaining/" >Obtaining</a></li>
<li><a href="/data/supplying/" >Supplying</a></li>
<li><a href="/data/hf/" >High-Frequency</a></li>
<li><a href="/data/bottom_pressure/" >Bottom Pressure Records</a></li>
<li><a href="/data/longrecords/" >Other Long Records</a></li>
<li><a href="/data/calibrations/"  >GLOSS/ODINAFRICA Calibration Data</a></li>
</ul>

<br /><br />

<h2 class="SideBarTitle">Data Notes</h2>
<ul class="SideBarNav1">
<li><a href="/data/obtaining/notes.php">Individual Station Data and Plot Notes</a></li>
<li><a href="/data/obtaining/reference.php">Referencing the Data Set</a></li>
<li><a href="/data/obtaining/psmsl.hel">PSMSL Help File</a></li>
<li><a href="/about_us/news/2010/data_changes.php">2010 Changes to the PSMSL Data Files</a></li>
</ul>

<br /><br />

<h2 class="SideBarTitle">Extracted from Database</h2>
<div id="update">
25 Mar 2019</div>

<link rel="stylesheet" href="https://openlayers.org/en/v4.6.5/css/ol.css" type="text/css">
<!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://openlayers.org/en/v4.6.5/build/ol.js"></script>
<script src="https://code.jquery.com/jquery-2.1.0.min.js"></script>
<script src="/ol/ol-layerswitcher.js"></script>
<script src="/ol/olcommon.js"></script>
<link rel="stylesheet" href="/ol/ol-layerswitcher.css" type="text/css">
<link rel="stylesheet" href="/ol/olstyle.css" type="text/css">

<script type="text/javascript" charset="utf-8">
    var lat = -23.866667;
var lon = 35.376667;
var station_id = 2226;
var isrlr = "N";
 

    var mainIconStyle = new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [10, 34],
            anchorXUnits: 'pixels',
            anchorYUnits: 'pixels',
            src: '/graphics/icons/markers/arrow.png'
        })
    });
    
    var rlrIconStyle = new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [5, 20],
            anchorXUnits: 'pixels',
            anchorYUnits: 'pixels',
            src: '/graphics/icons/markers/yellow.png'
        })
    });

    var metricIconStyle = new ol.style.Style({
        image: new ol.style.Icon({
            anchor: [5, 20],
            anchorXUnits: 'pixels',
            anchorYUnits: 'pixels',
            src: '/graphics/icons/markers/red.png'
        })
    });

    var baseLayerGroup = createBaseLayers();
    
    var tooltip = document.getElementById('tooltip');

    function onLoad() {

        var map = new ol.Map({
            layers: [baseLayerGroup],
            target: document.getElementById('map'),
            controls: ol.control.defaults({attributionOptions: {collapsible: false, collapsed: false}}),
            view: new ol.View({
                center: ol.proj.transform([lon, lat], 'EPSG:4326', 'EPSG:3857'),
                zoom: 8
            })
        });
        var layerSwitcher = new ol.control.LayerSwitcher();
        map.addControl(layerSwitcher);

        var markerSource = new ol.source.Vector({
            projection : 'EPSG:3857',
            url: 'stationLocations.json',
            format: new ol.format.GeoJSON()
        })
        var markerLayer = new ol.layer.Vector({
            source: markerSource,
            style: iconStyle,
        });
        map.addLayer(markerLayer);

        var tooltip = document.getElementById('tooltip');
        var tooltipOverlay = new ol.Overlay({
            element: tooltip,
            offset: [10, -5],
            positioning: 'bottom-left'
        });
        map.addOverlay(tooltipOverlay);
        map.on('pointermove', createDisplayTooltipCallback(map,tooltip,tooltipOverlay));
        
        map.on('singleclick',createClickCallback(map));
        
        function createClickCallback() {
            return function(evt) {
                var feature = map.forEachFeatureAtPixel(evt.pixel,
                    function(feature) {
                        return feature;
                    });
                if (feature) {
                    var this_id = feature.getId();
                    window.location.assign(this_id + ".php");
                }
            }
        }
        
        function iconStyle(feature) {
            var this_id = feature.getId();
            var this_rlr = feature.get('rlr');
            if (this_id === station_id) {
                return mainIconStyle;
            } else if (this_rlr) {
                return rlrIconStyle;
            } else {
                return metricIconStyle;
            }
        }
        
        function createDisplayTooltipCallback() {
            return function(evt) {
                var pixel = evt.pixel;
                var feature = map.forEachFeatureAtPixel(pixel, function(feature) {
                    return feature;
                });
                if (feature) {
                    tooltip.style.display = '';
                    tooltipOverlay.setPosition(evt.coordinate);
                    tooltip.innerHTML = createTooltip(feature);
                    map.getTarget().style.cursor = 'pointer';
                } else {
                  tooltip.style.display = 'none';
                  map.getTarget().style.cursor = '';
                }
            }
        };
        
        function createTooltip(feature) {
            return feature.getId() + ": " + feature.get("name");
        }

    }
    
</script>

</div>

<div id="MainContent">

<div id="mainTitle">
<h1>IMHAMBANE II</h1>
</div>


<div id="warning">WARNING: METRIC STATION<BR>THIS IS NOT RESEARCH QUALITY DATA.<BR>USE WITH EXTREME CAUTION.</div>
<div class="indiv_stat">
  <h2>Station Information</h2>
<!-- Beginning of mini map -->
  <div id="miniMap">
    <script type="text/javascript" charset="utf-8">
        document.write('<div id="map" style="width: 300px; height: 300px">');
        document.write('<div id="tooltip" class="tooltip"></div>')
        document.write('</div>');
    </script>
    <noscript>
      <b>Javascript must be enabled in order to view the interactive map</b>
    </noscript>
  </div>
<!-- End of mini map -->

<!-- Beginning of data table -->
  <table cellpadding="2" >
    <tr>
      <td>Station ID:</td>
      <td>2226</td>
    </tr>
    <tr>
      <td>Latitude:</td>
      <td>-23.866667</td>
    </tr>
    <tr>
      <td>Longitude:</td>
      <td>35.376667</td>
    </tr>
    <tr>
      <td>GLOSS ID:</td>
      <td><a href='http://www.gloss-sealevel.org/station_handbook/stations/10/' target='_blank'>10</a></td>
    </tr>
    <tr>
      <td>Coastline code:</td>
      <td>432</td>
    </tr>	
    <tr>
      <td>Station code:</td>
      <td>6</td>
    </tr>	
    <tr>
      <td>Country:</td>
      <td>MOZAMBIQUE</td>
<!--      <td><A HREF=# ONCLICK="return false">MOZAMBIQUE</A></td>
//-->
    </tr>	
    <tr>
      <td>Time span of data:</td>
      <td>2013 &ndash; 2013</td>
    </tr>
    <tr>
      <td>Completeness (%):</td>
      <td>67</td>
    </tr>
<!--    <tr>
      <td>Frequency Code:</td>
      <td>Not Specified</td>
    </tr>-->

    
    
    <tr>
      <td>Date of last update:</td>
      <td>23 Jul 2014</td>
    </tr>
  </table>
<!-- End of data table -->
<br>
  <table class="mapkey">
    <tr>
        <td id="currentst">Green Arrow:</td>
        <td>Current Station</td>
    </tr>
    <tr>
        <td id="nearrlr">Yellow Marker:</td>
        <td>Neighbouring RLR Station</td>
    </tr>
    <tr>
        <td id="nearmetric">Red Marker:</td>
        <td>Neighbouring Metric Station</td>
    </tr>
   </table>

<p>Please note: In many cases, the station position in our database is accurate 
to only one minute.  Thus, the tide gauge may not appear to be on the coast.</p> 
</div>

<div class="indiv_stat">
  <h2>Tide Gauge Data</h2>
<center>
<a href="../met.monthly.data/2226.metdata">Download metric sea level data.  Use only with extreme caution.</a>
</center>
</div>

<div class="indiv_stat">
  <h2>Additional Data Sources (<a href="data_source_guide.php">guide to additional data sources</a>)</h2>
Fast Delivery Data from UHSLC station 900: <a href="http://uhslc.soest.hawaii.edu/data/download/fd#uh900" target="_blank">hourly and daily</a><br>
Research Quality Data from UHSLC station 900: <a href="http://uhslc.soest.hawaii.edu/data/download/rq#uh900a" target="_blank">hourly and daily</a><br>
</div>
 
<div class="indiv_stat" id="docu">
  <h2>Station Documentation</h2>
</div>
			
<div class="indiv_stat">
  <h2>Data Authority</h2>
Instituto Nacional de Hidrographia e Navegacao<br>Av. Karl Marx No. 153<br>Maputo<br></div>

</div>

<div id="Footer">
<p>
<a href="http://ioc-unesco.org/" target="_blank"><img src="/graphics/ioc_en_color_small_60.png" alt="Intergovernmental Oceanographic Commission logo"></a> 
<a href="http://www.icsu-wds.org" target="_blank"><img src="/graphics/WDS_logo_RGB_60.png" alt="World Data System logo"></a> 
<a href="http://www.ggos.org/"  target="_blank"><img src="/graphics/ggos_logo_60.png" alt="Global Geodetic Observing System logo"></a>
<a href="http://www.iag-aig.org/"  target="_blank"><img src="/graphics/iag_logo_60.png" alt="International Association of Geodesy logo"></a><br>
<a href="http://noc.ac.uk/" target="_blank"><img src="/graphics/noc_logo_cmyk_50.png" alt=" National Oceanography Centre logo"></a>
<a href="http://www.bodc.ac.uk/" target="_blank"><img src="/graphics/bodc_logo_50.png" alt="British Oceanographic Data Centre logo"></a>
<a href="http://www.nerc.ac.uk/" target="_blank"><img src="/graphics/nerc_long_logo_bw_50.png" alt="Natural Environment Research Council logo"></a>
</p>
</div>

</div>
</body>
</html>
