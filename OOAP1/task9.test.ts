import { describe, expect, test } from "vitest";
import { PowerSet } from "./task9";

// Запуск тестов: 
// cd OOAP1
// npm test -- task9.test.ts

describe("PowerSet  тесты", () => {
    test("equals", () => {

        const a = new PowerSet<number>(3);
        const b = new PowerSet<number>(3);
        const c = new PowerSet<number>(3);

        a.put(1);
        a.put(2);

        b.put(2);
        b.put(1);

        c.put(1);
        c.put(3);

        expect(a.equals(b)).toBe(true);
        expect(b.equals(a)).toBe(true);


        expect(a.equals(c)).toBe(false);
        expect(c.equals(a)).toBe(false);

    });


    test("intersection", () => {

        const a = new PowerSet<number>(3);
        const b = new PowerSet<number>(3);


        a.put(1);
        a.put(2);
        a.put(3);

        b.put(2);
        b.put(3);
        b.put(4);

        const c = a.intersection(b);
        
        expect(c.count()).toBe(2);
        expect(c.get(2)).toBe(true);
        expect(c.get(3)).toBe(true);

    });


    test("union", () => {

        const a = new PowerSet<number>(3);
        const b = new PowerSet<number>(3);


        a.put(1);
        a.put(2);
        a.put(3);

        b.put(2);
        b.put(3);
        b.put(4);

        const c = a.union(b);
        
        expect(c.count()).toBe(4);
        expect(c.get(1)).toBe(true);
        expect(c.get(2)).toBe(true);
        expect(c.get(3)).toBe(true);
        expect(c.get(4)).toBe(true);

    });


    test("difference", () => {

        const a = new PowerSet<number>(3);
        const b = new PowerSet<number>(3);


        a.put(1);
        a.put(2);
        a.put(3);

        b.put(2);
        b.put(3);
        b.put(4);

        const c = a.difference(b);
        
        expect(c.count()).toBe(2);
        expect(c.get(1)).toBe(true);
        expect(c.get(4)).toBe(true);

    });


    test("is_subset", () => {

        const a = new PowerSet<number>(3);
        const b = new PowerSet<number>(3);


        a.put(1);
        a.put(2);
        a.put(3);

        b.put(2);
        b.put(3);
        b.put(4);


        
        expect(a.is_subset(b)).toBe(false);

        b.remove(4);
        expect(a.is_subset(b)).toBe(true);

    });


});
