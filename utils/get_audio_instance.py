import numpy as np
from pydub import AudioSegment
import io

def read_audio(path):
    # Đọc file âm thanh bằng pydub (hỗ trợ nhiều định dạng)
    audio = AudioSegment.from_file(path)
    
    # Chuyển đổi audio thành dạng mono channel, sample rate 16000 Hz
    audio = audio.set_channels(1).set_frame_rate(16000)
    
    # Chuyển đổi audio thành mảng numpy
    audio_samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768.0  # Chuẩn hóa giá trị về [-1, 1]
    
    return audio_samples
