from django.urls import path

from main.views import show_main, show_experience, show_skills, show_education, show_achievement, show_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("education/", show_education, name="show_education"),
    path("achievement/", show_achievement, name="show_achievement"),
    path("project/", show_project, name="show_project"),
]