import { describe, expect, test } from "vitest";
import { createHash } from "node:crypto";
import { HashTable, Hashable } from "./task7";

// Запуск тестов: 
// cd OOAP1
// npm test -- task7.test.ts

describe("HashTable вспомогательные тесты", () => {
    test("HashTable строки", () => {
        const ht = new HashTable<string>(5);
        
        expect(ht.is_empty()).toBe(true);
        expect(ht.capacity()).toBe(5);

        ht.put("q")

        expect(ht.is_empty()).toBe(false);
        expect(ht.count()).toBe(1);
        expect(ht.get_put_status()).toBe("OK");

        
        ht.put("qw")
        ht.put("qwe")
        ht.put("ewq")
        ht.put("qwert")

        expect(ht.count()).toBe(5);
        expect(ht.get_put_status()).toBe("OK");
        expect(ht.find("ewq")).toBe(true);
        expect(ht.find("ewq2")).toBe(false);


        ht.put("ewq2")
        expect(ht.get_put_status()).toBe("ERR_TABLE_FULL");
        expect(ht.count()).toBe(5);

        ht.remove("qwert");
        expect(ht.get_remove_status()).toBe("OK");
        expect(ht.count()).toBe(4);

        ht.remove("ewq2");
        expect(ht.get_remove_status()).toBe("ERR_NO_ELEMENT");
        expect(ht.count()).toBe(4);    

        ht.put("ewq2")
        expect(ht.get_put_status()).toBe("OK");
        expect(ht.count()).toBe(5);

        ht.clear();
        expect(ht.capacity()).toBe(5);
        expect(ht.count()).toBe(0);

    });


    test("HashTable для Hashable объекта", () => {
        const ht = new HashTable<CalendarEvent>(5);

        const o1 = new CalendarEvent("Встреча",1);
        const o2 = new CalendarEvent("Встреча",2);
        const o3 = new CalendarEvent("Встреча",1);

        ht.put(o1);        
        expect(ht.find(o1)).toBe(true);

        expect(ht.find(o2)).toBe(false);

        expect(ht.find(o3)).toBe(true);        


    });

});


class CalendarEvent extends Hashable {
    constructor(
        private readonly name: string,
        private readonly time: number
    ) {
        super();
    }

    public override hash(): string {
        return createHash("md5")
            .update(JSON.stringify([this.name, this.time]))
            .digest("hex");
    }

    public override equals(other: CalendarEvent): boolean {
        return this.name === other.name && this.time === other.time;
    }   
    

}

