export class Position {
  constructor(private x: number, private y: number) {}

  getX() {
    return this.x;
  }

  getY() {
    return this.y;
  }
}

export interface Move {
  translate(pos: Position): Position;
}

export class MoveUp implements Move {
  translate(pos: Position): Position {
    return new Position(pos.getX(), pos.getY() - 1);
  }
}

export class MoveDown implements Move {
  translate(pos: Position): Position {
    return new Position(pos.getX(), pos.getY() + 1);
  }
}

export class MoveLeft implements Move {
  translate(pos: Position): Position {
    return new Position(pos.getX() - 1, pos.getY());
  }
}

export class MoveRight implements Move {
  translate(pos: Position): Position {
    return new Position(pos.getX() + 1, pos.getY());
  }
}
