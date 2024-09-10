import ctypes
import os

rust_lib = ctypes.CDLL("/usr/lib/x86_64-linux-gnu/libhash.so")
rust_lib.device_info.argtypes = [ctypes.c_char_p]
rust_lib.device_info.restype = ctypes.c_char_p

def version():
    return rust_lib.version()

def device_info(key):
    if key:
        key_bytes = key.encode('utf-8')
    else:
        key_bytes = b""
    return rust_lib.device_info(key_bytes)

def get_device_info(key="123"):
    device_infos = device_info(key)
    import json
    device_infos = json.loads(device_infos)
    nonce = device_infos["devices"][0]["nonce"]
    seed = device_infos["devices"][0]["s1"]
    return (nonce, seed)


if __name__ == "__main__":
    key = "AMSMgPqkDGFPANDuJ1MpUiG3N7fcoVyABakcfQixnLa3"
    device_index = 0
    device_uuid = "30dcf980f95b736939b3da28170dc6f824a8901d456fc60da4c9156b4e4f8c20550081155abdbfeed01546846f0735731f565cddf5f7dc6d7804777fd9a796eb"
    device_infos = device_info(key)
    print(device_infos)


