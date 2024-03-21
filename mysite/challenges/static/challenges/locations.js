
if (navigator.geolocation == undefined) {
    throw "geolocation is not available in this browser";
}

function file_attached() {
    return document.getElementById("input_image").files.length > 0
}

function submit_form() {
    $('body').append(`
    <div id="loader-container" class="loader-container center">
        <div class="loader-background"></div>
        <div class="loader"></div>
    </div>`
    );
    if (!file_attached()) {
        alert("You must attach an image as proof of completion!");
        document.getElementById("loader-container").remove();
    } else if (document.getElementById("task-lat").value == "None") {
        submit_and_record();
    } else {
        navigator.geolocation.getCurrentPosition(setLocation, this.showError, {enableHighAccuracy: true, timeout: 30000});
    }
}

function getCookie(cookieName) {
    const name = cookieName + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
    for(let i = 0; i <cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

function today_end(){
        // Get current date
        var date = new Date();

        // Advance date by one day
        date.setDate(date.getDate() + 1);
    
        // Set time to 00:00:00
        date.setHours(0);
        date.setMinutes(0);
        date.setSeconds(0);
        date.setMilliseconds(0);
    
        return date;
}

function submit_and_record() {
    var value = document.getElementById("task-id").value;

    let completed = getCookie("completed_tasks");
    if (completed) {
        completed = JSON.parse(completed);
        completed.push(value);
    } else {
        completed = [value];
    }

    document.cookie = "completed_tasks="+JSON.stringify(completed)+";expires=" + today_end().toUTCString()+";path=/" ;

    document.getElementById("form").submit();
    document.getElementById("loader-container").remove();
}

async function setLocation(user_pos) {
    if (user_pos.coords.accuracy >= 50) {
        await new Promise(r => setTimeout(r, 10000));
        if (user_pos.coords.accuracy >= 50) {
            alert("Unable to submit: location accuracy too low!\nAccuracy of your GeoLocation service: "+user_pos.coords.accuracy);
        }
    }
    if (!comparePosition(user_pos)) {
        alert("User location too far from task location!");
        document.getElementById("loader-container").remove();
    } else {
        document.getElementById("usr-lat").value = user_pos.coords.latitude;
        document.getElementById("usr-lng").value = user_pos.coords.longitude;

        submit_and_record();
    }
}

function deg2rad(deg) {
    return deg * (Math.PI/180);
}

function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Radius of the Earth in kilometers
    const dLat = deg2rad(lat2 - lat1);
    const dLon = deg2rad(lon2 - lon1); 
    const a = 
        Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
        Math.sin(dLon/2) * Math.sin(dLon/2); 
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    const distance = R * c * 1000; // Distance in meters
    return distance;
}

/**
 * Compares the position of user and the task
 * @param {*} user_pos 
 * @returns {boolean} passes the check or not
 */
function comparePosition(user_pos) {
    const taskLat = document.getElementById("task-lat").value;
    const taskLon = document.getElementById("task-lng").value;

    const userLat = user_pos.coords.latitude;
    const userLon = user_pos.coords.longitude;

    const dist = getDistance(userLat, userLon, taskLat, taskLon);

    const tolerance = 150; // how far off can user location be in meters

    // Check if user location is close enough to task loc
    if (dist <= tolerance) {
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

