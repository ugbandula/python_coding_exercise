import sys
import unittest

from assertpy import assert_that

from src.coding_exercise.domain.model.cable import Cable

class TestCable(unittest.TestCase):

    def test_should_have_length(self):
        given_length = 101

        assert_that(Cable(given_length, "coconuts").length).is_equal_to(given_length)


    def test_should_raise_error_if_float_provided_for_length(self):
        assert_that(Cable).raises(ValueError).when_called_with(101.101, "coconuts")


    def test_should_raise_error_if_none_provided_for_length(self):
        assert_that(Cable).raises(ValueError).when_called_with(None, "coconuts")


    def test_should_raise_error_if_negative_provided_for_length(self):
        assert_that(Cable).raises(ValueError).when_called_with(-101, "coconuts")


    def test_should_raise_error_if_greater_than_maxsize_provided_for_length(self):
        assert_that(Cable).raises(ValueError).when_called_with(sys.maxsize + 1, "coconuts")


    def test_should_equal(self):
        given_length = 101
        given_name = "coconuts"

        assert_that(Cable(given_length, given_name)).is_equal_to(
            Cable(given_length, given_name)
        )


    def test_should_not_equal_if_lengths_differ(self):
        given_name = "coconuts"

        assert_that(Cable(101, given_name)).is_not_equal_to(Cable(1010, given_name))


    def test_should_not_equal_if_names_differ(self):
        given_length = 101

        assert_that(Cable(given_length, "coconuts")).is_not_equal_to(
            Cable(given_length, "bob")
        )


    def test_should_not_equal_if_not_a_cable(self):
        assert_that(Cable(101, "coconuts")).is_not_equal_to("bob")


    def test_should_have_name(self):
        given_name = "coconuts"

        assert_that(Cable(101, given_name).name).is_equal_to(given_name)

if __name__ == "__main__":
   unittest.main()
