def get_value(object, key):
    keys = key.split('/')
    current = object

    for k in keys:
        current = current.get(k)
    
    return current

if __name__ == "__main__":
    object1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    print(f"The value for key '{key1}' is: {get_value(object1, key1)}")  # Output: d

    object2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    print(f"The value for key '{key2}' is: {get_value(object2, key2)}")  # Output: a

    object1 = {"a": {"b": {"c": "d"}}}
    key1 = "a"
    print(f"The value for key '{key1}' is: {get_value(object1, key1)}")  # Output: {'b': {'c': 'd'}}

    object2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y"
    print(f"The value for key '{key2}' is: {get_value(object2, key2)}")  # Output: {'z': 'a'}