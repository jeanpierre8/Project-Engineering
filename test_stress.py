import pytest
import requests
import json
import app


def test_home_get_200():
	assert requests.get('http://localhost:5000').status_code == 200