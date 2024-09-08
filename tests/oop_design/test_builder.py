from hexlet_exercises.oop_design.builder import Booking


def test_booking():
    booking = Booking()

    assert not booking.book("2008-11-10", "2008-11-05")
    assert booking.book("2008-11-11", "2008-11-13")
    assert not booking.book("2008-11-12", "2008-11-12")
    assert not booking.book("2008-11-12", "2008-11-14")
    assert booking.book("2008-11-10", "2008-11-11")
    assert not booking.book("2008-11-12", "2008-11-13")
    assert not booking.book("2008-11-13", "2008-11-13")
    assert booking.book("2008-11-13", "2008-11-14")
    assert booking.book("2008-05-08", "2008-05-18")
    assert not booking.book("2008-05-09", "2008-05-10")
