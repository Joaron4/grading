from otter.api import grade_submission
grade = grade_submission("demo.ipynb", "autograder.zip")
print('--->',(grade.get_score('q_1')))
