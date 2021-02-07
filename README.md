# CSC427-DirtyC0W-Lab

Welcome to the Dirty Cow lab!

NOTE: There are hints spread out through the file (base64 encoded). You can 
decode these strings if you need a hint.

HINT: aHR0cHM6Ly9naXRodWIuY29tL2RpcnR5Y293L2RpcnR5Y293LmdpdGh1Yi5pby9ibG9iL21hc3Rlci9kaXJ0eWMwdy5j

Step 1: Fill in the two thread_function's using the methods provided by the
Kernel so that rootfile.txt is modified. 

NOTE: Run `python3 kernel.pyc` and play around with the kernel and it's methods
to get more familar with them. The docstring and function stubs are provided
for you below.

ORIGINAL: HAHA ONLY ROOT CAN WRITE TO THIS!
    GOAL: HAHA I CAN WRITE TO THIS!

Step 2: Modify the _copy_on_write method in KernelPatched to patch the dirty
cow exploit. Remember to uncomment # k = KernelPatched() in the main block below
after you patch the kernel

You're done! 