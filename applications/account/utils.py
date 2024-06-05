from email import message

from django.core.mail import send_mail
from django.core.mail import EmailMessage


def send_activation_code(email, code):
    message = f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n http://127.0.0.1:8000/api/v1/account/activate/{code}'

    email_message = EmailMessage(
        'Samirkk',
        message,
        'iptest228228@gmail.com',
        [email],
    )

    email_message.attach_file('C:/Users/user/PycharmProjects/samirkkk/emailimages/samirkk_.png')

    email_message.send()


def send_forgot_password_code(email, code):
    send_mail(
        'Samirkk',
        f'Вот ваш код для востоновления пароля, никому не показывайте его: {code}',
        'iptest228228@gmail.com',
        [email]
    )


