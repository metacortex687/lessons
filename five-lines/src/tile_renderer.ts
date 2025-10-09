namespace App {
  const TILE_SIZE = 30;

  const SVG_DOOR = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"> <rect x="5" y="2" width="14" height="20" rx="1.5" ry="1.5"/>
      <circle cx="15.5" cy="12" r="1.25" fill="currentColor"/> </svg>`;

  export class TileRenderer {
    private g: CanvasRenderingContext2D;
    canvas: HTMLCanvasElement;
    private svgImgCache = new globalThis.Map<string, HTMLImageElement>();

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

    drawDoor(x: number, y: number) {
      const color = "#1d4c07ff";
      const colored = SVG_DOOR.replace(/fill="[^"]*"/g, `fill="${color}"`);
      this.fillRect(x, y, "#999999");
      this.drawSvgString(colored, x, y);
    }

    private drawSvgString(svgMarkup: string, x: number, y: number) {
      // 1) быстрый путь: картинка уже есть
      const cached = this.svgImgCache.get(svgMarkup);
      if (cached && cached.complete) {
        this.g.drawImage(
          cached,
          x * TILE_SIZE,
          y * TILE_SIZE,
          TILE_SIZE,
          TILE_SIZE
        );
        return;
      }

      // 2) грузим один раз и кладём в кеш
      const blob = new Blob([svgMarkup], { type: "image/svg+xml" });
      const url = URL.createObjectURL(blob);
      const img = new Image();
      // необязательно, но иногда помогает браузеру:
      // (не во всех движках влияет, но не мешает)
      (img as any).decoding = "sync";

      img.onload = () => {
        this.svgImgCache.set(svgMarkup, img);
        this.g.drawImage(
          img,
          x * TILE_SIZE,
          y * TILE_SIZE,
          TILE_SIZE,
          TILE_SIZE
        );
        URL.revokeObjectURL(url);
      };
      img.src = url;
    }

    clearСanvas() {
      this.g.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
  }
}
