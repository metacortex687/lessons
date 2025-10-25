import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Move } from "./position.js";
import { MoveUp, MoveDown, MoveLeft, MoveRight } from "./position.js";

interface Slot {
  draw(tr: TileRenderer): void;
}

class EmptySlot implements Slot {
  draw(tr: TileRenderer): void {}
}

class WaterSlot implements Slot {
  draw(tr: TileRenderer): void {
    tr.drawRect(new Position(8, 0), "#0000cc");
  }
}

export interface MovePlayer {
  move(player: Player, pos: Position, map: GameMap): void;
}

export class PlayerMoveUp implements MovePlayer {
  move(player: Player, pos: Position, map: GameMap): void {
    map.moveVertical(player, pos, new MoveUp());
  }
}

export class PlayerMoveDown implements MovePlayer {
  move(player: Player, pos: Position, map: GameMap): void {
    map.moveVertical(player, pos, new MoveDown());
  }
}

export class PlayerMoveLeft implements MovePlayer {
  move(player: Player, pos: Position, map: GameMap): void {
    map.moveHorizontal(player, pos, new MoveLeft());
  }
}

export class PlayerMoveRight implements MovePlayer {
  move(player: Player, pos: Position, map: GameMap): void {
    map.moveHorizontal(player, pos, new MoveRight());
  }
}

export class Player {
  private slot_for_water = new EmptySlot();

  constructor(private pos: Position) {}

  pushHorisontal(layer: Layer, tile: Tile, move: Move) {
    layer.pushHorisontal(this, tile, this.pos, move);
  }

  draw(tr: TileRenderer) {
    this.draw_player(tr);

    this.slot_for_water.draw(tr);
  }

  private draw_player(tr: TileRenderer) {
    tr.drawRect(this.pos, "#ff0000");
  }

  setWater() {
    this.slot_for_water = new WaterSlot();
  }

  dropWater() {
    this.slot_for_water = new EmptySlot();
  }

  // moveHorizontal(map: GameMap, move: Move) {
  //   map.moveHorizontal(this, this.pos, move);
  // }

  // moveVertical(map: GameMap, move: Move) {
  //   map.moveVertical(this, this.pos, move);
  // }

  move1_FromInputs(map: GameMap, move: MovePlayer) //Уже есть другой move
  {
    move.move(this,this.pos,map);
  }

  move(layer: Layer, move: Move) {
    this.moveToTile(layer, this.pos.moved(move));
  }

  moveToTile(layer: Layer, new_pos: Position) {
    layer.moveTileTo(this.pos, new_pos);
    this.pos = new_pos;
  }
}
