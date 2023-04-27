import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db.service import get_list_data

rooms_db = get_list_data('rooms')
