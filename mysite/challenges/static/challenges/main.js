document.addEventListener("DOMContentLoaded", function() {
    // get dataset from django template render
    var dataset = document.getElementById("map-script").dataset;

    // init map
    var maps = new Maps();
    var positions = JSON.parse(dataset.positions);
    var center = JSON.parse(dataset.map_center);
    maps.initMap(positions, center);
});
