import { GameMap } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { Air, type Tile } from "./tiles.js";
import { Position } from "./position.js";
import { type Direction } from "./position.js";
import { type MoveOnTileStrategy } from "./map.js";

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

export interface PlayerMove {
  dispatchEnter(tile: Tile, map: GameMap, player: Player): void;
  nextPosition(pos: Position): Position;
}

export class PlayerMoveVertical implements PlayerMove {
  constructor(private direction: Direction) {}

  dispatchEnter(tile: Tile, map: GameMap, player: Player): void {
    tile.onEnter(player);
    tile.onEnterVertical(map, player, this.direction);
  }

  nextPosition(pos: Position): Position {
    return pos.moved(this.direction);
  }
}

export class PlayerMoveHorizontal implements PlayerMove {
  constructor(private direction: Direction) {}

  dispatchEnter(tile: Tile, map: GameMap, player: Player): void {
    tile.onEnter(player);
    tile.onEnterHorizontal(map, player, this.direction);
  }

  nextPosition(pos: Position): Position {
    return pos.moved(this.direction);
  }
}

export class Player {
  private waterContainer = new EmptySlot();

  constructor(private pos: Position) {}

  pushHorisontal(map: GameMap, tile: Tile, move: Direction) {
    map.pushHorisontal(this, tile, this.pos, move);
  }

  draw(tr: TileRenderer) {
    this.drawPlayer(tr);

    this.waterContainer.draw(tr);
  }

  private drawPlayer(tr: TileRenderer) {
    tr.drawRect(this.pos, "#ff0000");
  }

  collectWater() {
    this.waterContainer = new WaterSlot();
  }

  pourWater() {
    this.waterContainer = new EmptySlot();
  }

  tryEnterTile(map: GameMap, m: PlayerMove) {
    map.tryEnterTile(this, this.pos, m);
  }

  comitEnterTile(
    map: GameMap,
    move: Direction,
    moveStrategy: MoveOnTileStrategy
  ) {
    this.occupyTile(map, this.pos.moved(move), moveStrategy);
  }

  occupyTile(
    map: GameMap,
    new_pos: Position,
    moveStrategy: MoveOnTileStrategy
  ) {
    map.moveTileTo(this.pos, new_pos, moveStrategy);
    this.pos = new_pos;
  }
}
