from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("website_context.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Total text length:", len(text))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print("Total chunks created:", len(chunks))

print("Sample chunk:")
print(chunks[0])