tree_height = input("How tall is the tree:")
tree_height = int(tree_height)
spaces = tree_height - 1
Hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print(' ',end ="")
    for i in range (Hashes):
        print('#',end="")
    print()
    spaces -=1
    Hashes +=2
    tree_height -= 1
for i in range(stump_spaces):
    print(" ", end="")
print("#")
