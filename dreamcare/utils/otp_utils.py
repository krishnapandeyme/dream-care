from random import randrange
from dreamcare.utils.jwt_utils import encode
import requests

SMS_API_URL = "http://sms.textmysms.com/app/smsapi/index.php?" \
              "key=55EB69B252E489&routeid=13&type=text&" \
              "senderid=SOFTLZ&msg=Your OTP is \n{}&campaign=0&contacts={}"


def generate_otp():
    otp = ""
    for i in range(4):
        otp += str(randrange(10))
    return otp


def send_otp(user):
    otp = generate_otp()
    mobile = user.get('mobile', '')
    payload = {
        'mobile': mobile,
        'otp': otp
    }
    otp_token = encode(payload)
    res = requests.get(SMS_API_URL.format(otp, mobile[3:]))
    if res.status_code == 200:
        return otp, otp_token
    else:
        return None, None



