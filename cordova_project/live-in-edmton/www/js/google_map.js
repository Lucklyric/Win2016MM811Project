/**
 * Created by Alvin on 2016-03-30.
 */
function MapManager(){
    var mapInstance = this;
    this.map =null;
    this.currentMarker=null;
    this.desMarker=null;
    this.desPoly=null;

    this.initialize=function() {
        var mapProp = {
            center:new google.maps.LatLng(51.508742,-0.120850),
            zoom:10,
            mapTypeId:google.maps.MapTypeId.ROADMAP
        };
        mapInstance.map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
        // Try HTML5 geolocation.
        var myCenter;
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                myCenter = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                mapInstance.map.setCenter(myCenter);
                mapInstance.currentMarker=new google.maps.Marker({
                    position:myCenter,
                    map:mapInstance.map,
                    label:"U"
                });

            }, function() {
                //handleLocationError(true, infoWindow, map.getCenter());
            });
        } else {
            // Browser doesn't support Geolocation
            //handleLocationError(false, infoWindow, map.getCenter());
        }
        $("#google-loading").css('background-color','transparent');
        $("#googleMap").show();
    };

    this.moveToNei = function(neiData){
        console.log("start update map");
        console.log(neiData);
        var neiInfo;
        neiInfo = neiData;
        var nName = neiInfo["name"];
        var neiPos = {
            lat:neiInfo["latitude"],
            lng:neiInfo["longitude"]
        };
        mapInstance.map.panTo(neiPos);
        mapInstance.map.setZoom(13);
        if (this.desMarker){
            this.desMarker.setMap(null);
        }
        this.desMarker = new google.maps.Marker({
            position:neiPos,
            map:mapInstance.map,
            animation:google.maps.Animation.BOUNCE
        });

        //draw poly

        var triangleCoords = [];
        for (var i = 0 ; i < neiInfo["area"].length ; i++){
            var pos = {
                lat:parseFloat(neiInfo["area"][i][1]),
                lng:parseFloat(neiInfo["area"][i][0])
            };
            triangleCoords.push(pos);
        }
        // Construct the polygon.
        if (mapInstance.desPoly){
            mapInstance.desPoly.setMap(null);
        }
        mapInstance.desPoly  = new google.maps.Polygon({
            paths: triangleCoords,
            strokeColor: '#0000FF',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#0000FF',
            fillOpacity: 0.35
        });

        mapInstance.desPoly.setMap(mapInstance.map);

    };
    //google.maps.event.addDomListener(window, 'load', this.initialize);
}
//
