from hypothesis import (
    given,
    strategies as st,
)
from trie.utils.nibbles import (
    nibbles_to_bytes,
    bytes_to_nibbles,
)


# @given(value=st.binary(min_size=0, max_size=1024))
# def test_round_trip_nibbling(value):
#     value_as_nibbles = bytes_to_nibbles(value)
#     result = nibbles_to_bytes(value_as_nibbles)
#     assert result == value
