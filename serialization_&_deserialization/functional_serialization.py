import pickle

def serialize_objects(objects):
    """
    Serialize clusters of objects.

    :param objects: List of objects to serialize
    :return: Serialized data
    """
    try:
        serialized_data = pickle.dumps(objects)
        return serialized_data
    except Exception as e:
        return str(e)

def deserialize_objects(serialized_data):
    """
    Deserialize data back into objects.

    :param serialized_data: Serialized data
    :return: List of deserialized objects
    """
    try:
        objects = pickle.loads(serialized_data)
        return objects
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Define some objects to serialize
    objects_to_serialize = [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35}
    ]

    # Serialize objects
    serialized_data = serialize_objects(objects_to_serialize)
    print("Functional Serialization Result:")
    print(serialized_data)

    # Deserialize objects
    deserialized_objects = deserialize_objects(serialized_data)
    print("Functional Deserialization Result:")
    print(deserialized_objects)

    # Check if deserialized objects match original objects
    if deserialized_objects == objects_to_serialize:
        print("Functional Test Passed: Serialization and deserialization are correct.")
    else:
        print("Functional Test Failed: Deserialized objects do not match the original.")
