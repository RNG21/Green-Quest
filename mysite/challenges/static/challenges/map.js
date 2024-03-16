// Initialize and add the map
let map;

async function initMap(positions, center) {
    positions = JSON.parse(positions);
    center = JSON.parse(center)
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
    initMap(document.getElementById("positions").value, document.getElementById("center").value);
});
