// черновик, не решение

pub trait DynArrayTrait<T> {
    // Конструктор
    // Предусловие:
    // capacity > 0
    // постусловие:
    // Создан пустой динамический массив
    fn new(capacity: usize = 16, capacity_calculator: CapacityCalculatorTrait = MultiplicativeCapacityCalculator()) -> Self;

    // команды

    // индекс границы элементов
    fn size() -> usize;

    

    fn set(index: usize);

    

    fn remove(index: usize);

    fn insert(index: usize);

    // предусловие:
    // массив не должен быть пустым
    fn remove_last();

    fn append(value: T);


    // запросы
    fn get(index: usize) -> &T;

    fn capacity() -> usize;

}

pub trait CapacityCalculatorTrait {
    
}

pub trait AdditiveCapacityCalculatorTrait: CapacityCalculatorTrait {

}

pub trait MultiplicativeCapacityCalculatorTrait: CapacityCalculatorTrait {

}

pub trait BankersMethodCapacityCalculatorTrait: CapacityCalculatorTrait {

}


// реализация MultiplicativeCapacityCalculatorTrait
pub struct MultiplicativeCapacityCalculator {

}

impl CapacityCalculatorTrait for MultiplicativeCapacityCalculator {

}

impl MultiplicativeCapacityCalculatorTrait for MultiplicativeCapacityCalculator {

}





