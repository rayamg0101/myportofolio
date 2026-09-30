from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project
from main.models import Experience
from main.models import Education
from main.models import Skills
from main.models import Achievement
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]


    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Project name can't contain only HTML tags.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "tech_stack",
            "experience_url",
            "experience_image_url",
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi Experience",
            "tech_stack": "Apa yang berlaku",
            "experience_url": "URL Experience",
            "experience_image_url": "URL Gambar Experience",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "experience_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "experience_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "tech_stack",
            "education_url",
            "education_image_url",
        ]

        labels = {
            "title": "Nama Institusi",
            "description": "Deskripsi Institusi",
            "tech_stack": "Isi institusi",
            "education_url": "URL Institusi",
            "education_image_url": "URL Gambar Institusi",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "education_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "education_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = [
            "title",
            "category",
            "tech_stack",
            "skills_url",
            "skills_image_url",
        ]

        labels = {
            "title": "Nama skill",
            "category": "Kategori skill",
            "tech_stack": "Jenis skill",
            "skills_url": "URL skill",
            "skills_image_url": "URL Gambar skill",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "category": Textarea(
                attrs={
                    "placeholder": "Tell us about your skill",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "skills_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "skills_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "description",
            "tech_stack",
            "achievement_url",
            "achievement_image_url",
        ]

        labels = {
            "title": "Nama Achievement",
            "description": "Deskripsi Achievement",
            "tech_stack": "Jenis Achievement",
            "achievement_url": "URL Achievement",
            "achievement_image_url": "URL Gambar Achievement",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "achievement_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "achievement_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
