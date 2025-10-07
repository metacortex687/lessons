namespace App {
  interface Input {
    handle(player: Player, map: Map): void;
  }

  class Right implements Input {
    handle(player: Player, map: Map) {
      player.moveHorizontal(map, 1);
    }
  }

  class Left implements Input {
    handle(player: Player, map: Map) {
      player.moveHorizontal(map, -1);
    }
  }

  class Up implements Input {
    handle(player: Player, map: Map) {
      player.moveVertical(map, -1);
    }
  }

  class Down implements Input {
    handle(player: Player, map: Map) {
      player.moveVertical(map, 1);
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

    public inputs: Input[];

    constructor() {
      this.inputs = [];
    }

    getInputs() {
      return this.inputs;
    }

    is_empty() {
      return inputs.getInputs().length == 0;
    }

    pop() {
      return this.inputs.pop();
    }

    push(key: string) {
      this.inputs.push(this.RawInputs[key].transform());
    }
  }
}
