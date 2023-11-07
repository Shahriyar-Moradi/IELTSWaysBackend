
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import( 
ExamViewSet,
BookList
)

router = DefaultRouter()
router.register(r'',ExamViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('book_list', BookList.as_view(), name='book_list'),
    # Add other URL patterns as needed
]

