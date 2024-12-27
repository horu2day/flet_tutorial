플랫 따라하기 메뉴얼이다.

# Todo App with Flet

Clean Architecture를 적용한 Python Flet 기반의 Todo 애플리케이션입니다.

## 설치 방법

1. 저장소 클론
```bash
git clone <repository-url>
cd todo-app




일단 Root 폴더 만들고
소스를 생성해라.
AI를 시켜서 프레임 워크를 만든다.
- Todo App
todo_app/
├── .venv/                     # 가상환경 디렉토리
├── core/
│   ├── __init__.py
│   ├── models.py
│   └── state.py
├── ui/
│   ├── __init__.py
│   ├── widgets/
│   │   ├── __init__.py
│   │   └── todo_item.py
│   └── app.py
├── main.py
├── requirements.txt          # 의존성 파일
├── .gitignore               # Git 설정 파일
└── README.md                # 프로젝트 설명 파일

cd todo_app
# 파이썬 가상환경 생성
python -m venv .venv

# 가상환경 활성화
# Windows의 경우:
.venv\Scripts\activate
# macOS/Linux의 경우:
source .venv/bin/activate

requirements.txt 생성: 
flet>=0.21.0
``` bash 의존성 설치
pip install -r requirements.txt
```
실행
``` bash
python main.py
```
디버깅 vsCode 디버거에서 
launch.json 생성
 "args"에서 -r 은 핫리로더 : 저장하면 UI 재로딩 개 편함.
-------------------------------------------------------------
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Flet: Run with Hot Reload",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/.venv/Lib/site-packages/flet_cli/cli.py",
      "args": [
        "run",
        "-r",
        "${workspaceFolder}/client/app.py"
      ],
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    },
    {
      "name": "Flet: Run Debug",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/client/app.py",
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  ]
}
---------------------------------------------------------------------------------------------------


.gitignore 파일: 
--------------------------------------------------------------------------------------------
# 가상환경
.venv/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.idea/
.vscode/
*.swp
*.swo

# 운영체제
.DS_Store
Thumbs.db
--------------------------------------------------------------------------------------------








