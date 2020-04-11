from json import dumps

from DerivedField import DerivedField
from InvalidDataError import InvalidDataError
from NonDerivedField import NonDerivedField


class Inputter(object):
    """
    Accepts the specified fields as inputs from user.
    """

    def __init__(self, fields):
        self.fields = fields

    def start(self):
        """
        Starts accepting the input and generates the final JSON.
        """
        non_derived_fields = [x for x in self.fields if isinstance(x(), NonDerivedField)]
        derived_fields = [x for x in self.fields if isinstance(x(), DerivedField)]

        record = Inputter.get_non_derived(non_derived_fields)
        record = Inputter.fadd_derived_fields(derived_fields, record)

        print(dumps(record))
        return record

    @staticmethod
    def get_non_derived(non_derived_fields):
        """
        Accepts non derived fields from user as input.
        :param non_derived_fields:
        :return: (dict) record
        """

        record = dict()

        for field in non_derived_fields:
            f = field()
            try:
                field_value = f.get_input()
            except InvalidDataError as e:
                print('Aborting...')
                print(str(e))
                return
            if field_value:
                record[f.name] = field_value

        return record

    @staticmethod
    def add_derived_fields(derived_fields, record):
        """
        Derives the derived fields from the non derived fields.
        :param derived_fields: (list) derived fields
        :param record: (dict) object made up of non-derived fields
        :return: record (dict)
        """
        for field in derived_fields:
            f = field()
            field_value = f.generate_value(record)
            record[f.name] = field_value

        return record
