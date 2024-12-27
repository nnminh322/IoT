from pydub import AudioSegment
import io

# Hàm đọc file âm thanh từ đường dẫn và trả về đối tượng audio
def read_audio(path):
    # Đọc file âm thanh bằng pydub (hỗ trợ nhiều định dạng)
    audio = AudioSegment.from_file(path)
    
    # Chuyển đổi audio thành dạng raw bytes để Whisper có thể sử dụng
    # Định dạng mono channel, sample rate 16000 Hz (là chuẩn của Whisper)
    audio = audio.set_channels(1).set_frame_rate(16000)
    
    # Chuyển đổi audio thành dữ liệu raw
    audio_data = io.BytesIO()
    audio.export(audio_data, format="wav")
    audio_data.seek(0)
    
    return audio_data