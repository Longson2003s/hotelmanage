#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
from string import digits, ascii_lowercase, ascii_uppercase
from random import choices, choice, randint, random
from base64 import b64encode

ho = [
	"Phạm",
	"Hoàng",
	"Phan",
	"Nguyễn",
	"Trần",
	"Đặng",
	"Lê",
	"Vũ",
	"Bùi",
	"Đỗ",
	"Hồ",
	"Ngô",
	"Dương",
	"Nguyên",
	"Võ",
	"Đinh",
	"Huỳnh"
]

dem = [
	"Văn",
	"Thị",
	"Hoàng",
	"Nhất",
	"Minh",
	"Khánh",
	"Quang",
	"Đình",
	"Đức",
	"Kiều",
	"Kim",
	"Mộng",
	"Thu",
	"Như",
	"Tuấn",
	"Thành",
	"Thiên",
	"Gia"
]

ten = [
	"Duy",
	"Hiếu",
	"Nam",
	"Huy",
	"Vân",
	"Hà",
	"Hoàng",
	"Trang",
	"Bé",
	"Cúc",
	"Ngọc",
	"Xinh",
	"Trung",
	"Hiệp",
	"Nguyên",
	"Ninh",
	"Bảo",
	"Mai",
	"Đạt",
	"Việt",
	"Hào",
	"Sơn",
	"Phượng"
]

sdt = [
	"086",
	"096",
	"097",
	"098",
	"0162",
	"0163",
	"0164",
	"0165",
	"0166",
	"0167",
	"0168",
	"0169",
	"089",
	"090",
	"093",
	"0120",
	"0121",
	"0122",
	"0123",
	"0124",
	"0125",
	"0126",
	"0127",
	"0128",
]

phuong = [
	"Tân Định",
	"Đa Kao",
	"Bến Nghé",
	"Bến Thành",
	"Nguyễn Thái Bình",
	"Phạm Ngũ Lão",
	"Cầu Ông Lãnh",
	"Cô Giang",
	"Nguyễn Cư Trinh",
	"Cầu Kho",
	"Thạnh Xuân",
	"Thạnh Lộc",
	"Hiệp Thành",
	"Thới An",
	"Tân Chánh Hiệp",
	"An Phú Đông",
	"Tân Thới Hiệp",
	"Trung Mỹ Tây",
	"Tân Hưng Thuận",
	"Đông Hưng Thuận",
	"Tân Thới Nhất",
	"Linh Xuân",
	"Bình Chiểu",
	"Linh Trung",
	"Tam Bình",
	"Tam Phú",
	"Hiệp Bình Phước",
	"Hiệp Bình Chánh",
	"Linh Chiểu",
	"Linh Tây",
	"Linh Đông",
	"Bình Thọ",
	"Trường Thọ",
	"Long Bình",
	"Long Thạnh Mỹ",
	"Tân Phú",
	"Hiệp Phú",
	"Tăng Nhơn Phú A",
	"Tăng Nhơn Phú B",
	"Phước Long B",
	"Phước Long A",
	"Trường Thạnh",
	"Long Phước",
	"Long Trường",
	"Phước Bình",
	"Phú Hữu",
	"Tân Sơn Nhì",
	"Tây Thạnh",
	"Sơn Kỳ",
	"Tân Qúy",
	"Tân Thành",
	"Phú Thọ Hoà",
	"Phú Thạnh",
	"Phú Trung",
	"Hoà Thạnh",
	"Hiệp Tân",
	"Tân Thới Hoà",
	"Thảo Điền",
	"An Phú",
	"Bình An",
	"Bình Trưng Đông",
	"Bình Trưng Tây",
	"Bình Khánh",
	"An Khánh",
	"Cát Lái",
	"Thạnh Mỹ Lợi",
	"An Lợi Đông",
	"Thủ Thiêm"
]

quan = [
	"1",
	"12",
	"Thủ Đức",
	"9",
	"Gò Vấp",
	"Bình Thạnh",
	"Tân Bình",
	"Tân Phú",
	"Phú Nhuận",
	"2",
	"3",
	"10",
	"11",
	"4",
	"5",
	"6",
	"8",
	"Bình Tân",
	"7"
]

