import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from . import issues_number, repo, github


@allure.tag('Web')
@allure.epic('lesson_6_9')
@allure.feature('test with steps')
@allure.label("owner", "alexander_kashkin")
@allure.severity(Severity.NORMAL)
def test_simple_selene():
    browser.open(github)

    s('.header-search-input').click()
    s('.header-search-input').send_keys(f'{repo}')
    s('.header-search-input').submit()

    s(by.link_text(f'{repo}')).click()

    s('#issues-tab').click()

    s(by.partial_text(f'{issues_number}')).should(be.visible)
