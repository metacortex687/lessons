class Stack<T> {
    private _items: T[] = [];

    private _pop_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";
    private _peek_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";

    // Конструктор (по умолчанию):
    // постусловие: создана пустая очередь
    

    // Команды:

    // постусловие: добавлен элемент на вершину стека
    push(value: T): void {
        this._items.push(value);
    }

    // предусловие: стек не пустой
    // постусловие: удален элемент с вершины стека
    pop(): void {
        if(this.is_empty()) {
            this._pop_status = "ERR_EMPTY";
            return
        }

        this._pop_status = "OK";
        this._items.pop();
    }

    // Запросы:
    // предусловие: стек не пустой
    peek(): T | undefined {

        if(this.is_empty()) {
            this._peek_status = "ERR_EMPTY";
            return undefined;
        }

        this._pop_status = "OK";
        return this._items[this._items.length-1]
    }

    size(): number {
        return this._items.length;
    }

    is_empty(): boolean {
        return this.size() === 0;
    }

    // Запросы статусов

    get_pop_status() {
        return this._pop_status
    }

    get_peek_status() {
        return this._peek_status
    }

}


abstract class ParentQueue<T> {

    private _remove_front_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";
    private _get_front_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";
    
    protected _front_stack: Stack<T> = new Stack<T>();
    protected _tail_stack: Stack<T> = new Stack<T>();

    // Конструктор (по умолчанию):
    // постусловие: создана пустая очередь
    

    // Команды:

    // постусловие: элемент добавлен в хвост очереди
    public add_tail(value: T) : void 
    {
        this._tail_stack.push(value);
    }


    // предусловие: очередь не пуста
    // постусловие: элемент удален из головы очереди
    public remove_front() : void 
    {
        if(this.is_empty()) {
            this._remove_front_status = "ERR_EMPTY";
            return;
        }

        if(this._front_stack.is_empty()) {
            this._transfer_all(this._tail_stack, this._front_stack);
        }

        this._front_stack.pop();
    }

    // Запросы:

    // предусловие: очередь не пуста
    public get_front() : T | undefined {
        if(this.is_empty()) {
            this._get_front_status = "ERR_EMPTY";
            return undefined;
        }

        if(this._front_stack.is_empty()) {
            this._transfer_all(this._tail_stack, this._front_stack);
        }

        return this._front_stack.peek();

    }


    public is_empty():boolean {
        return this._front_stack.is_empty() && this._tail_stack.is_empty()
    }

    public size():number {
        return this._front_stack.size() + this._tail_stack.size()
    }  

    protected _transfer_all(
        source: Stack<T>,
        destinatio: Stack<T>
    ): void {
        while(!source.is_empty()) {
            destinatio.push(source.peek()!);
            source.pop();            
        }
    }

    //Запросы статусов:    
    public get_remove_front_status () {
        return this._remove_front_status;
    }

    public get_get_front_status () {
        return this._get_front_status;
    }

}


class Queue<T> extends ParentQueue<T> {
                
}


class Deque<T> extends ParentQueue<T> {
 
    private _remove_tail_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";
    private _get_tail_status: "NIL" | "OK" | "ERR_EMPTY" = "NIL";

    // Конструктор (по умолчанию):
    // постусловие: создана пустая очередь


    // Команды:

    // постусловие: элемент добавлен в голову очереди
    public add_front(value: T) : void 
    {
        this._front_stack.push(value);
    }

    // предусловие: очередь не пуста
    // постусловие: элемент удален из хвоста очереди
    public remove_tail() : void 
    {
        if(this.is_empty()) {
            this._remove_tail_status = "ERR_EMPTY";
            return;
        }

        if(this._tail_stack.is_empty()) {
            this._transfer_all(this._front_stack , this._tail_stack);
        }

        this._tail_stack.pop();
    }


    // Запросы:
    // предусловие: очередь не пуста
    public get_tail() : T | undefined {
        if(this.is_empty()) {
            this._get_tail_status = "ERR_EMPTY";
            return undefined;
        }

        if(this._tail_stack.is_empty()) {
            this._transfer_all(this._front_stack , this._tail_stack);
        }

        return this._tail_stack.peek();
    }

    //Запросы статусов:    
    public get_remove_tail_status () {
        return this._remove_tail_status;
    }

    public get_get_tail_status () {
        return this._get_tail_status;
    }

             
} 

export {Queue, Deque}