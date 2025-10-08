namespace App {
  const TILE_SIZE = 30;

  export class TileRenderer {
    private g: CanvasRenderingContext2D;
    canvas: HTMLCanvasElement;

    constructor(private html_canvas_element_id: string) {
      this.canvas = document.getElementById(
        html_canvas_element_id
      ) as HTMLCanvasElement;
      this.g = this.canvas.getContext("2d")!;
    }

    fillRect(x: number, y: number, color: string) {
      this.g.fillStyle = color;
      this.g.fillRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
    }

    clearСanvas() {
      this.g.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
  }
}
