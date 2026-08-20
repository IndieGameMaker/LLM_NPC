# FastAPI : 웹 서버 본체를 만드는 클래스
from fastapi import FastAPI
# BaseModel : 요청/응답 JSON의 형태를 클래스로 정의하고 검증해주는 도구
from pydantic import BaseModel

# 서버 객체 생성 (앞으로 모든 엔드포인트를 여기에 등록한다)
app = FastAPI()

# 유니티(스타터 패키지)가 보낼 요청 형태
# = : 뒤의 값은 기본값. 유니티가 안 보내도 이 값이 들어간다
class NpcChatRequest(BaseModel):
    player_id: str = "player1"   # 어느 플레이어인가 (세이브 슬롯)
    npc_id: str = "wizard"       # 누구에게 말을 거는가 (wizard/guard/blacksmith)
    message: str                 # 무슨 말을 했는가

# @app.get(...) : 아래 함수를 GET 요청 처리기로 등록하는 데코레이터
@app.get("/check")
def health():
    # 파이썬 딕셔너리를 반환하면 FastAPI가 알아서 JSON으로 바꿔준다
    return {"status": "ok"}

# @app.post(...) : POST 요청 처리기로 등록
@app.post("/npc/chat")
def npc_chat(req: NpcChatRequest):   # req 안에 검증된 요청 데이터가 들어온다
    # 아직 에코 — 통신만 확인
    # f"..." : 문자열 안에 {변수}를 넣는 f-string (C#의 $"..." 와 같다)
    return {
        "reply": f"[echo] {req.npc_id} 에게: {req.message}",
        "npc_name": req.npc_id,
        "gold": -1,               # 아직 골드 기능 없음 → -1이면 유니티가 HUD를 안 건드린다
    }