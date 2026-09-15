export {};

abstract class ParentNode<T> {
    private _value: T | null;
         
    protected constructor(value:T | null = null) {
        this._value = value;
    }

    // команды
    // предусловие 
    public replace(value: T) {
        this._value = value;
    }

    // Запросы        
    public is_value(): boolean {
        return this._value !== null;
    }
    // предусловие:
    // Узел имеет значение (не dummy)  
    public value(): T {
        return this._value!;
    }

    public abstract get_right_node():ParentNode<T>;

}

class RightWayNode<T> extends ParentNode<T> {

    private _right!: RightWayNode<T>;

    // команды

    // предусловие:
    // справа уже есть узел, со значением или dummy
    // постусловие:
    // между этим узлом и узлом справа добавлен новый узел
    public put_right(value: T): void {
        const node = new RightWayNode<T>(value);
        node._right = this._right;
        this._right = node;
    }

    // предусловие:
    // справа уже есть узел, и этот узел не dummy
    // постусловие:
    // узел справа удален
    public remove_right_node() {
        this._right = this._right._right;
    }

    // запросы 

    // предусловие:
    // справа уже есть узел, со значением или dummy
    public get_right_node(): RightWayNode<T> {
        return this._right;
    }



    //фабричные методы:
    public static create_linked_dummy_head_tail_pair<T>(): [RightWayNode<T>, RightWayNode<T>] {
        const head = new RightWayNode<T>();
        const tail = new RightWayNode<T>();
        head._right = tail;
        return [head, tail];
    }



}

class TwoWayNode<T> extends ParentNode<T> {

    private _right!: TwoWayNode<T>;
    private _left!: TwoWayNode<T>;

    // команды

    // предусловие:
    // справа уже есть узел, со значением или dummy
    // постусловие:
    // между текущим узлом и узлом справа добавлен новый узел
    public put_right(value: T): void {
        const node = new TwoWayNode<T>(value);
        node._right = this._right;
        node._left = this;
        this._right._left = node;
        this._right = node;
    }

    // предусловие:
    // это не dummy узел
    // постусловие:
    // элемент слева и элемент справа ссылаются друг на друга, что опривдет к удалению текущего элемента 
    remove_links() {
        this._left._right = this._right;
        this._right._left = this._left;
    }

    // предусловие:
    // слева уже есть узел, со значением или dummy
    // постусловие:
    // между текущим узлом и узлом слева добавлен новый узел
    public put_left(value: T): void {
        const node = new TwoWayNode<T>(value);
        node._left = this._left;
        node._right = this;
        this._left._right = node;
        this._left = node;
    }


    // запросы 

    // предусловие:
    // справа уже есть узел, со значением или dummy
    public get_right_node(): TwoWayNode<T> {
        return this._right;
    } 

    // предусловие:
    // справа уже есть узел, со значением или dummy
    public get_left_node(): TwoWayNode<T> {
        return this._right;
    }  

    // фабричны методы
    public static create_linked_dummy_head_tail_pair<T>(): [TwoWayNode<T>, TwoWayNode<T>] {
        const head = new TwoWayNode<T>();
        const tail = new TwoWayNode<T>();
        head._right = tail;
        tail._left  = head;
        return [head, tail]
    }

}


abstract class ParentList<T, N extends ParentNode<T>> {
    public static readonly HEAD_NIL = 0;
    public static readonly HEAD_OK = 1;
    public static readonly HEAD_ERR_LIST_EMPTY = 2;

    public static readonly TAIL_NIL = 0;
    public static readonly TAIL_OK = 1;
    public static readonly TAIL_ERR_LIST_EMPTY = 2;

    public static readonly REPLACE_NIL = 0;
    public static readonly REPLACE_OK = 1;
    public static readonly REPLACE_ERR_LIST_EMPTY = 2; 
    
