import {Bullet} from "./bullet.js";



export class Player {
    constructor() {
        this.shootTimer = 500;

        this.player = document.getElementById("player");

        this.bullets = [];
        
        this.isIdle = true;
        this.isAttacking = false

    }



    setPlayerPos() {
        this.player.style.position = "absolute";
        this.player.style.left = "5%";
        this.player.style.bottom = "30%";
    }


    setPlayerModel(modelName, duration) {
        let thisplayer = this 
        setTimeout(function() {
            this.player.src = "/models/player/heroidle.png";
            thisplayer.isAttacking = false
            console.log("No longer attacking")
            console.log(this.isAttacking)
        }, duration);
        this.player.src = "/models/player/"+modelName+".png";
        console.log("shooting...")
    }


    addControl() {
        addEventListener('keypress', (event) => {
            if (KeyboardEvent.key = " ") {
                if (! this.isAttacking) {
                    this.isAttacking = true;
                    this.setPlayerModel("herogun", this.shootTimer)
                    let bullet = new Bullet(["50px", "30%"]);
                    // let img = bullet.draw();
                    this.bullets.push(bullet)
                    console.log(bullet.img.style.bottom.toString()+" pos");
                } else {
                    console.log("Already attacking...")
                    console.log(this.isAttacking)
                }
            }
        
        });
    }



    handleBullets() {
        this.bullets.forEach(bullet => {
            let currentLeft = bullet.getCurrentLeft()
            bullet.img.style.left = (currentLeft+bullet.velocity).toString()+"px";
            bullet.accelerate()
            if (bullet.velocity <= 0) {
                bullet.img.remove()
                this.bullets = this.bullets.filter(function(value, index, arr){ 
                    return value !== bullet;
                });
            }
        });

    }


}



