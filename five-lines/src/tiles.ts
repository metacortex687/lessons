  import {GameMap, type Layer} from "./map.js";
  import { TileRenderer } from "./tile_renderer.js";
  import { Player } from "./player.js";
  
  interface FallingState {
    drop(map: GameMap, y: number, x: number): void;
    moveHorizontal(player: Player, map: GameMap, tile: Tile, dx: number): void;
  }

  export class Falling implements FallingState {
    drop(map: GameMap, y: number, x: number): void {
      map.moveTileTo(x, y, x, y + 1);
    }
    moveHorizontal(
      player: Player,
      map: GameMap,
      tile: Tile,
      dx: number
    ): void {}
  }

  class FallStrategy {
    moveHorizontal(player: Player, map: GameMap, tile: Tile, dx: number) {
      this.falling.moveHorizontal(player, map, tile, dx);
    }
    private falling: FallingState;

    constructor(falling: FallingState) {
      this.falling = falling;
    }

    update(layer:Layer, map: GameMap, x: number, y: number): void {
      this.drop(layer,map, y, x);
    }

    private drop(layer:Layer, map: GameMap, y: number, x: number) {
      this.falling = layer.getBlockOnTopState(x, y + 1);

      this.falling.drop(map, y, x);
    }
  }

  export class Resting implements FallingState {
    drop(map: GameMap, y: number, x: number): void {}
    moveHorizontal(player: Player, map: GameMap, tile: Tile, dx: number): void {
      player.pushHorisontal(map, tile, dx);
    }
  }


  
  export interface Tile {
    getBlockOnTopState(): FallingState;
    update(layer:Layer,map: GameMap, x: number, y: number): void;

    moveVertical(player: Player, map: GameMap, dy: number): void;
    moveHorizontal(player: Player, map: GameMap, dx: number): void;
    draw(tr: TileRenderer, x: number, y: number): void;
    isAir(): boolean;
    getGroundLayer(): GroundLayer;
    setGroundLayer(gl: GroundLayer): void;
  }

  interface GroundLayer {
    draw(tr: TileRenderer, x: number, y: number): void;
  }

  export class EmptyGround implements GroundLayer {
    draw(tr: TileRenderer, x: number, y: number): void {}
  }

  export class Garden implements GroundLayer {
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, "#000000ff");
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: GameMap, dx: number): void {
      player.move(map, dx, 0);
    }

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, "#ccffcc");
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {}

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, "#999999");
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {}

    draw(tr: TileRenderer, x: number, y: number): void {
      // tr.fillRect(x, y, "#999999");
      tr.drawDoor(x, y);
    }

    isAir(): boolean {
      return false;
    }
  }

  export class Stone implements Tile {
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

    update(layer:Layer,map: GameMap, x: number, y: number): void {
      this.fallStrategy.update(layer,map, x, y);
    }

    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {
      this.falling.moveHorizontal(player, map, this, dx);
    }

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, "#0000cc");
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: GameMap, dx: number): void {
      player.move(map, dx, 0);
    }

    draw(tr: TileRenderer, x: number, y: number): void {
      this.ground.draw(tr, x, y);
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {}

    draw(tr: TileRenderer, x: number, y: number): void {}

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

    update(layer:Layer,map: GameMap, x: number, y: number): void {
      this.fallStrategy.update(layer,map, x, y);
    }

    constructor(falling: FallingState) {
      this.fallStrategy = new FallStrategy(falling);
    }

    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {
      this.fallStrategy.moveHorizontal(player, map, this, dx);
    }
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, "#8b4513");
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

    update(layer:Layer,map: GameMap, x: number, y: number): void {}

    moveVertical(player: Player, map: GameMap, dy: number): void {
      map.removeTile(this.lock);
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: GameMap, dx: number): void {
      map.removeTile(this.lock);
      player.move(map, dx, 0);
    }
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, this.color);
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
    update(layer:Layer,map: GameMap, x: number, y: number): void {}
    moveVertical(player: Player, map: GameMap, dy: number): void {}
    moveHorizontal(player: Player, map: GameMap, dx: number): void {}
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.drawRect(x, y, this.color);
    }

    isAir(): boolean {
      return false;
    }
  }
