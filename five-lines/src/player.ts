import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Move } from "./position.js";

export class Player {
  private have_water: boolean = false;

  constructor(private pos: Position) {}

  pushHorisontal(layer: Layer, tile: Tile, move: Move) {
    layer.pushHorisontal(this, tile, this.pos, move);
  }

  draw(tr: TileRenderer) {
    tr.drawRect(this.pos, "#ff0000");

    if (this.have_water) tr.drawRect(new Position(8, 0), "#0000cc");
  }

  setWater() {
    this.have_water = true;
  }

  dropWater() {
    this.have_water = false;
  }

  moveHorizontal(map: GameMap, move: Move) {
    map.moveHorizontal(this, this.pos, move);
  }

  moveVertical(map: GameMap, move: Move) {
    map.moveVertical(this, this.pos, move);
  }

  move(layer: Layer, move: Move) {
    this.moveToTile(layer, this.pos.moved(move));
  }

  moveToTile(layer: Layer, new_pos: Position) {
    layer.moveTileTo(this.pos, new_pos);
    this.pos = new_pos;
  }
}
