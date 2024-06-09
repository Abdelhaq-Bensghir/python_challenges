if __name__ == "__main__":

    from oop_serialisation import serialize_objects as fser
    from functional_serialisation import ObjectSerializer

    # Define some objects to serialize
    objects_to_serialize = [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35}
    ]

    # Test Functional Implementation
    functional_serialized_data = fser(objects_to_serialize)

    # Test Object-Oriented Implementation
    oop_serializer = ObjectSerializer(objects_to_serialize)
    oop_serialized_data = oop_serializer.serialize_objects()

    # Compare the results of both implementations
    if functional_serialized_data == oop_serialized_data:
        print("Test Passed: Both serializations are equivalent")
    else:
        print("Test Failed: Implementations produce different results.")