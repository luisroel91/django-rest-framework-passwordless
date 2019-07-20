from django.urls import path
from drfpasswordless.views import (
     ObtainEmailCallbackToken,
     ObtainMobileCallbackToken,
     ObtainAuthTokenFromCallbackToken,
     VerifyAliasFromCallbackToken,
     ObtainEmailVerificationCallbackToken,
     ObtainMobileVerificationCallbackToken,
)

urlpatterns = [
     path('callback/', ObtainAuthTokenFromCallbackToken.as_view(), name='auth_callback'),
     path('email/', ObtainEmailCallbackToken.as_view(), name='auth_email'),
     path('mobile/', ObtainMobileCallbackToken.as_view(), name='auth_mobile'),
     path('callback/verify/', VerifyAliasFromCallbackToken.as_view(), name='verify_callback'),
     path('verify/email/', ObtainEmailVerificationCallbackToken.as_view(), name='verify_email'),
     path('verify/mobile/', ObtainMobileVerificationCallbackToken.as_view(), name='verify_mobile'),
]
