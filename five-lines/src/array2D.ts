export class Array2d<T> {
  private map: T[][];
  constructor(private size_x: number, private size_y: number) {
    this.map = new Array<T[]>(size_y);
    for (let y = 0; y < size_y; y++) {
      this.map[y] = new Array<T>(size_x);
    }
  }

  setValue(x: number, y: number, value: T): void {
    this.map[y][x] = value;
  }

  getValue(x: number, y: number): T {
    return this.map[y][x];
  }

  removeTile(tile: T, new_tile: T) {
    for (let y = 0; y < this.map.length; y++) {
      for (let x = 0; x < this.map[y].length; x++) {
        if (this.map[y][x] === tile) {
          this.map[y][x] = new_tile;
        }
      }
    }
  }
}
