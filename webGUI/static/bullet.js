

export class Bullet {
    constructor(position) {
        this.position = position
        this.damage = 2
        this.velocity = 15
        this.acceleration = -0.14

        this.src = "models/items/bullet.png"
        this.img = this.draw();
    }

    accelerate() {
        this.velocity += this.acceleration
    }


    draw() {
        let img = document.createElement("img");
        img.src = this.src;
        document.getElementById("body").appendChild(img)
        img.style.position = "absolute";
        img.style.width = "10%";
        img.style.height = "auto";
        img.style.left = this.position[0];
        img.style.bottom = this.position[1];
        img.style.imageRendering= "pixelated";
        img.style.imageRendering= "-moz-crisp-edges";
        img.style.imageRendering= "crisp-edges";
        return img
    }


    getCurrentLeft() {
        let leftString = this.img.style.left;
        let left = parseFloat(leftString.replace("px", "").replace("%", ""))
        return left
    }
}