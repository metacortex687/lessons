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

class Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map!: Tile[][];

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

  removeTile(tile: Tile) {
    for (let y = 0; y < this.map.length; y++) {
      for (let x = 0; x < this.map[y].length; x++) {
        if (this.map[y][x] === tile) {
          this.map[y][x] = new Air(new EmptyGround());
        }
      }
    }
  }

  private getMap() {
    return this.map;
  }

  isAir(y: number, x: number) {
    return this.getMap()[y][x].isAir();
  }

  draw(tr: TileRenderer) {
    for (let y = 0; y < this.getMap().length; y++) {
      for (let x = 0; x < this.getMap()[y].length; x++) {
        this.getMap()[y][x].draw(tr, x, y);
      }
    }
  }

  getBlockOnTopState(x: number, y: number) {
    return this.getMap()[y][x].getBlockOnTopState();
  }


   moveHorizontal(map:GameMap,player: Player, x: number, y: number, dx: number) {

    this.getMap()[y][x + dx].moveHorizontal(player, map, dx);
  }

  moveVertical(map:GameMap,player: Player, x: number, y: number, dy: number) {
    this.getMap()[y + dy][x].moveVertical(player, map, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.getMap()[newy][newx] = this.getMap()[y][x];
    this.getMap()[y][x] = new Air(new EmptyGround());
  }

  pushHorisontal(map:GameMap, player: Player, tile: Tile, x: number, y: number, dx: number) {
    if (this.isAir(y, x + dx + dx) && !this.isAir(y + 1, x + dx)) {
      this.getMap()[y][x + dx + dx] = tile;
      player.moveToTile(map, x + dx, y);
    }
  }

  update(map: GameMap) {
    for (let y = this.getMap().length - 1; y >= 0; y--)
      for (let x = 0; x < this.getMap()[y].length; x++)
        this.getMap()[y][x].update(map, x, y);
  }
}

export class GameMap {
  private layer = new Layer();

  constructor() {}

  getBlockOnTopState(x: number, y: number) {
    return this.layer.getBlockOnTopState(x,y);
  }

  draw(tr: TileRenderer) {
    this.layer.draw(tr);
  }

  moveHorizontal(player: Player, x: number, y: number, dx: number) {
    this.layer.moveHorizontal(this,player, x, y, dx);
  }

  moveVertical(player: Player, x: number, y: number, dy: number) {
    this.layer.moveVertical(this,player, x, y, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.layer.moveTileTo(x,y,newx,newy);
  }

  pushHorisontal(player: Player, tile: Tile, x: number, y: number, dx: number) {
    this.layer.pushHorisontal(this,player, tile, x, y, dx);
  }

  removeTile(tile: Tile) {
    this.layer.removeTile(tile);
  }

  update() {
    this.layer.update(this);
  }
}
