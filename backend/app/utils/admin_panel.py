from starlette.requests import Request
from app.models.models import (Manager, Office, Candidate,
                               Course, CandidateCourse, ManagerCandidate,
                               )
from passlib.context import CryptContext
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend

from app.models.models import (
    Manager,
    Office,
    Candidate,
    Course,
    CandidateCourse,
    ManagerCandidate,
    CandidateSkill,
    Skill,
)


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        print(type(form))
        username, password = form["username"], form["password"]

        request.session.update({"token": "..."})
        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ManagerAdmin(ModelView, model=Manager):
    name = "Руководитель"
    name_plural = "Руководители"

    # form_extra_fields = {
    #     'photo': form.FileUploadField('Загрузите фотографию', base_path='static/photo/',
    #                                   allowed_extensions=['jpg', 'png', 'gif']),
    # }

    # form_overrides = {'photo': FileUploadField}

    # form_args = {
    #     'photo': {
    #         'label': 'Загрузка фотографии',
    #         'base_path': 'static/photo/',  # Укажите путь для загрузки файлов
    #         'relative_path': 'photo/'
    #     }
    # }

    async def on_model_change(
        self, data: dict, model: Manager, is_created: bool, request: Request
    ) -> None:
        # Получаем данные формы
        form_data = await request.form()
        # if is_created and 'photo' in form_data:
        #     photo_file = form_data['photo']
        #     filename = await storageI.upload(photo_file)  # загружаем файл
        #     model.photo = filename  # сохраняем имя файла в модели
        # else:
        #     print("нет фотографии")

        if is_created:
            data["password"] = pwd_context.hash(data["password"])

    column_list = [
        Manager.full_name,
        Manager.email,
        Manager.office,
        Manager.quotas,
        Manager.photo,
    ]
    form_columns = [
        Manager.full_name,
        Manager.email,
        Manager.password,
        Manager.quotas,
        Manager.office,
        Manager.candidates,
        Manager.photo,
    ]
    column_details_exclude_list = ["office_id"]
    column_searchable_list = [
        Manager.photo,
        Manager.full_name,
        Manager.email,
        Manager.quotas,
        Manager.office,
    ]
    column_sortable_list = [
        Manager.photo,
        Manager.full_name,
        Manager.email,
        Manager.quotas,
    ]
    column_labels = {
        Manager.id: "ID",
        Manager.full_name: "ФИО",
        Manager.email: "Электронная почта",
        Manager.office: "Офис",
        Manager.quotas: "Квота",
        Manager.password: "Пароль",
        Manager.candidates: "Кандидаты",
        Manager.photo: "Фотография",
        Manager.created_at: "Время создания",
        Manager.updated_at: "Время последнего изменения",
    }


class OfficeAdmin(ModelView, model=Office):
    name = "Офис"
    name_plural = "Офисы"

    column_list = [Office.name, Office.location, Office.managers]
    column_searchable_list = [Office.name, Office.location]
    column_sortable_list = [Office.name, Office.location]
    form_columns = [Office.location, Office.managers]

    column_labels = {
        Office.name: "Название",
        Office.location: "Локация",
        Office.managers: "Руководитель",
    }


class CandidateAdmin(ModelView, model=Candidate):
    name = "Кандидат"
    name_plural = "Кандидаты"

    # form_extra_fields = {
    #     'photo': form.FileUploadField('Загрузите фотографию', base_path='static/photo/'),
    # }

    # form_overrides = {
    #     'photo': FileUploadField
    # }

    # form_args = {
    #     'photo': {
    #         'label': 'Загрузка фотографии',
    #         'base_path': 'static/photo/',  # Укажите путь для загрузки файлов
    #         'relative_path': 'static/photo/'
    #     }
    # }

    async def on_model_change(
        self, data: dict, model: Manager, is_created: bool, request: Request
    ) -> None:
        # Получаем данные формы
        form_data = await request.form()
        # if is_created and 'photo' in form_data:
        #     photo_file = form_data['photo']
        #     filename = await storageI.upload(photo_file)  # загружаем файл
        #     model.photo = filename  # сохраняем имя файла в модели
        # else:
        #     print("нет фотографии")

    column_list = [
        Candidate.full_name,
        Candidate.email,
        Candidate.location,
        Candidate.phone,
        Candidate.is_hired,
        Candidate.clients,
        Candidate.objects,
        Candidate.courses,
        Candidate.photo,
        Candidate.skills,
    ]
    column_searchable_list = [
        Candidate.photo,
        Candidate.full_name,
        Candidate.email,
        Candidate.location,
        Candidate.objects,
    ]
    column_sortable_list = [
        Candidate.photo,
        Candidate.full_name,
        Candidate.email,
        Candidate.location,
        Candidate.phone,
        Candidate.is_hired,
        Candidate.clients,
        Candidate.objects,
    ]
    form_columns = [
        Candidate.full_name,
        Candidate.email,
        Candidate.location,
        Candidate.phone,
        Candidate.is_hired,
        Candidate.clients,
        Candidate.objects,
        Candidate.photo,
    ]
    column_details_exclude_list = ["id"]

    column_labels = {
        Candidate.full_name: "ФИО",
        Candidate.email: "Электронная почта",
        Candidate.location: "Адрес",
        Candidate.phone: "Телефон",
        Candidate.is_hired: "Нанят",
        Candidate.clients: "Клиенты",
        Candidate.objects: "Объекты",
        Candidate.photo: "Фотография",
        Candidate.courses: "Курсы",
        Candidate.skills: "Навыки",
    }


