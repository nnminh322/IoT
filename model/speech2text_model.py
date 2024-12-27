from whisper import whisper


def get_s2t_model(name="medium", **kwargs):
    model = whisper.load_model(name=name)
    return model


def get_text(model, audio, language="vi"):
    response = model.transcribe(audio, language=language)
    text = response["text"]
    return text


