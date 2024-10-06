from django.urls import path

from app.views import ChallengeListAPIView, CreateChallengeTransactionView

urlpatterns = [
    path("challenges/", ChallengeListAPIView.as_view(), name="challenge-list"),
    path(
        "challenges/create/",
        CreateChallengeTransactionView.as_view(),
        name="challenge-create",
    ),
]
