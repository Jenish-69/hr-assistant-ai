from typing import TypedDict
from langgraph.graph import StateGraph, END


class HRState(TypedDict):
    question: str
    intent: str
    answer: str


def classify_question(state: HRState):
    question = state["question"].lower()

    if "leave" in question:
        intent = "leave"
    elif "regularize" in question or "regularization" in question:
        intent = "regularization"
    elif "attendance" in question or "check in" in question or "check out" in question:
        intent = "attendance"
    else:
        intent = "general"

    return {"intent": intent}


def answer_question(state: HRState):
    intent = state["intent"]

    if intent == "leave":
        answer = "This is a leave-related question."
    elif intent == "regularization":
        answer = "This is an attendance regularization question."
    elif intent == "attendance":
        answer = "This is an attendance-related question."
    else:
        answer = "This is a general HR question."

    return {"answer": answer}


graph = StateGraph(HRState)

graph.add_node("classify_question", classify_question)
graph.add_node("answer_question", answer_question)

graph.set_entry_point("classify_question")
graph.add_edge("classify_question", "answer_question")
graph.add_edge("answer_question", END)

app = graph.compile()


question = input("Ask HR Graph: ")

result = app.invoke({
    "question": question,
    "intent": "",
    "answer": ""
})

print("\nDetected Intent:", result["intent"])
print("Answer:", result["answer"])