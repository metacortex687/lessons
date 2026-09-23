import { describe, expect, test } from "vitest";
import { NativeDictionary } from "./task8";

// Запуск тестов: 
// cd OOAP1
// npm test -- task8.test.ts

describe("NativeDictionary вспомогательные тесты", () => {
    test("NativeDictionary", () => {

        const d = new NativeDictionary<string>(3);
        
        expect(d.is_empty()).toBe(true);
        expect(d.capacity()).toBe(3);

        d.set("a","A")
        d.set("b","B")
        d.set("c","C")

        expect(d.is_empty()).toBe(false);
        expect(d.count()).toBe(3);
        expect(d.get("b")).toBe("B");
        expect(d.get_get_status()).toBe("OK");



        d.get("d");
        expect(d.get_get_status()).toBe("ERR");

        expect(d.can_set("c")).toBe(true);
        expect(d.can_set("d")).toBe(false);

        d.set("c","C!")
        expect(d.count()).toBe(3);

    });

});

