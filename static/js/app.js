function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(45.4554270, 9.2071370),
        zoom: 15
    };

    var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

    var drawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.MARKER,
        drawingControl: true,
        drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: [
                google.maps.drawing.OverlayType.MARKER,
                google.maps.drawing.OverlayType.CIRCLE,
                google.maps.drawing.OverlayType.POLYGON,
                google.maps.drawing.OverlayType.POLYLINE,
                google.maps.drawing.OverlayType.RECTANGLE
            ]
        },
        circleOptions: {
            fillColor: '#ffff00',
            fillOpacity: 1,
            strokeWeight: 5,
            clickable: false,
            editable: true,
            zIndex: 1
        }
    });

    drawingManager.setMap(map);
    google.maps.event.addListener(drawingManager, 'polygoncomplete', function (polygon) {
        drawingManager.setDrawingMode(null);
        var arr = [];
        polygon.getPath().forEach(function (latLng) {
            arr.push(latLng.D.toString() + " " + latLng.k.toString());
        });
        arr.push(arr[0]);
        var query = 'geo:"IsWithin(POLYGON((' + arr + '))) distErrPct=0"';
        var marker = new Array();
        var contentString = new Array();
        var infowindow = new google.maps.InfoWindow();
        $.get('/geo/?' + query, function (results) {
            for (var i = 0; i < results.length; i++) {
                var location = results[i].geo[0].split(',');
                var myLatLng = new google.maps.LatLng(location[0], location[1]);
                marker[i] = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    title: results[i].tagline
                });

                contentString[i] = '<div id="content">' +
                '<div id="siteNotice">' +
                '</div>' +
                '<h1 id="firstHeading" class="firstHeading">' + results[i].tagline + '</h1>' +
                '<div id="bodyContent">' +
                '<p>' + results[i].description + '</p>' +
                '<p> Price: ' + results[i].listprice + '<br/>' +
                ' Beds:' + results[i].numbeds + '</p>' +
                ' Baths:' + results[i].numfullbaths + '</p>' +
                ' Parking Space:' + results[i].parkingspaces + '</p>' +
                '<a href="/' + results[i].documentid + '">More Info</a>' +
                '</div>' +
                '</div>';

                google.maps.event.addListener(marker[i], 'click', function () {
                    infowindow.setContent(contentString[i]);
                    infowindow.open(map, this);
                });
            }
        });
        console.log(query);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
