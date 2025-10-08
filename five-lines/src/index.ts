// import { Game } from "./game";

const FPS = 30;
const SLEEP = 1000 / FPS;

const game = new App.Game();
const inputs = new App.Inputs();

function gameLoop(tile_renderer: App.TileRenderer) {
  let before = Date.now();
  game.update(inputs);
  game.draw(tile_renderer);
  let after = Date.now();
  let frameTime = after - before;
  let sleep = SLEEP - frameTime;
  setTimeout(() => gameLoop(tile_renderer), sleep);
}

window.onload = () => {
  let tile_renderer = new App.TileRenderer("GameCanvas");
  gameLoop(tile_renderer);
};

window.addEventListener("keydown", (e) => {
  inputs.push(e.key);
});

console.log("tsc bundling ok ");
