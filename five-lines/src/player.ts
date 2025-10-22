import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
  
  export class Player {
    constructor(private x: number, private y: number) {}

    pushHorisontal(map: GameMap, tile: Tile, dx: number) {
      map.pushHorisontal(this, tile, this.x, this.y, dx);
    }
    draw(tr: TileRenderer) {
      tr.drawRect(this.x, this.y, "#ff0000");
    }

    moveHorizontal(map: GameMap, dx: number) {
      map.moveHorizontal(this, this.x, this.y, dx);
    }

    moveVertical(map: GameMap, dy: number) {
      map.moveVertical(this, this.x, this.y, dy);
    }

    move(layer: Layer, map: GameMap, dx: number, dy: number) {
      this.moveToTile(layer,map, this.x + dx, this.y + dy);
    }

    moveToTile(layer: Layer, map: GameMap, newx: number, newy: number) {
      layer.moveTileTo(this.x, this.y, newx, newy);
      this.x = newx;
      this.y = newy;
    }
  }
