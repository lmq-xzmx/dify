import ctypes
import json
import os
import sys
import traceback


# setup sys.excepthook
def excepthook(type, value, tb):
    sys.stderr.write("".join(traceback.format_exception(type, value, tb)))
    sys.stderr.flush()
    sys.exit(-1)


sys.excepthook = excepthook

lib = ctypes.CDLL("/var/sandbox/sandbox-python/python.so")
print(lib)
lib.DifySeccomp.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_bool]
lib.DifySeccomp.restype = None

os.chdir("/var/sandbox/sandbox-python")

lib.DifySeccomp(65537, 1001, 1)

# declare main function here
# 测试代码可以写在此处

import pandas as pd
import ibm_db


def main() -> dict:
    s = pd.Series([1, 3, 5, 6, 8])
    return {
        "result": "test",
    }


from base64 import b64decode
from json import dumps, loads

# execute main function, and return the result
# inputs is a dict, and it
inputs = b64decode("e30=").decode("utf-8")
output = main(**json.loads(inputs))

# convert output to json and print
output = dumps(output, indent=4)

result = f"""<<RESULT>>
{output}
<<RESULT>>"""

print(result)
