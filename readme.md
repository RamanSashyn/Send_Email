Этот проект позволяет отправлять персонализированные email-сообщения с использованием Python и SMTP. Используются переменные окружения для защиты чувствительных данных, таких как логин и пароль.

Установка
Клонируйте репозиторий:
"""git clone https://github.com/your-username/your-repo.git

cd your-repo
"""

Создайте виртуальное окружение:
"""python -m venv .venv

source .venv/bin/activate # для Linux/MacOS

.venv\Scripts\activate # для Windows
"""

Установите зависимости:
"""pip install -r requirements.txt
"""

Создайте файл .env:
Скопируйте файл .env_example в .env:
cp .env_example .env # Linux/MacOS copy .env_example .env # Windows
Заполните файл .env реальными данными:
"""EMAIL_LOGIN=your_email@gmail.com

PASSWORD=your_password
"""

Запустите код:
"""python main.py
"""

Структура проекта
`Sendingemails/
├── .venv/
├── main.py
├── .env_example
├── .gitignore

Персонализация email
Вы можете изменить текст письма в файле main.py. Переменные friend_name, my_name и site_url заменяются на реальные значения.

Конфигурация SMTP
Для отправки email через Gmail используется:

SMTP-сервер: smtp.gmail.com
Порт: 465

Убедитесь, что у вашей учетной записи Gmail включен доступ для менее защищенных приложений или настроен OAuth2.
