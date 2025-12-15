import pytest
import sys
import os
from io import StringIO

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def check_hardcoding():
    """Helper function to check for hard-coding with test data"""
    with open('task1.py', 'r') as f:
        code = f.read()
    
    # Replace initial values with different ones
    modified_code = code.replace('people = 2', 'people = 3')
    modified_code = modified_code.replace('bagA = 23', 'bagA = 30')
    modified_code = modified_code.replace('bagB = 17', 'bagB = 25')
    modified_code = modified_code.replace('bagC = 19', 'bagC = 20')
    
    # Execute modified code and capture output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        exec(modified_code)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Check if outputs match expected values with modified inputs
    expected_total = 75
    expected_first_share = 18
    expected_second_share = 15
    
    hardcoded = False
    
    if str(expected_total) not in output:
        hardcoded = True
    if str(expected_first_share) not in output:
        hardcoded = True
    if str(expected_second_share) not in output:
        hardcoded = True
    
    return hardcoded


def test_total_candy_variable_exists():
    """Test that total_candy variable exists"""
    try:
        import task1
        assert hasattr(task1, 'total_candy'), "Missing required variable: total_candy"
    except ImportError:
        pytest.fail("Could not import task1.py")


def test_share_variable_exists():
    """Test that share variable exists"""
    try:
        import task1
        assert hasattr(task1, 'share'), "Missing required variable: share"
    except ImportError:
        pytest.fail("Could not import task1.py")


def test_leftover_variable_exists():
    """Test that leftover variable exists"""
    try:
        import task1
        assert hasattr(task1, 'leftover'), "Missing required variable: leftover"
    except ImportError:
        pytest.fail("Could not import task1.py")


def test_total_candy(capsys):
    """Test total candy calculation - 3 points"""
    try:
        import task1
        import importlib
        importlib.reload(task1)
    except ImportError:
        pytest.fail("Could not import task1.py")
    
    output = capsys.readouterr().out
    expected_total = 59
    
    assert str(expected_total) in output, "total_candy miscalculated or not printed"
    assert task1.total_candy == expected_total, "total_candy miscalculated"
    assert not check_hardcoding(), "Hard-coding detected"


def test_first_each_share(capsys):
    """Test first division - share with 3 people - 3 points"""
    try:
        import task1
        import importlib
        importlib.reload(task1)
    except ImportError:
        pytest.fail("Could not import task1.py")
    
    output = capsys.readouterr().out
    expected_share = 19
    
    assert str(expected_share) in output, "share miscalculated in scenario 1"
    assert not check_hardcoding(), "Hard-coding detected"


def test_first_leftover(capsys):
    """Test first division - leftover with 3 people - 2 points"""
    try:
        import task1
        import importlib
        importlib.reload(task1)
    except ImportError:
        pytest.fail("Could not import task1.py")
    
    output = capsys.readouterr().out
    expected_leftover = 2
    
    assert str(expected_leftover) in output, "leftover miscalculated in scenario 1"
    assert not check_hardcoding(), "Hard-coding detected"


def test_second_each_share(capsys):
    """Test second division - share with 4 people - 3 points"""
    try:
        import task1
        import importlib
        importlib.reload(task1)
    except ImportError:
        pytest.fail("Could not import task1.py")
    
    output = capsys.readouterr().out
    expected_share = 14
    lines = output.split('\n')
    
    assert str(expected_share) in '\n'.join(lines[-3:]), "share miscalculated in scenario 2"
    assert task1.share == expected_share, "share miscalculated in scenario 2"
    assert not check_hardcoding(), "Hard-coding detected"


def test_second_leftover(capsys):
    """Test second division - leftover with 4 people - 2 points"""
    try:
        import task1
        import importlib
        importlib.reload(task1)
    except ImportError:
        pytest.fail("Could not import task1.py")
    
    output = capsys.readouterr().out
    expected_leftover = 3
    lines = output.split('\n')
    
    assert str(expected_leftover) in '\n'.join(lines[-2:]), "leftover miscalculated in scenario 2"
    assert task1.leftover == expected_leftover, "leftover miscalculated in scenario 2"
    assert not check_hardcoding(), "Hard-coding detected"
