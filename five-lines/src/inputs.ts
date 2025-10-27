import { GameMap } from "./map.js";
import { Player } from "./player.js";
import { PlayerMoverVertical, PlayerMoverHorizontal } from "./player.js";
import {
  DirectionDown,
  DirectionUp,
  DirectionLeft,
  DirectionRight,
} from "./position.js";

interface Input {
  handle(player: Player, map: GameMap): void;
}

class Right implements Input {
  handle(player: Player, map: GameMap) {
    player.tryEnterTile(map, new PlayerMoverHorizontal(new DirectionRight()));
  }
}

class Left implements Input {
  handle(player: Player, map: GameMap) {
    player.tryEnterTile(map, new PlayerMoverHorizontal(new DirectionLeft()));
  }
}

class Up implements Input {
  handle(player: Player, map: GameMap) {
    player.tryEnterTile(map, new PlayerMoverVertical(new DirectionUp()));
  }
}

class Down implements Input {
  handle(player: Player, map: GameMap) {
    player.tryEnterTile(map, new PlayerMoverVertical(new DirectionDown()));
  }
}

interface RawInputValue {
  transform(): Input;
}
class UpValue implements RawInputValue {
  transform(): Input {
    return new Up();
  }
}
class DownValue implements RawInputValue {
  transform(): Input {
    return new Down();
  }
}

class LeftValue implements RawInputValue {
  transform(): Input {
    return new Left();
  }
}

class RightValue implements RawInputValue {
  transform(): Input {
    return new Right();
  }
}

class RawInput {
  transform(): Input {
    return this.value.transform();
  }
  static readonly UP = new RawInput(new UpValue());
  static readonly DOWN = new RawInput(new DownValue());
  static readonly LEFT = new RawInput(new LeftValue());
  static readonly RIGHT = new RawInput(new RightValue());

  private constructor(private value: RawInputValue) {}
}

export class Inputs {
  readonly RawInputs: Record<string, RawInput> = {
    a: RawInput.LEFT,
    w: RawInput.UP,
    d: RawInput.RIGHT,
    s: RawInput.DOWN,
    ArrowLeft: RawInput.LEFT,
    ArrowUp: RawInput.UP,
    ArrowRight: RawInput.RIGHT,
    ArrowDown: RawInput.DOWN,
  };

  private inputs: Input[];

  constructor() {
    this.inputs = [];
  }

  is_empty() {
    return this.inputs.length == 0;
  }

  pop() {
    return this.inputs.pop();
  }

  push(key: string) {
    this.inputs.push(this.RawInputs[key].transform());
  }
}
