def GenerateBBSTArray(a: list) -> list:
    if len(a) == 0:
        return []
    
    if len(a) == 1:
        return [a[0]]
  
    result = [None]*_size_tree(len(a))
    _GenerateBBSTArray(sorted(a), 0, len(a)-1,0,result,1)

    return result

def _size_tree(count_elements):
    _size = 1
    _count_in_level = 1
    while _size < count_elements:
        _count_in_level *=2
        _size += _count_in_level
    return _size


def _GenerateBBSTArray(a: list, start_index_a, end_index_a, index_insert, result: list, count_in_level) -> None:

    if start_index_a == end_index_a:
        result[index_insert] = a[start_index_a]
        return

    index_root = (start_index_a + end_index_a +1)//2
    result[index_insert] = a[index_root]

    if end_index_a-start_index_a == 1:
        result[index_insert*2+1] = a[start_index_a] 
        return      
    
    _GenerateBBSTArray(a,start_index_a,index_root-1,index_insert*2+1,result,count_in_level)
    _GenerateBBSTArray(a,index_root+1,end_index_a,index_insert*2+2,result,count_in_level)


