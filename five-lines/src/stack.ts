export class Stack<T>
{
    private data: T[] = [];

    constructor(private makeEmpty: ()=>T)
    {

    }

    push(x: T) { this.data.push(x); }

    pop(): T
    {
        return this.data.length ? this.data.pop()! : this.makeEmpty();
    }

    peek(): T
    {
       return this.data.length ? this.data[this.data.length-1] : this.makeEmpty(); 
    }

    apply_function(fn:(v:T) => void): void
    {
        for(const val of this.data) fn(val);
    }

}