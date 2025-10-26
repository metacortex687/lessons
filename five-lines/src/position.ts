export class Position {
  constructor(private x: number, private y: number) {}

  getX() {
    return this.x;
  }

  getY() {
    return this.y;
  }

  up(): Position {
    return new Position(this.x, this.y - 1);
  }

  down(): Position {
    return new Position(this.x, this.y + 1);
  }

  left(): Position {
    return new Position(this.x - 1, this.y);
  }

  right(): Position {
    return new Position(this.x + 1, this.y);
  }

  moved(d: Direction) {
    return d.move(this);
  }
}

export interface Direction {
  move(pos: Position): Position;
}

export class DirectionUp implements Direction {
  move(pos: Position): Position {
    return pos.up();
  }
}

export class DirectionDown implements Direction {
  move(pos: Position): Position {
    return pos.down();
  }
}

export class DirectionLeft implements Direction {
  move(pos: Position): Position {
    return pos.left();
  }
}

export class DirectionRight implements Direction {
  move(pos: Position): Position {
    return pos.right();
  }
}
