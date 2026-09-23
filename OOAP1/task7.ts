
type PutStatus = "NIL" | "OK" | "ERR_TABLE_FULL";
type RemoveStatus = "NIL" | "OK" | "ERR_NO_ELEMENT";

// Здесь хранится ключ значение
class StringHashTable<T extends string | number| Hashable > {

    private _array:Array<T | undefined | null>;
    private _count: number;

    private _put_status: PutStatus = "NIL";
    private _remove_status: RemoveStatus = "NIL";

    // Конструктор:
    // постусловие: создана пустая хэш-таблица
    constructor(size: number) {
        this._array = new Array<T | undefined | null>(size); 
        this._count = 0; 
    }

    // Команды:

    // предусловие: есть свободный слот или элемент уже содержится в таблице
    // постусловие: добавлен или обновлен элемент
    public put(key: string, value: T): void {
        const index = this._seek_slot(key, value);

        if (index === undefined) {
            this._put_status =  "ERR_TABLE_FULL";
            return;
        }

        if(this._array[index] !== value) {
            this._count++;
        }

        this._put_status = "OK";
        this._array[index] = value;

    }


    // предусловие: элемент есть в хэш таблице
    // постусловие: удален элемент из таблицы
    public remove(key: string, value: T): void {
        const index = this._seek_slot(key, value);

        if (index === undefined || this._array[index] === undefined) {
            this._remove_status = "ERR_NO_ELEMENT";
            return;
        }

        this._count--;
        this._remove_status = "OK";    
        this._array[index] = null;        
    }

    // постусловие: таблица пуста
    public clear() {
        this._count = 0;
        this._array = new Array<T | undefined | null>(this.capacity());;
    }

    // Запросы:

    public find(key: string, value: T): boolean {
        let start_index = this._key_to_number(key) % this.capacity();

        for (let i = 0; i < this.capacity(); i++)
        {
            const index = (start_index+i) % this.capacity();

            if(this._array[index] === undefined) {
                return false;
            } 

            if(this._array[index] === null) {
                continue;
            } 

            if(this._equals(this._array[index],value)) {
                return true;
            }
        }

        return false;

    }


    public count(): number {
        return this._count;
    }

    is_empty(): boolean {
        return this.count() === 0;
    } //не уверен в названии

    public capacity(): number {
        return this._array.length;
    }

    *[Symbol.iterator](): IterableIterator<T> {
        for (const value of this._array) {
            if( value === undefined || value === null) {
                continue;
            }
            yield value;
        }
    }

    // Дополнительные запросы статусов

    get_put_status(): PutStatus {
        return this._put_status;
    }

    get_remove_status(): RemoveStatus {
        return this._remove_status;
    }


    // приватные методы
    private _key_to_number(key: string): number {
        const r  = 31;
        const p  = 1000_000_007;

        let res = 0;

        for (const char of key) {
            const code = char.codePointAt(0)!;
            res = (res*r + code) % p;
        }

        return res;
    } 

    private _seek_slot(key: string, value: T): number | undefined {
        let start_index = this._key_to_number(key) % this.capacity();

        for (let i = 0; i < this.capacity(); i++)
        {
            const index = (start_index+i) % this.capacity();

            if(this._array[index] === undefined || this._array[index] === null || this._equals(this._array[index],value)) {
                return index
            }
        }

        return undefined;
    } 

    private _equals(a: T, b: T): boolean {
        if(typeof a === "string" || typeof b === "string") {
            return a === b
        }

        if(typeof a === "number" || typeof b === "number") {
            return a === b
        }

        return a.equals(b);
    }


}

abstract class Hashable {
    abstract hash(): string;
    abstract equals(other: Hashable): boolean;
}

class HashTable<T extends string | number | Hashable> {
    private  _hash_table: StringHashTable<T>;

    // Конструктор:
    // постусловие: создана пустая хэш-таблица
    constructor(size: number) {
       this._hash_table = new StringHashTable<T>(size);
    }   


    //Команды:
    
    // предусловие: есть свободный слот или элемент уже содержится в таблице
    // постусловие: добавлен или обновлен элемент
    public put(value: T): void {
        if (typeof value === "string") {
            this._hash_table.put(value, value);
        }
        else if (typeof value === "number") {
            this._hash_table.put(String(value), value);
        }
        else {
            this._hash_table.put(value.hash(), value);
        }
    }

    // предусловие: элемент есть в хэш таблице
    // постусловие: удален элемент из таблицы
    public remove(value: T): void {
        if (typeof value === "string") {
            return this._hash_table.remove(value, value);
        }
        else if (typeof value === "number") {
            this._hash_table.remove(String(value), value);
        }
        else {
            return this._hash_table.remove(value.hash(), value);
        }
    }

    // постусловие: таблица пуста
    public clear() {
        this._hash_table.clear();
    }


    // Запросы:

    public find(value: T): boolean {
        if (typeof value === "string") {
            return this._hash_table.find(value, value);
        }
        else if (typeof value === "number") {
            return this._hash_table.find(String(value), value);
        }
        else {
            return this._hash_table.find(value.hash(), value);
        }
    }

    public count(): number {
        return this._hash_table.count();
    }

    public is_empty(): boolean {
        return this._hash_table.is_empty();
    }  

    public capacity(): number {
        return this._hash_table.capacity();
    }

    *[Symbol.iterator](): IterableIterator<T> {
        for (const value of this._hash_table) {
            yield value;
        }
    }


    // Дополнительные запросы статусов

    public get_put_status(): PutStatus {
        return this._hash_table.get_put_status();
    }

    public get_remove_status(): RemoveStatus {
        return this._hash_table.get_remove_status();
    }

}


export {HashTable, Hashable}