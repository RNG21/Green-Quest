function show_submit(name, location, task_id, task_lat, task_lng) {
    document.getElementById("task-name").textContent = name;
    document.getElementById("task-loc").textContent = "At: "+location;
    document.getElementById("task-id").value = task_id;
    document.getElementById("task-lat").value = task_lat;
    document.getElementById("task-lng").value = task_lng;
    $('#submit-challenge-form').show();
}

function hide_submit(){
    $('#submit-challenge-form').hide();
}