duong = [
	"An Hội",
	"An Nhơn",
	"Bạch Đằng",
	"Bùi Quang Là",
	"Bùi Văn Thêm",
	"Đỗ Tấn Phong",
	"Dương Quảng Hàm",
	"Hoàng Hoa Thám",
	"Hoàng Minh Giám",
	"Huỳnh Khương An",
	"Huỳnh Văn Nghệ",
	"Lê Đức Thọ",
	"Lê Lai",
	"Lê Lợi",
	"Lê Quang Định",
	"Lê Thị Hồng",
	"Lê Văn Thọ",
	"Lý Thường Kiệt",
	"Nguyễn Bỉnh Khiêm",
	"Nguyễn Duy Cung",
	"Nguyên Hồng",
	"Nguyễn Kiệm",
	"Nguyễn Minh Khiêm",
	"Nguyễn Oanh",
	"Nguyễn Thái Sơn",
	"Nguyễn Thượng Hiền",
	"Nguyễn Tư Giản",
	"Nguyễn Tuân",
	"Nguyễn Văn Bảo",
	"Nguyễn Văn Công",
	"Nguyễn Văn Lượng",
	"Nguyễn Văn Nghi",
	"Phạm Huy Thông",
	"Phạm Ngũ Lão",
	"Phạm Văn Chiêu",
	"Phạm Văn Đồng",
	"Phan Huy Ích",
	"Phan Văn Trị",
	"Phổ Quang",
	"Quang Trung",
	"Nguyễn Văn Lượng",
	"Tân Sơn",
	"Thiên Hộ Dương",
	"Thích Bửu Đằng",
	"Thích Quảng Đức",
	"Thống Nhất",
	"Trần Bá Giao",
	"Trần Phú Cường",
	"Trần Thị Nghỉ",
	"Trưng Nữ Vương",
	"Trương Đăng Quế",
	"Trương Minh Ký",
	"Bác Ái",
	"Cầu Bình Đức",
	"Chu Mạnh Trinh",
	"Chương Dương",
	"Công Lý",
	"Dân Chủ",
	"Đặng Văn Bi",
	"Đoàn Công Hớn",
	"Đoàn Kết",
	"Độc Lập",
	"Dương Văn Cam",
	"Einstein",
	"Gò Dưa",
	"Hiệp Bình",
	"Hồ Văn Tư",
	"Hòa Bình",
	"Hoàng Diệu",
	"Hồng Đức",
	"Kha Vạn Cân",
	"Khổng Tử",
	"Lê Thị Hoa",
	"Lê Văn Chí",
	"Linh Trung",
	"Lương Khải Siêu",
	"Ngô Chí Quốc",
	"Nguyễn Khuyến",
	"Nguyễn Thị Nhung",
	"Nguyễn Văn Bá",
	"Pasteur",
	"Phạm Văn Đồng",
	"Phú Châu",
	"Tam Bình",
	"Tam Châu",
	"Tam Hà",
	"Thống Nhất",
	"Tô Ngọc Vân",
	"Tô Vĩnh Diện",
	"Vận Hành",
	"Việt Thắng",
	"Võ Văn Ngân",
	"Xa Lộ Hà Nội"
]

dichvu = [
	"Massage",
	"Xông hơi",
	"Tắm nắng",
	"Hồ bơi",
	"Cano",
	"Phao bơi",
	"Lửa trại",
	"Lặn ngắm san hô",
	"Bay dù",
	"Golf",
	"Tennis",
	"Casino",
	"Quầy bar",
	"Buffet"
]

thucpham = [
	"Coca",
	"Bia",
	"Khan lanh",
	"Trai cay",
	"7 Up",
	"Pepsi"
]
loaiphong = [
	"Giường đơn",
	"Giường đơn lớn",
	"Giường đôi",
	"Giường đôi lớn",
	"Standard (STD)",
	"Superior (SUP)",
	"Deluxe (DLX)",
	"Junior Suite",
	"Executive Suite"
]

