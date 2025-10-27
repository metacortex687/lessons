import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Direction } from "./position.js";

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

export interface PlayerMover {
  dispatchEnter(tile: Tile, layer: Layer, player: Player): void;
  nextPosition(pos: Position): Position;
}

export class PlayerMoverVertical implements PlayerMover {
  constructor(private direction: Direction) {}

  dispatchEnter(tile: Tile, layer: Layer, player: Player): void {
    tile.onEnterVertical(layer, player, this.direction);
  }

  nextPosition(pos: Position): Position {
    return pos.moved(this.direction);
  }
}

export class PlayerMoverHorizontal implements PlayerMover {
  constructor(private direction: Direction) {}

  dispatchEnter(tile: Tile, layer: Layer, player: Player): void {
    tile.onEnterHorizontal(layer, player, this.direction);
  }

  nextPosition(pos: Position): Position {
    return pos.moved(this.direction);
  }
}

export class Player {
  private slotForWater = new EmptySlot();

  constructor(private pos: Position) {}

  pushHorisontal(layer: Layer, tile: Tile, move: Direction) {
    layer.pushHorisontal(this, tile, this.pos, move);
  }

  draw(tr: TileRenderer) {
    this.drawPlayer(tr);

    this.slotForWater.draw(tr);
  }

  private drawPlayer(tr: TileRenderer) {
    tr.drawRect(this.pos, "#ff0000");
  }

  setWater() {
    this.slotForWater = new WaterSlot();
  }

  dropWater() {
    this.slotForWater = new EmptySlot();
  }

  tryEnterTile(map: GameMap, m: PlayerMover) {
    map.tryEnterTile(this, this.pos, m);
  }

  comitEnterTile(layer: Layer, move: Direction) {
    this.occupyTile(layer, this.pos.moved(move));
  }

  occupyTile(layer: Layer, new_pos: Position) {
    layer.moveTileTo(this.pos, new_pos);
    this.pos = new_pos;
  }
}
