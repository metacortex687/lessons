import { Game } from "./game.js";
import { Inputs } from "./inputs.js";
import { TileRenderer } from "./tile_renderer.js";

const FPS = 30;
const SLEEP = 1000 / FPS;

const game = new Game();
const inputs = new Inputs();

function gameLoop(tile_renderer: TileRenderer) {
  let before = Date.now();
  game.update(inputs);
  game.draw(tile_renderer);
  let after = Date.now();
  let frameTime = after - before;
  let sleep = SLEEP - frameTime;
  setTimeout(() => gameLoop(tile_renderer), sleep);
}

window.onload = () => {
  let tile_renderer = new TileRenderer("GameCanvas");
  gameLoop(tile_renderer);
};

window.addEventListener("keydown", (e) => {
  inputs.push(e.key);
});

console.log("tsc bundling ok ");
