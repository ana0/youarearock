import unittest
import questionnode
import database


nodes = {i: database.__dict__[i] for i in database.__dict__ if 
        isinstance(database.__dict__[i], questionnode.GameNode)}

class TestAnswers(unittest.TestCase):

    def test_all_answers_mapped(self):
        global nodes
        for node in nodes:
            try:
                self.assertLessEqual(len(nodes[node].options), 
                    len(nodes[node].answer_map), 
                    "node %s has %s options and %s map points" % 
                    (str(nodes[node].idnum), str(len(nodes[node].options)), 
                    str(len(nodes[node].answer_map))))
            except AttributeError:
                self.assertEqual(len(nodes[node].answer_map), 1,
                "node %s has no options and %s map points" % 
                (str(nodes[node].idnum), str(len(nodes[node].answer_map))))

if __name__ == '__main__':
    unittest.main()