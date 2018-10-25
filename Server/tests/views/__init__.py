from unittest import TestCase


class TestCaseBase(TestCase):
    def __int__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass
