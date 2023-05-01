from db.service import get_list_data

# (get_list_data_pretty_table('instructors'))
instructors_data = get_list_data('instructors')

def get_instructor_by_id(id):
    for instructor_tuple in instructors_data:
        instructor = {'id': instructor_tuple[0], 'name': instructor_tuple[1], 'sex': instructor_tuple[2], 'email': instructor_tuple[3], 'phone_number': instructor_tuple[4], 'address': instructor_tuple[5]}
        if instructor['id'] == int(id):
            return instructor

print(get_instructor_by_id(2))

