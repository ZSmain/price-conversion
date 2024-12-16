from enum import Enum

from core.models.flexup_enum import FlexUpEnum


class TestObject:
    def __init__(self, name=None, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.age}), {self.address['street']}, {self.address['city']}"

    def __eq__(self, other):
        if not isinstance(other, TestObject):
            return False
        return (
            self.name == other.name
            and self.age == other.age
            and self.address["street"] == other.address["street"]
        )


def setup_test_data(cls):
    # Primitives
    cls.string = "hello"
    cls.number = 42
    cls.boolean = True

    cls.list_names = ["john", "jane", "abe"]
    cls.list_numbers = [1, 2, 3]
    cls.list_mixed = ["john", 2, True]

    # Dictionaries
    cls.dict_john = {
        "name": "John",
        "age": 40,
        "address": {"street": "93 Main St", "city": "Boston"},
    }
    cls.dict_jane = {
        "name": "Jane",
        "age": 20,
        "address": {"street": "456 Elm St", "city": "New York"},
    }
    cls.dict_abe = {
        "name": "Abe",
        "age": 35,
        "address": {"street": "789 Oak St", "city": "Chicago"},
    }
    cls.list_dicts = [cls.dict_abe, cls.dict_john, cls.dict_jane]

    # Objects

    cls.object_john = TestObject(**cls.dict_john)
    cls.object_jane = TestObject(**cls.dict_jane)
    cls.object_abe = TestObject(**cls.dict_abe)

    # print_object(cls.object_john)
    # print_object(cls.object_jane)
    # print_object(cls.object_abe)

    cls.list_objects = [cls.object_john, cls.object_jane, cls.object_abe]
    # print_object(cls.list_objects)

    # Simple Enum
    class SimpleEnum(Enum):
        PENDING = "PE"
        ACTIVE = "AC"
        PAYABLE = "PY"

        # the comparison is based on the order of the items in the list
        def __lt__(self, other):
            if cls.__class__ is other.__class__:
                # Get the indices from _member_names_ list
                self_idx = cls.__class__._member_names_.index(cls.name)
                other_idx = cls.__class__._member_names_.index(other.name)
                return self_idx < other_idx
            return self.value < other.value

    cls.SE = SimpleEnum

    cls.se_pending = SimpleEnum.PENDING
    cls.se_active = SimpleEnum.ACTIVE
    cls.se_payable = SimpleEnum.PAYABLE

    cls.list_se = [cls.se_payable, cls.se_active]

    # Simple Enum
    class FlxUpEnum(FlexUpEnum):
        label: str
        level: int
        description: str

        # name =    value,  label,      level,  description
        PENDING = "PE", "Pending", 10, "Commitment is pending"
        ACTIVE = "AC", "Active", 20, "Commitment is active"
        PAYABLE = "PY", "Payable", 30, "Commitment is payable"

        # # the comparison is based on name of the items
        # def __lt__(self, other):
        #     if cls.__class__ is other.__class__:
        #         self_name = cls._value2member_map_[cls.value].name
        #         other_name = cls._value2member_map_[other.value].name
        #         return self_name < other_name
        #     return cls.value < other.value

    cls.FE = FlxUpEnum
    cls.fe_pending = FlxUpEnum.PENDING
    cls.fe_active = FlxUpEnum.ACTIVE
    cls.fe_payable = FlxUpEnum.PAYABLE

    cls.list_fe = [cls.fe_payable, cls.fe_active]
