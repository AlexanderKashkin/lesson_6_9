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
@allure.step(f'Открываем ссылку {github}')
def open_link(link: str) -> None:
    browser.open(link)


@allure.step(f'Ищем репозиторий {repo}')
def find_repo(link_repo: str) -> None:
    s('.header-search-input').click()
    s('.header-search-input').send_keys(f'{link_repo}')
    s('.header-search-input').submit()


@allure.step(f'Переходим в репозиторий {repo}')
def click_to_repo(link_repo: str) -> None:
    s(by.link_text(f'{link_repo}')).click()


@allure.step('Кликаем по табу issues_number')
def find_tab_issues() -> None:
    s('#issues-tab').click()


@allure.step(f'Ищем issues_number с номером {issues_number}')
def check_issues(number: str) -> None:
    s(by.partial_text(f'{number}')).should(be.visible)


def test_with_func(set_window_size):
    open_link(github)
    find_repo(repo)
    click_to_repo(repo)
    find_tab_issues()
    check_issues(issues_number)
