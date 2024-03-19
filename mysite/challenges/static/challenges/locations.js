
if (navigator.geolocation == undefined) {
    throw "geolocation not available in this browser";
}

function submit_form() {
    $('body').append(`
    <div id="loader-container" class="loader-container center">
        <div class="loader-background"></div>
        <div class="loader"></div>
    </div>`
    );
    navigator.geolocation.getCurrentPosition(setLocation, this.showError);
}

function setLocation(user_pos) {
    if (!comparePosition) {
        alert("User location too far from task location!");
        return;
    }
    document.getElementById("usr-lat").value = user_pos.coords.latitude;
    document.getElementById("usr-lng").value = user_pos.coords.longitude;

    document.getElementById("form").submit();

    document.getElementById("loader-container").remove();
}

/**
 * Compares the position of user and the task
 * @param {*} user_pos 
 * @returns {boolean} passes the check or not
 */
function comparePosition(user_pos) {
    const userLat = user_pos.coords.latitude;
    const userLon = user_pos.coords.longitude;

    const taskLat = document.getElementById("task-lat").value;
    const taskLon = document.getElementById("task-lng").value;
    const tolerance = 0.01; // how far off can user location be

    // Check if user location is close enough to task loc
    if (Math.abs(userLat - taskLat) <= tolerance && Math.abs(userLon - taskLon) <= tolerance) {
        return true;
    } else {
        return false;
    }
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
    document.getElementById("loader-container").remove();
}

