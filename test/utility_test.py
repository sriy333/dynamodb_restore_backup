import dynamodb.utility
import unittest


class UtilityTest(unittest.TestCase):

    def test_testing_via_cli(self):
        dynamodb.utility.login_via_cli()


if __name__ == '__main__':
    unittest.main()
