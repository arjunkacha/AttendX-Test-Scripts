
import unittest


def mark_attendance(student_id, status):
    """Sample attendance logic for demonstrating test cases."""
    if not student_id:
        return False

    if status not in ("Present", "Absent"):
        return False

    return True


class AttendanceMarkingTests(unittest.TestCase):

    def test_mark_student_present(self):
        self.assertTrue(mark_attendance("STU001", "Present"))

    def test_mark_student_absent(self):
        self.assertTrue(mark_attendance("STU002", "Absent"))

    def test_reject_empty_student_id(self):
        self.assertFalse(mark_attendance("", "Present"))

    def test_reject_invalid_attendance_status(self):
        self.assertFalse(mark_attendance("STU003", "Unknown"))


if __name__ == "__main__":
    unittest.main()