class CourseAdmin(ModelView, model=Course):
    name = "Курс"
    name_plural = "Курсы"

    column_list = [Course.id, Course.name, Course.candidates]
    column_searchable_list = [Course.id, Course.name, Course.candidates]
    form_columns = [Course.name]
    column_labels = {Course.name: "Название", Course.candidates: "Кандидаты"}


class CandidateCourseAdmin(ModelView, model=CandidateCourse):
    name = "Кандидат-курс"
    name_plural = "Кандидаты-курсы"

    column_list = [
        CandidateCourse.id,
        CandidateCourse.candidate,
        CandidateCourse.course,
    ]
    column_searchable_list = [CandidateCourse.id]
    column_sortable_list = [CandidateCourse.id]
    form_columns = [CandidateCourse.candidate, CandidateCourse.course]

    column_labels = {
        CandidateCourse.candidate: "Кандидат",
        CandidateCourse.course: "Курс",
    }


class ManagerCandidateAdmin(ModelView, model=ManagerCandidate):
    name = "История приглашений"
    name_plural = "История приглашений"

    def get_created_at(self, obj):
        my_date = self.created_at
        formatted_date = my_date.strftime("%Y-%m-%d %H:%M")
        return formatted_date

    def get_updated_at(self, obj):
        my_date = self.updated_at
        formatted_date = my_date.strftime("%Y-%m-%d %H:%M")
        return formatted_date

    column_list = [
        ManagerCandidate.id,
        ManagerCandidate.manager,
        ManagerCandidate.candidate,
        ManagerCandidate.created_at,
        ManagerCandidate.updated_at,
        ManagerCandidate.is_viewed,
        ManagerCandidate.is_favorite,
        ManagerCandidate.note,
    ]
    column_searchable_list = [
        ManagerCandidate.id,
        ManagerCandidate.created_at,
        ManagerCandidate.updated_at,
        ManagerCandidate.is_viewed,
    ]
    column_sortable_list = [
        ManagerCandidate.id,
        ManagerCandidate.created_at,
        ManagerCandidate.updated_at,
        ManagerCandidate.is_viewed,
    ]
    form_columns = [
        ManagerCandidate.manager,
        ManagerCandidate.candidate,
        ManagerCandidate.is_viewed,
        ManagerCandidate.is_favorite,
        ManagerCandidate.note,
    ]

    column_labels = {
        ManagerCandidate.manager: "Руководитель",
        ManagerCandidate.candidate: "Кандидат",
        ManagerCandidate.is_viewed: "Приглашен",
        ManagerCandidate.is_favorite: "Избранное",
        ManagerCandidate.note: "Заметка",
        ManagerCandidate.created_at: "Время создания",
        ManagerCandidate.updated_at: "Время редактирования",
    }

    column_formatters = {
        ManagerCandidate.created_at: get_created_at,
        ManagerCandidate.updated_at: get_updated_at,
    }


class CandidateSkillAdmin(ModelView, model=CandidateSkill):
    name = "Кандидат-навык"
    name_plural = "Кандидаты-навыки"

    column_list = [CandidateSkill.candidate, CandidateSkill.skill]
    column_searchable_list = [CandidateSkill.id]
    column_sortable_list = [CandidateSkill.id]
    form_columns = [CandidateSkill.candidate, CandidateSkill.skill]

    column_labels = {
        CandidateSkill.candidate: "Кандидат",
        CandidateSkill.skill: "Навык",
    }


class SkillAdmin(ModelView, model=Skill):
    name = "Навык"
    name_plural = "Навыки"

    column_list = [Skill.name, Skill.candidates]
    column_searchable_list = [Skill.name, Skill.candidates]
    form_columns = [Skill.name]
    column_labels = {Skill.name: "Название", Skill.candidates: "Кандидаты"}
