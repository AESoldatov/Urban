from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    # def __str__(self):
    #     return self.title
    def __repr__(self):
        return self.title
    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            return False

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def __repr__(self):
        return (f"\nПлощадка UrTube: \n"
                f"Зарегистрировано пользователей: {len(self.users)}\n"
                f"Добавленно видео: {len(self.videos)}\n"
                f"Текущий пользователь: {self.current_user}\n")
    def register(self, nickname, password, age):
        if all(nickname != user.nickname for user in self.users):
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
        else:
            print(f"Пользователь {nickname} уже существует")
    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname == user.nickname) and (hash(password) == user.password):
                self.current_user = user
                return
        print("Неверный логин или пароль")
    def log_out(self):
        self.current_user = None
    def add (self, *videos):
        for new_video in videos:
            if all(new_video != old_video for old_video in self.videos):
                self.videos.append(new_video)
    def get_videos(self, find_word):
        find_video = []
        for video in self.videos:
            if find_word.lower() in str(video).lower():
                find_video.append(video)
        return find_video
    def watch_video(self, film):
        if self.current_user != None:
            for video in self.videos:
                if film == str(video):
                    if (video.adult_mode == True) and (self.current_user.age < 18):
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for sec in range(video.time_now, video.duration + 1):
                            print(sec, end=' ')
                            sleep(1)
                        print("Конец видео")
                        video.time_now = 0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')







