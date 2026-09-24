import { describe, expect, test } from "vitest";
import { NativeDictionary } from "./task8";
import { Random } from "random";


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

    test("Воспроизведение ошибки, когда не освобождается слот для записи", () => {

        const d = new NativeDictionary<string>(200);

        const chars: string[] = []
        for(let i = 27; i <= 122; i ++) {
            chars.push(String.fromCodePoint(i));
        }

        for(const ch of chars) {
            d.set(ch, `${ch}!`);
            expect(d.is_key(ch)).toBe(true);
        }

        const shuffle_chars = new Random(15).shuffle(chars);

        for(let i = 0; i < 15; i ++) {
            const ch = shuffle_chars.pop()!;
            expect(d.is_key(ch)).toBe(true); 
            d.remove(ch);  
            expect(d.is_key(ch)).toBe(false);          
        }

        for(const ch of shuffle_chars) {
            expect(d.is_key(ch), `символ ${ch}`).toBe(true);
        }


    });





});

