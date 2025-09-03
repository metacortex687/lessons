import unittest
from task1 import SimpleTree, SimpleTreeNode

#run tests: 
# python ./DSA2/task1-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task1-2", "./DSA2/task1-2.py")
task1_2 = importlib.util.module_from_spec(spec)
sys.modules["task1-2"] = task1_2
spec.loader.exec_module(task1_2)
SimpleTree2 = task1_2.SimpleTree2
SimpleTreeNode2 = task1_2.SimpleTreeNode2

class TestSimpleTree(unittest.TestCase):

    def test_AddChild_Count_LeafCount_GetAllNodes(self):
        st = SimpleTree(None)
        self.assertEqual(st.Count(),0) 
        self.assertEqual(st.LeafCount(),0)
        self.assertEqual(st.GetAllNodes(),[])

        root = SimpleTreeNode(100,None)
        st = SimpleTree(root)
        self.assertEqual(st.Count(),1) 
        self.assertEqual(st.LeafCount(),1)
        self.assertCountEqual(st.GetAllNodes(),[root])

        stn10 = SimpleTreeNode(10,None)
        st.AddChild(root, stn10)
        self.assertEqual(st.Count(),2) 
        self.assertEqual(st.LeafCount(),1)
        self.assertCountEqual(st.GetAllNodes(),[root,stn10])

        stn20 = SimpleTreeNode(20,None)
        st.AddChild(stn10, stn20)
        self.assertEqual(st.Count(),3) 
        self.assertEqual(st.LeafCount(),1)  
        self.assertCountEqual(st.GetAllNodes(),[root,stn10,stn20])      

        stn30 = SimpleTreeNode(30,None)
        st.AddChild(stn10, stn30)
        self.assertEqual(st.Count(),4) 
        self.assertEqual(st.LeafCount(),2)
        self.assertCountEqual(st.GetAllNodes(),[root,stn10,stn20,stn30])  

    def test_MoveNode(self):
        root = SimpleTreeNode(100)
        st = SimpleTree(root)

        stn10 = SimpleTreeNode(10)
        st.AddChild(root, stn10)

        stn20 = SimpleTreeNode(20,None)
        st.AddChild(stn10, stn20)

        stn30 = SimpleTreeNode(30,None)
        st.AddChild(stn10, stn30)

        self.assertEqual(st.Count(),4) 
        self.assertEqual(st.LeafCount(),2)
        self.assertCountEqual(st.GetAllNodes(),[root,stn10,stn20,stn30]) 

        st.MoveNode(stn20,root)
        st.MoveNode(stn30,root)
        self.assertEqual(st.Count(),4) 
        self.assertEqual(st.LeafCount(),3)
        self.assertCountEqual(st.GetAllNodes(),[root,stn10,stn20,stn30])         

    def test_DeleteNode(self):
        root = SimpleTreeNode(100)
        st = SimpleTree(root)
        self.assertEqual(st.Count(),1) 
        st.DeleteNode(root)
        self.assertEqual(st.Count(),0) 

        st = SimpleTree(root)
        stn10 = SimpleTreeNode(10)
        stn20 = SimpleTreeNode(20)
        stn30 = SimpleTreeNode(30)

        st.AddChild(root,stn10)
        st.AddChild(stn10,stn20)
        st.AddChild(stn20,stn30)

        self.assertEqual(st.Count(),4) 
        self.assertEqual(st.LeafCount(),1)

        st.DeleteNode(stn20)
        self.assertEqual(st.Count(),2) 
        self.assertEqual(st.LeafCount(),1)

    def test_FindNodesByValue(self):
        st = SimpleTree(None)
        self.assertEqual(st.FindNodesByValue(20),[])

        root = SimpleTreeNode(20)
        st = SimpleTree(root)
        stn10 = SimpleTreeNode(10)
        stn20 = SimpleTreeNode(20)
        stn20_2 = SimpleTreeNode(20)
        stn30 = SimpleTreeNode(30)

        st.AddChild(root,stn10)
        st.AddChild(root,stn20)
        st.AddChild(stn10,stn20_2)
        st.AddChild(stn20,stn30)

        self.assertEqual(st.FindNodesByValue(10),[stn10])
        self.assertEqual(st.FindNodesByValue(30),[stn30])
        self.assertCountEqual(st.FindNodesByValue(20),[root,stn20,stn20_2])


class TestSimpleTree2(unittest.TestCase): 
     
     def test_SetLevels(self):
        st = SimpleTree2(None)
        st.SetLevels()

        root = SimpleTreeNode2(20)
        st = SimpleTree2(root)
        stn10 = SimpleTreeNode2(10)
        stn20 = SimpleTreeNode2(20)
        stn20_2 = SimpleTreeNode2(20)
        stn30 = SimpleTreeNode2(30)

        st.AddChild(root,stn10)
        st.AddChild(root,stn20)
        st.AddChild(stn10,stn20_2)
        st.AddChild(stn20_2,stn30)

        st.SetLevels()
        self.assertEqual(root.Level,0)
        self.assertEqual(stn10.Level,1)
        self.assertEqual(stn20.Level,1)
        self.assertEqual(stn20_2.Level,2)
        self.assertEqual(stn30.Level,3)

     def test_GetLevelNode(self):

        root = SimpleTreeNode2(20)
        st = SimpleTree2(root)
        stn10 = SimpleTreeNode2(10)
        stn20 = SimpleTreeNode2(20)
        stn20_2 = SimpleTreeNode2(20)
        stn30 = SimpleTreeNode2(30)

        st.AddChild(root,stn10)
        st.AddChild(root,stn20)
        st.AddChild(stn10,stn20_2)
        st.AddChild(stn20_2,stn30)

        self.assertEqual(st.GetLevelNode(root),0)
        self.assertEqual(st.GetLevelNode(stn10),1)
        self.assertEqual(st.GetLevelNode(stn20),1)
        self.assertEqual(st.GetLevelNode(stn20_2),2)
        self.assertEqual(st.GetLevelNode(stn30),3)

        
if __name__ == '__main__':
    unittest.main()
   
   
     
        