    public static readonly ADD_TO_EMPTY_NIL = 0;
    public static readonly ADD_TO_EMPTY_OK = 1;
    public static readonly ADD_TO_EMPTY_ERR_LIST_NOT_EMPTY = 2;  

    public static readonly REMOVE_NIL = 0;
    public static readonly REMOVE_OK = 1;
    public static readonly REMOVE_ERR_LIST_EMPTY = 2; 

    public static readonly GET_NIL = 0;
    public static readonly GET_OK = 1;
    public static readonly GET_ERR_LIST_EMPTY = 2;  

    private _head_status = ParentList.HEAD_NIL;
    private _tail_status = ParentList.TAIL_NIL;
    private _replace_status = ParentList.REPLACE_NIL;
    protected _add_to_empty_status = ParentList.ADD_TO_EMPTY_NIL;
    protected _remove_status = ParentList.REMOVE_NIL;
    private _get_status = ParentList.GET_NIL;


    declare protected _head: N;
    declare protected _tail: N;
    declare protected _left_dummy: N;
    declare protected _right_dummy: N;

    declare protected _cursor: N | null;
    private _create_linked_dummy_head_tail_pair: () => [N, N];

    // конструктор
    // постусловие: создан новый пустой список
    protected constructor(create_linked_dummy_head_tail_pair : () => [N, N]) {
        this._create_linked_dummy_head_tail_pair = create_linked_dummy_head_tail_pair;
        this.clear();              
    }

    // Команды
    // предусловие: список не пуст; (HEAD_ERR_LIST_EMPTY)
    // постусловие: курсор установлен на первый узел в списке
    public head(): void {
        if(!this.is_value()) {
            this._head_status = ParentList.HEAD_ERR_LIST_EMPTY;
            return;
        }
        this._cursor = this._head;
        this._head_status = ParentList.HEAD_OK;
    }

    // предусловие: список не пуст; 
    // постусловие: курсор установлен на последний узел в списке
    public tail(): void {
        if(!this.is_value()) {
            this._tail_status = ParentList.TAIL_ERR_LIST_EMPTY;
            return;
        }
        this._cursor = this._tail;
        this._tail_status = ParentList.TAIL_OK;
    }

    // постусловие: список очищен от всех элементов
    public clear() {
        [this._head, this._tail] = this._create_linked_dummy_head_tail_pair();
        this._cursor = null;
    }

    // предусловие:
    // список не пустой
    public replace(value: T) {
        if(!this.is_value()) {
            this._tail_status = ParentList.REPLACE_ERR_LIST_EMPTY;
            return;
        }

        this._cursor!.replace(value);
        this._replace_status = ParentList.REPLACE_OK;
    }

    // предусловие: список пуст; 
    // постусловие: в списке один узел
    public abstract add_to_empty(value: T): void;

    // предусловие: список не пуст; 
    // постусловие: текущий узел удалён, 
    // курсор смещён к правому соседу, если он есть, 
    // в противном случае курсор смещён к левому соседу,
    // если он есть
    public abstract remove(): void;

    // Запросы
    public is_value(): boolean {
        return this._head.is_value()
    }

    // предусловие: список не пуст
    public get(): T | null {
       if(!this.is_value()) {
            this._get_status = ParentList.GET_ERR_LIST_EMPTY;
            return null;
        }    

        this._get_status = ParentList.GET_OK;

        return this._cursor!.value();
    }

    public is_head(): boolean {
        if(!this.is_value()) {
            return false
        }

        return this._cursor === this._head;
    }

    public is_tail(): boolean {
        if(!this.is_value()) {
            return false
        }

        return this._cursor === this._tail;
    }

    public size(): number {
        if(!this._head.is_value()) {
            return 0;
        }

        let count = 0;
        let cursor: ParentNode<T> = this._head;

        while(cursor.is_value()) {
            count +=1;
            cursor = cursor.get_right_node();
        }
        return count;
    }

    // запросы статусов


    public get_head_status():number {
        return this._head_status
    }

