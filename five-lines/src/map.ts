import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air } from "./tiles.js";
import { Player, type PlayerMover } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
// import { Array2dCell } from "./array2D.js";
import { Position, type Direction } from "./position.js";
import { Stack } from "./stack.js";

let rawMapMidle: number[][] = [
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

// export interface Layer2 {
//   movePlayer(player: Player, pos: Position, m: PlayerMover): void;
//   update(map: GameMap): void;
//   pushHorisontal(
//     player: Player,
//     tile: Tile,
//     pos: Position,
//     move: Direction
//   ): void;
//   moveTileTo(pos: Position, new_pos: Position, groundTile: Tile): void;
//   draw(tr: TileRenderer): void;
//   getBlockOnTopState(pos: Position): Falling;
//   removeTile(tile: Tile): void;
// }

export class Cell {
  private data: Stack<Tile> = new Stack<Tile>(() => new Air());

  update(map: GameMap, p: Position): void {
    this.data.apply_function(t => t.update(map, p));
  }

  pushTile(t: Tile) {
    this.data.push(t);
  }

  isAir(): boolean {
    return this.topTile().isAir();
  }

  draw(tr: TileRenderer, p: Position): void {
    this.data.apply_function(t => t.draw(tr, p));
  }

  getBlockOnTopState() {
    return this.topTile().getBlockOnTopState();
  }

  // pop2(): Tile {
  //   return this.data.pop();
  // }

  deleteTile(): void {
    this.data.pop();  
  }

  topTile(): Tile {
    return this.data.peek();
  }

  moveTile(to: Cell) {
    to.data.push(this.data.pop());
  }

  // toString(): string {
  //   const result_body = this.tiles
  //     .filter((_, i) => i < this.count)
  //     .map((x) => x.constructor?.name)
  //     .join(",");
  //   return `Cell[${result_body}]`;
  // }
}

// class LayerMid2 implements Layer2 {
//   private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
//   private map2D: Cell[][];

//   constructor(private size_x: number, private size_y: number) {
//     this.map2D = new NumberToTileTransformer().load_tile_array_2D(
//       size_x,
//       size_y,
//       rawMap
//     );
//     //this.gravity = new Gravity(this);
//   }

//   removeTile(tile: Tile) {
//     for (let y = 0; y < this.size_y; y++)
//       for (let x = 0; x < this.size_x; x++)
//         if (this.map2D[y][x].peek() == tile) this.map2D[y][x].pop();
//     // this.map2D.change_value(tile, new Air());
//   }

//   isAir(pos: Position) {
//     return this.map2D[pos.getY()][pos.getX()].peek().isAir();
//   }

//   draw(tr: TileRenderer) {
//     for (let y = 0; y < this.size_y; y++)
//       for (let x = 0; x < this.size_x; x++)
//         this.map2D[y][x].draw(tr, new Position(x, y));

//     // this.map2D.appleToAllCels((v, p) => v.draw(tr, p));
//   }

//   getBlockOnTopState(pos: Position) {
//     return this.map2D[pos.getY()][pos.getX()].getBlockOnTopState();
//   }

//   movePlayer(player: Player, pos: Position, m: PlayerMover): void {
//     let next_pos = m.nextPosition(pos);
//     let om_moved_tile = this.map2D[next_pos.getY()][next_pos.getX()].peek();
//     om_moved_tile.premove(player);
//     m.dispatchEnter(om_moved_tile, this, player);
//   }

//   private getCell(p: Position) {
//     return this.map2D[p.getY()][p.getX()];
//   }

//   moveTileTo(pos: Position, new_position: Position) {
//     let cell = this.getCell(pos);
//     let new_cell = this.getCell(new_position);
//     new_cell.push(cell.pop());
//     // cell.popValue();

//     // this.map2D.setValue(new_position, this.map2D.getValue(pos));
//     // this.map2D.setValue(pos, new Air());
//   }

//   pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
//     if (
//       this.isAir(pos.moved(move).moved(move)) &&
//       !this.isAir(pos.moved(move).down())
//     ) {
//       this.getCell(pos.moved(move).moved(move)).push(tile);
//       // this.map2D.setValue(pos.moved(move).moved(move), tile);
//       player.occupyTile(this, pos.moved(move), new Air());
//     }
//   }

//   update(map: GameMap) {
//     this.appleToAllCels((v, p) => v.update(this, map, p));
//   }

//   private appleToAllCels(f: (value: Cell, p: Position) => void): void {
//     for (let y = 0; y < this.size_y; y++) {
//       for (let x = 0; x < this.size_x; x++)
//         f(this.map2D[y][x], new Position(x, y));
//     }
//   }
// }

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
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map2D: Cell[][];

  constructor(private size_x: number, private size_y: number) {
    this.map2D = this.init_array(size_x, size_y);
    this.load_layer(rawMapMidle);

    // this.map2D = new NumberToTileTransformer().load_tile_array_2D(
    //   size_x,
    //   size_y,
    //   rawMapMidle
    // );
    // this.layer_mid = new LayerMid(8, 6);
    // this.layer_ground = new LayerGround(8, 6);
  }

  private load_layer(rawMap: number[][]) {
    let ntt = new NumberToTileTransformer();
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        this.map2D[y][x].pushTile(ntt.transform(rawMap[y][x]));
  }

  private init_array(size_x: number, size_y: number) {
    let map = new Array<Cell[]>(size_y);
    for (let y = 0; y < size_y; y++) {
      map[y] = new Array<Cell>(size_x);
      for (let x = 0; x < this.size_x; x++) map[y][x] = new Cell();
    }
    return map;
  }

  draw(tr: TileRenderer) {
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        this.map2D[y][x].draw(tr, new Position(x, y));
  }

  tryEnterTile(player: Player, pos: Position, m: PlayerMover) {
    let next_pos = m.nextPosition(pos);
    let om_moved_tile = this.map2D[next_pos.getY()][next_pos.getX()].topTile();
    console.log(om_moved_tile);
    // om_moved_tile.premove(player);
    console.log(`tryEnterTile om_moved_tile=${om_moved_tile.constructor.name}`);

    m.dispatchEnter(om_moved_tile, this, player);
  }

  moveTileTo(pos: Position, new_position: Position) {
    let cell = this.getCell(pos);
    let new_cell = this.getCell(new_position);
    new_cell.deleteTile();
    cell.moveTile(new_cell);
    // console.log(`cell до : ${cell}`);
    // new_cell.pop();
    // new_cell.pushTile(cell.pop());
    // cell.pop();
    // cell.pop();
    // console.log(`cell после : ${cell}`);

    // cell.popValue();

    // this.map2D.setValue(new_position, this.map2D.getValue(pos));
    // this.map2D.setValue(pos, new Air());
  }

  private getCell(p: Position) {
    return this.map2D[p.getY()][p.getX()];
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
    if (
      this.isAir(pos.moved(move).moved(move)) &&
      !this.isAir(pos.moved(move).down())
    ) {
      this.getCell(pos.moved(move).moved(move)).pushTile(tile);
      // this.map2D.setValue(pos.moved(move).moved(move), tile);
      player.occupyTile(this, pos.moved(move));
    }
  }

  isAir(pos: Position) {
    return this.map2D[pos.getY()][pos.getX()].topTile().isAir();
  }

  update() {
    this.appleToAllCels((v, p) => v.update(this, p));
  }

  private appleToAllCels(f: (value: Cell, p: Position) => void): void {
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++)
        f(this.map2D[y][x], new Position(x, y));
    }
  }

  getBlockOnTopState(pos: Position) {
    return this.map2D[pos.getY()][pos.getX()].getBlockOnTopState();
  }

  removeTile(tile: Tile) {
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        if (this.map2D[y][x].topTile() == tile) this.map2D[y][x].deleteTile();
    // this.map2D.change_value(tile, new Air());
  }
}
