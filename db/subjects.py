from service import get_list_data

subjects_data = get_list_data('subjects')


def get_subject_by_id(id):
    """ 
    Lấy thông tin môn học theo id
    """
    for subject_tuple in subjects_data:
        subject = {'id': subject_tuple[0], 'name': subject_tuple[1], 'number_of_period': subject_tuple[2]}
        if subject['id'] == id:
            return subject




