import pytest

try:
    from campus_agent.agent import get_campus_resource_info
except ImportError:
    # Fallback import if running tests from inside the campus_agent directory
    from agent import get_campus_resource_info

def test_library_lookup():
    """TEST 1: Verify standard library resource lookup."""
    result = get_campus_resource_info("library")
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert result.get("status") == "success"
    
    # Handles both flat dictionary returns and nested resource structures
    resource_name = result.get("name") or result.get("resource", {}).get("name")
    assert resource_name == "Library"

def test_tutoring_alias():
    """TEST 2: Verify that resource aliases work correctly."""
    result = get_campus_resource_info("tutoring")
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert result.get("status") == "success"
    
    resource_name = result.get("name") or result.get("resource", {}).get("name")
    assert resource_name == "Tutoring Center"

def test_case_insensitive():
    """TEST 3: Verify case-insensitivity in queries."""
    result = get_campus_resource_info("LIBRARY")
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert result.get("status") == "success"
    
    resource_name = result.get("name") or result.get("resource", {}).get("name")
    assert resource_name == "Library"

def test_resource_not_found():
    """TEST 4: Verify error handling when a resource doesn't exist."""
    result = get_campus_resource_info("dental office")
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert result.get("status") == "error"
    assert "error_message" in result
    assert "Available resources" in result["error_message"]

def test_list_all_resources():
    """TEST 5: Verify listing all available resources."""
    result = get_campus_resource_info("all")
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert result.get("status") == "success"
    assert "available_resources" in result
    
    resources_list = result["available_resources"]
    assert isinstance(resources_list, list), "available_resources must be a list"
    assert len(resources_list) >= 4, f"Expected at least 4 resources, found {len(resources_list)}"