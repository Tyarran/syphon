NOT_IMPLEMENTED = NotImplemented('Method not implemented')


class ITask(object):
    target = None
    requires = []

    @property
    def requires(self):
        """Must return a iterable object"""
        raise NOT_IMPLEMENTED

    @property
    def target(self):
        """ Return a target """
        raise NOT_IMPLEMENTED

    @property
    def input(self):
        """ return a generator with all targets from requires tasks """
        return (task.target for task in self.requires)

    def run(self):
        """ The task execution code """
        raise NOT_IMPLEMENTED


class ITarget(object):
    """ ITarget interface. Must be use as a context manager """

    def exists(self):
        raise NOT_IMPLEMENTED

    def __enter__(self):
        raise NOT_IMPLEMENTED

    def __exit__(self):
        raise NOT_IMPLEMENTED

    def read(self):
        raise NOT_IMPLEMENTED
