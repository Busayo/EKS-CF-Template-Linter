from sys import prefix
from unittest import TestCase
from pathlib import Path

import pytest

from cloud_radar.cf.unit._template import (
    Template,
)


@pytest.fixture
def template():
    template_path = Path(__file__).parent / \
        "/Users/busayo.akanni/Desktop/templates/amazon-eks-controlpane-template.yaml" #ensure to change the file path appropriately.

    return Template.from_yaml(template_path.resolve(), {})


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)
