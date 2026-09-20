import { describe, expect, test } from "vitest";
import { Queue, Deque } from "./task6";

// Запуск тестов: 
// cd OOAP1
// npm test -- task6.test.ts

describe("Queue, Deque вспомогательные тесты", () => {
    test("Queue", () => {
        const q = new Queue<number>();
        
        expect(q.is_empty()).toBe(true);

        q.add_tail(1)
        q.add_tail(2)
        q.add_tail(3)

        expect(q.is_empty()).toBe(false);

        expect(q.get_front()).toBe(1);

        q.remove_front()
        expect(q.get_front()).toBe(2);

        q.remove_front()
        expect(q.get_front()).toBe(3);   
        
        q.remove_front()
        expect(q.is_empty()).toBe(true);


    });

    test("Deque", () => {
        const q = new Deque<number>();
        
        expect(q.is_empty()).toBe(true);

        q.add_tail(1)
        q.add_tail(2)
        q.add_tail(3)
        q.add_tail(4)
        q.add_tail(5)

        expect(q.is_empty()).toBe(false);

        expect(q.get_front()).toBe(1);

        q.remove_front()
        expect(q.get_front()).toBe(2);

        q.remove_front()
        expect(q.get_front()).toBe(3);   
        
        expect(q.get_tail()).toBe(5); 

        q.remove_tail();
        expect(q.get_tail()).toBe(4); 

        q.remove_tail();
        expect(q.get_tail()).toBe(3); 

        q.remove_tail();
        expect(q.is_empty()).toBe(true);

    });

});