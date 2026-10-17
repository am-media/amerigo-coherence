"""Tiny deterministic fixtures. Examples, not a universal simulator."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Pose:
    capture_ms: int
    yaw: float

def pose_fixture():
    return [Pose(0, 0.0), Pose(40, 10.0), Pose(80, 20.0)]

def frame_fixture():
    return [(0, "frame0"), (40, "frame1"), (80, "frame2")]

def align_by_capture_time(frames, poses, pose_delivery_delay_ms=0):
    """Illustrates why capture timestamps, not receipt times, define pairing."""
    delivered = [(p.capture_ms + pose_delivery_delay_ms, p) for p in poses]
    by_capture = {p.capture_ms: p for _, p in delivered}
    return [(name, by_capture[t].yaw) for t, name in frames]

def test_alignment_under_delay():
    assert align_by_capture_time(frame_fixture(), pose_fixture(), 120) == [
        ("frame0", 0.0), ("frame1", 10.0), ("frame2", 20.0)
    ]

def test_bad_matching_detected():
    bad = [("frame0", 10.0), ("frame1", 0.0), ("frame2", 20.0)]
    expected = align_by_capture_time(frame_fixture(), pose_fixture(), 120)
    assert bad != expected

if __name__ == "__main__":
    test_alignment_under_delay()
    test_bad_matching_detected()
    print("Fixture examples passed (illustrative, not real SRT or FreeD validation)")
