// Initialize and add the map
let map;

async function initMap(positions, center) {
    // Request needed libraries.
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    map = new Map(document.getElementById("map"), {
        zoom: 16,
        center: center,
        mapId: "campus"
    });

    for (let position of positions) {
        new AdvancedMarkerElement({
            map: map,
            position: position
        });
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // get dataset from django template render
    var dataset = document.getElementById("map-script").dataset;

    // init map
    var positions = JSON.parse(dataset.positions);
    var center = JSON.parse(dataset.map_center);
    initMap(positions, center);
});
