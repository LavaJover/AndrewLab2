from django.urls import path, include
import reg.views

urlpatterns = [
    path('', reg.views.main, name="main"),
    path('login/', reg.views.login_view, name="login"),
    path('signup/', reg.views.signup, name="signup"),
    path('courses/<str:course_name>/', reg.views.course, name="course"),
    path('homework/<int:hw_id>/', reg.views.homework, name="homework"),
    path('profile/', reg.views.profile, name="profile"),
    path('journal/', reg.views.journal, name='journal')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]