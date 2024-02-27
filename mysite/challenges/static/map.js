// Initialize and add the map
let map;

async function initMap(positions) {
    positions = JSON.parse(positions);
    // Request needed libraries.
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    map = new Map(document.getElementById("map"), {
        zoom: 4,
        center: positions[0],
        mapId: "campus"
    });

    for (let position of positions) {
        new AdvancedMarkerElement({
            map: map,
            position: position
        });
    }
}

initMap(document.getElementById("positions").value);
