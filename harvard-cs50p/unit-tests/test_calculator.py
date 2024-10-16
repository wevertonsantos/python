from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) != 4
    except AssertionError:
        print("2 squared was not 4")
       
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()