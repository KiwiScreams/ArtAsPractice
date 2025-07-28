from flask_admin.form import ImageUploadField
from src.admin_views.base import SecureModelView
from src.config import Config
from os import path
from uuid import uuid4

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class CourseView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_editable_list = ("title", "description", "type", "price", "mentor")
    column_filters = ("mentor", "type")
    column_exclude_list = ("photo",)
    column_formatters = {
        "description": lambda v, c, m, n: m.description if len(m.description) <= 250 else m.description[:250] + "...",
    }
    form_overrides = {
        'photo': ImageUploadField
    }
    form_args = {
        "photo": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }