package linkedlist

type node[T any] struct {
	value T
	right *node[T]	
}

type linkedList[T any] struct {
	head *node[T]
	tail *node[T]
	cursor *node[T]

	is_empty bool

	headStatus StatusHead
	tailStatus StatusTail
	putRightStatus StatusPutRight
	putLeftStatus StatusPutLeft
}

// New implements [LinkedList].
func New[T any]() LinkedList[T] {
	return &linkedList[T]{
		is_empty: true,
		headStatus: HeadNil,
		tailStatus: TailNil,
		putRightStatus: PutRightNil,
		putLeftStatus: PutLeftNil,
	}
}

// AddTail implements [LinkedList].
func (l *linkedList[T]) AddTail() {
	panic("unimplemented")
}

// AddToEmpty implements [LinkedList].
func (l *linkedList[T]) AddToEmpty(value T) {
	l.is_empty = false	
	n := &node[T]{value: value}
	l.head = n
	l.tail = n
	l.cursor = n
}

// Clear implements [LinkedList].
func (l *linkedList[T]) Clear() {
	panic("unimplemented")
}

// Find implements [LinkedList].
func (l *linkedList[T]) Find() {
	panic("unimplemented")
}

// Get implements [LinkedList].
func (l *linkedList[T]) Get() T {
	return l.cursor.value
}

// GetAddTailStatus implements [LinkedList].
func (l *linkedList[T]) GetAddTailStatus() StatusAddTail {
	panic("unimplemented")
}

// GetAddToEmptyStatus implements [LinkedList].
func (l *linkedList[T]) GetAddToEmptyStatus() StatusAddToEmpty {
	panic("unimplemented")
}

// GetFindStatus implements [LinkedList].
func (l *linkedList[T]) GetFindStatus() StatusFind {
	panic("unimplemented")
}

// GetGetStatus implements [LinkedList].
func (l *linkedList[T]) GetGetStatus() StatusGet {
	panic("unimplemented")
}

// GetHeadStatus implements [LinkedList].
func (l *linkedList[T]) GetHeadStatus() StatusHead {
	return l.headStatus
}

// GetIsHeadStatus implements [LinkedList].
func (l *linkedList[T]) GetIsHeadStatus() StatusIsHead {
	panic("unimplemented")
}

// GetIsTailStatus implements [LinkedList].
func (l *linkedList[T]) GetIsTailStatus() StatusIsTail {
	panic("unimplemented")	
}

// GetPutLeftStatus implements [LinkedList].
func (l *linkedList[T]) GetPutLeftStatus() StatusPutLeft {
	return l.putLeftStatus
}

// GetPutRightStatus implements [LinkedList].
func (l *linkedList[T]) GetPutRightStatus() StatusPutRight {
	return l.putRightStatus
}

// GetRemoveStatus implements [LinkedList].
func (l *linkedList[T]) GetRemoveStatus() StatusRemove {
	panic("unimplemented")
}

// GetReplaceStatus implements [LinkedList].
func (l *linkedList[T]) GetReplaceStatus() StatusReplace {
	panic("unimplemented")
}

// GetTailStatus implements [LinkedList].
func (l *linkedList[T]) GetTailStatus() StatusTail {
	return l.tailStatus
}

// Head implements [LinkedList].
func (l *linkedList[T]) Head() {
	if l.is_empty {
		l.headStatus = HeadErrListEmpty
		return
	}

	l.cursor = l.head
	l.headStatus = HeadOK	
}

// IsHead implements [LinkedList].
func (l *linkedList[T]) IsHead() bool {
	return l.cursor == l.head
}

// IsTail implements [LinkedList].
func (l *linkedList[T]) IsTail() bool {
	return l.cursor == l.tail
}

// IsValue implements [LinkedList].
func (l *linkedList[T]) IsValue() bool {
	panic("unimplemented")
}

// New implements [LinkedList].
func (l *linkedList[T]) New() LinkedList[T] {
	panic("unimplemented")
}

// PutLeft implements [LinkedList].
func (l *linkedList[T]) PutLeft(value T) {
	if l.is_empty {
		l.putLeftStatus = PutLeftErrListEmpty
		return
	}

	l.head = &node[T]{value: value}
	l.cursor = l.head

	l.putLeftStatus = PutLeftOK
}

// PutRight implements [LinkedList].
func (l *linkedList[T]) PutRight(value T) {
	if l.is_empty {
		l.putRightStatus = PutRightErrListEmpty
		return
	}

	// l.cursor.right = 

	// l.tail = *node[T]{value: value}
	// l.cursor = l.tail

	l.putRightStatus = PutRightOK
}

// Remove implements [LinkedList].
func (l *linkedList[T]) Remove() {
	panic("unimplemented")
}

// RemoveAll implements [LinkedList].
func (l *linkedList[T]) RemoveAll(value T) {
	panic("unimplemented")
}

// Replace implements [LinkedList].
func (l *linkedList[T]) Replace() {
	panic("unimplemented")
}

// Replace implements [LinkedList].
func (l *linkedList[T]) Right() {
	panic("unimplemented")
}

// Size implements [LinkedList].
func (l *linkedList[T]) Size() int {
	panic("unimplemented")
}

// Tail implements [LinkedList].
func (l *linkedList[T]) Tail() {
	if l.is_empty {
		l.tailStatus = TailErrListEmpty
		return
	}

	l.cursor = l.tail
	l.tailStatus = TailOK	
}


