from scheduler.controller import Controller
import pytest

controller = Controller()

def test_scheduler():

    # Basic add
    date_time = '2021-2-6 04:00'
    user_id = '123'
    response = controller.addAppointment(date_time, user_id)
    assert response['status'] == 200

    # Add same day
    date_time = '2021-2-6 05:00'
    user_id = '123'
    response = controller.addAppointment(date_time, user_id)
    assert response['status'] == 422

    # Add diff day but not on a half-hour block
    date_time = '2021-2-7 05:20'
    user_id = '123'
    response = controller.addAppointment(date_time, user_id)
    assert response['status'] == 422

    # Add diff day
    date_time = '2021-2-7 05:30'
    user_id = '123'
    response = controller.addAppointment(date_time, user_id)
    assert response['status'] == 200

    # Get appointments
    user_id = '123'
    response = controller.getAppointments(user_id)
    assert len(response['appointments']) == 2

    # Get first appointment details
    assert response['appointments'][0]['user_id'] == 123
    assert str(response['appointments'][0]['date_time']) == '2021-02-06 04:00:00'
