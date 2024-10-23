import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хеширование пароля
        self.age = age

    def __str__(self):
        return f"Пользователь {self.nickname}"

    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Видео '{self.title}' ({self.duration} секунд)"

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title.lower() == other.title.lower()
        return False

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Вход выполнен: {user}")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print("Выход из аккаунта")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Добавлено видео: {video}")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        found_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Просмотр видео '{video.title}'")
                for i in range(1, video.duration + 1):
                    print(i, end=' ')
                    time.sleep(1)
                print("nКонец видео")
                video.time_now = 0
                return
        print("Видео не найдено")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
