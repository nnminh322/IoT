# Danh sách các nhiệm vụ IoT
options = [
    "Bật đèn", 
    "Tắt đèn", 
    "Kiểm tra trạng thái thiết bị", 
    "Chơi nhạc", 
    "Tăng âm lượng", 
    "Giảm âm lượng", 
    "Hỏi đáp"
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
    formatted_options = '\n'.join([f"{i+1}. {option}" for i, option in enumerate(options)])

    
    # Tạo prompt
    prompt = f"""
    Dưới đây là một đoạn văn bản. Bạn hãy phân loại đoạn văn bản này vào một trong các nhiệm vụ IoT sau: 
    {formatted_options}


    Đoạn văn bản:
    "{text}"

    Dựa trên nội dung của đoạn văn bản, vui lòng trả lời nhiệm vụ IoT phù hợp nhất từ các lựa chọn trên. 
    Chỉ trả lời một trong các nhiệm vụ đã được liệt kê, không thêm bất kỳ văn bản nào ngoài danh sách nhiệm vụ.
    """
    
    return prompt