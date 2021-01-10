from django.urls import path

from . import views


urlpatterns = [
    path('', views.index,
         name='index'),
    path('translate/upload/', views.TranslationFilesView.as_view(),
         name='translate'),
    path('translate/list/', views.TranslationListView.as_view(),
         name='translation-list'),
    path('translate/<int:pk>/update/', views.TranslationUpdateView.as_view(),
         name='translation-update'),
    path('translate/download/', views.translation_download,
         name='translation-download'),
    path('translate/download/file/', views.download_file,
         name='file-download'),
]
