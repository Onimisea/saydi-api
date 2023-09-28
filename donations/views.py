import json
import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Donation
from .serializers import CreateDonationSerializer
from django.shortcuts import get_object_or_404
from django.conf import settings

api_key = settings.PAYSTACK_TEST_SECRET_KEY
customer_url = settings.PAYSTACK_CREATE_CUSTOMER_URL
init_url = settings.PAYSTACK_PAYMENT_INIT_URL
subscription_url = settings.PAYSTACK_SUBSCRIPTION_URL
list_plans = settings.PAYSTACK_LISTPLANS_URL

headers = {"authorization": f"Bearer {api_key}"}

plans = {
    "weekly": "PLN_w16amc2k1nj99yx",
    "monthly": "PLN_lmez2fllqeafu4v",
    "quarterly": "PLN_abs9mcdsc2ea7cm",
    "semi-annually": "PLN_4quktdlkhzagpxd",
    "annually": "PLN_l920yjb71pser2f",
}

success_url = "https://saydi.org/"
cancel_url = "https://saydi.org/?error=failed"


class CreateDonationView(APIView):
    def post(self, request, format=None):

        data = request.data

        if 'frequency' not in data:
            data['frequency'] = "one-time"

        serializer = CreateDonationSerializer(data=data)

        if serializer.is_valid():
            donation = serializer.save()

            metadata = json.dumps({"donation_id": donation.id, "frequency": data["frequency"], 'first_name': donation.first_name,
                                   'last_name': donation.last_name, "cancel_action": cancel_url, })

            # print(donation)

            if data['frequency'] == "one-time":
                donation_data = {
                    'email': donation.email,
                    'amount': int(donation.amount) * 100,
                    'callback_url': success_url,
                    'metadata': metadata
                }

                r = requests.post(
                    init_url, headers=headers, data=donation_data)
                res = r.json()

                response_data = {
                    "checkout_url": res['data']['authorization_url']
                }

                return Response(response_data, status=status.HTTP_201_CREATED)

            else:
                check = requests.get(
                    f"https://api.paystack.co/customer/{donation.email}", headers=headers)

                exists = check.json()

                if exists['status']:
                    cus_subs = exists['data']['subscriptions']
                    cus_code = exists['data']['customer_code']
                    cus_auth_code = exists['data']['authorizations'][-1]['authorization_code']

                    if len(cus_subs) > 0:
                        sb_data = {"authorization_code": cus_auth_code,
                                   "email": donation.email, "amount": donation.amount * 100, "metadata": metadata}

                        r2 = requests.post(
                            "https://api.paystack.co/transaction/charge_authorization", headers=headers, data=sb_data)
                        res2 = r2.json()

                        if res2['status']:
                            return Response({"success": "Donation received successfully"}, status=status.HTTP_200_OK)

                    else:
                        if donation.frequency == "weekly":
                            plan = plans["weekly"]
                        elif donation.frequency == "monthly":
                            plan = plans["monthly"]
                        elif donation.frequency == "quarterly":
                            plan = plans["quarterly"]
                        elif donation.frequency == "semi-annually":
                            plan = plans["semi-annually"]
                        elif donation.frequency == "annually":
                            plan = plans["annually"]

                        donation_data = {
                            'email': donation.email,
                            'amount': int(donation.amount) * 100,
                            'plan': plan,
                            'callback_url': success_url,
                            'metadata': metadata
                        }

                        r = requests.post(
                            init_url, headers=headers, data=donation_data)
                        res = r.json()
                        return Response({"checkout_url": res['data']['authorization_url']}, status=status.HTTP_200_OK)

                else:
                    if donation.frequency == "weekly":
                        plan = plans["weekly"]
                    elif donation.frequency == "monthly":
                        plan = plans["monthly"]
                    elif donation.frequency == "quarterly":
                        plan = plans["quarterly"]
                    elif donation.frequency == "semi-annually":
                        plan = plans["semi-annually"]
                    elif donation.frequency == "annually":
                        plan = plans["annually"]

                    donation_data = {
                        'email': donation.email,
                        'amount': int(donation.amount) * 100,
                        'plan': plan,
                        'callback_url': success_url,
                        'metadata': metadata
                    }

                    r = requests.post(
                        init_url, headers=headers, data=donation_data)
                    res = r.json()
                    return Response({"checkout_url": res['data']['authorization_url']}, status=status.HTTP_200_OK)

        return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)
