import sys
import os
import pytest

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel" in header.text


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
