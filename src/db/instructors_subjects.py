from db.service import get_list_data

# get_list_data_pretty_table('instructors_subjects')
instructors_subjects_data = get_list_data('instructors_subjects')

def get_instructor_subject_by_id(id):
    for instructor_subject_tuple in instructors_subjects_data:
        instructor_subject = {'id': instructor_subject_tuple[0], 'instructor_id': instructor_subject_tuple[1], 'subject_id': instructor_subject_tuple[2]}
        if instructor_subject['id'] == int(id):
            return instructor_subject
    
def get_subject_by_instructor_id(id):
    for instructor_subject_tuple in instructors_subjects_data:
        instructor_subject = {'id': instructor_subject_tuple[0], 'instructor_id': instructor_subject_tuple[1], 'subject_id': instructor_subject_tuple[2]}
        if instructor_subject['instructor_id'] == int(id):
            return instructor_subject
        