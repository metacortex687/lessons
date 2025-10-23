import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air, EmptyGround } from "./tiles.js";
import { Player } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
import { Array2d } from "./array2D.js";
import { Position } from "./position.js";

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
    player: Player,
    tile: Tile,
    pos: Position,
    dx: number
  ): void;
  moveTileTo(pos: Position, new_pos: Position): void;
  moveVertical(
    player: Player,
    pos: Position,
    dy: number
  ): void;
  moveHorizontal(
    player: Player,
    pos: Position,
    dx: number
  ): void;
  draw(tr: TileRenderer): void;
  getBlockOnTopState(pos: Position): Falling;
  removeTile(tile: Tile): void;
}

class LayerMid implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map: Array2d<Tile>;

  constructor(private size_x: number, private size_y: number) {
    this.map = this.tile_loader.load_tile_array_2D(size_x, size_y, rawMap);
  }

  removeTile(tile: Tile) {
    this.map.change_value(tile, new Air(new EmptyGround()));
  }

  isAir(pos: Position) {
    return this.map.getValue(pos.getX(), pos.getY()).isAir();
  }

  draw(tr: TileRenderer) {
    this.map.appleToAllCels((v, x, y) => v.draw(tr, new Position(x, y)));
  }

  getBlockOnTopState(pos: Position) {
    return this.map.getValue(pos.getX(), pos.getY()).getBlockOnTopState();
  }

  moveHorizontal(
    player: Player,
    pos: Position,
    dx: number
  ) {
    this.map.getValue(pos.getX() + dx, pos.getY()).moveHorizontal(this, player, dx);
  }

  moveVertical(player: Player, pos: Position, dy: number) {
    this.map.getValue(pos.getX(), pos.getY() + dy).moveVertical(this, player, dy);
  }

  moveTileTo(positiom: Position, new_position: Position) {
    this.map.setValue(new_position.getX(), new_position.getY(), this.map.getValue(positiom.getX(), positiom.getY()));
    this.map.setValue(positiom.getX(), positiom.getY(), new Air(new EmptyGround()));
  }

  pushHorisontal(
    player: Player,
    tile: Tile,
    pos: Position,
    dx: number
  ) {
    if (this.isAir(new Position(pos.getX() + dx + dx,pos.getY())) && !this.isAir(new Position(pos.getX() + dx, pos.getY() + 1))) {
      this.map.setValue(pos.getX() + dx + dx, pos.getY(), tile);
      player.moveToTile(this, new Position(pos.getX() + dx, pos.getY()));
    }
  }

  update(map: GameMap) {
    this.map.appleToAllCels((v, x, y) => v.update(this, map, new Position(x, y)));
  }
}

class LayerGround implements Layer {
  private tile_loader: NumberToTileTransformer = new NumberToTileTransformer();
  private map: Array2d<Tile>;

  constructor(private size_x: number, private size_y: number) {
    this.map = this.tile_loader.load_tile_array_2D(
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
    dx: number
  ): void {}
  moveTileTo(pos: Position, new_pos: Position): void {}
  moveVertical(
    player: Player,
    pos: Position,
    dy: number
  ): void {}
  moveHorizontal(
    player: Player,
    pos: Position,
    dx: number
  ): void {}

  draw(tr: TileRenderer): void {
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++) {
        this.map.getValue(x, y).draw(tr, new Position(x,y));
      }
    }
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

  moveHorizontal(player: Player, pos: Position, dx: number) {
    this.layer_mid.moveHorizontal(player, pos, dx);
  }

  moveVertical(player: Player, pos: Position, dy: number) {
    this.layer_mid.moveVertical(player, pos, dy);
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, dx: number) {
    this.layer_mid.pushHorisontal(player, tile, pos, dx);
  }

  update() {
    this.layer_mid.update(this);
  }
}
