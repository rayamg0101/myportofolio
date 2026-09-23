from django.urls import path
from main.views import show_main, show_experience, show_skills, show_education, show_achievement, show_project, create_project, get_projects_json, delete_project, create_skills, get_skills_json, delete_skills, create_education, get_education_json, delete_education, create_achievement, get_achievement_json, delete_achievement, create_experience, get_experience_json, delete_experience, register, login_user, logout_user, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experience_json, name="get_experience_json"),
    path("experiences/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skills, name="create_skills"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skill_id>/delete/", delete_skills, name="delete_skills"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("api/educations/", get_education_json, name="get_education_json"),
    path("educations/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("achievement/", show_achievement, name="show_achievement"),
    path("achievement/add/", create_achievement, name="create_achievement"),
    path("api/achievements/", get_achievement_json, name="get_achievement_json"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",),

]