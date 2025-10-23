import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Move } from "./position.js";
  
  export class Player {
    constructor(private pos: Position) {}

    pushHorisontal(layer: Layer, tile: Tile, move: Move) {
      layer.pushHorisontal(this, tile, this.pos, move);
    }

    draw(tr: TileRenderer) {
      tr.drawRect(this.pos, "#ff0000");
    }

    moveHorizontal(map: GameMap, move: Move) {
      map.moveHorizontal(this, this.pos, move);
    }

    moveVertical(map: GameMap, move: Move) {
      map.moveVertical(this, this.pos, move);
    }


    move(layer: Layer, move: Move) {
      this.moveToTile(layer, move.translate(this.pos));
    }

    moveToTile(layer: Layer, new_pos: Position) {
      layer.moveTileTo(this.pos, new_pos);
      this.pos = new_pos;

    }
  }
