from field import Field


class NonDerivedField(Field):

    clean_data = 'NO DATA'

    def __init__(self):
        super().__init__()

    def get_input(self):
        """
        Displays field name and gets input from console,
        validates the input and returns the data. Raises
        InvalidDataError on invalid data.
        :return: validated data from input
        """
        pass

    def valid(self, raw_input):
        """
        Validates a input string.
        :param raw_input: string read from console
        :return: boolean indicating validation status of data
        """
        pass
