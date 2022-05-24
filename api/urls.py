from django.urls import path
from .views.story_views import Stories, StoryDetail
from .views.prompt_views import Prompts, PromptDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('stories/', Stories.as_view(), name='stories'),
    path('stories/<int:pk>/', StoryDetail.as_view(), name='story_detail'),
    path('prompts/', Prompts.as_view(), name='prompts'),
    path('prompts/<int:pk>/', PromptDetail.as_view(), name='prompt_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
