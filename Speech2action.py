import os
import warnings
from pydub.exceptions import CouldntDecodeError
from model.speech2text_model import *
from model.llm_model import *
from utils.get_audio_instance import read_audio
from utils.get_prompt import generate_iot_prompt, get_prompt_param
from utils.IoT_task import *
from configs import parse_arguments
import re

# Bỏ qua các cảnh báo không mong muốn
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

args = parse_arguments()


def speech2action(path_file, speech2text_model):
    try:
        # Load model và đọc file audio
        print("-" * 50)
        audio_instance = read_audio(path=path_file)
        print(f"path: {path_file}")

        # Chuyển âm thanh thành text
        text = get_text(speech2text_model, audio_instance)
        print(f"text: {text}")

        # Sinh prompt và thực hiện action
        prompt = generate_iot_prompt(text=text)
        print(f"prompt: {prompt}")

        tasks = api_call_classify_task(prompt)

        print(f"tasks: {tasks}")
        set_task = tasks.split(",")

        for action in set_task:
            action = "".join(re.findall(r"\d", action.strip()))
            prompt_param = get_prompt_param(text=text, task_iot=action)
            param = api_call_param_task(prompt_param) 
            print(param)
            # IoT_task_call(action=action)

    except CouldntDecodeError:
        print(f"Could not decode file: {path_file}")
    except Exception as e:
        print(f"Error processing file {path_file}: {e}")
    # Không trả về gì để tiếp tục xử lý các file khác


def main():
    root_data_path = "./data_demo"
    dir_audio = os.listdir(root_data_path)
    speech2text_model = get_s2t_model(name=args.name)

    for audio_instance_name in dir_audio:
        audio_instance_path = os.path.join(root_data_path, audio_instance_name)

        # Kiểm tra nếu file có định dạng hợp lệ
        if not audio_instance_name.lower().endswith((".mp3", ".m4a", ".wav", ".flac")):
            print(f"Skipping non-audio file: {audio_instance_name}")
            continue

        # Xử lý file
        speech2action(audio_instance_path, speech2text_model)


if __name__ == "__main__":
    main()
