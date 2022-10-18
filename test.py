import pytest
from otter.api import grade_submission
grade = grade_submission("demo.ipynb", "autograder.zip")
def test_hola():
    assert grade.get_score('q_1') == 1

