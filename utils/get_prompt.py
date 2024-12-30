# Danh sách các nhiệm vụ IoT
options = [
    "1. Bật, tắt đèn",
    "2. Kiểm tra trạng thái thiết bị",
    "3. Chơi nhạc",
    "4. Âm thanh thiết bị",
    "5. Hỏi đáp",
]

number_map_name_task = {
    "1": "Bật tắt đèn",
    "2": "Kiểm tra trạng thái thiết bị",
    "3": "Chơi nhạc",
    "4": "Âm thanh thiết bị",
    "5": "Hỏi đáp",
}

param = {
    "1": {
        "lightAction": None,  # Bật hay tắt
        "fixedTime": None,  # Thời gian cố định (ví dụ: 10:30)
        "delayTime": None,  # Thời gian trễ (ví dụ: 30 phút)
    },
    "2": {
        "nameDevice": None,
        "nameAttribute": None,
    },
    "3": {
        "nameSong": None,
        "singer": None  # Tên bài hát
    },
    "4": {
        "volumeAction": None,
        "volumeTarget": None,
        "volumeStep": None,
    },
    "5": {},
}


def get_prompt_param(text, task_iot):
    """
    Tạo prompt trích xuất các tham số cho nhiệm vụ IoT từ đoạn văn bản và mẫu tham số.

    Args:
        text (str): Đoạn văn bản cần phân tích.
        task_iot (str): Loại nhiệm vụ IoT, ví dụ: "1", "2", "3", ...
        param_template (dict): Mẫu tham số tương ứng với nhiệm vụ IoT, ví dụ:
            {
                "lightAction": None,
                "fixedTime": None,
                "delayTime": None
            }.

    Returns:
        str: Prompt để cung cấp cho LLM.
    """
    prompt = f"""Hãy phân tích các tham số cho nhiệm vụ IoT '{number_map_name_task[task_iot]}' từ đoạn văn bản dưới đây theo mẫu tham số. 
    Yêu cầu trả chỉ về một từ điển như mẫu tham số, bỏ qua các keys không xác định được, không thêm các thông tin dư thừa:
    Văn bản: "{text}"

    Mẫu tham số: {param[task_iot]}
    """

    return prompt


def generate_iot_prompt(text, options=options):
    """
    Hàm nhận vào văn bản và danh sách các nhiệm vụ IoT, tạo ra prompt cho LLM.
    Ràng buộc mô hình chỉ trả về một trong các nhiệm vụ IoT có trong danh sách.

    Args:
    - text (str): Đoạn văn bản cần phân loại.
    - options (list): Danh sách các nhiệm vụ IoT, ví dụ: ['Bật đèn', 'Tắt đèn', 'Kiểm tra trạng thái thiết bị', ...]

    Returns:
    - str: Prompt đã được tạo ra.
    """

    # Chuyển danh sách nhiệm vụ thành dạng văn bản với đánh số
    formatted_options = "\n".join(options)

    # Tạo prompt
    prompt = f"""
    Dựa trên nội dung đoạn văn bản dưới đây, hãy chọn nhiệm vụ IoT phù hợp nhất từ danh sách sau, chỉ đưa ra số thứ tự. Liệt kê cách nhau bằng dấu ",". Ví dụ "1,2,3":
    {formatted_options}

    Đoạn văn bản:
    "{text}"
    """

    return prompt
