import pytest
import os


def test():
    pytest.main([os.path.abspath(os.path.dirname(__file__)) + '/tests'])

if __name__ == '__main__':
    test()
