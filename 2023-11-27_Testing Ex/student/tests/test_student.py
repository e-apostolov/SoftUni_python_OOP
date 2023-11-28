from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Evgeni", {"Python": ["note1", "note2", "note3"], "JS": ["note1", "note2"]})
        self.student_2 = Student("Diana")

    def test_init_with_courses(self):
        self.assertEqual("Evgeni", self.student_1.name)
        self.assertEqual({"Python": ["note1", "note2", "note3"], "JS": ["note1", "note2"]}, self.student_1.courses)

    def test_init_without_courses(self):
        self.assertEqual("Diana", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_enroll_existing_course(self):
        result = self.student_1.enroll("Python", ["note4", "note5"], "N")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note3", "note4", "note5"], "JS": ["note1", "note2"]},
                         self.student_1.courses)

        result = self.student_1.enroll("Python", ["note6", "note7"], "Y")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note3", "note4", "note5", "note6", "note7"], "JS": ["note1", "note2"]},
                         self.student_1.courses)

    def test_enroll_non_existing_course_with_y(self):
        result = self.student_1.enroll("C#", ["note1", "note2"], "Y")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student_1.courses["C#"])

    def test_enroll_non_existing_course_with_empty_sting(self):
        result = self.student_1.enroll("C#", ["note1", "note2"], "")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student_1.courses["C#"])

    def test_enroll_non_existing_course_not_adding_notes(self):
        result = self.student_1.enroll("C#", ["note1", "note2"], "N")

        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_1.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.student_2.enroll("C#", ["note1", "note2"])
        result = self.student_2.add_notes("C#", "note3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "note3"], self.student_2.courses["C#"])

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("C#", "note3")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_1.leave_course("JS")
        self.assertEqual("Course has been removed", result)
        self.assertFalse("JS" in self.student_1.courses)

    def test_leave_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("C#")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
