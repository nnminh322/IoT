import os
from model.speech2text_model import *
from model.llm_model import *
from utils.get_audio_instance import read_audio
from utils.get_prompt import generate_iot_prompt
from utils.IoT_task import *
from configs import parse_arguments

args = parse_arguments()


def speech2action(path_file):

    specch2text_model = get_s2t_model(name=args.name)

    audio_instance = read_audio(path=path_file)
    text = get_text(specch2text_model, audio_instance)
    prompt = generate_iot_prompt(text=text)

    action = api_call(prompt)
    action(action)
    return


def main():
    root_data_path = "./data_demo"
    dir_audio = os.listdir(root_data_path)

    for audio_instance_name in dir_audio:
        audio_instance_path = root_data_path + "/" + audio_instance_name
        speech2action(audio_instance_path)


if __name__ == "__main__":
    main()
