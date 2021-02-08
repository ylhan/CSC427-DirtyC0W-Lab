#!/usr/bin/python3

import time
import threading

class Kernel:
    
    def __init__(self, f="rootfile.txt"):
        with open(f, 'r') as file:
            self.O00OOOOO00OOOO = list(file.read())
            self.O00OOOO000OOOO = len(self.O00OOOOO00OOOO)
            self.O00OOOOO00OOOO.extend(['u']*(self.O00OOOO000OOOO))
        self._file = f
        self.O00OOOOO00OO0O = 0
        self.lock = threading.Lock()

    def write(self, addr, buffer):
        addr = int(addr, 16)
        if addr < 0:
            raise AddressError("You can't write to a negative address.")

        if addr >= len(self.O00OOOOO00OOOO):
            raise AddressError(f"The address you are trying to write to is >= {len(self.O00OOOOO00OOOO)} (size of memory).")

        if addr >= self.O00OOOO000OOOO and len(buffer) > (len(self.O00OOOOO00OOOO)-addr):
            raise MemoryError(f"Your buffer is too large to fit in memory at your given address.")

        if addr < self.O00OOOO000OOOO and len(buffer) > (self.O00OOOO000OOOO-addr):
            raise MemoryError(f"Your buffer is too large to fit in memory at your given address.")

        # Write to user memory
        if addr >= self.O00OOOO000OOOO:
            self.O00OOOOO00O00O(addr, buffer)
        
        # Writing to root memory: copy on write
        if addr < self.O00OOOO000OOOO:
            self.O00OOOOO00OO00(addr, buffer)
    
    def O00OOOOO00O00O(self, buffer):
        time.sleep(0.01)
        # print("_write: " + str(self.O00OOOOO00OO0O))
        j = 0
        for i in range(self.O00OOOOO00OO0O, self.O00OOOOO00OO0O+len(buffer)):
            self.O00OOOOO00OOOO[i] = buffer[j]
            j += 1

    def O00OOOOO00OO00(self, addr, buffer):
        time.sleep(0.01)
        # print("copy on write: " + str(self.O00OOOOO00OO0O))
        self.O00OOOOO00OO0O = addr+self.O00OOOO000OOOO
        self.O00OOOOO00OOOO[self.O00OOOO000OOOO:]= self.O00OOOOO00OOOO[:self.O00OOOO000OOOO]
        self.O00OOOOO00O00O(buffer)

    def dontneed(self, addr, length):
        self.lock.acquire()
        self.O00OOOOO00OO0O = int(addr, 16)
        # Write back to disk
        if self.O00OOOOO00OO0O < 0:
            raise AddressError("You can't write to a negative address.")

        if self.O00OOOOO00OO0O >= len(self.O00OOOOO00OOOO):
            raise AddressError(f"The address you are trying to write to is >= {len(self.O00OOOOO00OOOO)} (size of memory).")

        if self.O00OOOOO00OO0O >= self.O00OOOO000OOOO:
            print("No write permissions to rootfile discarding memory...")
            self.O00OOOOO00OOOO[self.O00OOOO000OOOO:] = ['u']*(self.O00OOOO000OOOO)
            return

        if self.O00OOOOO00OO0O < self.O00OOOO000OOOO and self.O00OOOOO00OO0O + length > self.O00OOOO000OOOO:
            raise AddressError("Length too long. No write permissions to rootfile discarding memory...")
        
        with open(self._file, 'w') as file:
            out = "".join(self.O00OOOOO00OOOO[self.O00OOOOO00OO0O:self.O00OOOOO00OO0O+length])
            file.write(out)
        self.lock.release()

    def peek(self, col=8):
        if col <= 0:
            print(f"Provided columns per row must be > 0")
            return

        print(f"Read only bounds: {0:08x}...{self.O00OOOO000OOOO-1:08x}")
        print(f"Free bounds:      {self.O00OOOO000OOOO-1:08x}...{len(self.O00OOOOO00OOOO)-1:08x}")
        print("=== Memory ===")
        for i in range(0, len(self.O00OOOOO00OOOO), col):
            out = f"0x{i:08x}: "
            for j in range(i, min(i+col, len(self.O00OOOOO00OOOO))):
                out += f" {self.O00OOOOO00OOOO[j]}"
            print(out)


class MemoryError(Exception):
    def __init__(self, message):
        super().__init__(message)

class AddressError(Exception):
    def __init__(self, message):
        super().__init__(message)
