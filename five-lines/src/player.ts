import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
  
  export class Player {
    constructor(private pos: Position) {}

    pushHorisontal(layer: Layer, tile: Tile, dx: number) {
      layer.pushHorisontal(this, tile, this.pos, dx);
    }
    
    draw(tr: TileRenderer) {
      tr.drawRect(this.pos, "#ff0000");
    }

    moveHorizontal(map: GameMap, dx: number) {
      map.moveHorizontal(this, this.pos, dx);
    }

    moveVertical(map: GameMap, dy: number) {
      map.moveVertical(this, this.pos, dy);
    }

    move(layer: Layer, dx: number, dy: number) {
      this.moveToTile(layer, this.pos.getX() + dx, this.pos.getY() + dy);
    }

    moveToTile(layer: Layer, newx: number, newy: number) {
      let new_pos = new Position(newx,newy);
      layer.moveTileTo(this.pos, new_pos);
      this.pos = new_pos;

    }
  }
