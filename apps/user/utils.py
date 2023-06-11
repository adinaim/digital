import re
from django.contrib.auth import get_user_model

User = get_user_model()


def normalize_phone(phone):
    phone = re.sub('[^0-9]', '', phone)
    if phone.startswith('0'):
        phone = f'996{phone[1:]}'
    if not phone.startswith('996'):
        phone = f'996{phone}'
    phone = f'+{phone}'
    return phone

def activate_account(self):
    if user.code_method == 'phone':
        phone = self.validated_data.get('phone')
        user = User.objects.get(phone=phone)
    elif user.code_method == 'email':
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
    user.is_active = True
    user.activation_code = ''
    user.save()