function createBaseLayers() {
    
    // First, load attribution info for each layer:
    var streetLayerAttribution = loadJson('https://static.arcgis.com/attribution/World_Street_Map');
    var imageryLayerAttribution = loadJson('https://static.arcgis.com/attribution/World_Imagery');
    var terrainLayerAttribution = loadJson('https://static.arcgis.com/attribution/World_Topo_Map');
    
      var streetLayer = new ol.layer.Tile({
        source: new ol.source.XYZ({
              attributions: getStreetLayerAttributionText,
              url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +
                  'World_Street_Map/MapServer/tile/{z}/{y}/{x}',
            }),
        type: 'base',
        title: 'Map',
        visible: true
      });
      var imageryLayer = new ol.layer.Tile({
        source: new ol.source.XYZ({
              attributions: getImageryLayerAttributionText,
              url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +
                  'World_Imagery/MapServer/tile/{z}/{y}/{x}',
            }),
            type: 'base',
            title: 'Imagery',
            visible: false
      });
      
    var imageryLabelLayer = new ol.layer.Group({
        type: 'base',
        title: 'Imagery with Labels',
        visible: false,
        combine: true,
        layers: [
          new ol.layer.Tile({
      source: new ol.source.XYZ({
            attributions: '',
            url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +
                'World_Imagery/MapServer/tile/{z}/{y}/{x}',
          }),
    }),              
            new ol.layer.Tile({
      source: new ol.source.XYZ({
              attributions: getImageryLayerAttributionText,
            url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +
                'Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}',
          })
            })
      ]
    });
      
      var terrainLayer = new ol.layer.Tile({
        source: new ol.source.XYZ({
              attributions: getTerrainLayerAttributionText,
              url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +
                  'World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
            }),
        type: 'base',
        title: 'Terrain',
        visible: false
      });
      
      var baseLayerGroup = new ol.layer.Group({
              'title': 'Base Layer',
              'layers': [terrainLayer, imageryLabelLayer, imageryLayer, streetLayer]
          });
    return baseLayerGroup;
    
    
    function getStreetLayerAttributionText(frameState) {
        return getAttributionText(frameState,streetLayerAttribution);
    }
    
    function getImageryLayerAttributionText(frameState) {
        return getAttributionText(frameState,imageryLayerAttribution);
    }
    
    function getTerrainLayerAttributionText(frameState) {
        return getAttributionText(frameState,terrainLayerAttribution);
    }
    
}

function loadJson(url) {
    return (function () {
            var json = null;
            $.ajax({
                'async': false,
                'global': false,
                'url': url,
                'dataType': "json",
                'success': function (data) {
                    json = data;
                }
            });
            return json;
        })();
}

function getAttributionText(frameState,attributionInfo) {
    var zoom = frameState.viewState.zoom;
    var extent = frameState.extent;
    var attributions = [];
    if (attributionInfo === undefined) {
        return "Cannot fetch attributions";
    } else {
        for (var iAttribution = 0, nAttribution = attributionInfo.contributors.length; iAttribution < nAttribution; ++iAttribution) {
            var imageryProvider = attributionInfo.contributors[iAttribution];
            var intersects = false;
            var coverageAreas = imageryProvider.coverageAreas;
            for (var i = 0, ii = coverageAreas.length; i < ii; ++i) {
              var coverageArea = coverageAreas[i];
              if (zoom >= coverageArea.zoomMin && zoom <= coverageArea.zoomMax) {
                var bbox = coverageArea.bbox;
                var epsg4326Extent = ol.proj.transformExtent([bbox[1], bbox[0], bbox[3], bbox[2]],'EPSG:4326','EPSG:3857');
                if (ol.extent.intersects(epsg4326Extent, extent)) {
                  intersects = true;
                  break;
                }
              }
            }
            if (intersects) {
              attributions.push(imageryProvider.attribution);
            }
        }
        if (attributions.indexOf("Esri")===-1) {
            attributions.unshift("Esri");
        }
        return "Sources: " + attributions.join(", ");
    }
}

