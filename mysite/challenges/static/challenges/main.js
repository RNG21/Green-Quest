document.addEventListener("DOMContentLoaded", function() {
    // get dataset from django template render
    var dataset = document.getElementById("map-script").dataset;

    // init map
    var maps = new Maps();
    var positions = JSON.parse(dataset.positions);
    var center = JSON.parse(dataset.map_center);
    maps.initMap(positions, center);

    // setup collapibles
    var collapsible = new Collapsible();
    let callback = maps.center_marker_by_name.bind(maps)
    collapsible.add_lisenters(callback);

    // Set listeners for popup tutorial
    popup_listeners();

    var completed = getCookie("completed_tasks");
    if (completed) {
        completed = JSON.parse(completed);
        for (var task_id of completed) {
            document.getElementById(task_id).remove();
        }
    }
});

