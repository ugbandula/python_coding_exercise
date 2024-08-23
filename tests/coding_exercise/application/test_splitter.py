import sys
import unittest
from assertpy import assert_that

from src.coding_exercise.application.splitter import Splitter
from src.coding_exercise.domain.model.cable import Cable

class TestSplitter(unittest.TestCase):
    def test_should_not_return_none_when_splitting_cable(self):

        # Positive Tests
        assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()
        assert_that(Splitter().split(Cable(10, "coconuts"), 2)).is_not_none()
        assert_that(Splitter().split(Cable(5, "mangoes"), 2)).is_not_none()
        assert_that(Splitter().split(Cable(36, "avocados"), 3)).is_not_none()
        assert_that(Splitter().split(Cable(36, "avocados"), 4)).is_not_none()
        assert_that(Splitter().split(Cable(150, "grapes"), 5)).is_not_none()
        # assert_that(Splitter().split(Cable(1020, "avocados"), 50)).is_not_none()

    # def test_split_with_negative_tests(self):
    #     # check that split fails when the arguments are invalid and raises ValueError
    #     assert_that(Splitter).raises(ValueError).when_called_with(Splitter().split(Cable(10, "coconuts"), -1))
    #     assert_that(Splitter).raises(ValueError).when_called_with(Splitter().split(Cable(1, "coconuts"), 1))
    #     assert_that(Splitter).raises(ValueError).when_called_with(Splitter().split(Cable(-10, "coconuts"), 2))

if __name__ == "__main__":
   unittest.main()