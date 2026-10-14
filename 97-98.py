class Icon:
    def draw(self, x, y):
        pass


class FileIcon(Icon):
    def __init__(self, file_type):
        self.file_type = file_type

    def draw(self, x, y):
        print(f"Draw {self.file_type} icon at {x},{y}")


class IconFactory:
    _icons = {}

    @staticmethod
    def get_icon(file_type):
        if file_type not in IconFactory._icons:
            IconFactory._icons[file_type] = FileIcon(file_type)
        return IconFactory._icons[file_type]



class VideoPlayer:
    def play(self, file):
        print(f"Playing video: {file}")


class AudioPlayer:
    def play(self, file):
        print(f"Playing audio: {file}")


class MediaFacade:
    def __init__(self):
        self.video = VideoPlayer()
        self.audio = AudioPlayer()

    def play_media(self, file):
        if file.endswith(".mp4"):
            self.video.play(file)
        else:
            self.audio.play(file)


# Client
if __name__ == "__main__":
    facade = MediaFacade()
    facade.play_media("movie.mp4")

    icon1 = IconFactory.get_icon("mp4")
    icon2 = IconFactory.get_icon("mp4")

    icon1.draw(10, 20)
    icon2.draw(30, 40)