#!/usr/bin/python3

"""
Welcome to the Dirty Cow lab!

REQUIREMENT: >= python 3.6

NOTE: There are hints spread out through the file (base64 encoded). You can 
decode these strings if you need a hint.

NOTE: To complete this lab you ONLY need the methods provided in the Kernel
below. Do not access/use attributes or methods with an _ or obfuscated names.

HINT: aHR0cHM6Ly9naXRodWIuY29tL2RpcnR5Y293L2RpcnR5Y293LmdpdGh1Yi5pby9ibG9iL21hc3Rlci9kaXJ0eWMwdy5j

Step 1: Fill in the two thread_function's using the methods provided by the
Kernel so that rootfile.txt is modified. 

NOTE: Run `python3 -i kernel.pyc` and play around with the kernel and it's methods
to get more familar with them. The docstring and function stubs are provided
for you below.

TRY THIS:
$ python3 -i kernel.pyc
>>> k = Kernel()
>>> k.peek() # try me
>>> k.write("0x0", "test")
>>> k.peek() # What happens in memory? What is triggered?


ORIGINAL: HAHA ONLY ROOT CAN WRITE TO THIS!
    GOAL: HAHA USERS CAN WRITE TO THIS TOO!

Step 2: Modify the _copy_on_write method in KernelPatched to patch the dirty
cow exploit. Remember to uncomment # k = KernelPatched() in the main block below
after you patch the kernel

You're done! 

!!!!!!! NOTE: addresses (addr) are hexstrings e.g. "0x00000008"

========= KERNEL =========
class Kernel:
    
    def __init__(self, f="rootfile.txt") -> None:
        # Maps the given file (f) into memory

    def write(self, addr: String, buffer: str) -> None:
        # Writes the buffer to the address

    def dontneed(self, addr: String, length: int -> None:
        # Hints the kernel that memory at address to address + length will not
        # be used. This will result in the kernel writing out the memory to 
        # disk if possible depending on your permissions.

    def peek(self, col=8: int) -> None:
        # Allows you to peek at memory, also outputs the bounds of the read only
        # memory and free memory (memory you can write to).
        # Parameter: col how many bytes per row
"""
import threading
from kernel import Kernel

def thread_function1(kernel):
    # TODO: STEP 1
    # VXNlIGRvbnRuZWVkIGhlcmUuIFRoaXMgbWV0aG9kIHdpbGwgY2F1c2UgYSBnaXZlbiByYW5nZSBvZiBtZW1vcnkgdG8gYmUgd3JpdHRlbiBiYWNrIHRvIGRpc2su
    pass

def thread_function2(kernel):
    # TODO: STEP 1
    # VXNlIHdyaXRlIGhlcmUgdG8gY2F1c2UgYSBjb3B5IG9uIHdyaXRlIChDT1cp
    pass
    
class KernelPatched(Kernel):
    def _copy_on_write(self, addr, buffer):
        # TODO: Modify this function to patch dirtyc0w
        # HINT:  c2VsZi5sb2NrIApodHRwczovL2RvY3MucHl0aG9uLm9yZy8zL2xpYnJhcnkvdGhyZWFkaW5nLmh0bWwjdGhyZWFkaW5nLkxvY2s=
        self._write_pointer = addr+self._root_mem_bound
        print("copy_write", self._write_pointer)
        self._memory[self._root_mem_bound:]= self._memory[:self._root_mem_bound]
        self._write(buffer)

if __name__ == "__main__":
    k = Kernel()

    # TODO: Uncomment this after patching the Kernel
    # k = KernelPatched()
    x = threading.Thread(target=thread_function1, args=(k,))
    y = threading.Thread(target=thread_function2, args=(k,))
    y.start()
    x.start()
    x.join()
    y.join()