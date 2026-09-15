import { describe, expect, test } from "vitest";
import { LinkedList, TwoWayList } from "./task3";


describe("ParentList вспомогательные тесты", () => {
    test("LinkedList", () => {
        const list = new LinkedList<number>();
        expect(list.is_value()).toBe(false);

        list.add_to_empty(10);
        expect(list.is_value()).toBe(true);
        expect(list.get()).toBe(10);

        list.put_right(15);
        expect(list.get()).toBe(15);
        expect(list.size()).toBe(2);

        list.head();
        expect(list.get()).toBe(10);

        list.remove();
        expect(list.get()).toBe(15);

        expect(list.get_remove_status()).toBe(LinkedList.REMOVE_OK);

    });

    test("TwoWayList", () => {
        const list = new TwoWayList<number>();
        expect(list.is_value()).toBe(false);

        list.add_to_empty(10);
        expect(list.is_value()).toBe(true);
        expect(list.get()).toBe(10);

        list.put_right(15);
        expect(list.get()).toBe(15);
        expect(list.size()).toBe(2);

        list.head();
        expect(list.get()).toBe(10);

        list.remove();
        expect(list.get()).toBe(15);

        expect(list.get_remove_status()).toBe(TwoWayList.REMOVE_OK);

    });

});

