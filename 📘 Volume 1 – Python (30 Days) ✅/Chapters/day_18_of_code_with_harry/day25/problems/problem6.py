# Deadly Moderate
# countries = ("India", "USA", "Japan", "Germany", "Australia")

# Convert the tuple into a list.

# Then:

# Add "Canada"
# Remove "USA"
# Replace "Japan" with "South Korea"
# Convert it back into a tuple.
# Print the final tuple.


countries = ("India", "USA", "Japan", "Germany", "Australia")
new = list(countries)
new.append("Canada")
new.remove("USA")
new[2] = "South Korea"
countries = tuple(new)
print(countries)