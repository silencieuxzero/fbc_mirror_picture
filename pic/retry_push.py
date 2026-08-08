import time, subprocess

# 持续重试 push，直到成功
for i in range(20):
    r = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=r"E:\fbc_github",
        capture_output=True, text=True, timeout=240
    )
    if r.returncode == 0:
        with open(r"E:\fbc_github\push_result.txt", "w", encoding="utf-8") as f:
            f.write(f"PUSH OK on attempt {i+1}\n{r.stdout}")
        print(f"PUSH 成功 (第{i+1}次)")
        break
    else:
        print(f"第{i+1}次失败: {r.stderr.strip()[-120:]}")
        time.sleep(20)
else:
    with open(r"E:\fbc_github\push_result.txt", "w", encoding="utf-8") as f:
        f.write("PUSH FAILED after 20 attempts")
    print("PUSH 最终失败")
