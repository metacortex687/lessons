import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Air, EmptyGround } from "./tiles.js";
import { Player } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";

let rawMap: number[][] = [
  [2, 2, 2, 2, 2, 2, 12, 2],
  [2, 3, 0, 13, 1, 2, 0, 2],
  [2, 4, 2, 6, 1, 2, 0, 2],
  [2, 8, 4, 1, 1, 2, 0, 2],
  [2, 4, 1, 1, 1, 9, 0, 2],
  [2, 2, 2, 2, 2, 2, 2, 2],
];

export class GameMap {
  private map!: Tile[][];
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();

  constructor() {
    this.load_data();
  }

  private load_data() {
    this.map = new Array(rawMap.length);
    for (let y = 0; y < rawMap.length; y++) {
      this.map[y] = new Array(rawMap[y].length);
      for (let x = 0; x < rawMap[y].length; x++) {
        this.map[y][x] = this.tile_loader.transform(rawMap[y][x]);
      }
    }
  }

  isAir(y: number, x: number) {
    return this.map[y][x].isAir();
  }

  removeTile(tile: Tile) {
    for (let y = 0; y < this.map.length; y++) {
      for (let x = 0; x < this.map[y].length; x++) {
        if (this.map[y][x] === tile) {
          this.map[y][x] = new Air(new EmptyGround());
        }
      }
    }
  }

  getBlockOnTopState(x: number, y: number) {
    return this.map[y][x].getBlockOnTopState();
  }

  draw(tr: TileRenderer) {
    for (let y = 0; y < this.map.length; y++) {
      for (let x = 0; x < this.map[y].length; x++) {
        this.map[y][x].draw(tr, x, y);
      }
    }
  }

  moveHorizontal(player: Player, x: number, y: number, dx: number) {
    this.map[y][x + dx].moveHorizontal(player, this, dx);
  }

  moveVertical(player: Player, x: number, y: number, dy: number) {
    this.map[y + dy][x].moveVertical(player, this, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.map[newy][newx] = this.map[y][x];
    this.map[y][x] = new Air(new EmptyGround());
  }

  pushHorisontal(player: Player, tile: Tile, x: number, y: number, dx: number) {
    if (this.isAir(y, x + dx + dx) && !this.isAir(y + 1, x + dx)) {
      this.map[y][x + dx + dx] = tile;
      player.moveToTile(this, x + dx, y);
    }
  }

  update() {
    for (let y = this.map.length - 1; y >= 0; y--)
      for (let x = 0; x < this.map[y].length; x++)
        this.map[y][x].update(this, x, y);
  }
}
