<!-- Folder structure -->
## Folder structure
```
TIMETABLE_GENERATOR_GA
├── app/
│   ├── __init__.py (chứa mã nguồn cho ứng dụng web)
│   ├── routes.py (chứa các định tuyến (routing) cho ứng dụng web)
│   ├── models.py (chứa các lớp mô tả cấu trúc dữ liệu và đối tượng cho ứng dụng web)
│   ├── templates/ ( chứa các tệp mẫu HTML cho ứng dụng web)
│   │   ├── base.html
│   │   ├── index.html
│   │   └── ...
│   ├── static/ (chứa các tệp tĩnh như CSS, JavaScript và hình ảnh)
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── ...
│   ├── forms.py (chứa các lớp mô tả các biểu mẫu HTML cho ứng dụng)
│   ├── utils/ (chứa các tiện ích hỗ trợ cho ứng dụng)
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── ...
│   └── ga/ ()
│       ├── __init__.py
│       ├── individual.py
│       ├── population.py
│       ├── fitness.py
│       ├── genetic_algorithm.py
│       └── ...
├── config.py (chứa các cấu hình cho ứng dụng, như các cài đặt cơ sở dữ liệu)
├── requirements.txt (chứa các yêu cầu về các gói phần mềm cần thiết để chạy ứng dụng)
├── README.md (chứa các hướng dẫn cài đặt và sử dụng ứng dụng )
├── tests/ (chứa các tệp kiểm thử (test) cho ứng dụng)
│   ├── __init__.py
│   └── ...
├── migrations/ (chứa các phiên bản cơ sở dữ liệu.)
│   ├── __init__.py
│   └── ...
├── setup.py (chứa các thông tin về gói của ứng dụng của bạn.)
├── run.py (tệp thực thi ứng dụng)
└── manage.py (tệp quản lý các tác vụ)
```
