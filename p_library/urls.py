from django.urls import reverse_lazy
from django.urls import path
from p_library import views
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, PublisherDetailView
from p_library.views import PublisherList
from p_library.views import index, RegisterView, CreateUserProfile
from allauth.account.views import login, logout
from django.conf.urls.static import static
from django.conf import settings


app_name = 'p_library'

urlpatterns = [
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publisher/', views.book_publisher),
    path('publishers', PublisherList.as_view()),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('<int:pk>/', PublisherDetailView.as_view(), name="publisher-detail"),
    path('hometask/', views.hometask, name="hometask-detail"),
    path('', index, name='index'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('p_library:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
