package linkedlist

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// Head
// предусловие: список не пустой;
func TestHeadPreconditions(t *testing.T) {
	l := New[int]()
	assert.Equal(t, HeadNil, l.GetHeadStatus())

	l.Head()
	assert.Equal(t, HeadErrListEmpty, l.GetHeadStatus())

	l.AddToEmpty(1)
	l.Head()
	assert.Equal(t, HeadOK, l.GetHeadStatus())
}

// Head
// постусловие: курсор на первом узле в списке.
func TestHeadPostconditions(t *testing.T) {
	l := New[int]()

	l.AddToEmpty(1)
	l.PutRight(2)

	assert.Equal(t, false, l.IsHead())

	l.Head()
	assert.Equal(t, true, l.IsHead())
}

// Tail
// предусловие: список не пустой;
func TestTailPreconditions(t *testing.T) {
	l := New[int]()
	assert.Equal(t, TailNil, l.GetTailStatus())

	l.Tail()
	assert.Equal(t, TailErrListEmpty, l.GetTailStatus())

	l.AddToEmpty(1)
	l.Tail()
	assert.Equal(t, TailOK, l.GetTailStatus())
}

// Tail
// постусловие: курсор на первом узле в списке.
func TestTailPostconditions(t *testing.T) {
	l := New[int]()

	l.AddToEmpty(1)
	l.PutLeft(2)

	assert.Equal(t, false, l.IsTail())

	l.Tail()
	assert.Equal(t, true, l.IsTail())
}

// PutRight
// предусловие: список не пустой;
func TestPutRightPreconditions(t *testing.T) {
	l := New[int]()

	// вначале Nil
	assert.Equal(t, PutRightNil, l.GetPutRightStatus())

	l.PutRight(1)
	assert.Equal(t, PutRightErrListEmpty, l.GetPutRightStatus())

	l.AddToEmpty(2)
	l.PutRight(1)
	assert.Equal(t, PutRightOK, l.GetPutRightStatus())
}

// PutRight
// постусловие:
//
//	значение вставлено справа от курсора
//	курсор на этом вставленном значении
func TestPutRightPostconditions(t *testing.T) {
	l := New[int]()

	l.AddToEmpty(1)
	l.PutRight(2)

	l.Head()
	assert.Equal(t, 1, l.Get())

	l.Tail()
	assert.Equal(t, 2, l.Get())

	l.Head()
	l.Right()
	assert.Equal(t, 2, l.Get())
}