    public get_tail_status():number {
        return this._tail_status
    }

    public get_replace_status():number {
        return this._replace_status
    }

    public get_add_to_empty_status():number {
        return this._add_to_empty_status
    }

    public get_remove_status():number {
        return this._remove_status
    }

    public get_get_status():number {
        return this._get_status
    }

} 


class LinkedList<T> extends ParentList<T, RightWayNode<T>> {

    public static readonly PUT_RIGHT_NIL = 0;
    public static readonly PUT_RIGHT_OK = 1;
    public static readonly PUT_RIGHT_ERR_LIST_EMPTY = 2;  

    public static readonly RIGHT_NIL = 0;
    public static readonly RIGHT_OK = 1;
    public static readonly RIGHT_ERR_LIST_EMPTY = 2; 
    public static readonly RIGHT_ERR_IS_TAIL = 2; 

    private _put_right_status = LinkedList.PUT_RIGHT_NIL;
    private _right_status = LinkedList.RIGHT_NIL;



    // констурктор создан пустой список
    public constructor() {
        super(RightWayNode.create_linked_dummy_head_tail_pair)
    }


    // команды

    // предусловие: список не пуст; 
    // постусловие: следом за текущим узлом добавлен 
    // новый узел с заданным значением  
    public put_right(value: T): void {
        if(!this.is_value()) {
            this._put_right_status = LinkedList.PUT_RIGHT_ERR_LIST_EMPTY;
            return
        }



        this._cursor!.put_right(value)
        const right_node = this._cursor!.get_right_node();

        if(this._tail === this._cursor) {
            this._tail = right_node;
        } 

        this._cursor = right_node;   
        
        this._put_right_status = LinkedList.PUT_RIGHT_OK;
    } 

    // предусловие: списко не пуст; курсор не на последнем элементе; 
    // постусловие: курсор сдвинут на один узел вправо   
    public right(): void {
        if(!this.is_value()) {
            this._right_status = LinkedList.RIGHT_ERR_LIST_EMPTY;
            return
        }
        if(this._cursor === this._tail) {
            this._right_status = LinkedList.RIGHT_ERR_IS_TAIL;
            return
        }
        this._right_status = LinkedList.RIGHT_OK;


        this._cursor = this._cursor!.get_right_node();                
    }

    // предусловие: список пуст; 
    // постусловие: в списке один узел
    public override add_to_empty(value: T): void{
        if(this.is_value()) {
            this._add_to_empty_status = LinkedList.ADD_TO_EMPTY_ERR_LIST_NOT_EMPTY;
            return
        }
        this._add_to_empty_status = LinkedList.ADD_TO_EMPTY_OK;

        this._left_dummy = this._head;
        this._right_dummy = this._tail;


        this._head.put_right(value);
        this._cursor = this._head.get_right_node();
        this._head = this._cursor;
        this._tail = this._cursor;

        
    }   

    // O(N) !!!!
    // предусловие: список не пуст; 
    // постусловие: текущий узел удалён, 
    // курсор смещён к правому соседу, если он есть, 
    // в противном случае курсор смещён к левому соседу,
    // если он есть
    public override remove(): void {
        if(!this.is_value()) {
            this._remove_status = LinkedList.REMOVE_ERR_LIST_EMPTY;
            return
        }

        this._remove_status = LinkedList.REMOVE_OK;

        if(this.is_head() && this.size() === 1) {
            this.clear();
            return;
        }

        if(this.is_head()) {
            this._left_dummy.remove_right_node();
            this._head = this._left_dummy.get_right_node();
            this._cursor = this._head;
            return;
        }
        
        let prev_cursor = this._head;
        let cursor = prev_cursor.get_right_node();

        while(cursor !== this._cursor) {
            prev_cursor = cursor;
            cursor = prev_cursor.get_right_node();
        }

        prev_cursor.remove_right_node(); 

        if(this._tail === prev_cursor) {
            this._cursor = prev_cursor; 
            return           
        }

        this._cursor = prev_cursor.get_right_node();      
        

    }

