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


// Function to set a cookie
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

document.addEventListener("DOMContentLoaded", function() {
    // Show if cookie is not set
    if (document.cookie.split(';').some((item) => item.trim().startsWith('tutorial-seen='))) {
        document.getElementById("tutorial-popup").classList.add("hideform");
    } else {
        document.getElementById("tutorial-popup").classList.remove("hideform");
    }

    // Close and set cookie
    document.getElementById("dont-show-again").addEventListener("click", function() {
        document.getElementById("tutorial-popup").classList.add("hideform");
        setCookie("tutorial-seen", "true", 365);
    });

    //Close
    document.getElementById("close-tutorial").addEventListener("click", function() {
        document.getElementById("tutorial-popup").classList.add("hideform");
    });
});
