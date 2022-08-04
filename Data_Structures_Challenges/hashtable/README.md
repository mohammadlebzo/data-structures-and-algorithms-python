# Hashtables
<!-- Short summary or background information -->

HashTables or HashMaps are a type of abstract data, that can be used to map keys to values.

## Challenge
<!-- Description of the challenge -->

Implement a Hashtable Class with the following methods:

- set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
- get
  - Arguments: key
  - Returns: Value associated with that key in the table
- contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- keys
  - Returns: Collection of keys
- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

All methods don't use loops except the get() method, which takes a liner iterative approach, as for the Big O:

- _set_:

  - **Time**: O(1)
  - **Space**: O(n) because we created a linked list within the hashmap.

- _get_:

  - **Time**: O(n)
  - **Space**: O(n) because we created a list.

- _contains_:

  - **Time**: O(n)
  - **Space**: O(n) as the get function is called, and it creates a list within it

- _keys_:

  - **Time**: O(1)
  - **Space**: O(1)

- _hash_:

  - **Time**: O(1)
  - **Space**: O(1)

## API
<!-- Description of each method publicly available in each of your hashtable -->

- _set_: this method inserts data to the hash table.
- _get_: this method gets value of a passed key, also handles collision.
- _contains_: this method checks wither a value is available with in the hash table or not.
- _keys_: this method returns a collection of all the keys within the hashed table.

