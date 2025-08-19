import requests
import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, validator

from enums import DepartmentEnum

url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'

response = requests.get(url)
data = response.json()
#print(data)

class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4)
    course: str | None
    department: DepartmentEnum
    fees_paid: bool

    @validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        sixteen_years_ago = sixteen_years_ago.date()

        if value > sixteen_years_ago:
            raise ValueError("Too young to enrol, sorry!")
        return value

for student in data:
    # create Pydantic model object by unpacking key/val pairs from our JSON dict as arguments 
    model = Student(**student)
    print(model.json())


