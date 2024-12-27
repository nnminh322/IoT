def increase_volume():
    print('call to Inscrease Volume API of IoT device')
    pass

def decrease_volume():
    print('call to Descrease Volume API of IoT device')
    pass
def turn_on_light():
    print('call to Turn On Light API of IoT device')
    pass
def turn_of_light():
    print('call to to Turn Off Light API of IoT device')
    pass
def play_music():
    print('call to Play Music API of IoT device')
    pass
def question_answering():
    print('call to Question Answering API of IoT device')
    pass


def IoT_task_call(task):
    if task == "Bật đèn":
        turn_on_light()
    elif task == "Tắt đèn":
        turn_of_light()
    elif task == "Tăng âm lượng":
        increase_volume()
    elif task == "Giảm âm lượng":
        decrease_volume()
    elif task == "Chơi nhạc":
        play_music()
    elif task == "Kiểm tra trạng thái thiết bị":
        print("call to Check Device Status API of IoT device")
    elif task == "Hỏi đáp":
        question_answering()
    else:
        print("Task not recognized.")