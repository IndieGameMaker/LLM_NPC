# 벡터 인덱스 구축 (적재 단계) / 1회 실행
from langchain_community.document_loaders import TextLoader  # md 파일 로딩
from langchain_qdrant import QdrantVectorStore # 벡터 검색 및 저장
from langchain_text_splitters import RecursiveCharacterTextSplitter # Chunk 단위로 문장을 분리
from langchain_ollama import OllamaEmbeddings

# 1) 로어 파일 로딩
docs = TextLoader("lore.md", encoding="utf-8").load()

# 2) 청크 단위로 분리
splitter = RecursiveCharacterTextSplitter(
    chunk_size=60, chunk_overlap=0, separators=["\n"]
)
chunks = splitter.split_documents(docs)

# 3) 임베딩 모델 적용 (벡터 DB화)
em = OllamaEmbeddings(model="bge-m3")

# 4) Qdrant 에 저장
db = QdrantVectorStore.from_documents(
    chunks,
    em,
    url="http://localhost:6333",
    collection_name="game_lore",
    force_recreate=True,
)

print(f"인덱싱 완료: {len(chunks)}개 조각")
