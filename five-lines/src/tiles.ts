import { GameMap, type Layer } from "./map.js";
import { TileRenderer } from "./tile_renderer.js";
import { Player } from "./player.js";
import { Position, type Move } from "./position.js";

interface FallingState {
  drop(layer: Layer, map: GameMap, pos: Position): void;
  moveHorizontal(player: Player, layer: Layer, tile: Tile, move: Move): void;
}

export class Falling implements FallingState {
  drop(layer: Layer, map: GameMap, pos: Position): void {
    layer.moveTileTo(pos, new Position(pos.getX(), pos.getY() + 1));
  }
  moveHorizontal(player: Player, layer: Layer, tile: Tile, move: Move): void {}
}

class FallStrategy {
  moveHorizontal(player: Player, layer: Layer, tile: Tile, move: Move) {
    this.falling.moveHorizontal(player, layer, tile, move);
  }
  private falling: FallingState;

  constructor(falling: FallingState) {
    this.falling = falling;
  }

  update(layer: Layer, map: GameMap, pos: Position): void {
    this.drop(layer, map, pos);
  }

  private drop(layer: Layer, map: GameMap, pos: Position) {
    this.falling = layer.getBlockOnTopState(new Position(pos.getX(), pos.getY() + 1));

    this.falling.drop(layer, map, pos);
  }
}

export class Resting implements FallingState {
  drop(layer: Layer, map: GameMap, pos: Position): void {}
  moveHorizontal(player: Player, layer: Layer, tile: Tile, move: Move): void {
    player.pushHorisontal(layer, tile, move);
  }
}

export interface Tile {
  getBlockOnTopState(): FallingState;
  update(layer: Layer, map: GameMap, pos: Position): void;

  moveVertical(layer: Layer, player: Player, move: Move): void;
  moveHorizontal(layer: Layer, player: Player, move: Move): void;
  draw(tr: TileRenderer, pos: Position): void;
  isAir(): boolean;
  getGroundLayer(): GroundLayer;
  setGroundLayer(gl: GroundLayer): void;
}

interface GroundLayer {
  draw(tr: TileRenderer, pos: Position): void;
}

export class EmptyGround implements GroundLayer {
  draw(tr: TileRenderer, pos: Position): void {}
}

export class Garden implements GroundLayer {
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#000000ff");
  }
}

export class Flux implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {
    player.move(layer, move);
  }
  moveHorizontal(layer: Layer, player: Player, move: Move): void {
    player.move(layer, move);
  }

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#ccffcc");
  }

  isAir(): boolean {
    return false;
  }
}

export class Unbreakable implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {}

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#999999");
  }

  isAir(): boolean {
    return false;
  }
}

export class Door implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {}

  draw(tr: TileRenderer, pos: Position): void {
    // tr.fillRect(x, y, "#999999");
    tr.drawDoor(pos);
  }

  isAir(): boolean {
    return false;
  }
}

export class Water implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  private falling: FallingState;

  constructor(falling: FallingState) {
    this.fallStrategy = new FallStrategy(falling);
    this.falling = falling;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  private fallStrategy: FallStrategy;

  update(layer: Layer, map: GameMap, pos: Position): void {
    this.fallStrategy.update(layer, map, pos);
  }

  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {
    this.falling.moveHorizontal(player, layer, this, move);
  }

  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#0000cc");
  }
  isAir(): boolean {
    return false;
  }
}

export class Air implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  constructor(private ground: GroundLayer) {}

  getBlockOnTopState(): FallingState {
    return new Falling();
  }
  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {
    player.move(layer, move);
  }
  moveHorizontal(layer: Layer, player: Player, move: Move): void {
    player.move(layer, move);
  }

  draw(tr: TileRenderer, pos: Position): void {
    this.ground.draw(tr, pos);
  }

  isAir(): boolean {
    return true;
  }
}

export class PlayerTile implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {}

  draw(tr: TileRenderer, pos: Position): void {}

  isAir(): boolean {
    return false;
  }
}

export class Box implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  private fallStrategy: FallStrategy;

  update(layer: Layer, map: GameMap, pos: Position): void {
    this.fallStrategy.update(layer, map, pos);
  }

  constructor(falling: FallingState) {
    this.fallStrategy = new FallStrategy(falling);
  }

  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {
    this.fallStrategy.moveHorizontal(player, layer, this, move);
  }
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, "#8b4513");
  }

  isAir(): boolean {
    return false;
  }
}

export class Key implements Tile {
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  constructor(private lock: LockTile, private color: string) {}

  update(layer: Layer, map: GameMap, pos: Position): void {}

  moveVertical(layer: Layer, player: Player, move: Move): void {
    layer.removeTile(this.lock);
    player.move(layer, move);
  }
  moveHorizontal(layer: Layer, player: Player, move: Move): void {
    layer.removeTile(this.lock);
    player.move(layer, move);
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
  private grounLayer: GroundLayer = new EmptyGround();
  getGroundLayer(): GroundLayer {
    return this.grounLayer;
  }
  setGroundLayer(gl: GroundLayer): void {
    this.grounLayer = gl;
  }
  getBlockOnTopState(): FallingState {
    return new Resting();
  }
  constructor(private color: string) {}
  update(layer: Layer, map: GameMap, pos: Position): void {}
  moveVertical(layer: Layer, player: Player, move: Move): void {}
  moveHorizontal(layer: Layer, player: Player, move: Move): void {}
  draw(tr: TileRenderer, pos: Position): void {
    tr.drawRect(pos, this.color);
  }

  isAir(): boolean {
    return false;
  }
}
