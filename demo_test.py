from otter.api import grade_submission
import pytest

grade = grade_submission("demo.ipynb", "autograder.zip")


def test_function():
    assert grade.get_score("q_1") == 1