    // постусловие: новый узел добавлен в хвост списка
    public add_tail(value: T): void {
        if(!this.is_value()) {
            this.add_to_empty(value);
            return;
        }

        this._tail.put_right(value);
        this._tail = this._tail.get_right_node();        
    }

    // постусловие: в списке удалены все узлы с заданным значением
    public remove_all(value: T): void {
        
        let prev_cursor = this._head;
        let cursor = prev_cursor.get_right_node();

        while(true) {
            if(cursor === this._tail) {
                break;
            }

            if(cursor.value() === value) {
                prev_cursor.remove_right_node();
                cursor = prev_cursor.get_right_node();
                continue;                
            } 
 
            prev_cursor = cursor;
            cursor = prev_cursor.get_right_node();
        }

    } 

    // постусловие: курсор установлен на следующий узел 
    // с искомым значением, если такой узел найден
    public find(value: T) {
        if(!this.is_value()) { //список пуст
            return;
        }

        let next_node = this._cursor!.get_right_node();
        while(next_node.is_value()) {
            if(next_node.value() === value) {
                this._cursor = next_node;
                return 
            }; 
            next_node = next_node.get_right_node();
        }
    }

    // запросы статусов
    public get_put_right_status():number {
        return this._put_right_status
    }

    public get_right_status():number {
        return this._right_status
    }

}

class TwoWayList<T> extends ParentList<T, TwoWayNode<T>> {

    public static readonly PUT_RIGHT_NIL = 0;
    public static readonly PUT_RIGHT_OK = 1;
    public static readonly PUT_RIGHT_ERR_LIST_EMPTY = 2;  

    public static readonly RIGHT_NIL = 0;
    public static readonly RIGHT_OK = 1;
    public static readonly RIGHT_ERR_LIST_EMPTY = 2; 
    public static readonly RIGHT_ERR_IS_TAIL = 2; 

    public static readonly PUT_LEFT_NIL = 0;
    public static readonly PUT_LEFT_OK = 1;
    public static readonly PUT_LEFT_ERR_LIST_EMPTY = 2;  

    public static readonly LEFT_NIL = 0;
    public static readonly LEFT_OK = 1;
    public static readonly LEFT_ERR_LIST_EMPTY = 2; 
    public static readonly LEFT_ERR_IS_TAIL = 2; 

    private _put_right_status = LinkedList.PUT_RIGHT_NIL;
    private _right_status = LinkedList.RIGHT_NIL;
    private _put_left_status = LinkedList.PUT_RIGHT_NIL;
    private _left_status = LinkedList.RIGHT_NIL;


    public constructor() {
        super(TwoWayNode.create_linked_dummy_head_tail_pair)
    }

    // предусловие: список не пуст; 
    // постусловие: следом за текущим узлом добавлен 
    // новый узел с заданным значением  
    public put_right(value: T): void {

        if(!this.is_value()) {
            this._put_right_status = TwoWayList.PUT_RIGHT_ERR_LIST_EMPTY;
            return
        }

        this._cursor!.put_right(value)
        const right_node = this._cursor!.get_right_node();

        if(this._tail === this._cursor) {
            this._tail = right_node;
        } 
        
        this._cursor = right_node; 
        
        this._put_right_status = TwoWayList.PUT_RIGHT_OK;
    } 

    // предусловие: правее курсора есть элемент; 
    // постусловие: курсор сдвинут на один узел вправо   
    public right(): void {
        if(!this.is_value()) {
            this._right_status = TwoWayList.RIGHT_ERR_LIST_EMPTY;
            return
        }
        if(this._cursor === this._tail) {
            this._right_status = TwoWayList.RIGHT_ERR_IS_TAIL;
            return
        }
        this._right_status = TwoWayList.RIGHT_OK;

        this._cursor = this._cursor!.get_right_node();                
    }

