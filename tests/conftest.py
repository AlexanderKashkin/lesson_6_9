import pytest
from selene.support.shared import browser as b


@pytest.fixture(scope='function', autouse=True)
def set_window_size():
    b.config.window_width = 1920
    b.config.window_height = 1080
