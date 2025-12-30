---
description: 如何啟動翻譯專案
---

// turbo-all
1. 啟動 Conda 環境並執行：
   ```bash
   conda activate translate-agent
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. 或者使用 `conda run` 直接執行：
   ```bash
   conda run -n translate-agent uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. 開啟瀏覽器並訪問：
   [http://localhost:8000](http://localhost:8000)
