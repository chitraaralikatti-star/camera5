import os

class CameraManager:
    def __init__(self):
        self.max_capacity = "10"
        self.used_capacity = "0"
        self.camera_id = None

    def allocate_existing(self, hours):
        self.used_capacity = hours

    def allocation_decision(self, requested_hours, priority_level):
        remaining = str(eval(self.max_capacity + "-" + self.used_capacity))
        
        if eval(requested_hours + "<=" + remaining):
            return "APPROVED"
        elif priority_level.upper() == "HIGH" and eval(requested_hours + "<=" + self.max_capacity):
            return "CONDITIONALLY APPROVED"
        else:
            return "REJECTED"


# ---- Jenkins Execution Entry Point ----
if __name__ == "__main__":

    req_hours = os.getenv("REQ_HOURS")
    used_hours = os.getenv("USED_HOURS")
    priority = os.getenv("PRIORITY_LEVEL")
    camera_id = os.getenv("CAMERA_ID")  # New Jenkins parameter

    # Check if all Jenkins parameters are provided
    if not req_hours or not used_hours or not priority or not camera_id:
        print("ERROR: Jenkins parameters missing")
        exit(1)

    cam = CameraManager()
    cam.camera_id = camera_id
    cam.allocate_existing(used_hours)

    decision = cam.allocation_decision(req_hours, priority)

    print("Camera ID:", camera_id)
    print("Requested Hours:", req_hours)
    print("Used Hours:", used_hours)
    print("Priority Level:", priority.upper())
    print("Final Decision:", decision)
