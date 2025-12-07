# from pydantic import BaseModel

# class Student(BaseModel):
#     name:str

# new_student={"name":"Guslhan"}
# student=Student(**new_student)
# print(student)



# # but if we pass integer instead of string in name then  it will throw error 
# # this validate the data
# from pydantic import BaseModel
# from typing import Optional
# class Student(BaseModel):
#     name:str="Gulshan"
#     age:Optional[int]=None
# new_student={"age":"21"}  #will not work for "twenty-one"
# student=Student(**new_student)
# print(student)

## Field function
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str="Gulshan"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0 , lt=10 ,default =6,description="Academically weak or strong student cannot only be evaluated by cgpa")
    phone: str = Field(
        pattern=r"^[6-9]\d{9}$",default='8709596670',
        description="Indian phone number must be 10 digits and start with 6-9"
    )
new_student={"age":"21",'email':'gks@gmail.com','cgpa':9.3} 
new_student2={"age":"21",'email':'gks@gmail.com','phone':'8709596673'}
student1=Student(**new_student)
student2=Student(**new_student2)
print("="*40)
print(student1)
print("-"*40)
print(student2)
stud=student1.model_dump_json()
print("="*40)
print(stud)

