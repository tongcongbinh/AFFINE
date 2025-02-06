# AFFINE CIPHER

Ứng dụng **Affine Cipher** giúp người dùng mã hóa và giải mã văn bản bằng thuật toán mã hóa Affine, sử dụng giao diện dễ sử dụng. Thuật toán Affine Cipher là một phương pháp mã hóa thay thế, trong đó mỗi chữ cái của văn bản được thay thế bằng một chữ cái khác thông qua một phép toán tuyến tính.

## Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Cài Đặt](#cài-đặt)
3. [Sử Dụng](#sử-dụng)
4. [Thuật Toán Affine Cipher](#thuật-toán-affine-cipher)
5. [Giao Diện Người Dùng](#giao-diện-người-dùng)

## Giới Thiệu

Ứng dụng **Affine Cipher** cung cấp một giao diện đơn giản cho phép người dùng thực hiện các thao tác mã hóa và giải mã văn bản. Thuật toán Affine Cipher sử dụng công thức sau để mã hóa mỗi ký tự trong văn bản:

E(x) = (ax + b) mod m
- `x` là giá trị của ký tự cần mã hóa.
- `a` và `b` là các khóa được lựa chọn bởi người dùng.
- `m` là số lượng ký tự trong bảng chữ cái (thường là 26 cho bảng chữ cái Latin).

Ứng dụng này sẽ cho phép người dùng nhập văn bản và khóa, sau đó sẽ trả về kết quả mã hóa hoặc giải mã.

## Cài Đặt

1. Clone dự án về máy tính của bạn:

   ```bash
   git clone https://github.com/username/affine-cipher.git
2. Cài đặt các phụ thuộc cần thiết (ví dụ: nếu ứng dụng sử dụng Python):

   ```bash
      Chỉnh sửa
      pip install -r requirements.txt

3. Chạy ứng dụng:
   ```bash
   python GUI.py

## Sử Dụng
### Mã hóa:
Nhập văn bản cần mã hóa vào ô nhập liệu.
Nhập giá trị khóa a và b cho thuật toán.
Nhấn nút "Encrypt" để nhận kết quả mã hóa.

### Giải mã:
Nhập văn bản mã hóa.
Nhập giá trị khóa a và b tương ứng với quá trình mã hóa.
Nhấn nút "Decrypt" để nhận kết quả giải mã.

### Lưu ý:
Các giá trị khóa a và b cần phải tuân theo quy tắc của thuật toán Affine (a phải là số nguyên có ước chung với 26 là 1).

## Affine Cipher
**Affine Cipher** là một hệ thống mã hóa thay thế trong đó mỗi ký tự trong văn bản rõ được thay thế bằng một ký tự khác thông qua công thức toán học. Công thức mã hóa là:

E(x) = (ax + b) mod m
Với:
x là giá trị của ký tự trong bảng chữ cái.
a và b là các khóa riêng biệt do người dùng nhập vào.
m là số ký tự trong bảng chữ cái (26 cho chữ cái Latin).

Để giải mã, sử dụng công thức:
D(y) = a_inv * (y - b) mod m
Trong đó:
a_inv là nghịch đảo modulo của a đối với m (26 trong trường hợp bảng chữ cái Latin).

## Giao Diện Người Dùng
Ứng dụng cung cấp giao diện dễ sử dụng với các chức năng:

Nhập văn bản cần mã hóa hoặc giải mã.
Nhập khóa a và b để điều chỉnh quá trình mã hóa.
Hiển thị kết quả mã hóa hoặc giải mã sau khi người dùng thực hiện thao tác.

