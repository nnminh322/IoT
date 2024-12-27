# Danh sách các nhiệm vụ IoT
options = [
    "1. Bật đèn", 
    "2. Tắt đèn", 
    "3. Kiểm tra trạng thái thiết bị", 
    "4. Chơi nhạc", 
    "5. Tăng âm lượng", 
    "6. Giảm âm lượng", 
    "7. Hỏi đáp"
]


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
    formatted_options = '\n'.join(options)

    # Tạo prompt
    prompt = f"""
    Dựa trên nội dung đoạn văn bản dưới đây, hãy chọn nhiệm vụ IoT phù hợp nhất từ danh sách sau, chỉ đưa ra số thứ tự. Liệt kê cách nhau bằng dấu ",". Ví dụ "1,2,3":
    {formatted_options}

    Đoạn văn bản:
    "{text}"
    """
    
    return prompt
