export class Position {
  constructor(private x: number, private y: number) {}

  getX() {
    return this.x;
  }

  getY() {
    return this.y;
  }

  up() : Position
  {
     return new Position(this.x, this.y - 1); 
  }

  down() : Position
  {
     return new Position(this.x, this.y + 1); 
  }

  left() : Position
  {
    return new Position(this.x - 1, this.y);  
  }

  right() : Position
  {
    return new Position(this.x + 1, this.y);  
  }

  moved(m: Move)
  {
    return m.translate(this);
  }

}

export interface Move {
  translate(pos: Position): Position;
}

export class MoveUp implements Move {
  translate(pos: Position): Position {
    return pos.up();    
  }
}

export class MoveDown implements Move {
  translate(pos: Position): Position {
    return pos.down();
  }
}

export class MoveLeft implements Move {
  translate(pos: Position): Position {
    return pos.left();
  }
}

export class MoveRight implements Move {
  translate(pos: Position): Position {
    return pos.right();
  }
}
