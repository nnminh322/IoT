def turn_on_off_light(param):
    print(f"call to Turn On/Off Light API of IoT device with param: {param}")
    pass


def check_device_status(param):
    print(f"call to Check Device Status API of IoT device with param: {param}")
    pass


def play_music(param):
    print(f"call to Play Music API of IoT device with param: {param}")
    pass


def increase_descrease_device_sound(param):
    print(f"call to Increase Device Sound API of IoT device with param: {param}")
    pass


def question_answering(param):
    print(f"call to Question Answering API of IoT device with param: {param}")
    pass


# Dictionary ánh xạ các ký tự vào hàm
task_map = {
    "1": turn_on_off_light,
    "2": check_device_status,
    "3": play_music,
    "4": increase_descrease_device_sound,
    "5": question_answering,
}


def IoT_task_call(action, param):
    # Sử dụng dictionary để gọi hàm tương ứng với ký tự tác vụ
    task_function = task_map.get(action)

    if task_function:
        task_function(param=param)  # Gọi hàm tương ứng
    else:
        print("Task not recognized.")
