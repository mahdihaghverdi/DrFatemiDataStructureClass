from dsp.projects import Priority, Task


class TestTask:
    @classmethod
    def setup_class(cls):
        cls.title = "Testing"
        cls.steps = ["Write Task class", "Test Task class"]
        cls.priority = Priority.HIGH
        cls.time_limit = 24
        cls.note = "This is fun"
        cls.basic_task = Task(
            title=cls.title,  # noqa
            priority=cls.priority,  # noqa
            time_limit=cls.time_limit,  # noqa
        )
        cls.complete_task = Task(
            title=cls.title,  # noqa
            priority=cls.priority,  # noqa
            time_limit=cls.time_limit,  # noqa
            steps=cls.steps,  # noqa
            note=cls.note,  # noqa
        )

    def test_attrs(self):
        assert self.basic_task.title == self.title
