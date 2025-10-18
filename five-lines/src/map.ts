import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air, EmptyGround } from "./tiles.js";
import { Player } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";

let rawMap: number[][] = [
  [2, 2, 2, 2, 2, 2, 12, 2],
  [2, 3, 0, 1, 1, 2, 0, 2],
  [2, 4, 2, 6, 1, 2, 0, 2],
  [2, 8, 4, 1, 1, 2, 0, 2],
  [2, 4, 1, 1, 1, 9, 0, 2],
  [2, 2, 2, 2, 2, 2, 2, 2],
];

let rawMapGround: number[][] = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 13, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
];

interface Layer {
  update(map: GameMap): void;
  pushHorisontal(
    map: GameMap,
    player: Player,
    tile: Tile,
    x: number,
    y: number,
    dx: number
  ): void;
  moveTileTo(x: number, y: number, newx: number, newy: number): void;
  moveVertical(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dy: number
  ): void;
  moveHorizontal(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dx: number
  ): void;
  draw(tr: TileRenderer): void;
  getBlockOnTopState(x: number, y: number): Falling;
  removeTile(tile: Tile): void;
}

class LayerMid implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map!: Tile[][];

  constructor() {
    this.map = this.tile_loader.load_data(rawMap);  
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

  moveHorizontal(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dx: number
  ) {
    this.getMap()[y][x + dx].moveHorizontal(player, map, dx);
  }

  moveVertical(map: GameMap, player: Player, x: number, y: number, dy: number) {
    this.getMap()[y + dy][x].moveVertical(player, map, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.getMap()[newy][newx] = this.getMap()[y][x];
    this.getMap()[y][x] = new Air(new EmptyGround());
  }

  pushHorisontal(
    map: GameMap,
    player: Player,
    tile: Tile,
    x: number,
    y: number,
    dx: number
  ) {
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

class LayerGround implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map!: Tile[][];

  constructor() {
    this.map = this.tile_loader.load_data(rawMapGround); 
  }

  update(map: GameMap): void {}
  pushHorisontal(
    map: GameMap,
    player: Player,
    tile: Tile,
    x: number,
    y: number,
    dx: number
  ): void {}
  moveTileTo(x: number, y: number, newx: number, newy: number): void {}
  moveVertical(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dy: number
  ): void {}
  moveHorizontal(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dx: number
  ): void {}

  draw(tr: TileRenderer): void {
    for (let y = 0; y < this.map.length; y++) {
      for (let x = 0; x < this.map[y].length; x++) {
        this.map[y][x].draw(tr, x, y);
      }
    }
  }

  getBlockOnTopState(x: number, y: number): Falling {
    return new Resting();
  }
  removeTile(tile: Tile): void {}
}

export class GameMap {
  private layer_mid: Layer; 
  private layer_ground: Layer; 

  constructor() {
    this.layer_mid = new LayerMid();
    this.layer_ground = new LayerGround();
  }

  getBlockOnTopState(x: number, y: number) {
    return this.layer_mid.getBlockOnTopState(x, y);
  }

  draw(tr: TileRenderer) {
    this.layer_ground.draw(tr);
    this.layer_mid.draw(tr);
  }

  moveHorizontal(player: Player, x: number, y: number, dx: number) {
    this.layer_mid.moveHorizontal(this, player, x, y, dx);
  }

  moveVertical(player: Player, x: number, y: number, dy: number) {
    this.layer_mid.moveVertical(this, player, x, y, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.layer_mid.moveTileTo(x, y, newx, newy);
  }

  pushHorisontal(player: Player, tile: Tile, x: number, y: number, dx: number) {
    this.layer_mid.pushHorisontal(this, player, tile, x, y, dx);
  }

  removeTile(tile: Tile) {
    this.layer_mid.removeTile(tile);
  }

  update() {
    this.layer_mid.update(this);
  }
}
