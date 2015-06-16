ma_target = MaTarget(param1, param2)


class Task1(ITask):
    target = ma_target
    requires = []

    def run(self):
        # do something
        pass


class Task2(ITask):

    @property
    def target(self):
        return ma_target

    @property
    def requires(self):
        return (Task1(), )

    def run(self):
        # do something
        pass

task = None


@task(name="Task3", require=[], target=ma_target)
def task3(context):
    pass


@task(name="Task4", require=[], output=ma_target)
class task4(object):

    def __init__(self, context):
        self.context = context

    def __call__(self):
        pass
