class Maps{
    
    constructor () {
        this.markers = {};
        this.map;
    }

    async initMap(positions, center) {
        // Request needed libraries.
        const { Map } = await google.maps.importLibrary("maps");

        this.map = new Map(document.getElementById("map"), {
            zoom: 16,
            center: center,
            mapId: "campus"
        });    

        for (let position of positions) {
            this.add_marker(position);
        }
    }

    async add_marker(position){
        const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
        const marker = new AdvancedMarkerElement({
            map: this.map,
            position: position
        });
        
        this.markers[position.location_name] = marker;
        this.add_infoWindow(this.map, marker, "<h3>"+position.location_name+"</h3>");
    }

    add_infoWindow(map, marker, content) {
        const info_window = new google.maps.InfoWindow({
            content: content
        });

        marker.content.addEventListener('mouseenter', () => {
            info_window.open(map, marker);
        });
        marker.content.addEventListener('mouseleave', () => {
            info_window.close();
        });
    }

    center_marker(marker) {
        this.map.setCenter(marker);
    }

    center_marker_by_name(location_name) {
        if (location_name != "Extras") {
            this.map.setCenter(this.markers[location_name].position);
        }
    }
}
