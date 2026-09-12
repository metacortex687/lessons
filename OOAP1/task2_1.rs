
// Статусы команд и запросов:
pub enum Status<E> {
    OK,
    Err(E),
}

pub enum StatusFind {
    OK,
    NotFind,
    Err(FindErr),
}


// Ошибки:
pub enum HeadErr {
    ListEmpty,
}

pub enum TailErr {
    ListEmpty,
}

pub enum RightErr {
    ListEmpty,
    CursorOnTail,
}

pub enum PutRightErr {
    ListEmpty,
}

pub enum PutLeftErr {
    ListEmpty,
}

pub enum RemoveErr {
    ListEmpty,
}

pub enum AddToEmptyErr {
    ListNotEmpty,
}

pub enum AddTailErr {
    ListEmpty,
}

pub enum ReplaceErr {
    ListEmpty,
}

pub enum FindErr {
    ListEmpty,
    CursorOnTail,
}

pub enum GetErr {
    ListEmpty,
}

pub enum IsHeadErr {
    ListEmpty,
}

pub enum IsTailErr {
    ListEmpty,
}

// Интерфейс

pub trait LinkedList<T> {
    // Конструктор:
	// постусловие: создан новый список
    fn new() -> Self;

	// предусловие: список не пустой;
    // постусловие: курсор на первом элементе в списке.  
 	fn head(&mut self) -> ((), Status<HeadErr>);

	// предусловие: список не пустой;
    // постусловие: курсор на последнем элементе в списке.  
	fn tail(&mut self) -> ((), Status<TailErr>);

	// предусловие: 
	// 	список не пустой;
	// 	курсор не в конце списка;
	// постусловие: курсор сдвинут вправо;	
	fn right(&mut self) -> ((), Status<RightErr>);

	// предусловие: список не пустой;
	// постусловие: 
	//     значение вставлено справа от курсора
	//     курсор на этом вставленном значении	
	fn put_right(&mut self, value: T) -> ((), Status<PutRightErr>);

	// предусловие: список не пустой;
	// постусловие: 
	//     значение вставлено слева от курсора
	//     курсор на этом вставленном значении
	fn put_left(&mut self, value: T) -> ((), Status<PutLeftErr>);

	// предусловие: список не пустой;
	// постусловие: 
	//     удален элемент на котором курсор;
	//     если курсор не на последнем элементе то курсор на элементе что был справа, иначе на элементе, что был слева;
	fn remove(&mut self) -> ((), Status<RemoveErr>);

    // постусловие: список пуст	
	fn clear(&mut self);

    // предусловие: список пуст;
    // постусловие: в списке один элемент; курсор на этом элементе; курсор одновременно и на начале и в конце списка;          
	fn add_to_empty(&mut self, value: T) -> ((), Status<AddToEmptyErr>);

    // предусловие: список не пустой;
    // постусловие: новый элемент в конце списка, курсор на новом элементе;     	
	fn add_tail(&mut self, value: T) -> ((), Status<AddTailErr>);

	// предусловие: список не пустой;
	// постусловие: новый элемент вместо того на котором был курсор; курсор на новом элементе;   	
	fn replace(&mut self, value: T) -> ((), Status<ReplaceErr>);


	// предусловие: 
	// 	список не пустой;
	// 	курсор не на последнем элементе;
	// постусловие: если элемент найден, курсор на первом вхождении элемента за исходной позицией курсора иначе элементе в конце списка; 
	fn find(&mut self, value: T) -> ((), StatusFind);


	// постусловие: в списке нет ни одного элемента равного удаляемому;  
	fn remove_all(&mut self, value: T);


	// Запросы:

	// предусловие: список не пустой; 
	fn get(&self) ->  -> (T, Status<GetErr>);	

	fn size(&self) -> usize;

	// предусловие: список не пустой; 
	fn is_head(&self) -> (bool, Status<IsHeadErr>);	

	// предусловие: список не пустой; 
	fn is_tail(&self) -> (bool, Status<IsTailErr>);	

	fn is_value(&self) -> bool;
}