import random
import os

score = 0

# khai báo vòng lặp vô hạn
while True:
    # yêu cầu người dùng nhập lựa chọn
    choice = input("Nhấn phím (1) >> Nhập từ vựng\nNhấn phím (2) >> Xóa từ vựng chỉ định\nNhấn phím (3) >> Xóa toàn bộ từ vựng\nNhấn phím (4) >> Sắp xếp lại từ vựng theo bảng chữ cái\nNhấn phím (5) >> Hiển thị tất cả từ vựng\nNhấn phím (6) >> Kiểm tra từ vựng\nNhấn phím (7) >> Thoát: ")
    
    # nếu người dùng nhấn phím 1
    if choice == "1":
        os.system('cls')
        # yêu cầu người dùng nhập từ vựng và nghĩa
        vocabulary = input("Nhập từ vựng: ")
        meaning = input("Nhập nghĩa của từ vựng: ")
        
        # mở tệp tuvung.txt để ghi
        with  open("tuvung.txt", "a", encoding='utf-8') as f:
            # ghi từ vựng và nghĩa vào tệp
            f.write(vocabulary + ": " + meaning + "\n")
        os.system('cls')
        print("Từ vựng đã được lưu trữ thành công.")
    
    # nếu người dùng nhấn phím 2
    elif choice == "2":
        # yêu cầu người dùng nhập từ vựng cần xóa
        vocabulary = input("Nhập từ vựng cần xóa: ")
        
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
            # ghi lại nội dung của tệp tuvung.txt sau khi xóa từ vựng
            f.writelines(lines)
        os.system('cls')
        print("Từ vựng đã được xóa thành công.")

    # nếu người dùng nhấn phím 3
    elif choice == "3":
        # mở tệp tuvung.txt để ghi lại
        with open("tuvung.txt", "w") as f:
            # ghi lại nội dung rỗng vào tệp
            f.write("")
        os.system('cls')
        print("Tất cả từ vựng đã được xóa thành công.")

    # nếu người dùng nhấn phím 4
    elif choice == "4":
        # đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
        with open("tuvung.txt", "r") as f:
            lines = f.readlines()
        
        # sắp xếp lại danh sách từ vựng theo thứ tự bảng chữ cái
        lines.sort()
        
        # mở tệp tuvung.txt để ghi lại
        with open("tuvung.txt", "w") as f:
            # ghi lại nội dung của tệp tuvung.txt sau khi sắp xếp lại
            f.writelines(lines)
        os.system('cls')
        print("Từ vựng đã được sắp xếp lại theo thứ tự bảng chữ cái.")
    elif choice == "5":
        os.system('cls')
        # đọc nội dung của tệp tuvung.txt và in ra màn hình
        with open("tuvung.txt", "r",encoding='utf-8') as f:
            print(f.read())

    # nếu người dùng nhấn phím 6
    elif choice == "6":
        os.system('cls')
        # đọc nội dung của tệp tuvung.txt và lưu vào một danh sách
        with open("tuvung.txt", "r",encoding='utf-8') as f:
            lines = f.readlines()
        bool = True
        while bool:
            # nếu danh sách từ vựng không rỗng
            if lines:
                # tạo ngẫu nhiên 1 số trong khoảng từ 0 đến số lượng từ vựng - 1
                index = random.randint(0, len(lines) - 1)
                
                # lấy từ vựng và nghĩa tương ứng từ danh sách
                vocabulary, meaning = lines[index].strip().split(": ")
                
                # tạo ngẫu nhiên 1 số trong khoảng từ 0 đến 1
                # nếu số là 0 thì hiển thị nghĩa của từ vựng và yêu cầu người dùng nhập từ vựng
                # nếu số là 1 thì hiển thị từ vựng và yêu cầu người dùng nhập nghĩa
                if random.randint(0, 1) == 0:
                    answer = input("Nghĩa của từ vựng '" + vocabulary + "' là gì? ")
                    if answer == meaning:
                        os.system('cls')
                        print("Đáp án đúng!")
                        score += 1
                    else:
                        print(f"Đáp án sai. Đáp án đúng là: '{meaning}'")
                        # hiển thị số điểm hiện tại
                        print("Số điểm hiện tại:", score)
                        
                        # hỏi người dùng có muốn tiếp tục không
                        choice = input("Bạn có muốn tiếp tục không (Y/N)? ")
                        if choice.lower() == "n":
                            # thoát khỏi vòng lặp và kết thúc chương trình
                            bool = False
                            os.system('cls')
                            break
                else:
                    answer = input(f"Từ có nghĩa '{meaning}' là gì? ")
                    if answer == vocabulary:
                        os.system('cls')
                        print("Đáp án đúng!")
                        score += 1
                    else:
                        print("Đáp án sai. Đáp án đúng là: " + vocabulary)
                        
                
                        # hiển thị số điểm hiện tại
                        print("Số điểm hiện tại:", score)
                        
                        # hỏi người dùng có muốn tiếp tục không
                        choice = input("Bạn có muốn tiếp tục không (Y/N)? ")
                        if choice.lower() == "n":
                            # thoát khỏi vòng lặp và kết thúc chương trình
                            bool = False
                            os.system('cls')
                            break
        else:
            os.system('cls')
            print("Không có từ vựng nào trong tệp.")

    else:
        # thoát khỏi vòng lặp và kết thúc chương trình
        os.system('cls')
        break