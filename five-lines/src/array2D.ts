import { Position } from "./position.js";

export class Array2d<T extends object> {
  private map: T[][];
  private pos: WeakMap<T, { x: number; y: number }>;

  constructor(private size_x: number, private size_y: number) {
    this.pos = new WeakMap<T, { x: number; y: number }>();
    this.map = new Array<T[]>(size_y);
    for (let y = 0; y < size_y; y++) {
      this.map[y] = new Array<T>(size_x);
    }
  }

  setValue(p: Position, value: T): void {
    let x = p.getX();
    let y = p.getY();
    this.map[y][x] = value;
    this.pos.set(value, { x, y });
  }

  getValue(p: Position): T {
    let x = p.getX();
    let y = p.getY();    
    return this.map[y][x];
  }

  change_value(value: T, new_value: T) {
    const p = this.pos.get(value);
    this.map[p!.y][p!.x] = new_value;
    this.pos.set(new_value, p!);
    this.pos.delete(value);
  }

  appleToAllCels(f: (value: T, p: Position) => void): void {
    for (let y = 0; y < this.size_y; y++) {
      for (let x = 0; x < this.size_x; x++) f(this.map[y][x], new Position(x,y));
    }
  }
}
