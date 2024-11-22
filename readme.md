# Персонализированные Email-сообщения с Python и SMTP

Этот проект позволяет отправлять персонализированные email-сообщения с использованием Python и SMTP. Используются переменные окружения для защиты чувствительных данных, таких как логин и пароль.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

    Для активации виртуального окружения:
    
    - **Linux/MacOS**:
    
    ```bash
    source .venv/bin/activate
    ```
    
    - **Windows**:
    
    ```bash
    .venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env`:

    Скопируйте файл `.env_example` в `.env`:

    - **Linux/MacOS**:
    
    ```bash
    cp .env_example .env
    ```

    - **Windows**:
    
    ```bash
    copy .env_example .env
    ```

5. Заполните файл `.env` реальными данными:

    ```env
    EMAIL_LOGIN=your_email@gmail.com
    PASSWORD=your_password
    ```

6. Запустите код:

    ```bash
    python main.py
    ```

## Структура проекта
`Sendingemails/
├── .venv/
├── main.py
├── .env_example
├── .gitignore


## Персонализация email

Вы можете изменить текст письма в файле `main.py`. Переменные `friend_name`, `my_name` и `site_url` заменяются на реальные значения.

## Конфигурация SMTP

Для отправки email через Gmail используется:

- SMTP-сервер: `smtp.gmail.com`
- Порт: `465`

Убедитесь, что у вашей учетной записи Gmail включен доступ для менее защищенных приложений или настроен OAuth2.

