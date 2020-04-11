from field import Field

class DerivedField(Field):

    def __init__(self):
        super().__init__()

    def generate_value(self, record):
        """
        Generates the value of the field from other
        fields.
        :param record: A record object
        :return: value of the field
        """
        pass

