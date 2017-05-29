"""

Below are the tests from CodeWars.

Test.assert_equals(summary_ranges([]),[])
Test.assert_equals(summary_ranges([1,1,1,1]),['1'])
Test.assert_equals(summary_ranges([1,2,3,4]),['1->4'])
Test.assert_equals(summary_ranges([0, 1, 2, 5, 6, 9]),["0->2", "5->6", "9"])
Test.assert_equals(summary_ranges([0, 1, 2, 3, 4, 5, 6, 7]),["0->7"])

"""
import pytest

RANGES_TESTS = [
    ([], []),
    ([1, 1, 1, 1], ['1']),
    ([1, 2, 3, 4], ['1->4']),
    ([0, 1, 2, 5, 6, 9], ["0->2", "5->6", "9"]),
    ([0, 1, 2, 3, 4, 5, 6, 7], ["0->7"]),
    ([100, 101], ['100->101']),
    ([0, 0, 0, 0], ['0']),
    ([-5, -4, -3, -2, 1, 2], ["-5->-2", "1->2"]),
    ([0, 1, 2, 3, 4, 5, 6, 7], ["0->7"])
]


@pytest.mark.parametrize('input_list, result', RANGES_TESTS)
def test_anagrams(input_list, result):
    """Test the output from the anagrams function."""
    from summarize_ranges import summary_ranges
    assert summary_ranges(input_list) == result
