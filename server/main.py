from fastapi import FastAPI
from server.routes.employee import router as employee_router
from server.routes.meeting import router as meeting_router

app = FastAPI()

app.include_router(employee_router, prefix="/api/v1/employees", tags=["employees"])
app.include_router(meeting_router, prefix="/api/v1/meetings", tags=["meetings"])