from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
import hmac
import hashlib
from django.conf import settings
from django.http import HttpResponse
from donations.models import Donation

api_key = settings.PAYSTACK_TEST_SECRET_KEY

payment_init_url = settings.PAYSTACK_PAYMENT_INIT_URL


@csrf_exempt
def PaystackView(request):
    # retrive the payload from the request body
    payload = request.body
    # signature header to to verify the request is from paystack
    sig_header = request.headers['x-paystack-signature']
    body = None
    event = None

    try:
        # sign the payload with `HMAC SHA512`
        hash = hmac.new(api_key.encode('utf-8'), payload,
                        digestmod=hashlib.sha512).hexdigest()
        # compare our signature with paystacks signature
        if hash == sig_header:
            # if signature matches,
            # proceed to retrive event status from payload
            body_unicode = payload.decode('utf-8')
            body = json.loads(body_unicode)
            # event status
            event = body['event']
        else:
            raise Exception
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except KeyError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except:
        # Invalid signature
        return HttpResponse(status=400)

    print(json.dumps(event))

    if event == 'charge.success':
        data = body['data']
        donation_id = body['data']['metadata']['donation_id']

        # validate status and gateway_response
        if (data["status"] == 'success') and (data["gateway_response"] == "Approved") or (data["gateway_response"] == "Successful"):
            try:
                donation = Donation.objects.get(id=donation_id)
            except Donation.DoesNotExist:
                return HttpResponse(status=404)

            # mark donation as paid
            donation.reference = data['reference']
            donation.paid = True
            donation.save(force_update=True)

    return HttpResponse(status=200)
