import pytest
import sys
import os
from io import StringIO

# Add parent directory to path to import student's code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def check_hardcoding():
    """Helper function to check for hard-coding with test data"""
    with open('task2.py', 'r') as f:
        code = f.read()
    
    # Replace with test dataset
    modified_code = code.replace('allowance = 10', 'allowance = 15')
    modified_code = modified_code.replace('dishes, room, trash, lawn, laundry, vacuum = 3, 5, 2, 8, 4, 6',
                                         'dishes, room, trash, lawn, laundry, vacuum = 4, 6, 3, 10, 5, 7')
    modified_code = modified_code.replace('candy, soda, game, movie, toy, snack = 4, 2, 15, 10, 7, 3',
                                         'candy, soda, game, movie, toy, snack = 5, 3, 20, 12, 9, 4')
    
    # Execute modified code and capture output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        namespace = {}
        exec(modified_code, namespace)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Calculate expected values with test dataset
    # Week 1: 15 + 4 + 6 - 5 = 20
    # Week 2: 20 * 2 + 10 - 20 = 30
    # Week 3: 30 / 2 = 15.0
    expected_final = 15.0
    
    hardcoded = False
    
    if 'allowance' in namespace and namespace['allowance'] != expected_final:
        hardcoded = True
    if str(expected_final) not in output and "15.0" not in output:
        hardcoded = True
    
    return hardcoded


def test_allowance_variable_exists():
    """Test that allowance variable exists"""
    try:
        import task2
        assert hasattr(task2, 'allowance'), "Missing required variable: allowance"
    except ImportError:
        pytest.fail("Could not import task2.py")


def test_week1_operations(capsys):
    """Test Week 1 operations - 3 points"""
    try:
        import task2
        import importlib
        importlib.reload(task2)
    except ImportError:
        pytest.fail("Could not import task2.py")
    
    assert not check_hardcoding(), "Hard-coding detected"


def test_week2_operations(capsys):
    """Test Week 2 operations - 3 points"""
    try:
        import task2
        import importlib
        importlib.reload(task2)
    except ImportError:
        pytest.fail("Could not import task2.py")
    
    assert not check_hardcoding(), "Hard-coding detected"


def test_week3_operations(capsys):
    """Test Week 3 operations - 3 points"""
    try:
        import task2
        import importlib
        importlib.reload(task2)
    except ImportError:
        pytest.fail("Could not import task2.py")
    
    expected_final = 10.5
    assert task2.allowance == expected_final, "allowance miscalculated in Week 3"
    assert not check_hardcoding(), "Hard-coding detected"


def test_output_format(capsys):
    """Test output format - 2 points"""
    try:
        import task2
        import importlib
        importlib.reload(task2)
    except ImportError:
        pytest.fail("Could not import task2.py")
    
    output = capsys.readouterr().out
    expected_final = 10.5
    
    assert "Allowance:" in output or "allowance:" in output, "Output missing 'Allowance:'"
    assert str(expected_final) in output, "Output missing final allowance value"
    assert not check_hardcoding(), "Hard-coding detected"
