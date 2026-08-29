# Dual General Position in Graph Products and Mixed Joins

## 项目目标

本项目研究图乘积与 join 中的 dual general position 问题。长期目标是：精确计算小规模例子，寻找结构规律，自动搜索反例，提出有依据且可检验的猜想，尝试严格证明，并用独立计算方法复核实现，最后形成 research note。

计算实验、猜想、证明和文献事实必须明确区分。目前不对研究问题的新颖性或解决状态作任何声明。

**Computational evidence is not a proof.**

**Novelty has not yet been established.**

## 继续项目

项目任务、已核验事实、当前进度和唯一下一步统一维护在 `PROJECT_STATUS.md`。新的工作窗口应先读取 `AGENTS.md` 和 `PROJECT_STATUS.md`，再根据其中状态继续。

## 当前研究问题

最初问题是 `gp_d(K_m ∘ T)`，其中 `K_m` 是完全图、`T` 是树；该方向已有精确覆盖它的 Jiang 预印本公式，并已在本项目中完成独立 proof audit 与计算复核。当前内部 research note 研究 Jiang 明确未覆盖的 mixed join `gp_d(K_r + T)`，范围为 `r >= 1`、`|V(T)| >= 3`。准确状态和唯一下一步始终以 `PROJECT_STATUS.md` 为准。

## 文件夹说明

- `papers_local/`：本地论文资料；该目录不进入 Git。
- `notes/`：研究日志、待核对定义、文献笔记和猜想记录。
- `src/`：Python 源代码。
- `tests/`：代码测试。
- `experiments/`：可复现的计算实验。
- `results/`：实验输出与整理后的结果。
- `proofs/`：证明草稿与证明检查记录。
- `drafts/`：research note 工作稿；最新已编译并逐页审阅的基线是
  `drafts/mixed_join_research_note_v6.tex`。冻结的 v4 已分别交给四个网页 AI
  审查，逐条裁决见 `notes/external_ai_review_adjudication.md`；吸收有效小修订
  后的 v5 已冻结。GLM 5.3 的后续对抗审稿、逐项裁决和有效修订形成当前
  v6，详见 `notes/glm_5_3_review_adjudication.md`。五个计划投稿
  期刊的本地格式版本位于 `drafts/journal_versions/`，文件名即期刊名；它们
  仍基于 v4，现只作格式参考，不能直接投稿。v6 已由 MiKTeX-pdfTeX
  真实编译并完成原生日志和 14 页逐页验收；多模型 AI 审查仍不等于人类
  同行评审。`v2` 至 `v5` 均冻结保留，
  内容同步的 Markdown 版本为 `drafts/mixed_join_research_note.md`。编号 TeX
  一经后续版本取代即不得覆盖；详细映射与格式依赖见
  `drafts/TEX_VERSION_HISTORY.md` 和 `drafts/journal_versions/README.md`。

## 安装环境

本项目使用 Python 虚拟环境，避免项目依赖影响系统中的其他 Python 项目。

Windows PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-lock.txt
```

macOS 或 Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
```

## 运行测试

激活虚拟环境后，在项目根目录运行：

```powershell
python -m pytest -q tests
```
