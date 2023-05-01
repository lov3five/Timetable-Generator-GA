
def add_dataframe_to_excel(file_path, new_sheet_name, df):
    """
    Thêm một DataFrame vào một trang tính mới của một tệp Excel đã có các trang tính.

    Parameters:
    file_path (str): Đường dẫn đến tệp Excel.
    new_sheet_name (str): Tên của trang tính mới.
    df (pandas.DataFrame): DataFrame cần thêm vào trang tính mới.

    Returns:
    pandas.DataFrame: DataFrame mới được tạo từ tệp Excel đã cập nhật.
    """
    # Ghi DataFrame mới vào trang tính mới của tệp Excel đã có sẵn
    with pd.ExcelWriter(file_path,engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=new_sheet_name, index=False)

    # Đọc tệp Excel đã cập nhật và trả về DataFrame mới
    with pd.ExcelFile(file_path) as xls:
        sheet_names = xls.sheet_names
        dfs = []
        for sheet_name in sheet_names:
            df = pd.read_excel(xls, sheet_name)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

#add_dataframe_to_excel('test.xlsx', 'Rooms', pd.DataFrame(ROOMS, columns=colums['Rooms']))

#add_dataframe_to_excel('test.xlsx', 'Subjects', pd.DataFrame(SUBJECTS, columns=colums['Subjects']))

#add_dataframe_to_excel('test.xlsx', 'Intructors', pd.DataFrame(INSTRUCTORS, columns=colums['Instructors']))

#add_dataframe_to_excel('test.xlsx', 'TimeLessons', pd.DataFrame(TIMELESSONS, columns=colums['TimeLessons']))