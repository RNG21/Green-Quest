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

function dont_show(){
    var checkbox = document.getElementById("dont-show-again");
    if (checkbox.checked) {
        setCookie("tutorial-seen", "true", 365);
    }
}

function popup_listeners() {
    // Show if cookie is not set
    if (document.cookie.split(';').some((item) => item.trim().startsWith('tutorial-seen='))) {
        document.getElementById("tutorial-popup").classList.add("hideform");
    } else {
        document.getElementById("tutorial-popup").classList.remove("hideform");
    }

    // Close and set cookie
    document.getElementById("okay").addEventListener("click", function() {
        document.getElementById("tutorial-popup").classList.add("hideform");
        dont_show();
    });

    // Close
    document.getElementById("close-tutorial").addEventListener("click", function() {
        document.getElementById("tutorial-popup").classList.add("hideform");
        dont_show();
    });
}
