import gradio as gr
import sounddevice as sd
import numpy as np
import wave
import os
from datetime import datetime

# Khởi tạo biến toàn cục
recording_buffer = []
is_recording = False
recordings_folder = "recordings"

# Tạo thư mục lưu trữ nếu chưa tồn tại
os.makedirs(recordings_folder, exist_ok=True)

def start_recording():
    """Bắt đầu ghi âm"""
    global is_recording, recording_buffer
    if is_recording:
        return "Ghi âm đã bắt đầu!"
    is_recording = True
    recording_buffer = []
    return "Đang ghi âm..."

def stop_recording():
    """Dừng ghi âm và lưu file"""
    global is_recording, recording_buffer
    if not is_recording:
        return "Không có ghi âm nào đang chạy."
    
    is_recording = False
    if len(recording_buffer) == 0:
        return "Không có dữ liệu ghi âm để lưu."
    
    file_path = save_audio(recording_buffer)
    recording_buffer = []  # Xóa buffer sau khi lưu
    return f"Ghi âm đã dừng. File đã lưu: {os.path.basename(file_path)}"

def save_audio(buffer):
    """Lưu file âm thanh từ buffer"""
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    file_path = os.path.join(recordings_folder, file_name)
    with wave.open(file_path, "wb") as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(44100)  # Sample rate
        wf.writeframes(np.array(buffer, dtype=np.int16).tobytes())
    return file_path

def audio_callback(indata, frames, time, status):
    """Callback để ghi dữ liệu vào buffer"""
    global recording_buffer, is_recording
    if status:
        print(f"Trạng thái: {status}")  # Debug trạng thái
    if is_recording:
        # Lưu dữ liệu đã chuẩn hóa
        recording_buffer.extend((indata[:, 0] * 32767).astype(np.int16))

def get_file_list():
    """Lấy danh sách file trong thư mục ghi âm"""
    return [f for f in os.listdir(recordings_folder) if f.endswith(".wav")]

def listen_to_file(file_name):
    """Trả về đường dẫn đầy đủ để phát file âm thanh"""
    if not file_name:
        print("Không có file nào được chọn.")
        return None
    file_path = os.path.join(recordings_folder, file_name)
    if os.path.exists(file_path):
        print(f"Đường dẫn file phát: {file_path}")  # Debug
        return file_path
    print("File không tồn tại.")
    return None


# Thiết lập thiết bị âm thanh
try:
    sd.default.samplerate = 44100
    sd.default.channels = 1
    audio_stream = sd.InputStream(callback=audio_callback)
    audio_stream.start()
except Exception as e:
    raise RuntimeError(f"Lỗi thiết lập thiết bị âm thanh: {e}")

# Tạo giao diện với Gradio
def create_ui():
    with gr.Blocks() as demo:
        with gr.Row():
            gr.Markdown("# Ghi Âm Giọng Nói")

        with gr.Row():
            start_button = gr.Button("Bắt đầu Ghi Âm")
            stop_button = gr.Button("Dừng Ghi Âm")

        status_text = gr.Textbox(label="Trạng Thái", interactive=False)

        start_button.click(start_recording, outputs=status_text)
        stop_button.click(stop_recording, outputs=status_text)

        with gr.Row():
            update_button = gr.Button("Cập Nhật Danh Sách File")
            file_dropdown = gr.Dropdown(label="Chọn File Để Nghe", choices=get_file_list())
            update_button.click(
                lambda: gr.update(choices=get_file_list()), 
                outputs=file_dropdown
            )

        with gr.Row():
            audio_player = gr.Audio(label="Nghe Lại", type="filepath")
            file_dropdown.change(
                listen_to_file, 
                inputs=file_dropdown, 
                outputs=audio_player
            )

        return demo

# Khởi chạy giao diện
try:
    demo = create_ui()
    demo.launch()
finally:
    if 'audio_stream' in locals():
        audio_stream.close()
