// import { Position } from "./position.js";
// import { Cell } from "./map.js";

// export class Array2dCell {
//   private map: Cell[][];
//   private pos: WeakMap<Cell, { x: number; y: number }>;

//   constructor(private size_x: number, private size_y: number) {
//     this.pos = new WeakMap<Cell, { x: number; y: number }>();
//     this.map = new Array<Cell[]>(size_y);
//     for (let y = 0; y < size_y; y++) {
//       this.map[y] = new Array<Cell>(size_x);
//     }
//   }

//   setValue(p: Position, value: Cell): void {
//     let x = p.getX();
//     let y = p.getY();
//     this.map[y][x] = value;
//     this.pos.set(value, { x, y });
//   }

//   getValue(p: Position): Cell {
//     let x = p.getX();
//     let y = p.getY();    
//     return this.map[y][x];
//   }

//   change_value(value: Cell, new_value: Cell) {
//     const p = this.pos.get(value);
//     this.map[p!.y][p!.x] = new_value;
//     this.pos.set(new_value, p!);
//     this.pos.delete(value);
//   }

//   appleToAllCels(f: (value: Cell, p: Position) => void): void {
//     for (let y = 0; y < this.size_y; y++) {
//       for (let x = 0; x < this.size_x; x++) f(this.map[y][x], new Position(x,y));
//     }
//   }
// }
