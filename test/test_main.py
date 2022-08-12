import re
from unittest import TestCase

from main import create_dict
from src.palette import Palette


class Test(TestCase):
    content = ["$bc-zapier-6: #13d0ab;",
               "$bc-zendesk: #000033;",
               "$bc-zendesk-1: #003;",
               "$bc-zendesk-2: #f79a3e;"]

    colors = create_dict(content)

    def test_check_content_ok(self):
        color_dict = {"bc-zapier": "#13d0ab", "bc-zendesk": "#000033 #003 #f79a3e"}
        self.assertEqual(self.colors, color_dict)

    def test_check_content_bad(self):
        color_dict = {"bc-zapier": "#13d0ab", "bc-zendesk": "#00363d,#f79a3e"}
        self.assertIsNot(self.colors, color_dict)

    def test_main(self):
        test_colors = ["bc-zapier: ['#13d0ab']", "bc-zendesk: ['#000033', '#003', '#f79a3e']"]
        str_colors = []
        for k, v in self.colors.items():
            c = Palette(k, v.split(' '))
            str_colors.append(str(c))
            print("generate file - generate png")

        self.assertEqual(str_colors, test_colors)