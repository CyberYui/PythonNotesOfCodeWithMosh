import time
import mlx.core as mx
from mlx_lm import load, generate

# 强制用GPU（MLX核心，彻底解决CPU fallback）
mx.set_default_device(mx.gpu)

# 你的模型路径（确认正确）
MODEL = "/Users/yui/.lmstudio/models/Lowkey-Loki/Codestral-22b-v0.1-mlx-3_6bit"

# 加载模型
print("正在加载模型（强制GPU）...")
model, tokenizer = load(MODEL)

# 测试prompt
prompt = "def hello():"

# 生成（极简参数，老版本mlx-lm100%兼容）
start = time.time()
out = generate(model, tokenizer, prompt=prompt, max_tokens=32)
end = time.time()

# 计算速度
tokens = len(tokenizer.encode(out))
speed = tokens / (end - start)
print(f"✅ 真实速度：{speed:.2f} tokens/s")
print(f"生成内容：{out}")
