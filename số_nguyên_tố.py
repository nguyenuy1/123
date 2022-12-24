import streamlit as st
import random
import os

score = 0
choice = st.radio('Lựa chọn:', ['Thêm từ vựng', 'Xóa từ vựng chỉ định', 'Xóa toàn bộ từ vựng', 'Xắp xếp theo bảng chữ cái', 'In ra toàn bộ từ vựng', 'Kiểm tra', 'Thoát'])
    
# khai báo vòng lặp vô hạn

# yêu cầu người dùng chọn lựa chọn
# nếu người dùng nhấn phím 1
if choice == "Thêm từ vựng":
    # yêu cầu người dùng nhập từ vựng và nghĩa
    vocabulary = st.text_input('Nhập từ vựng:',key = "add từ vựng")
    meaning = st.text_input('Nhập nghĩa của từ vựng:')
    
    if st.button('Lưu'):
      # mở tệp tuvung.txt để ghi
      with  open("tuvung.txt", "a", encoding='utf-8') as f:
          # ghi từ vựng và nghĩa vào tệp
          f.write(vocabulary + ": " + meaning + "\n")
    # in ra thông báo thành công
    st.write("Từ vựng đã được lưu trữ thành công.")

# nếu người dùng nhấn phím Xóa từ vựng chỉ định
elif choice == "Xóa từ vựng chỉ định":
    # yêu cầu người dùng nhập từ vựng cần xóa
    vocabulary = st.text_input('Nhập từ vựng cần xóa:')
    
    # mở tệp đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
    with open("tuvung.txt", "r") as f:
        lines = f.readlines()
    
    # duyệt qua từng dòng trong danh sách và xóa từ vựng cần xóa
    for i, line in enumerate(lines):
        if vocabulary in line:
            del lines[i]
            break
    
    # mở tệp tuvung.txt để ghi lại
    with open("tuvung.txt", "w") as f:
        # ghi lại nội dung của tệp tuvung.txt
        f.writelines(lines)
    # in ra thông báo thành công
    st.write("Từ vựng đã được xóa thành công.")
# Nếu người dùng ấn phím Xóa toàn bộ từ vựng
elif choice == "Xóa toàn bộ từ vựng":
    # mở tệp tuvung.txt để ghi lại
    with open("tuvung.txt", "w") as f:
        # ghi lại nội dung trống
        f.write("")
    # in ra thông báo thành công
    st.write("Đã xóa toàn bộ từ vựng.")
# Nếu người dùng ấn phím Xắp xếp theo bảng chữ cái
elif choice == "Xắp xếp theo bảng chữ cái":
    # mở tệp đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
    with open("tuvung.txt", "r") as f:
        lines = f.readlines()
    
    # sắp xếp lại danh sách theo bảng chữ cái
    lines.sort()
    
    # mở tệp tuvung.txt để ghi lại
    with open("tuvung.txt", "w") as f:
        # ghi lại nội dung của tệp tuvung.txt
        f.writelines(lines)
    # in ra thông báo thành công
    st.write("Đã sắp xếp lại từ vựng theo bảng chữ cái.")
# Nếu người dùng ấn phím In ra toàn bộ từ vựng
elif choice == "In ra toàn bộ từ vựng":
    # mở tệp đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
    with open("tuvung.txt", "r",encoding='utf-8') as f:
        lines = f.readlines()
    
    # in ra tất cả các từ vựng trong danh sách
    for line in lines:
        st.write(f"{line}")
# nếu người dùng nhấn phím Kiểm tra
elif choice == "Kiểm tra":
    # mở tệp đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
    with open("tuvung.txt", "r",encoding='utf-8') as f:
        lines = f.readlines()
    
    # khai báo biến đếm số từ vựng đúng
    count = 0
    
    # duyệt qua từng từ vựng trong danh sách
    for line in lines:
        # tách từ vựng và nghĩa từ dòng hiện tại
        vocabulary, meaning = line.split(": ")
        # yêu cầu người dùng nhập nghĩa của từ vựng
        answer = st.text_input('Nhập nghĩa của từ vựng "' + vocabulary + '":')
        # nếu người dùng trả lời đúng
        if st.button("Kiểm tra"):
            if answer == meaning.strip():
                # tăng biến đếm lên 1
                count += 1
            else:
                st.write(f"Đáp án sai. Đáp án đúng là: '{meaning}'")
                st.write(answer,meaning)
        # in ra kết quả kiểm tra
        st.write("Đúng " + str(count) + " trên tổng số " + str(len(lines)) + " từ vựng.")

# nếu người dùng nhấn phím Thoát
else:
    # in ra thông báo lỗi
    st.write("Lựa chọn không hợp lệ.")
