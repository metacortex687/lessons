
import {TileRenderer} from "./tile_renderer.js";
import { type Tile } from "./tiles.js";
import { Air, EmptyGround, Garden, Flux, 
  Unbreakable, PlayerTile, Stone, Resting, Falling,
  Box, KeyLockBundle, Door} from "./tiles.js";
import { Player } from "./player.js";


  interface RawTileValue {
    transform(): Tile;
  }
  class AirValue implements RawTileValue {
    transform(): Tile {
      return new Air(new EmptyGround());
    }
  }
  class GardenValue implements RawTileValue {
    transform(): Tile {
      return new Air(new Garden());
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
      return YELLOW_KEY_LOCK_FACTORY.key();
    }
  }
  class Lock1Value implements RawTileValue {
    transform(): Tile {
      return YELLOW_KEY_LOCK_FACTORY.lock();
    }
  }
  class Key2Value implements RawTileValue {
    transform(): Tile {
      return BLUE_KEY_LOCK_FACTORY.key();
    }
  }
  class Lock2Value implements RawTileValue {
    transform(): Tile {
      return BLUE_KEY_LOCK_FACTORY.lock();
    }
  }

  class DoorValue implements RawTileValue {
    transform(): Tile {
      return new Door();
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
    static readonly DOOR = new RawTile(new DoorValue());
    static readonly GARDEN = new RawTile(new GardenValue());

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
    RawTile.DOOR,
    RawTile.GARDEN,
  ];


  const YELLOW_KEY_LOCK_FACTORY = new KeyLockBundle("#ffcc00");
  const BLUE_KEY_LOCK_FACTORY = new KeyLockBundle("#00ccff");

  let rawMap: number[][] = [
    [2, 2, 2, 2, 2, 2, 12, 2],
    [2, 3, 0, 13, 1, 2, 0, 2],
    [2, 4, 2, 6, 1, 2, 0, 2],
    [2, 8, 4, 1, 1, 2, 0, 2],
    [2, 4, 1, 1, 1, 9, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
  ];

  export class GameMap {
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
            this.map[y][x] = new Air(new EmptyGround());
          }
        }
      }
    }

    getBlockOnTopState(x: number, y: number) {
      return this.map[y][x].getBlockOnTopState();
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

    moveTileTo(x: number, y: number, newx: number, newy: number) {
      this.map[newy][newx] = this.map[y][x];
      this.map[y][x] = new Air(new EmptyGround());
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

