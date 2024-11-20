import smtplib
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="D:/Py/Sendingemails/secret.env")

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
PASSWORD = os.getenv("PASSWORD")

site_url = "https://dvmn.org/profession-ref-program/romasashin60/2UGfN/"

friend_name = "Артем"

sender_email = EMAIL_LOGIN

my_name = "Рома"

email_to = "romasashin60@gmail.com"

subject = "Приглашение на курс!"

text_email = f"""\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

text_email = text_email.replace("%website%", site_url)
text_email = text_email.replace("%friend_name%", friend_name)
text_email = text_email.replace("%my_name%", my_name)

letter = """\
From: {sender_email}
To: {email_to}
Reply-To: {sender_email}
Subject: {subject}
Content-Type: text/plain; charset=utf-8

{text}""".format(
    sender_email=sender_email,
    email_to=email_to,
    subject=subject,
    text=text_email,
)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_LOGIN, PASSWORD)
server.sendmail(sender_email, email_to, letter.encode("utf-8"))
server.quit()

