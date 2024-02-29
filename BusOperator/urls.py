from django.urls import path
from BusOperator import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register("bus",views.BusView,basename="bus")
router.register("offers",views.OfferView,basename="offers")
router.register("category",views.CategoryView,basename="category")
router.register("PaymentView",views.PaymentView,basename="PaymentView")
router.register("ReservationView",views.ReservationView,basename="ReservationView")
# router.register("ProfileEdit",views.ProfileEdit,basename="ProfileEdit")



urlpatterns = [
    path("operatorregister/",views.OperatorCreationView.as_view(),name="OperatorSignup"),
    path("token/",ObtainAuthToken.as_view(),name="token"),


]+router.urls