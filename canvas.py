from canvasapi import Canvas # pip install canvasapi
import csv
import concurrent.futures
from functools import partial


KEY = '' # Your Canvas API key
URL = 'https://issaquah.instructure.com/' # Your Canvas API URL
STUDENT_ID = 1905851

COURSE = '' # Your course ID

canvas = Canvas(URL, KEY)

# assignments = len(list(course.get_assignments()))
# writer = csv.writer(open('report.csv', 'w'))

def main():
    student = canvas.get_user(STUDENT_ID)
    print(f'student: {student}')
    sections = course.get_sections()

#     writer.writerow(['Name', 'Building', 'Last Activity', 'Complete', 'Missing'])

#     for section in sections:
#         enrollments = section.get_enrollments(state="active", type="StudentEnrollment")
        
#         # Play with the number of workers.
#         with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            
#             data = []
#             job = partial(process_user, section=section)

#             results = [executor.submit(job, enrollment) for enrollment in enrollments]
        
#             for f in concurrent.futures.as_completed(results):
#                 data.append(f.result())
#                 print(f'Processed {len(data)} in {len(list(enrollments))} at {section}')
                
#         writer.writerows(data)

# def process_user(enrollment, section):
#     missing = get_user_missing(section, enrollment.user['id'])
#     return [ 
#         enrollment.user['sortable_name'], 
#         section.name, 
#         enrollment.last_activity_at, 
#         len(missing), ', '.join(missing)
#     ]

# def get_user_missing(section, user_id):
#     submissions = section.get_multiple_submissions(student_ids=[user_id], 
#                                                    include=["assignment", "submission_history"], 
#                                                    workflow_state="unsubmitted")

#     missing_list = [item.assignment['name'] for item in submissions \
#         if item.workflow_state == "unsubmitted" and item.excused is not True]

#     return missing_list


if __name__ == "__main__":
    main()