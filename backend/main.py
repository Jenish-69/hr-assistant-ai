from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hr_graph_rag import app as hr_graph_app

from schemas import (
    AskRequest,
    LeaveRequest,
    RegularizationRequest
)

from database import (
    attendance_data,
    leave_requests,
    regularization_requests
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "HR Assistant API Running"
    }


@app.get("/attendance")
def get_attendance():
    return attendance_data


@app.post("/apply-leave")
def apply_leave(request: LeaveRequest):

    leave_requests.append(request.dict())

    return {
        "message": "Leave request submitted successfully",
        "data": request.dict()
    }


@app.post("/regularize")
def regularize_attendance(
    request: RegularizationRequest
):

    regularization_requests.append(
        request.dict()
    )

    return {
        "message": "Regularization request submitted successfully",
        "data": request.dict()
    }


@app.get("/leave-requests")
def get_leave_requests():
    return leave_requests


@app.get("/regularization-requests")
def get_regularization_requests():
    return regularization_requests
@app.post("/ask")
def ask_hr_assistant(request: AskRequest):
    result = hr_graph_app.invoke(
    {
    "question": request.question,
    "context": "",
    "answer": "",
    "messages": [
        ("user", request.question)
    ]
},
    config={
        "configurable": {
            "thread_id": "hr-user-1"
        }
    }
)

    return {
        "answer": result["answer"]
    }