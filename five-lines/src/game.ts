import { GameMap } from "./map.js"
import {Inputs} from "./inputs.js"
import {TileRenderer} from "./tile_renderer.js"
import { Player } from "./player.js";

  export class Game {
    private player: Player;
    private map: GameMap;

    constructor() {
      this.map = new GameMap();
      this.player = new Player(1, 1);
    }

    update(inputs: Inputs) {
      this.handleInputs(inputs);
      this.map.update();
    }

    handleInputs(inputs: Inputs) {
      while (!inputs.is_empty()) {
        let current = inputs.pop()!;
        current.handle(this.player, this.map);
      }
    }

    draw(tr: TileRenderer) {
      tr.clearСanvas();
      this.map.draw(tr);
      this.player.draw(tr);
    }
  }

