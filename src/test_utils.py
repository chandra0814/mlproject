import dill
import unittest

class TestDillSerialization(unittest.TestCase):
    def test_dill_serialization(self):
        obj = {'key': 'value'}
        serialized_obj = dill.dumps(obj)
        deserialized_obj = dill.loads(serialized_obj)
        self.assertEqual(obj, deserialized_obj)

    def test_dill_serialization_empty_dict(self):
        obj = {}
        serialized_obj = dill.dumps(obj)
        deserialized_obj = dill.loads(serialized_obj)
        self.assertEqual(obj, deserialized_obj)

    def test_dill_serialization_nested_dict(self):
        obj = {'outer': {'inner': 'value'}}
        serialized_obj = dill.dumps(obj)
        deserialized_obj = dill.loads(serialized_obj)
        self.assertEqual(obj, deserialized_obj)

    def test_dill_serialization_list(self):
        obj = [1, 2, 3]
        serialized_obj = dill.dumps(obj)
        deserialized_obj = dill.loads(serialized_obj)
        self.assertEqual(obj, deserialized_obj)

    def test_dill_serialization_complex_object(self):
        class CustomClass:
            def __init__(self, value):
                self.value = value

        obj = CustomClass(10)
        serialized_obj = dill.dumps(obj)
        deserialized_obj = dill.loads(serialized_obj)
        self.assertEqual(obj.value, deserialized_obj.value)

if __name__ == '__main__':
    unittest.main()
