from app.services.rag_service import rag_service

response = rag_service.ask(
    "What is this project about??"
)

print("\n========================")
print("QUESTION")
print("========================")

print(response["question"])

print("\n========================")
print("AI ANSWER")
print("========================")

print(response["answer"])

print("\n========================")
print("SOURCES")
print("========================")

for source in response["sources"]:
    print(source)