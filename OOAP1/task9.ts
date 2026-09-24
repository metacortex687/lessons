import { HashTable, Hashable } from "./task7";

class PowerSet<T extends string | number | Hashable> {
    private _hash_table: HashTable<T>;

    // Конструктор:
    // инициализировано пустое множество указанной вместимости
    constructor(capacity: number) {
        this._hash_table = new HashTable<T>(capacity);
    }

    // Команды:
    // предусловие: в словаре есть меcто для ключа 
    // постусловие: добавлен или обновлен элемент
    put(value: T) {
        this._hash_table.put(value)
    }



    // предусловие: в словаре есть значение с этим ключом
    // постусловие: значение с указанным ключом удалено
    remove(value: T) {
        this._hash_table.remove(value);
    } 


    // Запросы:

    get(value: T): boolean {
        return this._hash_table.find(value);
    }


    intersection(other: PowerSet<T>): PowerSet<T> {
        const c = new PowerSet<T>(Math.min(this.capacity(),other.capacity()));

        for(const value of other) {
            if(this.get(value)) {
                c.put(value);
            }
        }

        return c;

    }

    union(other: PowerSet<T>): PowerSet<T> {

        const c = new PowerSet<T>(this.capacity() + other.capacity());

        for(const value of this) {
            c.put(value);
        }
        for(const value of other) {
            c.put(value);
        }

        return c;
    }


    difference(other: PowerSet<T>): PowerSet<T> {

        const c = new PowerSet<T>(this.capacity() + other.capacity());

        for(const value of this) {
            if(!other.get(value)) {
                c.put(value);
            }
        }

        for(const value of other) {
            if(!this.get(value)) {
                c.put(value);
            }
        }

        return c;

    }

    is_subset(other: PowerSet<T>): boolean {

        for(const value of other) {
            if(!this.get(value)) {
                return false;
            }
        }

        return true;

    }

    equals(other: PowerSet<T>): boolean {
        if(this.count() !== other.count()) {
            return false
        }

        for(const value of other) {
            if(!this.get(value)) {
                return false;
            }
        }

        return true;

    }
    

    count(): number {
        return this._hash_table.count();
    }

    capacity(): number {
        return this._hash_table.capacity();
    }   

    is_empty(): boolean {
        return this._hash_table.is_empty()
    } 

    *[Symbol.iterator](): IterableIterator<T> {
        for (const value of this._hash_table) {
            yield value;
        }
    }


    // Вспомогательные методы получения статусов команд:

    get_put_status() {
        return this._hash_table.get_put_status();
    }

    get_remove_status() {
        return this._hash_table.get_remove_status();
    }

}



export {PowerSet}