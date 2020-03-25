import os
import sys
from py.xml import html
import pytest
import logging

logger = logging.getLogger(__name__)

# #
# #
# This to resolved module import handling path issue
##
##
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# #
# #
# HTML Report Handler
##
##
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