    // предусловие: список не пуст; 
    // постусловие: следом за текущим узлом добавлен 
    // новый узел с заданным значением  
    public put_left(value: T): void {
        if(!this.is_value()) {
            this._put_right_status = TwoWayList.PUT_LEFT_ERR_LIST_EMPTY;
            return
        }
        this._put_right_status = TwoWayList.PUT_LEFT_OK;

        this._cursor!.put_left(value)

        const left_node = this._cursor!.get_right_node();
        if(this._head === this._cursor) {
            this._head = left_node;
        } 

        this._cursor = this._cursor!.get_left_node()           
    } 

    // предусловие: левее курсора есть элемент; 
    // постусловие: курсор сдвинут на один узел влево   
    public left(): void {
        if(!this.is_value()) {
            this._left_status = TwoWayList.LEFT_ERR_LIST_EMPTY;
            return
        }
        if(this._cursor === this._tail) {
            this._left_status = TwoWayList.LEFT_ERR_IS_TAIL;
            return
        }
        this._left_status = TwoWayList.LEFT_OK;

        
        this._cursor = this._cursor!.get_left_node();                
    }   

    // предусловие: список пуст; 
    // постусловие: в списке один узел 
    public override add_to_empty(value: T): void{
        if(this.is_value()) {
            this._add_to_empty_status = TwoWayList.ADD_TO_EMPTY_ERR_LIST_NOT_EMPTY;
            return
        }
        this._add_to_empty_status = TwoWayList.ADD_TO_EMPTY_OK;

        this._left_dummy = this._head;
        this._right_dummy = this._tail;

        this._head.put_right(value);
        this._cursor = this._head.get_right_node();
        this._head = this._cursor;
        this._tail = this._cursor;
    }

    // постусловие: новый узел добавлен в хвост списка
    public add_tail(value: T): void {
        this._tail.put_right(value);
        this._tail = this._tail.get_right_node();        
    }

    // предусловие: список не пуст; 
    // постусловие: текущий узел удалён, 
    // курсор смещён к правому соседу, если он есть, 
    // в противном случае курсор смещён к левому соседу,
    // если он есть
    public override remove(): void {
        if(!this.is_value()) {
            this._remove_status = TwoWayList.REMOVE_ERR_LIST_EMPTY;
            return
        }
        this._remove_status = TwoWayList.REMOVE_OK;




        if(!this._head.get_right_node().is_value()) { //один элемент 
            this.clear();
            return;
        }
                
        let left_node = this._cursor!.get_left_node()
        let right_node = this._cursor!.get_right_node()

        this._cursor!.remove_links(); 
        
        if(this._cursor === this._tail) {
            this._cursor = left_node;
            this._tail = this._cursor;
            return;
        }

        this._cursor = right_node;
    }

    // постусловие: в списке удалены все узлы с заданным значением
    public remove_all(value: T): void {

        let cursor = this._head;

        while(true) {
            if(cursor.value() === value) {
                cursor.remove_links();                
            }

            if(cursor.value() === value && cursor === this._tail) {
                                                                             
            }            


            if(cursor === this._tail) {
                break;
            }
        }

    }  
    
    // постусловие: курсор установлен на следующий узел 
    // с искомым значением, если такой узел найден
    public find(value: T) {
        if(!this.is_value()) { //список пуст
            return;
        }

        let next_node = this._cursor!.get_right_node();
        while(next_node.is_value()) {
            if(next_node.value() === value) {
                this._cursor = next_node;
                return 
            }; 
            next_node = next_node.get_right_node();
        }
    }

    // запросы статусов
    public get_put_right_status():number {
        return this._put_right_status
    }

    public get_right_status():number {
        return this._right_status
    }

    public get_put_left_status():number {
        return this._put_left_status
    }

    public get_left_status():number {
        return this._left_status
    }
    
}

export {LinkedList, TwoWayList}





