from fastapi import FastAPI
from server.routes.employee import router as employee_router
from server.routes.meeting import router as meeting_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(employee_router, prefix="/api/v1/employees", tags=["employees"])
app.include_router(meeting_router, prefix="/api/v1/meetings", tags=["meetings"])