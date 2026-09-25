import { describe, expect, test } from "vitest";
import { BloomFilter } from "./task10";

// Запуск тестов: 
// cd OOAP1
// npm test -- task10.test.ts

describe("BloomFilter  тесты", () => {
    test("тестирование на выборке оптимального размера, не должно быть ложно отрицательных", () => {
        const filter = new BloomFilter(32);

        const values = ["1-a","2-b","3-c","4-d","5-e","6-f","7-g","8-h","9-j","10-k"];

        for(const value of values) {
            filter.put(value);
        }

        for(const value of values) {
            expect(filter.get(value)).toBe(true);
        }                          

    });


});
