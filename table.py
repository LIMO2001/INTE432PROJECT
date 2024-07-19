class Table:
  # Same as before... (Table class definition)
  def show_tables(tables):
  #Prints information about all tables in the list."""
     print("Tables:")
  for table in tables:
    print(f"  - Table {table.table_number}: {table.status}")

# Create some tables
tables = [Table(1), Table(2), Table(3)]

# Set some statuses
tables[0].set_status('Occupied')
tables[2].set_status('Reserved')

# Show tables
show_tables(tables)

table = [
  ["Name", "Age", "City"],
  ["Alice", 30, "New York"],
  ["Bob", 25, "London"],
]

# Accessing elements
name = table[1][0]  # Accessing "Alice"
age = table[2][1]  # Accessing 25

# Printing the table
for row in table:
  print(row)

