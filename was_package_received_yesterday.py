def was_package_received_yesterday(tz_from, tz_to, start, duration):
    receive_time = (start + duration) - (tz_from - tz_to)
    return receive_time < 0
