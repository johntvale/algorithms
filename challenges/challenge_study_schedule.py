def study_schedule(permanence_period, target_time):
    students_in_target_time = 0
    try:
        for student_time_track in permanence_period:
            if student_time_track[0] <= target_time <= student_time_track[1]:
                students_in_target_time += 1
        return students_in_target_time
    except TypeError:
        return None
