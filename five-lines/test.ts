class BatchProcessor {

  constructor(private processor: ElementProcessor) {
  }
  process(arr: number[]) {
    for (let i = 0; i < arr.length; i++) this.processor.processElement(arr[i]);

    return this.processor.getAccumulator();
  }

}

interface ElementProcessor {
  processElement(e: number): void;
  getAccumulator(): number;
}

class MinimumProcessor implements ElementProcessor{
  processElement(e: number) {
    if (this.accumulator > e) this.accumulator = e;
  }
  constructor(private accumulator: number) {}
  getAccumulator() {
    return this.accumulator;
  }
}


class SumProcessor implements ElementProcessor {
  processElement(e: number) {
    this.accumulator += e;
  }
  constructor(private accumulator: number) {}
  getAccumulator() {
    return this.accumulator;
  }
}
