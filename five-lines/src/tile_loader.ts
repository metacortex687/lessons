import { type Tile } from "./tiles.js";
import { Array2d } from "./array2D.js";

import {
  Air,
  EmptyGround,
  Garden,
  Flux,
  Unbreakable,
  PlayerTile,
  Stone,
  Resting,
  Falling,
  Box,
  KeyLockBundle,
  Door,
} from "./tiles.js";

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

export class NumberToTileTransformer {
  transform(i: number): Tile {
    return RAW_TILES[i].transform();
  }

  load_tile_array_2D(size_x: number, size_y: number, rawMap: number[][]) {
    let map = new Array2d<Tile>(size_x,size_y);
    for (let y = 0; y < size_y; y++) {
      for (let x = 0; x < size_x; x++) {
        map.setValue(x,y,this.transform(rawMap[y][x]));
      }
    } 
    
    return map;

  }
}
