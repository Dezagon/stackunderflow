from fastapi import FastAPI, status

from models import Question, Answer
from schemas import CreateQuestionRequest



app = FastAPI()

questions: list[Question] = [
    Question(
        question="I've been trying to make a for loop but I cannot figure it out. Anyone have any idea?", 
        title="How do you make a for loop?", 
        topic="Python", 
        likes=3, 
        user="Tony", 
        answers=[
            Answer(
                response="Why would you even want to do it that way",
                likes=2000,
                answered=False,
                user="Treyson"
            ),
            Answer(
                response="ratioed",
                likes=6000,
                answered=False,
                user="Brandon"
            ),
            Answer(
                response="It should look something like this: for i in range(10): ....",
                likes=47,
                answered=True,
                user="Hannah"
            ),

        ]
    )
]

@app.get("/questions")
async def get_questions() -> list[Question]:
    return questions

@app.post("/questions", status_code=status.HTTP_201_CREATED)
async def create_question(create_question_request: CreateQuestionRequest) -> Question:
    question: Question = Question(**create_question_request.model_dump())
    questions.append(question)
    return question