import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air, EmptyGround } from "./tiles.js";
import { Player } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
import { Array2d } from "./array2D.js";

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

export interface Layer {
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
  private map: Array2d<Tile>;

  constructor(private size_x: number, private size_y: number ) {
    this.map = this.tile_loader.load_tile_array_2D(size_x,size_y,rawMap);
  }

  removeTile(tile: Tile) {
    this.map.removeTile(tile,new Air(new EmptyGround()));
    // for (let y = 0; y < this.map.length; y++) {
    //   for (let x = 0; x < this.map[y].length; x++) {
    //     if (this.map[y][x] === tile) {
    //       this.map[y][x] = new Air(new EmptyGround());
    //     }
    //   }
    // }
  }

  isAir(y: number, x: number) {
    return this.map.getValue(x,y).isAir();
  }

  draw(tr: TileRenderer) {
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++) {
        this.map.getValue(x,y).draw(tr, x, y);
      }
    }
  }

  getBlockOnTopState(x: number, y: number) {
    return this.map.getValue(x,y).getBlockOnTopState();
  }

  moveHorizontal(
    map: GameMap,
    player: Player,
    x: number,
    y: number,
    dx: number
  ) {
    this.map.getValue(x + dx,y).moveHorizontal(player, map, dx);
  }

  moveVertical(map: GameMap, player: Player, x: number, y: number, dy: number) {
    this.map.getValue(x,y + dy).moveVertical(player, map, dy);
  }

  moveTileTo(x: number, y: number, newx: number, newy: number) {
    this.map.setValue(newx,newy,this.map.getValue(x,y));
    this.map.setValue(x,y,new Air(new EmptyGround()));
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
      //this.map[y][x + dx + dx] = tile;
      this.map.setValue(x + dx + dx,y, tile);
      player.moveToTile(map, x + dx, y);
    }
  }

  update(map: GameMap) {
    for (let y = this.size_y - 1; y >= 0; y--)
      for (let x = 0; x < this.size_x; x++)
        this.map.getValue(x,y).update(this, map, x, y);
  }
}

class LayerGround implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
   private map: Array2d<Tile>;

  // constructor() {
  //   this.map = this.tile_loader.load_tile_array_2D(rawMapGround);

  // }

  constructor(private size_x: number, private size_y: number ) {
    this.map = this.tile_loader.load_tile_array_2D(size_x,size_y,rawMapGround);
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
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++) {
        this.map.getValue(x,y).draw(tr, x, y);
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
    this.layer_mid = new LayerMid(8,6);
    this.layer_ground = new LayerGround(8,6);
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
