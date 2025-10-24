import { TileRenderer } from "./tile_renderer.js";
import { Falling, Resting, type Tile } from "./tiles.js";
import { Air, EmptyGround } from "./tiles.js";
import { Player } from "./player.js";
import { NumberToTileTransformer } from "./tile_loader.js";
import { Array2d } from "./array2D.js";
import { Position, type Move } from "./position.js";

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
  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Move): void;
  moveTileTo(pos: Position, new_pos: Position): void;
  moveVertical(player: Player, pos: Position, move: Move): void;
  moveHorizontal(player: Player, pos: Position, move: Move): void;
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
    return this.map.getValue(pos).isAir();
  }

  draw(tr: TileRenderer) {
    this.map.appleToAllCels((v, p) => v.draw(tr, p));
  }

  getBlockOnTopState(pos: Position) {
    return this.map.getValue(pos).getBlockOnTopState();
  }

  moveHorizontal(player: Player, pos: Position, move: Move) {
    let newPos = move.translate(pos);
    this.map
      .getValue(newPos)
      .moveHorizontal(this, player, move);
  }

  moveVertical(player: Player, pos: Position, move: Move) {
    let newPos = move.translate(pos);
    this.map
      .getValue(newPos)
      .moveVertical(this, player, move);
  }

  moveTileTo(pos: Position, new_position: Position) {
    this.map.setValue(
      new_position,
      this.map.getValue(pos)
    );
    this.map.setValue(
      pos,
      new Air(new EmptyGround())
    );
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Move) {
    if (
      this.isAir(move.translate(move.translate(pos))) &&
      !this.isAir(new Position(move.translate(pos).getX(), pos.getY() + 1))
    ) {
      this.map.setValue(
        move.translate(move.translate(pos)),
        tile
      );
      player.moveToTile(this, move.translate(pos));
    }
  }

  update(map: GameMap) {
    this.map.appleToAllCels((v, p) =>
      v.update(this, map, p)
    );
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
  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Move): void {}
  moveTileTo(pos: Position, new_pos: Position): void {}
  moveVertical(player: Player, pos: Position, move: Move): void {}
  moveHorizontal(player: Player, pos: Position, move: Move): void {}

  draw(tr: TileRenderer): void {
    this.map.appleToAllCels((v, p) => v.draw(tr, p));
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

  moveHorizontal(player: Player, pos: Position, move: Move) {
    this.layer_mid.moveHorizontal(player, pos, move);
  }

  moveVertical(player: Player, pos: Position, move: Move) {
    this.layer_mid.moveVertical(player, pos, move);
  }

  pushHorisontal(player: Player, tile: Tile, pos: Position, move: Move) {
    this.layer_mid.pushHorisontal(player, tile, pos, move);
  }

  update() {
    this.layer_mid.update(this);
  }
}
