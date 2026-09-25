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

    test("оценка доли ложно положительных", () => {
        // тест может ломаться, тогда надо увеличивать размер выборки no_input_values
        const filter = new BloomFilter(32);

        const input_values = ["1-a","2-b","3-c","4-d","5-e","6-f","7-g","8-h","9-j","10-k"];
        const no_input_values = ["1-a*","2-b*","3-c*","4-d*","5-e*","6-f*","7-g*","8-h*","9-j*","10-k*"];

        for(const value of input_values) {
            filter.put(value);
        }

        let count_true = 0;
        for(const value of no_input_values) {
            if(filter.get(value)) {
                count_true++;
            }       
        }  
        const percent = count_true/no_input_values.length;
        expect(percent).lessThan(0.7);                        

    });


});
