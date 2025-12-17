import pytest
import sys
if __name__ == "__main__":
    exit_code = pytest.main(["-v", "test_my_math_lib.py"])
    sys.exit(exit_code)
