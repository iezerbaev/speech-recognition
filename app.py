from flask import Flask, render_template, request, redirect
from speech_recognition import AudioFile, Recognizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'file' not in request.files: #делаем проверку есть ли файл
            return redirect(request.url)

        file_name = request.files['file'] # имя файла который прислали 
        if file_name:
            recognizer = Recognizer() #Распознаем речь
            audioFile = AudioFile(file_name) #делаем из него аудио файл так как google требует)
            with audioFile as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, key=None) #используем API google для распознания речи 
            print(text)
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

