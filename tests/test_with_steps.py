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
def test_with_steps(set_window_size):
    with allure.step(f'Открываем ссылку {github}'):
        browser.open(github)
    with allure.step(f'Ищем репозиторий {repo}'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys(f'{repo}')
        s('.header-search-input').submit()
    with allure.step(f'Переходим в репозиторий {repo}'):
        s(by.link_text(f'{repo}')).click()
    with allure.step('Кликаем по табу issues'):
        s('#issues-tab').click()
    with allure.step(f'Ищем issues_number с номером {issues_number}'):
        s(by.partial_text(f'{issues_number}')).should(be.visible)
