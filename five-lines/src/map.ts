import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air } from "./tiles.js";
import { Player, type MovePlayer } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
import { Array2d } from "./array2D.js";
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
  movePlayer(player: Player, pos: Position, m: MovePlayer): void;
  update(map: GameMap): void;
  pushHorisontal(
    player: Player,
    tile: Tile,
    pos: Position,
    move: Direction
  ): void;
  moveTileTo(pos: Position, new_pos: Position): void;
  draw(tr: TileRenderer): void;
  getBlockOnTopState(pos: Position): Falling;
  removeTile(tile: Tile): void;
}

class LayerMid implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map2D: Array2d<Tile>;

  constructor(private size_x: number, private size_y: number) {
    this.map2D = new NumberToTileTransformer().load_tile_array_2D(
      size_x,
      size_y,
      rawMap
    );
    //this.gravity = new Gravity(this);
  }

  removeTile(tile: Tile) {
    this.map2D.change_value(tile, new Air());
  }

  isAir(pos: Position) {
    return this.map2D.getValue(pos).isAir();
  }

  draw(tr: TileRenderer) {
    this.map2D.appleToAllCels((v, p) => v.draw(tr, p));
  }

  getBlockOnTopState(pos: Position) {
    return this.map2D.getValue(pos).getBlockOnTopState();
  }

  movePlayer(player: Player, pos: Position, m: MovePlayer): void {
    let next_pos = m.next_pos(pos);
    let om_moved_tile = this.map2D.getValue(next_pos);
    om_moved_tile.premove(player);
    m.movePlayerOnTile(om_moved_tile, this, player);
  }

  moveTileTo(pos: Position, new_position: Position) {
    this.map2D.setValue(new_position, this.map2D.getValue(pos));
    this.map2D.setValue(pos, new Air());
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
    if (
      this.isAir(pos.moved(move).moved(move)) &&
      !this.isAir(pos.moved(move).down())
    ) {
      this.map2D.setValue(pos.moved(move).moved(move), tile);
      player.moveToTile(this, pos.moved(move));
    }
  }

  update(map: GameMap) {
    this.map2D.appleToAllCels((v, p) => v.update(this, map, p));
  }
}

class LayerGround implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map2D: Array2d<Tile>;

  constructor(private size_x: number, private size_y: number) {
    this.map2D = this.tile_loader.load_tile_array_2D(
      size_x,
      size_y,
      rawMapGround
    );
  }

  update(map: GameMap): void {}
  pushHorisontal(
    player: Player,
    tile: Tile,
    pos: Position,
    move: Direction
  ): void {}
  moveTileTo(pos: Position, new_pos: Position): void {}

  movePlayer(player: Player, pos: Position, m: MovePlayer): void {
    let next_pos = m.next_pos(pos);
    let om_moved_tile = this.map2D.getValue(next_pos);
    om_moved_tile.premove(player);
  }

  draw(tr: TileRenderer): void {
    this.map2D.appleToAllCels((v, p) => v.draw(tr, p));
  }

  getBlockOnTopState(pos: Position): Falling {
    return new Resting();
  }
  removeTile(tile: Tile): void {}
}

export class GameMap {
  private layer_mid: Layer;
  private layer_ground: Layer;

  constructor() {
    this.layer_mid = new LayerMid(8, 6);
    this.layer_ground = new LayerGround(8, 6);
  }

  draw(tr: TileRenderer) {
    this.layer_ground.draw(tr);
    this.layer_mid.draw(tr);
  }

  movePlayer(player: Player, pos: Position, m: MovePlayer) {
    this.layer_mid.movePlayer(player, pos, m);
    this.layer_ground.movePlayer(player, pos, m);
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Direction) {
    this.layer_mid.pushHorisontal(player, tile, pos, move);
  }

  update() {
    this.layer_mid.update(this);
  }
}
