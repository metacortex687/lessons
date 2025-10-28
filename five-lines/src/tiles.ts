import { GameMap } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { Player } from "./player.js";
import { Position, type Direction } from "./position.js";


interface FallingState {
  drop(map: GameMap, pos: Position): void;
  moveHorizontal(
    player: Player,
    map: GameMap,
    tile: Tile,
    move: Direction
  ): void;
}

export class Falling implements FallingState {
  drop(map: GameMap, pos: Position): void {
    map.moveTileTo(pos, new Position(pos.getX(), pos.getY() + 1));
  }
  moveHorizontal(
    player: Player,
    map: GameMap,
    tile: Tile,
    move: Direction
  ): void {}
}

class FallStrategy {
  moveHorizontal(player: Player, map: GameMap, tile: Tile, move: Direction) {
    this.falling.moveHorizontal(player, map, tile, move);
  }
  private falling: FallingState;

  constructor(falling: FallingState) {
    this.falling = falling;
  }

  update(map: GameMap, pos: Position): void {
    this.drop(map, pos);
  }

  private drop(map: GameMap, pos: Position) {
    this.falling = map.getBlockOnTopState(
      new Position(pos.getX(), pos.getY() + 1)
    );

    this.falling.drop(map, pos);
  }
}

export class Resting implements FallingState {
  drop(map: GameMap, pos: Position): void {}
  moveHorizontal(
    player: Player,
    map: GameMap,
    tile: Tile,
    move: Direction
  ): void {
    player.pushHorisontal(map, tile, move);
  }
}

export interface Tile {
  premove(player: Player): void;
  getBlockOnTopState(): FallingState;
  update(map: GameMap, pos: Position): void;

  onEnterVertical(map: GameMap, player: Player, move: Direction): void;
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void;
  draw(tr: TileRenderer, pos: Position): void;
  isAir(): boolean;
}



export class Garden implements Tile {
  premove(player: Player): void {
    player.pourWater();
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(map: GameMap, pos: Position): void {}
  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {}
  isAir(): boolean {
    return false;
  }

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#000000ff");
  }
}

export class Flux implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update( map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {
    player.comitEnterTile(map, move);
  }
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {
    player.comitEnterTile(map, move);
  }

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#ccffcc");
  }

  isAir(): boolean {
    return false;
  }
}

export class Unbreakable implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {}

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#999999");
  }

  isAir(): boolean {
    return false;
  }
}

export class Door implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {}

  draw(tr: TileRenderer, pos: Position): void {
    // tr.fillRect(x, y, "#999999");
    tr.drawDoor(pos);
  }

  isAir(): boolean {
    return false;
  }
}

export class Water implements Tile {
  private falling: FallingState;

  constructor(falling: FallingState) {
    this.fallStrategy = new FallStrategy(falling);
    this.falling = falling;
  }

  premove(player: Player): void {
    player.collectWater();
  }

  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  private fallStrategy: FallStrategy;

  update( map: GameMap, pos: Position): void {
    this.fallStrategy.update(map, pos);
  }

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {
    this.falling.moveHorizontal(player, map, this, move);
  }

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#0000cc");
  }
  isAir(): boolean {
    return false;
  }
}

export class Air implements Tile {
  premove(player: Player): void {}
  constructor() {}

  getBlockOnTopState(): FallingState {
    return new Falling();
  }
  update( map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {
    player.comitEnterTile(map, move);
  }
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {
    player.comitEnterTile(map, move);
  }

  draw(tr: TileRenderer, pos: Position): void {}

  isAir(): boolean {
    return true;
  }
}

export class PlayerTile implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {}

  draw(tr: TileRenderer, pos: Position): void {}

  isAir(): boolean {
    return false;
  }
}

export class Box implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  private fallStrategy: FallStrategy;

  update( map: GameMap, pos: Position): void {
    this.fallStrategy.update(map, pos);
  }

  constructor(falling: FallingState) {
    this.fallStrategy = new FallStrategy(falling);
  }

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {
    this.fallStrategy.moveHorizontal(player, map, this, move);
  }
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#8b4513");
  }

  isAir(): boolean {
    return false;
  }
}

export class Key implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  constructor(private lock: LockTile, private color: string) {}

  update(map: GameMap, pos: Position): void {}

  onEnterVertical(map: GameMap, player: Player, move: Direction): void {
    map.removeTile(this.lock);
    player.comitEnterTile(map, move);
  }
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {
    map.removeTile(this.lock);
    player.comitEnterTile(map, move);
  }
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, this.color);
  }

  isAir(): boolean {
    return false;
  }
}

export class KeyLockBundle {
  private _key: Key;
  private _lock: LockTile;

  constructor(private color: string) {
    this._lock = new LockTile(this.color);
    this._key = new Key(this._lock, this.color);
  }

  key(): Tile {
    return this._key;
  }

  lock(): Tile {
    return this._lock;
  }
}

export class LockTile implements Tile {
  premove(player: Player): void {}
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  constructor(private color: string) {}
  update(map: GameMap, pos: Position): void {}
  onEnterVertical(map: GameMap, player: Player, move: Direction): void {}
  onEnterHorizontal(map: GameMap, player: Player, move: Direction): void {}
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, this.color);
  }

  isAir(): boolean {
    return false;
  }
}
