package linkedlist


// Статусы команд и запросов:

type StatusHead int

const (
	HeadNil StatusHead = 0
	HeadOK StatusHead = 1
	HeadErrListEmpty StatusHead = 2
)


type StatusTail int

const (
	TailNil StatusTail = 0
	TailOK StatusTail = 1
	TailErrListEmpty StatusTail = 2
)


type StatusRight int

const (
	RightNil StatusRight = 0
	RightOK StatusRight = 1
	RightErrListEmpty StatusRight = 2
	RightErrCursorOnTail StatusRight = 3
)


type StatusPutRight int

const (
	PutRightNil StatusPutRight = 0
	PutRightOK StatusPutRight = 1
	PutRightErrListEmpty StatusPutRight = 2
)


type StatusPutLeft int

const (
	PutLeftNil StatusPutLeft = 0
	PutLeftOK StatusPutLeft = 1
	PutLeftErrListEmpty StatusPutLeft = 2
)


type StatusRemove int

const (
	RemovetNil StatusRemove = 0
	RemoveOK StatusRemove = 1
	RemoveErrListEmpty StatusRemove = 2
)


type StatusAddToEmpty int

const (
	AddToEmptyNil StatusRemove = 0
	AddToEmptyOK StatusRemove = 1
	AddToEmptyErrListNotEmpty StatusRemove = 2
)


type StatusAddTail int

const (
	AddTailNil StatusRemove = 0
	AddTailOK StatusRemove = 1
	AddTailErrListEmpty StatusRemove = 2
)


type StatusReplace int

const (
	ReplaceNil StatusReplace = 0
	ReplaceOK StatusReplace = 1
	ReplaceErrListEmpty StatusReplace = 2
)


type StatusFind int

const (
	FindNil StatusFind = 0
	FindOK StatusFind = 1
	FindNot StatusFind = 2
	FindErrListEmpty StatusFind = 3
	FindErrCursorOnTail StatusFind = 4
)


type StatusGet int

const (
	GetNil StatusGet = 0
	GetOK StatusGet = 1
	GetErrListEmpty StatusGet = 2
)


type StatusIsHead int

const (
	IsHeadNil StatusIsHead = 0
	IsHeadOK StatusIsHead = 1
	IsHeadErrListEmpty StatusIsHead = 2
)


type StatusIsTail int

const (
	IsTailNil StatusIsTail = 0
	IsTailOK StatusIsTail = 1
	IsTailErrListEmpty StatusIsTail = 2
)


// Интерфейс:

type LinkedList[T any] interface {

	// Конструктор:
	// постусловие: создан новый список
	New() LinkedList[T]

	
	// Команды:

	// предусловие: список не пустой;
	// постусловие: курсор на первом узле в списке.    
	Head()

	// предусловие: список не пустой;
    // постусловие: курсор на последнем узле в списке.  
	Tail()

	// предусловие: 
	// 	список не пустой;
	// 	курсор не в конце списка;
	// постусловие: курсор сдвинут вправо;	
	Right()

	// предусловие: список не пустой;
	// постусловие: 
	//     значение вставлено справа от курсора
	//     курсор на этом вставленном значении	
	PutRight(value T)

	// предусловие: список не пустой;
	// постусловие: 
	//     значение вставлено слева от курсора
	//     курсор на этом вставленном значении
	PutLeft(value T)

	// предусловие: список не пустой;
	// постусловие: 
	//     удален элемент на котором курсор;
	//     если курсор не на последнем элементе то курсор на элементе что был справа, иначе на элементе, что был слева;
	Remove()

    // постусловие: список пуст	
	Clear()

    // предусловие: список пуст;
    // постусловие: в списке один элемент; курсор на этом элементе; курсор одновременно и на начале и в конце списка;          
	AddToEmpty(value T)

    // предусловие: список не пустой;
    // постусловие: новый элемент в конце списка, курсор на новом элементе;     	
	AddTail()

	// предусловие: список не пустой;
	// постусловие: новый элемент вместо того на котором был курсор; курсор на новом элементе;   	
	Replace()


	// предусловие: 
	// 	список не пустой;
	// 	курсор не на последнем элементе;
	// постусловие: если элемент найден, курсор на первом вхождении элемента за исходной позицией курсора иначе элементе в конце списка; 
	Find()


	// постусловие: в списке нет ни одного элемента равного удаляемому;  
	RemoveAll(value T)	


	// Запросы:


	// предусловие: список не пустой; 
	Get() T	

	Size() int

	// предусловие: список не пустой; 
	IsHead() bool

	// предусловие: список не пустой; 
	IsTail() bool	

	IsValue() bool


	// Дополнительные запросы:

	GetHeadStatus() StatusHead
	GetTailStatus() StatusTail
	GetPutRightStatus() StatusPutRight
	GetPutLeftStatus() StatusPutLeft
	GetRemoveStatus() StatusRemove
	GetAddToEmptyStatus() StatusAddToEmpty
	GetAddTailStatus() StatusAddTail
	GetReplaceStatus() StatusReplace
	GetFindStatus() StatusFind
	GetGetStatus() StatusGet
	GetIsHeadStatus() StatusIsHead
	GetIsTailStatus() StatusIsTail
	
}








