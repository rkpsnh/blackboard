import blackboard


def test_package_imports() -> None:
    assert blackboard.__version__ == "0.1.0a0"
