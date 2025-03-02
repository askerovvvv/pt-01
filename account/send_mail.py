from django.core.mail import send_mail


def send_activation_code(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'

    send_mail(
        'Activation code TEST DJANGO',
        full_link,
        'bekbol.2019@gmail.com',
        [email]
    )

