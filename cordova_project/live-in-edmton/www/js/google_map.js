/**
 * Created by Alvin on 2016-03-30.
 */
function initialize() {
    var mapProp = {
        center:new google.maps.LatLng(51.508742,-0.120850),
        zoom:10,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
    // Try HTML5 geolocation.
    var myCenter;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            myCenter = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            map.setCenter(myCenter);
            var marker=new google.maps.Marker({
                position:myCenter,
                map:map,
                animation:google.maps.Animation.BOUNCE
            });
            var infowindow = new google.maps.InfoWindow({
                content:"You"
            });
            infowindow.open(map,marker);
        }, function() {
            //handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        //handleLocationError(false, infoWindow, map.getCenter());
    }

}
google.maps.event.addDomListener(window, 'load', initialize);
