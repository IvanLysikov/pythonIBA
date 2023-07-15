import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time


class TheInternetTests(unittest.TestCase):
    def setUp(self):
        # Запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()

    def wait_for_page_to_load(self):
        # Ожидание загрузки страницы
        time.sleep(2)

    def test_basic_authentication(self):
        driver = self.driver
        # Имя пользователя и пароль для аутентификации
        username = "admin"
        password = "admin"
        # Создание URL с именем пользователя и паролем
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        # Открытие в Chrome страницы с базовой аутентификацией
        driver.get(url)
        self.wait_for_page_to_load()
        # Проверка успешной аутентификации
        self.assertIn("Congratulations!", driver.page_source)

    def test_checkboxes(self):
        driver = self.driver
        # Открытие в Chrome страницы с флажками (чекбоксами)
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        self.wait_for_page_to_load()
        # Поиск флажков на странице
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        # Проверка начального состояния флажков (неотмечены)
        self.assertFalse(checkboxes[0].is_selected())
        self.assertTrue(checkboxes[1].is_selected())
        # Изменение состояния флажков
        checkboxes[0].click()
        checkboxes[1].click()
        # Проверка измененного состояния флажков
        self.assertTrue(checkboxes[0].is_selected())
        self.assertFalse(checkboxes[1].is_selected())

    def test_dynamic_controls(self):
        driver = self.driver
        # Открытие в Chrome страницы с динамическими элементами управления
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        self.wait_for_page_to_load()
        # Поиск кнопки "Enable"
        enable_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enable')]")
        # Поиск поля ввода
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text'][disabled][style='width: 30%;']")
        # Проверка начального состояния поля ввода (оно должно быть disabled)
        self.assertFalse(input_field.is_enabled())
        # Нажатие кнопки "Enable"
        enable_button.click()
        # Ожидание изменения состояния поля ввода
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']:not([disabled])[style='width: 30%;']")))
        # Обновление ссылки на элемент поля ввода
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']:not([disabled])[style='width: 30%;']")
        # Проверка измененного состояния поля ввода (оно должно быть enabled)
        self.assertTrue(input_field.is_enabled())

    def test_dropdown(self):
        driver = self.driver
        # Открытие в Chrome страницы с выпадающим списком
        driver.get("https://the-internet.herokuapp.com/dropdown")
        self.wait_for_page_to_load()
        # Поиск выпадающего списка
        dropdown = driver.find_element(By.ID, "dropdown")
        # Выбор значения из выпадающего списка
        webdriver.support.ui.Select(dropdown).select_by_visible_text("Option 1")
        # Проверка выбранного значения
        selected_option = webdriver.support.ui.Select(dropdown).first_selected_option
        self.assertEqual(selected_option.text, "Option 1")


    def test_hover(self):
        driver = self.driver
        # Открытие в Chrome страницы с наведением мыши на элементы
        driver.get("https://the-internet.herokuapp.com/hovers")
        self.wait_for_page_to_load()
        # Поиск элементов для наведения мыши
        avatars = driver.find_elements(By.CLASS_NAME, "figure")
        # Наведение мыши на каждый элемент
        for avatar in avatars:
            webdriver.ActionChains(driver).move_to_element(avatar).perform()
            # Проверка отображения имени пользователя при наведении
            user_name = avatar.find_element(By.TAG_NAME, "h5")
            self.assertTrue(user_name.is_displayed())

    def test_key_presses(self):
        driver = self.driver
        # Открытие в Chrome страницы для обработки нажатий клавиш
        driver.get("https://the-internet.herokuapp.com/key_presses")
        self.wait_for_page_to_load()
        # Нажатие клавиши "Enter" и проверка отображения результата
        input_field = driver.find_element(By.ID, "target")
        input_field.send_keys(Keys.SHIFT)
        result = driver.find_element(By.ID, "result")
        self.assertEqual(result.text, "You entered: SHIFT")

    def tearDown(self):
        # Закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
