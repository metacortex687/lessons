
class NativeDictionary<T> {
    private _count: number;
    private _capacity:number;
    private _array_values:Array<T | undefined>;
    private _array_keys:Array<string | undefined | null>;

    private _status_set: "NIL" | "OK" | "ERR" = "NIL";
    private _status_remove: "NIL" | "OK" | "ERR" = "NIL";
    private _status_get: "NIL" | "OK" | "ERR" = "NIL";

    // Конструктор:
    // инициализирует ассоциативный словарь указанной вместимости
    constructor(capacity: number) {
        this._count = 0;
        this._capacity = capacity;

        this._array_keys = new Array<string | undefined | null>(this._capacity);
        this._array_values = new Array<T | undefined>(this._capacity);

    }

    // Команды:
    // предусловие: в словаре есть меcто для ключа 
    // постусловие: добавлен или обновлен элемент
    set(key:string, value: T): void {
        if(!this.can_set(key)) {
            this._status_set = "ERR";
            return;
        }

        const index = this._seek_slot(key)!;

        if(this._array_values[index] === undefined) {
            this._count++;
        }

        this._status_set = "OK";
        this._array_keys[index] = key;
        this._array_values[index] = value;        
    }

    // предусловие: в словаре есть значение с этим ключом
    // постусловие: значение с указанным ключом удалено
    remove(key:string): void {
        if(!this.is_key(key)) {
            this._status_remove = "ERR";
            return
        };

        this._status_remove = "OK";

        this._count--;

        const index = this._seek_slot(key)!;
        this._array_keys[index] = null;
        this._array_values[index] = undefined; 

    }

    // постулови: ассоциативный словарь пуст
    clear(): void {
        this._count = 0;

        this._array_keys = new Array<string | undefined | null>(this._capacity);
        this._array_values = new Array<T | undefined>(this._capacity);
    }


    // Запросы:

    // предусловие: в словаре есть значение с этим ключом
    // постусловие: значение с указанным ключом удалено
    get(key:string): T | undefined {
        if(!this.is_key(key)) {
            this._status_get = "ERR";
            return undefined;
        };

        this._status_get = "OK";

        const index = this._seek_slot(key)!;
        return this._array_values[index];

    }    
    
    is_key(key: string): boolean {
        const index = this._seek_slot(key);

        if(index === undefined) {
            return false;
        }

        return true;

    }

    can_set(key: string): boolean {
        if(this.is_key(key)) {
            return true
        }

        return this.count() < this.capacity();
    }
    
    count(): number {
        return this._count;
    }

    capacity(): number {
        return this._capacity;
    }

    is_empty(): boolean {
        return this.count() === 0;
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

    private _seek_slot(key: string): number | undefined {
        let start_index = this._key_to_number(key) % this.capacity();

        for (let i = 0; i < this.capacity(); i++)
        {
            const index = (start_index+i) % this.capacity();
            if(this._array_keys[index] === undefined || this._array_keys[index] === key) {
                return index
            }
        }

        return undefined;
    } 


    // Вспомогательные методы получения статусов команд:

    get_get_status() {
        return this._status_get;
    }

    get_remove_status() {
        return this._status_remove;
    }

    get_set_status() {
        return this._status_set;
    }

}

export {NativeDictionary}