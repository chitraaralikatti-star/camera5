import pytest
from camera import CameraManager

# -------------------------------
# Test Cases: requested_hours, used_hours, priority, camera_id, expected_decision
# -------------------------------
test_cases = [
    ("3", "2", "LOW", "CAM001", "APPROVED"),
    ("5", "6", "LOW", "CAM002", "REJECTED"),
    ("5", "6", "HIGH", "CAM003", "CONDITIONALLY APPROVED"),
    ("10", "0", "LOW", "CAM004", "APPROVED"),
    ("11", "0", "HIGH", "CAM005", "REJECTED"),
]

@pytest.mark.parametrize("req_hours, used_hours, priority, cam_id, expected", test_cases)
def test_allocation_decision(req_hours, used_hours, priority, cam_id, expected):
    cam = CameraManager()
    cam.camera_id = cam_id
    cam.allocate_existing(used_hours)
    decision = cam.allocation_decision(req_hours, priority)
    assert decision == expected

# -------------------------------
# Test Priority Case-Insensitive
# -------------------------------
def test_priority_upper_case():
    cam = CameraManager()
    cam.camera_id = "CAM100"
    cam.allocate_existing("5")
    decision = cam.allocation_decision("3", "high")  # lowercase
    assert decision == "CONDITIONALLY APPROVED"

# -------------------------------
# Test CameraID Assignment
# -------------------------------
def test_camera_id_assignment():
    cam = CameraManager()
    cam.camera_id = "CAM999"
    assert cam.camera_id == "CAM999"
