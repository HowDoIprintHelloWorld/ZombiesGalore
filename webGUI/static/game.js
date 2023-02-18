import {Player} from "./player.js";
import {Ghost} from "./ghost.js";

let player = new Player();
player.setPlayerPos()
player.addControl()


let enemies = []


function handleEnemies() {
    enemies.forEach(ghost => {
        ghost.move()
    });
}


setInterval( function() {
    console.log((screen.width*0.9).toString())
    let ghost = new Ghost([(screen.width*0.9).toString()+"px", "30%"])
    enemies.push(ghost)
    console.log("spawn left", ghost.img.style.left)
}, 3000)



setInterval( function() {
    player.handleBullets();
    handleEnemies();
}, 1/60)