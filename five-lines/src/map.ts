import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air } from "./tiles.js";
import { Player, type PlayerMover } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
// import { Array2dCell } from "./array2D.js";
import { Position, type Direction } from "./position.js";

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
  movePlayer(player: Player, pos: Position, m: PlayerMover): void;
  update(map: GameMap): void;
  pushHorisontal(
    player: Player,
    tile: Tile,
    pos: Position,
    move: Direction
  ): void;
  moveTileTo(pos: Position, new_pos: Position, groundTile: Tile): void;
  draw(tr: TileRenderer): void;
  getBlockOnTopState(pos: Position): Falling;
  removeTile(tile: Tile): void;
}

export class Cell {
  update(layer: Layer, map: GameMap, p: Position): void {
    this.tile.update(layer, map, p);
  }

  push(t: Tile) {
    this.tile = t;
  }

  premove(player: Player) {
    throw new Error("Method not implemented.");
  }
  private tile: Tile = new Air();

  add(t: Tile): void {
    this.tile = t;
  }

  isAir(): boolean {
    return this.tile.isAir();
  }

  draw(tr: TileRenderer, p: Position): void {
    this.tile.draw(tr, p);
  }

  getBlockOnTopState() {
    return this.tile.getBlockOnTopState();
  }

  pop(): Tile {
    let res = this.tile;
    this.tile = new Air();
    return res;
  }

  peek(): Tile {
    return this.tile;
  }
}

class LayerMid implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map2D: Cell[][];

  constructor(private size_x: number, private size_y: number) {
    this.map2D = new NumberToTileTransformer().load_tile_array_2D(
      size_x,
      size_y,
      rawMap
    );
    //this.gravity = new Gravity(this);
  }

  removeTile(tile: Tile) {
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        if (this.map2D[y][x].peek() == tile) this.map2D[y][x].pop();
    // this.map2D.change_value(tile, new Air());
  }

  isAir(pos: Position) {
    return this.map2D[pos.getY()][pos.getX()].peek().isAir();
  }

  draw(tr: TileRenderer) {
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        this.map2D[y][x].draw(tr, new Position(x, y));

    // this.map2D.appleToAllCels((v, p) => v.draw(tr, p));
  }

  getBlockOnTopState(pos: Position) {
    return this.map2D[pos.getY()][pos.getX()].getBlockOnTopState();
  }

  movePlayer(player: Player, pos: Position, m: PlayerMover): void {
    let next_pos = m.nextPosition(pos);
    let om_moved_tile = this.map2D[next_pos.getY()][next_pos.getX()].peek();
    om_moved_tile.premove(player);
    m.dispatchEnter(om_moved_tile, this, player);
  }

  private getCell(p: Position) {
    return this.map2D[p.getY()][p.getX()];
  }

  moveTileTo(pos: Position, new_position: Position) {
    let cell = this.getCell(pos);
    let new_cell = this.getCell(new_position);
    new_cell.push(cell.pop());
    // cell.popValue();

    // this.map2D.setValue(new_position, this.map2D.getValue(pos));
    // this.map2D.setValue(pos, new Air());
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
    if (
      this.isAir(pos.moved(move).moved(move)) &&
      !this.isAir(pos.moved(move).down())
    ) {
      this.getCell(pos.moved(move).moved(move)).push(tile);
      // this.map2D.setValue(pos.moved(move).moved(move), tile);
      player.occupyTile(this, pos.moved(move), new Air());
    }
  }

  update(map: GameMap) {
    this.appleToAllCels((v, p) => v.update(this, map, p));
  }

  private appleToAllCels(f: (value: Cell, p: Position) => void): void {
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++)
        f(this.map2D[y][x], new Position(x, y));
    }
  }
}

// class LayerGround implements Layer {
//   private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
//   private map2D: Array2d<Tile>;

//   constructor(private size_x: number, private size_y: number) {
//     this.map2D = this.tile_loader.load_tile_array_2D(
//       size_x,
//       size_y,
//       rawMapGround
//     );
//   }

//   update(map: GameMap): void {}
//   pushHorisontal(
//     player: Player,
//     tile: Tile,
//     pos: Position,
//     move: Direction
//   ): void {}
//   moveTileTo(pos: Position, new_pos: Position): void {}

//   movePlayer(player: Player, pos: Position, m: PlayerMover): void {
//     let next_pos = m.nextPosition(pos);
//     let om_moved_tile = this.map2D.getValue(next_pos);
//     om_moved_tile.premove(player);
//   }

//   draw(tr: TileRenderer): void {
//     this.map2D.appleToAllCels((v, p) => v.draw(tr, p));
//   }

//   getBlockOnTopState(pos: Position): Falling {
//     return new Resting();
//   }
//   removeTile(tile: Tile): void {}
// }

export class GameMap {
  private layer_mid: Layer;
  // private layer_ground: Layer;

  constructor() {
    this.layer_mid = new LayerMid(8, 6);
    // this.layer_ground = new LayerGround(8, 6);
  }

  draw(tr: TileRenderer) {
    // this.layer_ground.draw(tr);
    this.layer_mid.draw(tr);
  }

  tryEnterTile(player: Player, pos: Position, m: PlayerMover) {
    this.layer_mid.movePlayer(player, pos, m);
    // this.layer_ground.movePlayer(player, pos, m);
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
    this.layer_mid.pushHorisontal(player, tile, pos, move);
  }

  update() {
    this.layer_mid.update(this);
  }
}
