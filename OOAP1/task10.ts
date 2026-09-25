abstract class Hashable {
    abstract hash(): string;
}


class BloomFilter<T extends string | Hashable> {

    private _bit_count: number;
    private _bits:number;

    private readonly HASH_BASE_1 = 17;
    private readonly HASH_BASE_2 = 223;


    // Конструктор:
    // постусловие: создан пустой фильтр Блума
    constructor(bit_count: number) {
        this._bit_count = bit_count;
        this._bits = 0;
    }

    // Команды:

    // постусловие: значение отмечено в фильтре
    put(value: T): void {
        const hash_of_value = this._hash(value);
        this._set_bit_on(this._hash_to_bit_index(hash_of_value,this.HASH_BASE_1))
        this._set_bit_on(this._hash_to_bit_index(hash_of_value,this.HASH_BASE_2))
    }

    // постусловие: фильтр очищен
    clear() {
        this._bits = 0;
    }

    // Запросы:

    get(value: T): boolean {
        const hash_of_value = this._hash(value);
        return this._get_bit(this._hash_to_bit_index(hash_of_value,this.HASH_BASE_1)) 
            && this._get_bit(this._hash_to_bit_index(hash_of_value,this.HASH_BASE_2)); 
    }



    // Приватные методы
    private _hash_to_bit_index(hash:string, hash_base: number): number {
        let result: number = 0;

        for(let ch of hash) {
            const code = ch.codePointAt(0)!;
            result = (result*hash_base + code) % this._bit_count;
        }

        return result;
    }

    private _set_bit_on(bit_index:number):void {
        this._bits |= (1 << bit_index);
    }

    private _get_bit(bit_index:number):boolean {
        return (this._bits & (1 << bit_index)) !== 0;
    }

    private _hash(value: T) {
        if(typeof value === "string") {
            return value;
        }

        return value.hash();
    }

}

export {Hashable, BloomFilter}