import sys

# main method

def func(obj, key):
    fields = key.split('/')

    response = None

    for field in fields:
        if not isinstance(obj, str) and obj.get(field) is not None:
            response = obj[field]
            obj = response

        else:
            raise Exception("Please check the key value passed...")

    return response

# Arguments passed

obj = {"x":{"y":{"z":"a"}}}
key = "x/y/z"
result = func(obj, key)
print(result)
