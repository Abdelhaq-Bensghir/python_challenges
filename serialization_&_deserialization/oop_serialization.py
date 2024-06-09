import pickle

class ObjectSerializer:
    def __init__(self, objects):
        """
        Initialize ObjectSerializer with a list of objects.

        :param objects: List of objects to serialize
        """
        self.objects = objects

    def serialize_objects(self):
        """
        Serialize clusters of objects.

        :return: Serialized data
        """
        try:
            serialized_data = pickle.dumps(self.objects)
            return serialized_data
        except Exception as e:
            return str(e)

    def deserialize_objects(self, serialized_data):
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

    # Create an instance of ObjectSerializer
    serializer = ObjectSerializer(objects_to_serialize)

    # Serialize objects
    serialized_data = serializer.serialize_objects()
    print("Object-Oriented Serialization Result:")
    print(serialized_data)

    # Deserialize objects
    deserialized_objects = serializer.deserialize_objects(serialized_data)
    print("Object-Oriented Deserialization Result:")
    print(deserialized_objects)

    # Check if deserialized objects match original objects
    if deserialized_objects == objects_to_serialize:
        print("Object-Oriented Test Passed: Serialization and deserialization are correct.")
    else:
        print("Object-Oriented Test Failed: Deserialized objects do not match the original.")
