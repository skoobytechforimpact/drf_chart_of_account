"""Chart of Accounts App Testing Environment."""
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()
    args = sys.argv + ["makemigrations", "drf_chart_of_account"]
    execute_from_command_line(args)
    args = sys.argv + ["migrate", "drf_chart_of_account"]
    execute_from_command_line(args)
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
