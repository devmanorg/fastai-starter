# Пользователям стартера

Стартер — это заготовка проекта, которая помогает быстро приступить к разработке нового ПО. Включет в себя репозиторий с предварительно настроенными инструментами: структура каталогов, зависимости, линтеры, минимальная документация и не только. 

## Чеклист проверки настройки стартера для своего проекта

- [ ] Все файлы и папки стартера скопированы в корень нового проекта
    - **Исключение**: скрытая папка `/.git` -- эта папка должна сохраниться в вашем локальном репозитории без изменений
- В файле [pyproject.toml](pyproject.toml) изменены:
    - [ ] название проекта
    - [ ] описание проекта
    - [ ] версия проекта
- [ ] Из [README.md](README.md) удалено упоминание файла с инструкциями к стартеру [USING_STARTER.md](USING_STARTER.md)

После выполнения всех пунктов удалите из вашего репозитория этот файл с инструкциями к стартеру [./USING_STARTER.md](USING_STARTER.md).
