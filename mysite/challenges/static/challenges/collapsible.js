class Collapsible {

    constructor() {
        this.buttons = [];
        var coll = document.getElementsByClassName("collapsible");

        for (var i = 0; i < coll.length; i++) {
            this.buttons.push(coll[i]);
        }
    }

    collapse(button) {
        button.classList.remove("active");
        button.nextElementSibling.style.display="none";
    }

    collapse_all() {
        for (let button of this.buttons) {
            this.collapse(button);
        };
    }

    expand(button) {
        button.classList.add("active");
        button.nextElementSibling.style.display="block";
    }

    focus(button) {
        this.collapse_all();
        this.expand(button);
    }

    add_lisenters(callback) {
        let self = this;
        for (var button of this.buttons) {
            button.addEventListener("click", function() {
                if (callback) {
                    callback(this.id.split('-')[0])
                }
                
                if (this.classList.contains("active")) {
                    self.collapse(this);
                } else {
                    self.focus(this);
                }
            });
        }
    }
}