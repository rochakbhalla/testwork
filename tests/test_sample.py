import pytest
# def func(x):
#     return x+1

# def test_answer():
#     assert func(2) == 4

'''
If you want to add a properties node at the test-suite level, which may contains properties that are relevant to all tests, you can use the record_testsuite_property session-scoped fixture:
The record_testsuite_property session-scoped fixture can be used to add properties relevant to all tests.
'''
@pytest.fixture(scope="session", autouse=True)
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("ARCH", "PPC")
    record_testsuite_property("STORAGE_TYPE", "CEPH")

#If you want to log additional information for a test, you can use the record_property fixture:
def test_function(record_property):
    record_property("example_key", 1)
    assert True

# To add attribute to the xml
def test_function1(record_xml_attribute):
    record_xml_attribute("assertions", "REQ-1234")
    record_xml_attribute("classname", "custom_classname")
    print("hello world")
    assert True

#pytest tests/test_sample.py -rA --maxfail=3 --junitxml=myfile.xml --resultlog=log.log

