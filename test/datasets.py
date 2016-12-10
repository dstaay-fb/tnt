import unittest
import torch
import dataset.listdataset
import dataset.tensordataset
import numpy as np
import os

class TestDatasets(unittest.TestCase):
    def testListDataset(self):
        identity = lambda x: x
        h = [0,1,2]
        d = dataset.listdataset.ListDataset(elem_list = h, load = identity)
        self.assertEqual(len(d), 3)
        self.assertEqual(d[0], 0)

        t = torch.LongTensor([0,1,2])
        d = dataset.listdataset.ListDataset(elem_list = t, load = identity)
        self.assertEqual(len(d), 3)
        self.assertEqual(d[0], 0)

        a = np.asarray([0,1,2])
        d = dataset.listdataset.ListDataset(elem_list = a, load = identity)
        self.assertEqual(len(d), 3)
        self.assertEqual(d[0], 0)

    def testListDataset_path(self):
        prefix = lambda x: 'bar/' + str(x)
        tbl = [0,1,2]
        d = dataset.listdataset.ListDataset(tbl, prefix, 'foo')
        self.assertEqual(len(d), 3)
        self.assertEqual(d[2], 'bar/foo/2')

    def testListDataset_file(self):
        filename = os.tempnam()
        with open(filename, 'w') as f:
            for i in range(0,50):
                f.write(str(i) + '\n')

        identity = lambda x: x
        d = dataset.listdataset.ListDataset(filename, identity, 'foo')
        self.assertEqual(len(d), 50)
        self.assertEqual(d[15], 'foo/15')

        os.remove(filename)

    def testTensorDataset(self):
        data = {
                # 'input': torch.range(0,7),
                'input': np.arange(0,8),
                'target': np.arange(0,8),
                }
        d = dataset.tensordataset.TensorDataset(data)
        self.assertEqual(len(d), 8)
        self.assertEqual(d[2], {'input': 2, 'target': 2})


if __name__ == '__main__':
    unittest.main()