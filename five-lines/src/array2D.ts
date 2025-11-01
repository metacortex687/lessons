import { Position } from "./position.js";

export class Array2d<T> {
  private data: T[];

  constructor(
    private size_x: number,
    private size_y: number,
    private makeDefaultVal: () => T
  ) {
    this.data = new Array<T>(size_y * size_x);
    for (let i = 0; i < this.data.length; i++)
      this.data[i] = this.makeDefaultVal();
  }

  private index_xy(x: number, y: number) {
    return y * this.size_x + x;
  }

  private index_p(p: Position) {
    return this.index_xy(p.getX(),p.getY());
  }

  getValue_p(p: Position): T {
    return this.data[this.index_p(p)];
  }

  getValue_xy(x: number, y: number): T {
    return this.data[this.index_xy(x, y)];
  }

  setValue(v: T, p: Position) {
    this.data[this.index_p(p)] = v;
  }

  applyFn(fn:(x: number,y: number,v: T)=>void): void
  {
    for (let y = 0; y < this.size_y; y++)
      for (let x = 0; x < this.size_x; x++)
        fn(x,y,this.getValue_xy(x,y));
  }
}
