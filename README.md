# Spotify Backend

Hướng dẫn cài đặt và chạy ứng dụng Spotify Backend trong WSL (Windows Subsystem for Linux).

## Yêu cầu

* WSL đã được cài đặt và cấu hình.
* PostgreSQL đã được cài đặt và cấu hình trong WSL.
* Python 3 đã được cài đặt trong WSL.

## Các bước cài đặt

1.  **Clone repository:**

    ```bash
    git clone https://github.com/Duongnl/spotify-fe.git
    ```

2.  **Di chuyển vào thư mục `spotify-be` và tạo môi trường ảo:**

    ```bash
    cd spotify-be
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Cài đặt các thư viện cần thiết:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Tạo file `.env` và thêm các biến môi trường:**

    Tạo file `.env` trong thư mục `spotify-be` và thêm các biến môi trường sau:

    ```
    DB_NAME=database
    DB_USER=username
    DB_PASSWORD=password
    DB_HOST=host
    DB_PORT=port
    ```

    * Thay `database`, `username`, `password`, `host`, và `port` bằng thông tin cấu hình PostgreSQL của bạn.

5.  **Chạy migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Chạy server:**

    ```bash
    python manage.py runserver
    ```

    Ứng dụng sẽ chạy tại `http://127.0.0.1:8000/`.

## Lưu ý

* Đảm bảo rằng PostgreSQL đang chạy trước khi chạy ứng dụng.
* Nếu bạn gặp lỗi liên quan đến các thư viện, hãy kiểm tra lại file `requirements.txt` và cài đặt lại các thư viện cần thiết.
* Nếu bạn sử dụng một port khác với 8000, hãy thay đổi port trong lệnh `runserver`.
* Nếu bạn thay đổi các biến môi trường trong file `.env`, hãy khởi động lại server.

## Liên hệ

Nếu bạn có bất kỳ câu hỏi hoặc vấn đề nào, vui lòng liên hệ với tôi.