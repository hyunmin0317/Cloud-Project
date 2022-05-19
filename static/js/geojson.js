var map = new naver.maps.Map(document.getElementById('map'), {
    scaleControl: false,
    logoControl: false,
    mapDataControl: false,
    zoomControl: true,
    minZoom: 6,
    zoom: 12,
});

naver.maps.Event.once(map, 'init', function () {
    $.ajax({
        url: 'https://raw.githubusercontent.com/ssm-lim/bPolygon/master/bPolygon/highmap/json/11.json',
        dataType: 'json',
        success: startDataLayer
    });
});

function startDataLayer(geojson) {
    map.data.addGeoJson(geojson);

    map.data.setStyle(function(feature) {
        var color = 'red';

        if (feature.getProperty('isColorful')) {
            color = feature.getProperty('color');
        }

        return {
            fillColor: color,
            strokeColor: color,
            strokeWeight: 2,
            icon: null
        };
    });

    map.data.addListener('click', function(e) {
        e.feature.setProperty('isColorful', true);
    });

    map.data.addListener('dblclick', function(e) {
        var bounds = e.feature.getBounds();

        if (bounds) {
            map.panToBounds(bounds);
        }
    });

    map.data.addListener('mouseover', function(e) {
        map.data.overrideStyle(e.feature, {
            strokeWeight: 8,
            icon: 'https://github.com/navermaps/maps.js.ncp/blob/master/docs/img/example/pin_spot.png?raw=true'
        });
    });

    map.data.addListener('mouseout', function(e) {
        map.data.revertStyle();
    });
}