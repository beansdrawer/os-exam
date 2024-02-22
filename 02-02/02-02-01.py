import psutil

# 실행중인 프로세스를 순차적으로 검색
for proc in psutil.process_iter():
  
  # 프로세스 이름을 ps_name에 할당
  ps_name = proc.name()

  name = "pwsh"

  if name in ps_name :
    child = proc.children()
    print(ps_name, proc.status(), proc.parent(), child)

    if child :
      print(f"{name}의 자식 프로세스:", child)