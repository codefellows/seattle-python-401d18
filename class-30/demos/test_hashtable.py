import pytest
from data_structures.hashtable import Hashtable

"""
set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
get
Arguments: key
Returns: Value associated with that key in the table
contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
keys
Returns: Collection of keys

"""


def test_exists():
    assert Hashtable


def test_create_default():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected


def test_hash():
    """
    hash
Arguments: key
Returns: Index in the collection for that key
    """
    ht = Hashtable()
    index = ht.hash("cat")
    assert 0 <= index < ht.size


def test_set_apple():
    ht = Hashtable()
    ht.set("fruit", "apple")
    fruit_index = ht.hash("fruit")
    actual = ht.buckets[fruit_index]
    expected = ("fruit", "apple")
    assert actual.head.value == expected


def test_get_apple():
    ht = Hashtable()
    ht.set("fruit", "apple")
    actual = ht.get("fruit")
    expected = "apple"
    assert actual == expected


def test_collisions():
    ht = Hashtable()
    ht.set("cat", "Josie")
    ht.set("act", "A Contemporary Theater")
    ht.set("tac", "Taco Tuesday")

    assert ht.get("cat") == "Josie"
    assert ht.get("act") == "A Contemporary Theater"
    assert ht.get("tac") == "Taco Tuesday"
