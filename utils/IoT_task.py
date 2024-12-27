def increase_volume():
    print('call to Increase Volume API of IoT device')
    pass

def decrease_volume():
    print('call to Decrease Volume API of IoT device')
    pass

def turn_on_light():
    print('call to Turn On Light API of IoT device')
    pass

def turn_off_light():
    print('call to Turn Off Light API of IoT device')
    pass

def play_music():
    print('call to Play Music API of IoT device')
    pass

def question_answering():
    print('call to Question Answering API of IoT device')
    pass

def check_device_status():
    print('call to Check Device Status API of IoT device')

# Dictionary ánh xạ các ký tự vào hàm
task_map = {
    "1": turn_on_light,  # "1" tương ứng với hàm turn_on_light
    "2": turn_off_light,  # "2" tương ứng với hàm turn_off_light
    "3": check_device_status,  # "3" tương ứng với hàm check_device_status
    "4": play_music,  # "4" tương ứng với hàm play_music
    "5": increase_volume,  # "5" tương ứng với hàm increase_volume
    "6": decrease_volume,  # "6" tương ứng với hàm decrease_volume
    "7": question_answering  # "7" tương ứng với hàm question_answering
}

def IoT_task_call(action):
    # Sử dụng dictionary để gọi hàm tương ứng với ký tự tác vụ
    task_function = task_map.get(action)
    
    if task_function:
        task_function()  # Gọi hàm tương ứng
    else:
        print("Task not recognized.")

