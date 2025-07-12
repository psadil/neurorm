from pathlib import Path

from neurorm import freesurfer


def test_freesurfer():
    # Example usage
    subjects_dir = Path("/Applications/freesurfer/7.4.1/subjects")
    subject_id = "bert"

    subject = freesurfer.FreeSurferSubject.from_subjects_dir(subjects_dir, subject_id)
    assert isinstance(subject, freesurfer.FreeSurferSubject)
