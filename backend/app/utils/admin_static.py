


"""

storageF = FileSystemStorage(path="/static/file")
storageI = FileSystemStorage(path="/static/image")

# Проверяем, существует ли директория
if not os.path.exists(storageF):
    os.makedirs(storageF)  # Создаем директорию, если она не существует

if not os.path.exists(storageI):
    os.makedirs(storageI)



class User(BaseUser):
    __tablename__ = "users"

    file = Column(FileType(storage=storageF))
    photo = Column(ImageType(storage=storageI))

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.file, User.photo]


Base.metadata.create_all(engine)  # Create tables


@app.post("/upload/")
def create_upload_file(file: UploadFile):
    user = User(file=file)
    with AsyncSessionFactory.engine as session:
        session.add(user)
        session.commit()
        return {"filename": user.file.name}

"""
