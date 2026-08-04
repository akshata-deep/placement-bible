ep1 = {
    122: 45,
    123: 89,
    567: 69
}

ep2 = {
    222: 67,
    566: 90
}


ep1.update(ep2)
ep1.pop(122)
ep1.popitem()
print(ep1)