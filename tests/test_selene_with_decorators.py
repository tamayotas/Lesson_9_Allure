import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Sergey Tamaev")
@allure.feature("Decorators")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_github():
    open_main_page()
    search_for_repository("tamayotas/Lesson_9_Allure")
    go_to_repository("tamayotas/Lesson_9_Allure")
    open_issue_tab()
    should_see_issue_with_number()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")

@allure.step("Ищем репозиторий {repo} ")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозиторий {repo} ")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером 3")
def should_see_issue_with_number():
    s(by.partial_text("#3")).should(be.visible)