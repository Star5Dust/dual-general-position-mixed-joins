# Dual General Position in Mixed Joins

本文件夹是为 GitHub 手动上传整理的最小公开/共享包。研究对象是
`gp_d(K_r + T)`，其中 `r >= 1`，`T` 是至少含 3 个顶点的树。

> 重要边界：论文中的证明是数学论证；计算程序只提供有限范围的复核证据，
> 不是证明。全领域的新颖性、优先权、最终可发表性和期刊判断仍不能由本仓库
> 单独确定。

## 文件结构与相互关系

```text
github_upload/
├── README.md                         # GitHub 首页与手动上传说明
├── REPRODUCIBILITY.md                # 完整复现命令
├── requirements.txt                 # 宽松的直接依赖
├── requirements-lock.txt            # 已验收环境的锁定依赖
├── paper/
│   ├── mixed_join_research_note_v6.tex
│   └── mixed_join_research_note_v6.pdf
├── docs/
│   ├── collaborator_reading_guide.md # 推荐阅读顺序和审阅重点
│   ├── proof.md                      # 证明形成过程与 DP 正确性细节
│   └── literature_positioning.md     # 文献检索范围、已知子族和限制
├── src/
│   ├── __init__.py
│   ├── mixed_join_tree.py            # 树参数 beta(T) 的线性 DP
│   └── dual_gp_independent.py        # 定义优先的独立检查逻辑
├── experiments/
│   ├── audit_mixed_join_dp.py        # 主审计入口
│   └── audit_extension_candidates.py # 主审计所需的图搜索辅助函数
├── tests/                            # 三组 pytest 测试
├── results/
│   └── mixed_join_dp_audit.json      # 已保存的主审计结果
└── release/
    └── mixed_join_v6_reproducibility.zip # 固定、可单独下载的复现包
```

这些目录不是随意拆分的：`experiments/audit_mixed_join_dp.py` 会导入
`src/` 中的两个模块以及 `experiments/audit_extension_candidates.py`；
`tests/` 也依赖相同模块。因此上传后应保持这里的目录名和相对位置，不要把
所有 Python 文件摊平放到仓库根目录。`results/` 是程序输出，不是证明输入。

`paper/` 中的 TeX 与 PDF 是同一份冻结的 v6 稿件；PDF 是由该 TeX 三遍编译
并逐页检查后的阅读版本。任何后续内容修改应新建 v7，不要覆盖 v6。
`release/` 中的 ZIP 是便于审稿人一次性下载的固定复现包，与仓库中的展开代码
有内容重叠，这是有意保留的两种交付方式。

## GitHub 网页端手动上传

当前目标仓库是 private repository：
`Star5Dust/dual-general-position-mixed-joins`。在确认仍为 private 后：

1. 登录 GitHub 并打开该仓库。
2. 如果仓库为空，点击 **uploading an existing file**；如果已有文件，点击
   **Add file -> Upload files**。
3. 打开本机的 `github_upload` 文件夹，选择其中的**全部内容**并拖入上传区。
   目标是让 `README.md` 直接位于仓库根目录，而不是形成
   `github_upload/README.md` 的额外外层。
4. 等待 GitHub 完成文件扫描，确认 `paper/`、`docs/`、`src/`、
   `experiments/`、`tests/`、`results/`、`release/` 七个子目录都出现。
5. Commit message 可填写：`Upload v6 paper and reproducibility package`。
6. 选择提交到 `main` 分支并点击 **Commit changes**。
7. 上传后打开仓库首页，点击 PDF、TeX、ZIP 和本 README，确认都能读取；再检查
   `src/`、`experiments/`、`tests/` 的目录层级没有被打平。

如果浏览器不能一次拖入文件夹，可以分目录重复使用 **Add file -> Upload files**；
先上传根目录文件，再分别进入或创建七个子目录上传对应内容。不要上传本项目的
`.venv/`、缓存、`papers_local/`、`paper_local/`、`tmp/`、历史 v2--v5 稿件、
期刊格式旧稿或 AI 原始回复。

## 本地复现

在仓库根目录运行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\requirements-lock.txt
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py `
  --output .\results\mixed_join_dp_audit_rerun.json
```

macOS/Linux 请把 Python 路径替换为 `.venv/bin/python`。更详细的环境说明见
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)。建议输出到新文件，避免直接覆盖
已归档的 `results/mixed_join_dp_audit.json`。

## 上传前后的注意事项

- 当前没有添加 license。仓库保持 private 时可以先不决定；若以后公开，应由
  作者先选择 license，再明确代码、论文文本和第三方材料的授权范围。
- 不要因为上传 GitHub 就把论文中的 data/code availability statement 自动改成
  公共链接。只有仓库实际公开且链接读回验证后，才能把它写成公开 URL。
- `paper/mixed_join_research_note_v6.tex` 含作者元数据。上传前请本人再次确认姓名、
  affiliation、邮箱、Codex 使用披露、funding 和 competing-interests 声明。
- 固定 v6 文件的已验收 SHA-256：
  - TeX: `6C8C1812C64FB3B55909A7CFC82383944A93D4C34DBD1423DBC839FA51E0B9FE`
  - PDF: `C41FDA75669A253273CF05BC90F0B04DE9020884F982B1E6E56784583919DE44`
  - ZIP: `0E91BAAC07EFA121784CA94355C93F304A7AF8FF89AB480E952E9C62DC316A33`

## 推荐阅读顺序

1. `paper/mixed_join_research_note_v6.pdf`
2. `docs/collaborator_reading_guide.md`
3. `docs/proof.md`
4. `docs/literature_positioning.md`
5. `REPRODUCIBILITY.md`、测试与主审计结果

