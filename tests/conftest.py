import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


# Preserve a deep copy of the original activities so tests can be isolated
ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Provides a TestClient for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_state():
    """Reset module-level in-memory `activities` to the original state after each test.

    This runs automatically for every test to ensure isolation.
    """
    yield
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
