from typing import List

from pydantic import BaseModel, Field


# =========================================================
# ASK
# =========================================================

class AskRequest(BaseModel):

    question: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )


class AskResponse(BaseModel):

    answer: str

    mode: str


# =========================================================
# QUIZ
# =========================================================

class QuizRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=300
    )

    difficulty: str = "medium"

    question_count: int = Field(
        default=5,
        ge=3,
        le=10
    )


class QuizQuestion(BaseModel):

    question: str

    options: List[str]

    answer: int

    explanation: str


class QuizResponse(BaseModel):

    topic: str

    difficulty: str

    questions: List[QuizQuestion]

    mode: str


# =========================================================
# QUIZ RESULT
# =========================================================

class QuizResultRequest(BaseModel):

    questions: List[QuizQuestion]

    answers: List[int]


class QuizResultResponse(BaseModel):

    score: int

    total: int

    percentage: float

    level: str

    feedback: str

    weak_topics: List[str]


# =========================================================
# SUMMARY
# =========================================================

class SummaryRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=20,
        max_length=20000
    )

    length: str = "medium"


class SummaryResponse(BaseModel):

    summary: str

    mode: str


# =========================================================
# LEARNING PATH
# =========================================================

class LearningPathRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=300
    )

    level: str = "beginner"

    weeks: int = Field(
        default=4,
        ge=1,
        le=24
    )


class LearningPathResponse(BaseModel):

    topic: str

    level: str

    weeks: int

    roadmap: str

    mode: str


# =========================================================
# RECOMMENDATIONS
# =========================================================

class RecommendationRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=300
    )

    goal: str = Field(
        ...,
        min_length=1,
        max_length=1000
    )

    level: str = "beginner"


class RecommendationResponse(BaseModel):

    recommendations: str

    mode: str