
  const TILE_SIZE = 30;

  const SVG_DOOR = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#1d4c07ff" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"> <rect x="5" y="2" width="14" height="20" rx="1.5" ry="1.5"/>
      <circle cx="15.5" cy="12" r="1.25" fill="currentColor"/> </svg>`;

  class ImgSVGCache {
    private cache = new globalThis.Map<string, HTMLImageElement>();

    getImg(svgMarkup: string): HTMLImageElement {
      const key = svgMarkup;
      const cached = this.cache.get(key);
      if (cached) return cached;

      const blob = new Blob([svgMarkup], { type: "image/svg+xml" });
      const url = URL.createObjectURL(blob);
      const img = new Image();

      img.onload = () => {
        URL.revokeObjectURL(url);
      };
      img.onerror = () => {
        URL.revokeObjectURL(url);
        console.error("Ошибка загрузки SVG");
      };

      img.src = url;
      this.cache.set(key, img);
      return img;
    }
  }

  export class TileRenderer {
    private g: CanvasRenderingContext2D;
    canvas: HTMLCanvasElement;
    private svgImgCache = new ImgSVGCache(); //Решение проблемы с мерцанием картинки

    constructor(private html_canvas_element_id: string) {
      this.canvas = document.getElementById(
        html_canvas_element_id
      ) as HTMLCanvasElement;
      this.g = this.canvas.getContext("2d")!;
    }

    drawRect(x: number, y: number, color: string) {
      this.g.fillStyle = color;
      this.g.fillRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
    }

    drawDoor(x: number, y: number) {
      this.drawRect(x, y, "#999999");
      this.g.drawImage(
        this.svgImgCache.getImg(SVG_DOOR),
        x * TILE_SIZE,
        y * TILE_SIZE,
        TILE_SIZE,
        TILE_SIZE
      );
    }

    clearСanvas() {
      this.g.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
  }

