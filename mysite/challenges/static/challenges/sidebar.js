function show_submit(name, location, task_id, lat, lng) {
    document.getElementById("task-name").textContent = name;
    document.getElementById("task-loc").textContent = "At: "+location;
    document.getElementById("task-id").value = task_id;
    document.getElementById("usr-lat").value = lat;
    document.getElementById("usr-lng").value = lng;
    $('#submit-challenge-form').show();
}

function hide_submit(){
    $('#submit-challenge-form').hide();
}

