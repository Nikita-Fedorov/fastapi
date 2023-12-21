from pathlib import Path

from pydantic import EmailStr
from app.config import settings
from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_template
from PIL import Image
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# @celery.task
# def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
#     email_to = settings.SMTP_USER
#     msg_content = create_booking_confirmation_template(booking, email_to)

#     # Создайте MIMEMultipart объект
#     msg = MIMEMultipart()
#     msg.attach(MIMEText(msg_content, 'html'))

#     # Добавьте необходимые заголовки, например, заголовок "Subject"
#     msg['Subject'] = 'Booking Confirmation'

#     # Укажите отправителя и получателя
#     msg['From'] = settings.SMTP_USER
#     msg['To'] = email_to

#     # Подключитесь к серверу SMTP
#     with smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT) as server:
#         # Включите шифрование STARTTLS
#         server.starttls()

#         # Войдите в учетную запись
#         server.login(user=settings.SMTP_USER, password=settings.SMTP_PASS)

#         # Отправьте письмо
#         server.sendmail(settings.SMTP_USER, email_to, msg.as_string())


@celery.task
def process_pic(path: str):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_1000_500 = im.resize((1000, 500))

    im_resized_200_100 = im.resize((200, 100))
    im_resized_1000_500.save(
        f'app/static/images/resized_1000_500_{im_path.name}'
    )
    im_resized_200_100.save(
        f'app/static/images/resized_200_100_{im_path.name}'
    )


@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    email_to = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(
        host=settings.SMTP_HOST, port=settings.SMTP_PORT
    ) as server:
        server.login(user=settings.SMTP_USER, password=settings.SMTP_PASS)
        server.send_message(msg_content)
