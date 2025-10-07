// import { Game } from "./game";

const FPS = 30;
const SLEEP = 1000 / FPS;

function createGraphics() {
  let canvas = document.getElementById("GameCanvas") as HTMLCanvasElement;
  let g = canvas.getContext("2d")!;

  g.clearRect(0, 0, canvas.width, canvas.height);

  return g;
}

const game = new App.Game();
const inputs = new App.Inputs();

function gameLoop() {
  let before = Date.now();
  let g = createGraphics();
  game.update(inputs);
  game.draw(g);
  let after = Date.now();
  let frameTime = after - before;
  let sleep = SLEEP - frameTime;
  setTimeout(() => gameLoop(), sleep);
}

window.onload = () => {
  gameLoop();
};

window.addEventListener("keydown", (e) => {
  inputs.push(e.key);
});

console.log("tsc bundling ok ");
