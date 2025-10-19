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

  setValue(x: number, y: number, value: T): void {
    this.map[y][x] = value;
    this.pos.set(value, { x, y })
  }

  getValue(x: number, y: number): T {
    return this.map[y][x];
  }

  removeTile(tile: T, new_tile: T) {
    const p = this.pos.get(tile);
    this.map[p!.y][p!.x] = new_tile;
    this.pos.set(new_tile,p!);
    this.pos.delete(tile);
  }
}
