namespace App {
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
}
