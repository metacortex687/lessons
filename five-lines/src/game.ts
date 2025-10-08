namespace App {
  interface FallingState {
    drop(map: Map, y: number, x: number): void;
    moveHorizontal(player: Player, map: Map, tile: Tile, dx: number): void;
  }

  class Falling implements FallingState {
    drop(map: Map, y: number, x: number): void {
      map.drop(x, y);
    }
    moveHorizontal(player: Player, map: Map, tile: Tile, dx: number): void {}
  }

  class FallStrategy {
    moveHorizontal(player: Player, map: Map, tile: Tile, dx: number) {
      this.falling.moveHorizontal(player, map, tile, dx);
    }
    private falling: FallingState;

    constructor(falling: FallingState) {
      this.falling = falling;
    }

    update(map: Map, x: number, y: number): void {
      this.drop(map, y, x);
    }

    private drop(map: Map, y: number, x: number) {
      this.falling = map.getBlockOnTopState(x, y + 1);

      this.falling.drop(map, y, x);
    }
  }

  class Resting implements FallingState {
    drop(map: Map, y: number, x: number): void {}
    moveHorizontal(player: Player, map: Map, tile: Tile, dx: number): void {
      player.pushHorisontal(map, tile, dx);
    }
  }

  interface RawTileValue {
    transform(): Tile;
  }
  class AirValue implements RawTileValue {
    transform(): Tile {
      return new Air();
    }
  }
  class FluxValue implements RawTileValue {
    transform(): Tile {
      return new Flux();
    }
  }
  class UnbreakableValue implements RawTileValue {
    transform(): Tile {
      return new Unbreakable();
    }
  }
  class PlayerValue implements RawTileValue {
    transform(): Tile {
      return new PlayerTile();
    }
  }
  class StoneValue implements RawTileValue {
    transform(): Tile {
      return new Stone(new Resting());
    }
  }
  class FallingStoneValue implements RawTileValue {
    transform(): Tile {
      return new Stone(new Falling());
    }
  }
  class BoxValue implements RawTileValue {
    transform(): Tile {
      return new Box(new Resting());
    }
  }
  class FallingBoxValue implements RawTileValue {
    transform(): Tile {
      return new Box(new Falling());
    }
  }
  class Key1Value implements RawTileValue {
    transform(): Tile {
      return YELLOW_KEY_LOCK_FACTORY.createKey();
    }
  }
  class Lock1Value implements RawTileValue {
    transform(): Tile {
      return YELLOW_KEY_LOCK_FACTORY.createLock();
    }
  }
  class Key2Value implements RawTileValue {
    transform(): Tile {
      return BLUE_KEY_LOCK_FACTORY.createKey();
    }
  }
  class Lock2Value implements RawTileValue {
    transform(): Tile {
      return BLUE_KEY_LOCK_FACTORY.createLock();
    }
  }

  class RawTile {
    transform(): Tile {
      return this.value.transform();
    }
    static readonly AIR = new RawTile(new AirValue());
    static readonly FLUX = new RawTile(new FluxValue());
    static readonly UNBREAKABLE = new RawTile(new UnbreakableValue());
    static readonly PLAYER = new RawTile(new PlayerValue());
    static readonly STONE = new RawTile(new StoneValue());
    static readonly FALLING_STONE = new RawTile(new FallingStoneValue());
    static readonly BOX = new RawTile(new BoxValue());
    static readonly FALLING_BOX = new RawTile(new FallingBoxValue());
    static readonly KEY1 = new RawTile(new Key1Value());
    static readonly LOCK1 = new RawTile(new Lock1Value());
    static readonly KEY2 = new RawTile(new Key2Value());
    static readonly LOCK2 = new RawTile(new Lock2Value());

    private constructor(private value: RawTileValue) {}
  }

  const RAW_TILES = [
    RawTile.AIR,
    RawTile.FLUX,
    RawTile.UNBREAKABLE,
    RawTile.PLAYER,
    RawTile.STONE,
    RawTile.FALLING_STONE,
    RawTile.BOX,
    RawTile.FALLING_BOX,
    RawTile.KEY1,
    RawTile.LOCK1,
    RawTile.KEY2,
    RawTile.LOCK2,
  ];

  interface Tile {
    getBlockOnTopState(): FallingState;
    update(map: Map, x: number, y: number): void;

    moveVertical(player: Player, map: Map, dy: number): void;
    moveHorizontal(player: Player, map: Map, dx: number): void;
    draw(tr: TileRenderer, x: number, y: number): void;
    isAir(): boolean;
  }

  class Flux implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    update(map: Map, x: number, y: number): void {}

    moveVertical(player: Player, map: Map, dy: number): void {
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: Map, dx: number): void {
      player.move(map, dx, 0);
    }

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, "#ccffcc");
    }

    isAir(): boolean {
      return false;
    }

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
  }

  class Unbreakable implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    update(map: Map, x: number, y: number): void {}

    moveVertical(player: Player, map: Map, dy: number): void {}
    moveHorizontal(player: Player, map: Map, dx: number): void {}

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, "#999999");
    }

    isAir(): boolean {
      return false;
    }

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
  }

  class Stone implements Tile {
    private falling: FallingState;

    constructor(falling: FallingState) {
      this.fallStrategy = new FallStrategy(falling);
      this.falling = falling;
    }
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    private fallStrategy: FallStrategy;

    update(map: Map, x: number, y: number): void {
      this.fallStrategy.update(map, x, y);
    }

    moveVertical(player: Player, map: Map, dy: number): void {}
    moveHorizontal(player: Player, map: Map, dx: number): void {
      this.falling.moveHorizontal(player, map, this, dx);
    }

    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, "#0000cc");
    }
    isAir(): boolean {
      return false;
    }

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
  }

  class Air implements Tile {
    getBlockOnTopState(): FallingState {
      return new Falling();
    }
    update(map: Map, x: number, y: number): void {}

    moveVertical(player: Player, map: Map, dy: number): void {
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: Map, dx: number): void {
      player.move(map, dx, 0);
    }

    draw(tr: TileRenderer, x: number, y: number): void {}

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
    isAir(): boolean {
      return true;
    }
  }

  class PlayerTile implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    update(map: Map, x: number, y: number): void {}

    moveVertical(player: Player, map: Map, dy: number): void {}
    moveHorizontal(player: Player, map: Map, dx: number): void {}

    draw(tr: TileRenderer, x: number, y: number): void {}

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
    isAir(): boolean {
      return false;
    }
  }

  class Box implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    private fallStrategy: FallStrategy;

    update(map: Map, x: number, y: number): void {
      this.fallStrategy.update(map, x, y);
    }

    constructor(falling: FallingState) {
      this.fallStrategy = new FallStrategy(falling);
    }

    moveVertical(player: Player, map: Map, dy: number): void {}
    moveHorizontal(player: Player, map: Map, dx: number): void {
      this.fallStrategy.moveHorizontal(player, map, this, dx);
    }
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, "#8b4513");
    }

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
    isAir(): boolean {
      return false;
    }
  }

  class Key implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    constructor(private lock: LockTile, private color: string) {}

    update(map: Map, x: number, y: number): void {}

    moveVertical(player: Player, map: Map, dy: number): void {
      map.removeTile(this.lock);
      player.move(map, 0, dy);
    }
    moveHorizontal(player: Player, map: Map, dx: number): void {
      map.removeTile(this.lock);
      player.move(map, dx, 0);
    }
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, this.color);
    }

    isLock1(): boolean {
      return false;
    }
    isLock2(): boolean {
      return false;
    }
    isAir(): boolean {
      return false;
    }
  }

  class KeyLockFactory {
    private key: Key;
    private lock: LockTile;

    constructor(private color: string) {
      this.lock = new LockTile(this.color);
      this.key = new Key(this.lock, this.color);
    }

    createKey(): Tile {
      return this.key;
    }

    createLock(): Tile {
      return this.lock;
    }
  }

  class LockTile implements Tile {
    getBlockOnTopState(): FallingState {
      return new Resting();
    }
    constructor(private color: string) {}
    update(map: Map, x: number, y: number): void {}
    moveVertical(player: Player, map: Map, dy: number): void {}
    moveHorizontal(player: Player, map: Map, dx: number): void {}
    draw(tr: TileRenderer, x: number, y: number): void {
      tr.fillRect(x, y, this.color);
    }

    isAir(): boolean {
      return false;
    }
  }

  const YELLOW_KEY_LOCK_FACTORY = new KeyLockFactory("#ffcc00");
  const BLUE_KEY_LOCK_FACTORY = new KeyLockFactory("#00ccff");

  export class Player {
    constructor(private x: number, private y: number) {}

    pushHorisontal(map: Map, tile: Tile, dx: number) {
      map.pushHorisontal(this, tile, this.x, this.y, dx);
    }
    draw(tr: TileRenderer) {
      tr.fillRect(this.x, this.y, "#ff0000");
    }

    moveHorizontal(map: Map, dx: number) {
      map.moveHorizontal(this, this.x, this.y, dx);
    }

    moveVertical(map: Map, dy: number) {
      map.moveVertical(this, this.x, this.y, dy);
    }

    move(map: Map, dx: number, dy: number) {
      this.moveToTile(map, this.x + dx, this.y + dy);
    }

    moveToTile(map: Map, newx: number, newy: number) {
      map.moveToTile(this.x, this.y, newx, newy);
      this.x = newx;
      this.y = newy;
    }
  }

  let rawMap: number[][] = [
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 3, 0, 1, 1, 2, 0, 2],
    [2, 4, 2, 6, 1, 2, 0, 2],
    [2, 8, 4, 1, 1, 2, 0, 2],
    [2, 4, 1, 1, 1, 9, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
  ];

  export class Map {
    private map!: Tile[][];
    constructor() {
      this.load_data();
    }

    private load_data() {
      this.map = new Array(rawMap.length);
      for (let y = 0; y < rawMap.length; y++) {
        this.map[y] = new Array(rawMap[y].length);
        for (let x = 0; x < rawMap[y].length; x++) {
          this.map[y][x] = RAW_TILES[rawMap[y][x]].transform();
        }
      }
    }

    isAir(y: number, x: number) {
      return this.map[y][x].isAir();
    }

    removeTile(tile: Tile) {
      for (let y = 0; y < this.map.length; y++) {
        for (let x = 0; x < this.map[y].length; x++) {
          if (this.map[y][x] === tile) {
            this.map[y][x] = new Air();
          }
        }
      }
    }

    getBlockOnTopState(x: number, y: number) {
      return this.map[y][x].getBlockOnTopState();
    }

    drop(x: number, y: number): void {
      this.map[y + 1][x] = this.map[y][x];
      this.map[y][x] = new Air();
    }

    draw(tr: TileRenderer) {
      for (let y = 0; y < this.map.length; y++) {
        for (let x = 0; x < this.map[y].length; x++) {
          this.map[y][x].draw(tr, x, y);
        }
      }
    }

    moveHorizontal(player: Player, x: number, y: number, dx: number) {
      this.map[y][x + dx].moveHorizontal(player, this, dx);
    }

    moveVertical(player: Player, x: number, y: number, dy: number) {
      this.map[y + dy][x].moveVertical(player, this, dy);
    }

    moveToTile(x: number, y: number, newx: number, newy: number) {
      this.map[y][x] = new Air();
      this.map[newy][newx] = new PlayerTile();
    }

    pushHorisontal(
      player: Player,
      tile: Tile,
      x: number,
      y: number,
      dx: number
    ) {
      if (this.isAir(y, x + dx + dx) && !this.isAir(y + 1, x + dx)) {
        this.map[y][x + dx + dx] = tile;
        player.moveToTile(this, x + dx, y);
      }
    }

    update() {
      for (let y = this.map.length - 1; y >= 0; y--)
        for (let x = 0; x < this.map[y].length; x++)
          this.map[y][x].update(this, x, y);
    }
  }

  export class Game {
    private player: Player;
    private map: Map;

    constructor() {
      this.map = new Map();
      this.player = new Player(1, 1);
    }

    update(inputs: Inputs) {
      this.handleInputs(inputs);
      this.map.update();
    }

    handleInputs(inputs: Inputs) {
      while (!inputs.is_empty()) {
        let current = inputs.pop()!;
        current.handle(this.player, this.map);
      }
    }

    draw(tr: TileRenderer) {
      tr.clearСanvas();
      this.map.draw(tr);
      this.player.draw(tr);
    }
  }
}
