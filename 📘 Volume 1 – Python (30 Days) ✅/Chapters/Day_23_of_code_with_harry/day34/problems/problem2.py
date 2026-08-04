# .update()

# Create two dictionaries:

# ep1 = {122: 45, 123: 89}
# ep2 = {222: 67, 566: 90}

# Use .update() to add all key-value pairs of ep2 into ep1.

# Print ep1.


ep1 = {122: 45, 123: 89}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)