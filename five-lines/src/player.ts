import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Move } from "./position.js";

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
  movePlayerOnTile(om_moved_tile: Tile, layer: Layer, player: Player): void;
  next_pos(pos: Position): Position;
}

export class PlayerMoveVertical implements MovePlayer {
  constructor(private direction: Move) {}
  movePlayerOnTile(om_moved_tile: Tile, layer: Layer, player: Player): void {
    om_moved_tile.moveVertical(layer, player, this.direction);
  }
  next_pos(pos: Position): Position {
    return pos.moved(this.direction);
  }
}

export class PlayerMoveHorizontal implements MovePlayer {
  constructor(private direction: Move) {}
  movePlayerOnTile(om_moved_tile: Tile, layer: Layer, player: Player): void {
    om_moved_tile.moveHorizontal(layer, player, this.direction);
  }

  next_pos(pos: Position): Position {
    return pos.moved(this.direction);
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

  movePlayer(map: GameMap, m: MovePlayer) {
    map.movePlayer(this, this.pos, m);
  }

  move(layer: Layer, move: Move) {
    this.moveToTile(layer, this.pos.moved(move));
  }

  moveToTile(layer: Layer, new_pos: Position) {
    layer.moveTileTo(this.pos, new_pos);
    this.pos = new_pos;
  }
}