viewPhong = [
	"Thanh Pho",
	"Bien",
	"Nui",
	"San Golf"
]

c = int(input("""WHAT DO YOU WANT TO GENERATE?
1: Khachhang
2: Nhanvien
3: DichVu
4: ThucPham
5: Phong
>> """))

def genName():
	return ' '.join([choice(ho), choice(dem), choice(ten)])

def genCMND():
	return ''.join(choices(digits, k=9))

def genDate():
	return "{}-{}-{}".format(randint(1970, 2002), randint(1,12),randint(1,28))

def genSDT():
	tmp = choice(sdt)
	return ''.join(list(tmp) + choices(digits, k=(10 - len(tmp))))

def genDiaChi():
	return "{} Đường {} Tổ {} Khu {} Phường {} Quận {} TP.Hồ Chí Minh".format(randint(1, 1000), choice(duong), randint(1, 20), randint(1, 10), choice(phuong), choice(quan))

def genPhong():
	roundup = lambda x: x if x % 1000 == 0 else x + 1000 - x % 1000
	loai = choice(loaiphong)
	gia = (loaiphong.index(loai)+1) * 2000000 + int(roundup(random() * 1000000))
	return loai, gia

if c == 1:
	n = int(input("Number? "))
	with open("Khachhang", "w") as f:
		f.write("INSERT INTO KhachHang(hoTen,CMND, ngaySinh, gioiTinh,sDT) VALUES\n")
		for _ in range(n):
			name = genName()
			cmnd = genCMND()
			ngay = genDate()
			dt = genSDT()
			rs = (f"(N'{name}', N'{cmnd}', '{ngay}', {randint(0,1)}, N'{dt}'),")
			f.write(rs + "\n")

elif c == 2:
	n = int(input("Number? "))
	with open("Nhanvien", "w", encoding="utf-8") as f:
		f.write("INSERT INTO NhanVien(hoTen,CMND,ngaySinh,gioiTinh,sDT,diaChi) VALUES\n")
		for _ in range(n):
			name =	genName()
			cmnd = genCMND()
			ngay = genDate()
			dt = genSDT()
			diachi = genDiaChi()
# 			INSERT INTO NhanVien(hoTen,CMND,ngaySinh,gioiTinh,sDT,diaChi) VALUES
# (N'Bùi Khánh Đạt', N'589077512', '1999-12-4', 0, N'0121060702', N'564 Đường Phạm Văn Đồng Tổ 20 Khu 9 Phường Bình Khánh Quận 8 TP.Hồ Chí Minh')
			# rs = ("(N'{}', N'{}', N'{}', '{}', {}, N'{}', N'{}'),".format(pw, name, cmnd, ngay, randint(0,1), dt, diachi))
			rs = (f"(N'{name}', N'{cmnd}', '{ngay}', {randint(0,1)}, N'{dt}', N'{diachi}'),")
			# rs = ("(N'{}', N'{}', N'{}', {}, {}, N'{}', N'{}'),".format(pw, name, cmnd, ngay, randint(0,1), dt, diachi))
			f.write(rs + "\n")


elif c == 3:
	print("Not implemented")
	sys.exit(1)
	with open("Dichvu", "w") as f:
		for dv in dichvu:
			rs = ("(N'{}'),".format(dv))
			f.write(rs + "\n")

elif c == 4:
	print("Not implemented")
	sys.exit(1)
	for fd in thucpham:
		rs = ("(N'{}', {}, {}000),".format(fd, randint(1, 500), randint(10, 100)))
		with open("Thucpham", "a+") as f:
			f.write(rs + "\n")

elif c == 5:
	n = int(input("Number? "))
	with open("Phong", "w") as f:
		f.write("INSERT INTO Phong(loaiPhong,ghiChu,giaPhong, tinhTrangPhong) VALUES\n")
		for _ in range(n):
			loai, gia = genPhong()
			view = choice(viewPhong)
			rs = ("(N'{}', N'{}', {}, {}),".format(loai, view, gia, randint(0, 3)))
			f.write(rs + "\n")

else:
	print("unknow command")
	sys.exit(2)
