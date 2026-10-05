from django.urls import path
from main.views import show_main, show_experience, show_skills, show_education, show_achievement, show_project,create_project, get_projects_json, delete_project, toggle_star, create_project_ajax,create_skills, get_skills_json, delete_skills, create_skill_ajax,create_education, get_educations_json, delete_education, create_education_ajax,create_achievement, get_achievements_json, delete_achievement, create_achievement_ajax,create_experience, get_experiences_json, delete_experience, create_experience_ajax, register, login_user, logout_user


app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    # Experience
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("experiences/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experiences/<uuid:experience_id>/star/", toggle_star, name="toggle_star"),
    path("experiences/add-ajax/", create_experience_ajax, name="create_experience_ajax"),

    # Skills
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skills, name="create_skills"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:skills_id>/delete/", delete_skills, name="delete_skills"),
    path("skills/<uuid:skills_id>/star/", toggle_star, name="toggle_star"),
    path("skills/add-ajax/", create_skill_ajax, name="create_skill_ajax"),

    # Education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
    path("educations/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("educations/<uuid:education_id>/star/", toggle_star, name="toggle_star"),
    path("educations/add-ajax/", create_education_ajax, name="create_education_ajax"),

    # Achievement
    path("achievement/", show_achievement, name="show_achievement"),
    path("achievement/add/", create_achievement, name="create_achievement"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("achievements/<uuid:achievement_id>/star/", toggle_star, name="toggle_star"),
    path("achievements/add-ajax/", create_achievement_ajax, name="create_achievement_ajax"),

    # Project
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),

    # Auth
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]