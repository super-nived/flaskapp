from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Dummy data simulating machine usage records
MACHINE_USAGE = [
    {
        "id": str(uuid.uuid4())[:15],
        "machineId": "MC235",
        "startTime": "2025-05-09 12:00:00.000Z",
        "endTime": "2025-05-12 12:00:00.000Z",
        "status": None
    }
    for _ in range(2)  # You can change this to more records if needed
]

@app.route("/api/machine-usage", methods=["GET"])
def get_machine_usage():
    time.sleep(2)  # ⏳ 2-second delay

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("perPage", 10))

    total_items = len(MACHINE_USAGE)
    total_pages = (total_items + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    items = MACHINE_USAGE[start:end]

    return jsonify({
        "data": {
            "items": items,
            "page": page,
            "perPage": per_page,
            "totalItems": total_items,
            "totalPages": total_pages
        },
        "message": "Data fetched successfully",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
