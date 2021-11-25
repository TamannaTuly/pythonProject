# assert sum([2,3])==1, 'test result should be 5'
# sum = 5*5
# assert sum == 25, '52'

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
