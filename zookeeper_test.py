import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    """
        Tarea Hernandez Martinez Miguel Angel
    """     
    def test_borrar_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.delete('/node1',0)
    
    def test_error_al_mostrar_hijo(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, '/')  
            tree.getChildren()  
    
    def test_buscar_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.exist('/node2')
    
    def test_cambiar_data(self):
        tree = Ztree()
        tree.create('/node1/node2/node3', 'algo', True, True, 10, '/')
        tree.setData('/node3','otra cosa')
    
    def test_ver_data(self):
        tree = Ztree()
        tree.create('/node2', 'info', True, True, 5, '/')
        tree.getData('/node2')
    

if __name__ == '__main__':
    unittest.main()

