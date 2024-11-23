#!/usr/bin/python3
import uuid

NAME  = "example.com"

# Generate a random UUID (Version 4)
random_uuid = uuid.uuid4()

# Generate a UUID based on the host ID and current time (Version 1)
time_based_uuid = uuid.uuid1()

# Generate a UUID based on a namespace and a name (Version 3)
namespace = uuid.NAMESPACE_DNS
namespace_based_uuid = uuid.uuid3(namespace, NAME)

# Generate a UUID based on a namespace and a name (Version 5)
namespace_based_uuid_v5 = uuid.uuid5(namespace, NAME)

print(f"""
    Namespace-based UUID (Version 5): {namespace_based_uuid_v5}\n
    Random UUID (Version 4): {random_uuid}\n
    Time-based UUID (Version 1): {time_based_uuid}\n
    Namespace-based UUID (Version 3): {namespace_based_uuid}
""")
