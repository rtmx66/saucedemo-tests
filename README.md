# 🧪 Saucedemo Automated Tests

Автоматизированные UI-тесты для [saucedemo.com](https://www.saucedemo.com) на Python + Playwright.

## 📋 Покрытие тестами

| Модуль | Тесты |
|--------|-------|
| Авторизация | Валидный логин, неверный пароль, пустые поля, заблокированный пользователь |
| Корзина | Добавление товара, несколько товаров, удаление, сохранение после навигации |
| Оформление заказа | Успешный заказ, валидация пустых полей формы |
| Сортировка | По цене (↑↓), по названию (A-Z, Z-A) |

**Итого: 16 тестов**

## 🛠 Технологии

- Python 3.14
- Playwright
- Pytest
- GitHub Actions (CI/CD)
- Page Object Model (POM)

## 🚀 Запуск

```bash
# Установка зависимостей
pip install pytest playwright pytest-playwright
playwright install

# Запуск всех тестов
pytest tests/ -v

# Запуск конкретного модуля
pytest tests/test_login.py -v
```

## 📁 Структура проекта

```
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_sorting.py
├── conftest.py
└── pytest.ini
```