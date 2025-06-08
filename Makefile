lint: ## Проверяет линтерами код в репозитории
	ruff check ./src
format: ## Запуск автоформатера
	ruff check --fix ./src
