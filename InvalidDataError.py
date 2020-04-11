class InvalidDataError(AssertionError):

    def __init__(self, msg):
        super().__init__(f'InvalidDataError: {msg}')
