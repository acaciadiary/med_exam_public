from scripts.exams.moex_sources import get_preset


def test_physician_115_first_preset_has_expected_subject_urls():
    subjects = get_preset("physician-115-first")

    assert len(subjects) == 6
    assert subjects[0].question_url.endswith("c=301&code=115020&q=1&s=0101&t=Q")
    assert subjects[1].answer_url.endswith("c=301&code=115020&q=1&s=0102&t=S")
    assert subjects[2].question_url.endswith("c=302&code=115020&q=1&s=0103&t=Q")
    assert subjects[-1].correction_url.endswith("c=302&code=115020&q=1&s=0106&t=M")


def test_physician_115_second_preset_uses_stage_specific_exam_codes():
    subjects = get_preset("physician-115-second")

    assert len(subjects) == 6
    assert subjects[0].question_url.endswith("c=301&code=115090&q=1&s=0101&t=Q")
    assert subjects[1].answer_url.endswith("c=301&code=115090&q=1&s=0102&t=S")
    assert subjects[2].question_url.endswith("c=302&code=115070&q=1&s=0101&t=Q")
    assert subjects[-1].answer_url.endswith("c=302&code=115070&q=1&s=0104&t=S")
    assert all(not subject.has_correction for subject in subjects)
