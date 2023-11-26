from unittest import TestCase, main
# from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.5, 2, 3)

    def test_correct_init_and_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_operation_adds_integer_to_the_list(self):
        actual_data = self.integer_list.get_data() + [5]

        self.integer_list.add(5)
        self.assertEqual(actual_data, self.integer_list.get_data())

    def test_add_operation_with_float_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_with_valid_index_removes_element(self):
        expected = [1, 3]
        deleted_element = 2

        actual_deleted_element = self.integer_list.remove_index(1)
        self.assertEqual(expected, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)

    def test_remove_index_operation_with_out_of_index_raises_value_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_returns_element(self):
        expected_element = 2
        actual_element = self.integer_list.get(1)

        self.assertEqual(expected_element, actual_element)

    def test_get_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_integer_on_valid_index_expected_element_inserted(self):
        expected_list = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_insert_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_float_element_on_valid_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_expect_success(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index_expect_success(self):
        self.assertEqual(1, self.integer_list.get_index(2))


if __name__ == "__main__":
    main()