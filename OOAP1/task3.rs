
    trait ParentNodeTrait<T> {
        fn new_dummy() -> Self;

        fn new(value: T) -> Self;

        fn is_value(&self) -> bool;
        fn value(&self) -> T;
    }

    trait Node<T> : ParentNodeTrait<T> {
        fn get_right_node(&self) -> Self;
        fn set_right_node(&mut self, value: Self);
    }

    trait TwoWayNode<T> : ParentNodeTrait<T> {
        fn get_right_node(&self) -> Self;
        fn set_right_node(&mut self, value: Self);
        fn get_left_node(&self) -> Self;
        fn set_left_node(&mut self, value: Self);    
    }

    trait ParentListTrait<T> {
        fn head(&mut self);
        fn tail(&mut self);

        fn add_to_empty(&mut self, value:T);

        fn is_value(&self) -> bool;
        fn value(&self);
    }


    trait LinkedList<T> : ParentListTrait<T> {
        fn put_right(&mut self);
        fn right(&self);
    }

    trait TwoWayList<T> : ParentListTrait<T> {
        fn put_right(&mut self);
        fn right(&self);   
        fn put_left(&mut self);
        fn left(&self);
    }


pub sruct LinkedList<T> {

}

impl<T> ParentListTrait<T> for ParentList<T> {

}

