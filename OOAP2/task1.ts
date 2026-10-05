abstract class Shape {
    public abstract area(): number;    
}

class Point {
    private _x: number;
    private _y: number;

    constructor (x:number, y: number) {
        this._x = x;
        this._y = y;
    }

    public get_x() {
        return this._x
    }

    public get_y() {
        return this._y
    }

}


class Circle extends Shape { //Наследование от Shape

    private _center: Point; //Композиция используются экземпляры класса Point
    private _radius: number;

    constructor(center: Point, radius: number) {
        super();
        this._center = center;
        this._radius = radius;
    }

    public area(): number {        
        return this._radius^2*Math.PI;
    }
} 


class Trianle extends Shape { //Наследование от Shape

    private _p1: Point; //Композиция используются экземпляры класса Point
    private _p2: Point; //Композиция используются экземпляры класса Point
    private _p3: Point; //Композиция используются экземпляры класса Point

    constructor(p1: Point, p2: Point, p3: Point) {
        super();
        this._p1 = p1;
        this._p2 = p2;
        this._p3 = p3;
    }

    public area(): number {
        let res = (this._p1.get_x()*(this._p2.get_y()-this._p3.get_y()) 
            + this._p2.get_x()*(this._p3.get_y()-this._p1.get_y()) 
            + this._p3.get_x()*(this._p1.get_y()-this._p2.get_y()));
        res = res/2;

        if(res < 0) {
            res = -res;
        }

        return res;
    }
} 


function area(shapes: Shape[]): number {
    let result = 0;
    for(const shape of shapes) {
        result += shape.area(); //Полиморфизм. Вызывается запрос area() для конкретного подкласса.
    }
    return result;
}

