


export class Ghost {
    constructor(position) {
        this.src = "/models/enemies/ghostskeleton.png"

        this.velocity = -1.5;

        this.position = position
        this.img = this.draw()
    
    }


    getCurrentLeft() {
        let leftString = this.img.style.left;
        let left = parseFloat(leftString.replace("px", "").replace("%", ""))
        return left
    }


    move() {
        let currentLeft = this.getCurrentLeft();
        this.img.style.left = (currentLeft+this.velocity).toString()+"px";
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
} 