from uuid import uuid4

from DerivedField import DerivedField
from NonDerivedField import NonDerivedField
from InvalidDataError import InvalidDataError
from Inputter import Inputter


class IdField(DerivedField):

    name = 'id'
    desc = 'Unique ID field'

    def __init__(self):
        super().__init__()

    def generate_value(self, record):
        return uuid4().int


class StreamName(DerivedField):

    name = 'stream-name'
    desc = 'Derived string form displayName and ID'

    def __init__(self):
        super().__init__()

    def generate_value(self, record):
        display_name = record.get('displayName', 'NO DISPLAY NAME FOUND')
        id_field = record.get('id', 'NO ID FOUND')
        return f'{display_name}_{id_field}'


class Query(NonDerivedField):

    name = 'query'
    desc = 'Query (GROUPBY, STATIC, RAW, TOPK)'
    WHITELIST = ['GROUPBY', 'STATIC', 'RAW', 'TOPK']

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for query field')

    def valid(self, raw_input):
        if raw_input in self.WHITELIST:
            self.clean_data = raw_input
            return True
        else:
            return False


class DisplayName(NonDerivedField):

    name = 'displayName'
    desc = 'Any human readable string.'

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for query field')

    def valid(self, raw_input):
        if len(raw_input) > 1:
            self.clean_data = raw_input
            return True
        else:
            return False


class AttributeCode(NonDerivedField):

    name = 'code'
    desc = 'attribute code'

    def __init__(self):
        super().__init__()

    def get_input(self):
        print('Attribute Code: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for attribute code field')

    def valid(self, raw_input):
        if len(raw_input) > 1:
            self.clean_data = raw_input
            return True
        return False


class AttributeName(NonDerivedField):

    name = 'name'
    desc = 'attribute name'

    def __init__(self):
        super().__init__()

    def get_input(self):
        print('Attribute Name: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for attribute name field')

    def valid(self, raw_input):
        if len(raw_input) > 1:
            self.clean_data = raw_input
            return True
        return False


class AttributeType(NonDerivedField):

    name = 'attrType'
    desc = 'attribute type'
    WHITELIST = ['int', 'long', 'double', 'string']

    def __init__(self):
        super().__init__()

    def get_input(self):
        print('Attribute type: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for attribute type field')

    def valid(self, raw_input):
        if raw_input in self.WHITELIST:
            self.clean_data = raw_input
            return True
        else:
            return False


class AttributeKeySize(DerivedField):

    name = 'key-size'
    desc = 'attribute key size'

    def __init__(self):
        super().__init__()

    def generate_value(self, record):
        if record.get('attrType', '') == 'string':
            return 64
        return 0


class AttributeIndex(NonDerivedField):

    name = 'Index'
    desc = 'attribute index'
    WHITELIST = ['NONE', 'NORMAL']

    def __init__(self):
        super().__init__()

    def get_input(self):
        print('Attribute index: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for attribute index field')

    def valid(self, raw_input):
        if raw_input in self.WHITELIST:
            self.clean_data = raw_input
            return True
        else:
            return False


class Attributes(NonDerivedField):

    name = 'attributes'
    desc = 'attr'
    attr_fields = [AttributeCode, AttributeName, AttributeType, AttributeIndex, AttributeKeySize]

    def __init__(self):
        super().__init__()

    def get_input(self):
        print('Attributes')
        local_inputter = Inputter(self.attr_fields)
        attributes = []
        stop = False
        while not stop:
            print('Input new attribute? 1/0')
            selection = input()
            if selection == '0':
                stop = True
                continue
            elif selection == '1':
                attribute = local_inputter.start()
                if not attribute:
                    break
                attributes.append(attribute)
            else:
                raise InvalidDataError('Invalid selection. Use only 0 or 1')
        return attributes if len(attributes) > 0 else None

    def valid(self, raw_input):
        return True


class Notification(NonDerivedField):

    name = 'notification'
    desc = 'NOTIF'
    WHITELIST = ['NOTIFICATION_NONE', 'NOTIFICATION_ALL']

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for notification field')

    def valid(self, raw_input):
        if raw_input in self.WHITELIST:
            self.clean_data = raw_input
            return True
        else:
            return False


class AppId(DerivedField):

    name = 'appId'
    desc = 'App ID field'

    def __init__(self):
        super().__init__()

    def generate_value(self, record):
        return str(uuid4())


class DescField(NonDerivedField):

    name = 'desc'
    desc = 'Any human readable string.'

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for desc field')

    def valid(self, raw_input):
        if len(raw_input) > 1:
            self.clean_data = raw_input
            return True
        else:
            return False


class ArchiveTTLSec(NonDerivedField):

    name = 'archive-ttlsec'
    desc = 'archive ttl'

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for archive ttl sec field')

    def valid(self, raw_input):
        try:
            int(raw_input)
            self.clean_data = raw_input
            return True
        except ValueError:
            return False


class SampleGran(NonDerivedField):

    name = 'sample-gran'
    desc = 'Query (GROUPBY, STATIC, RAW, TOPK)'
    WHITELIST = ['SECOND', 'MINUTE', 'HOUR']

    def __init__(self):
        super().__init__()

    def get_input(self):
        print(f'{self.name}: ')
        inp = input()
        if self.valid(inp):
            return self.clean_data
        raise InvalidDataError('Invalid data for sample-gran field')

    def valid(self, raw_input):
        if raw_input in self.WHITELIST:
            self.clean_data = raw_input
            return True
        else:
            return False
