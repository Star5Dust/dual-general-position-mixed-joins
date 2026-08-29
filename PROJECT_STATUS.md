# Project Status and Handoff

Last updated: 2026-08-29 (v7 compiled and verified with public GitHub availability)

本文件是项目任务和当前进度的单一交接入口。以后开启新的 Codex 窗口时，项目助手必须先完整阅读本文件和 `AGENTS.md`，再继续工作。完成任何研究阶段后，必须同步更新本文件，不能只把进度留在聊天记录中。

## 1. 给新窗口的继续工作说明

1. 先阅读根目录的 `AGENTS.md` 和本文件。
2. 根据本文件的“当前阶段”和“下一步任务”继续，不要依靠聊天上下文猜测。
3. 需要数学细节时，再读取本文件列出的对应 canonical notes。
4. 不得把 `UNKNOWN` 自动改成肯定或否定结论。
5. 本轮工作结束前，更新本文件中的日期、已完成事项、当前状态和下一步任务。

## 2. 用户背景与解释要求

- 用户是机械本科，数学背景较弱。
- 数学定义必须严格，同时使用本科低年级能够理解的中文解释。
- 不要假设用户熟悉图论、Python、Git 或 LaTeX。
- 结论必须区分为：**文献事实、直接逻辑推论、计算实验、猜想、证明**。
- “看起来正确”不能作为定理或证明。

## 3. 研究目标

研究对象是

$$
gp_d(K_m\circ T),
$$

其中 $K_m$ 是 $m$ 个顶点的完全图，$T$ 是树，$\circ$ 表示 lexicographic product，$gp_d$ 表示 dual general position number。

长期目标：

1. 精确计算小规模例子；
2. 寻找可能的结构规律；
3. 自动搜索反例；
4. 提出有依据且可检验的猜想；
5. 尝试严格证明；
6. 对最终结果进行独立计算验证；
7. 形成可投稿的 research note。

当前不能声称 restricted tree problem 是新的，也不能声称它已在整个数学文献中被解决或未被解决。

## 4. 当前阶段

当前处于：**mixed join $K_r+T$ 的 v3--v6 均已冻结；最新不可覆盖稿为 `drafts/mixed_join_research_note_v7.tex`，50,063 bytes，SHA-256 `8668552914DFC5B177FC951D102C3A8BB75EB0DFD92E5495DE51DED7A902D992`。v7 只把经匿名访问核验的公开仓库 `https://github.com/Star5Dust/dual-general-position-mixed-joins` 及其中固定 archive 路径写入复现和 data/code availability 段落，没有改变定理、证明、数值、引文或计算主张。公开仓库的 v6 PDF、固定 ZIP 与主 JSON 已分别与本地 canonical 文件逐字节匹配；TeX 在忽略行尾差异后内容相同。Pandoc 返回 0，测试重跑为 `30 passed in 0.36s`。MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 三遍编译得到 14 页 A4、470,873-byte PDF，SHA-256 `B10D50C0A77F76AD24E87A78DCFC9C9A1D9D7385FD42D38AA311C1989C887500`；27,395-byte 原生日志 SHA-256 为 `EB46D421FF2D3293C2F177156BF10349D198881E8053C64C810B18D34147C3F2`，扫描为零 error/warning/box warning/未定义引用引文/缺字/rerun。字体全部嵌入，PDF 中仓库 URI 可枚举，文本抽取无未解决投稿标记，14 页已渲染目检通过。DMGT 首投只需当前 v7 PDF；公开仓库已经提供代码与固定 ZIP，所以不再需要另附 ZIP 或发邮件。多模型 AI 审查仍不等于人类同行评审，全领域 novelty/priority/publishability 仍为 `UNKNOWN`。唯一直接下一步是作者删除投稿草稿中的 v6 PDF，上传并预览 v7 PDF，然后完成最终提交。**

已经完成：

- 项目目录、Git repository、`.gitignore`、Python 虚拟环境和基础笔记初始化；
- 核心论文全文读取及正式定义提取；
- 核心论文 references 的 citation-chain 起点整理；
- 两篇最关键基础论文的全文核验；
- 已核验定理对 $K_m\circ T$ 的 applicability audit；
- 对 Tian and Klavžar (2025)、2026 核心论文和 Anand et al. (2012) 完成窄范围 citation-forward search；
- 逐篇核验核心论文的两篇可识别前向引用，以及其他与 dual general position 相关的高相关候选；
- 完成带查询矩阵、数据库计数、去重和覆盖限制的系统性 topic-based literature search；
- 发现并全文核对 Weiqi Jiang 于 2026-08-27 发布的 exact-target Zenodo 预印本 v1.0.1；
- 从 Zenodo 重新恢复 Jiang v1.0.1 PDF 与 supplement，并核对 SHA-256 和 MD5；
- 逐步审计 Jiang Definitions、Theorems 3.1--3.2 和 Proposition 3.3 的必要性、充分性与全部指定边界情形，未发现漏洞；
- 在隔离目录验证 supplement manifest，使用 Python 3.13.5 复现 36/36 tests 和 1,064 次比较，全部 mismatch 为 0；
- 实现不使用位掩码、补图二染色或 supplement import 的第二套 direct/formula verifier，并增加 pytest 测试；
- 项目独立实现完成 217 个最大值比较和 4,780 个集合级分类比较，均为 0 mismatch；
- 独立证明 tree corollary：$K_1$ 为 $m$，$K_2,P_3,P_4$ 为 $2m$，其他树为 $0$（$m\ge2$）；
- 建立 `proofs/jiang_v1_0_1_audit.md`、`proofs/tree_corollary.md`、机器可读结果和本阶段 research log。
- 完成 Jiang 未覆盖方向的有边界文献与可行性审计，核对 mixed joins 与 arbitrary first factor 两条方向；
- 识别并排除已被 Jiang Theorem 5.1 覆盖的伪扩展 $P_3\circ T\cong T+2T$；
- 比较 $K_r+T$ 与 $P_n\circ T$ 两个具体候选，只选择 mixed join $K_r+T$ 继续；
- 得到尚待正式 proof audit 的两分支可行性归约，引入 apex-avoiding 树参数 $\beta(T)$；
- 保留反例 $gp_d(K_r+K_{1,3})=3$（所有 $r\ge1$），它否定 mixed join 只需简单加入 $r+q_2(T)$ 的朴素外推；
- 新增有测试的最小审计脚本；92 个 mixed-join 比较为 0 mismatch，17 个 path-first 筛选例均为 0，该阶段项目测试当时更新为 23 passed。
- 完成 mixed join 两分支的独立正式证明，逐步核对 apex-meeting、apex-avoiding、$q_2(T)=0$、$r=1$ 与小树边界；
- 证明 $\beta(T)$ 的局部结构刻画：入选的度 2 顶点必须恰有一个入选邻点，度至少 3 的顶点不能入选；
- 建立并证明四边界状态的 rooted-tree dynamic program，可在线性时间、线性空间内计算 $\beta(T)$ 并回溯一个最大集合；
- 实现不依赖 shortest-path checker 的 DP；在 3--12 阶全部 985 棵非同构树上与子集穷举比较，并做 11,003 次换根比较和 985 次回溯检查，全部 mismatch/failure 为 0；
- 在 3--8 阶全部 46 棵非同构树和 $r=1,2,3,4$ 上完成 184 次 mixed-join 公式与定义优先最短路 checker 比较，0 mismatch；项目测试更新为 29 passed，并包含 2,500 阶长路的非递归回溯回归测试。
- 完成围绕 $gp_d(K_r+T)$ 的系统文献定位：重新核对 Jiang concept/version 与同行评审关联，运行 arXiv、DataCite、zbMATH、Crossref、OpenCitations、survey 和通用网页的同义术语查询矩阵，并记录 OpenAlex/Semantic Scholar 的覆盖失败；
- 发现并核对同行评审论文中的直接既有子族：fan graph $F_n=K_1+P_n$ 的 $gp_d(F_n)=\lfloor2(n+1)/3\rfloor=\lceil2n/3\rceil$；因此 $r=1$ 的 path 子族不能作为新结果包装；
- 保留 removal-paper 版本差异：旧 author-hosted v1 写成 ceiling，arXiv v2 改为与既有 fan 公式和项目定理一致的 floor；version-of-record 正文的精确显示仍为 `UNKNOWN`；
- 明确真实增量是 all-tree、任意 $r$ 的 mixed-join 两分支分类、$\beta(T)$ 局部结构和线性最大集合回溯；与 dissociation set 相邻但不等价；
- 形成 `notes/mixed_join_literature_positioning.md` 的 query matrix、逐篇纳入/排除表、覆盖限制、research-note 结构和待补内容，结论为 **CONDITIONAL GO FOR AN INTERNAL DRAFT**。
- 建立 `drafts/mixed_join_research_note.md`，完成英文 Introduction / literature positioning 初稿，明确区分 Jiang 的 complete-first-factor 结果、其 mixed-join 边界和 removal paper 已知的 fan 子族，并保留全领域 novelty 为 `UNKNOWN`。
- 完成 research note 的自包含 Preliminaries：严格定义 graph distance、geodesic、interval、convexity、general/dual general position、complete join、$q_2(T)$ 与 $\beta(T)$，并固定 $C=V(K_r)$、$H=K_r+T$。
- 完成 research note 的 apex-meeting branch：自包含地证明 $X\cap C\ne\varnothing$ 时，$X$ 为 dual general-position set 当且仅当所选与未选 tree side 都诱导 clique；并推出该分支存在当且仅当 $q_2(T)>0$，最大值为 $r+q_2(T)$。
- 完成 research note 的 apex-avoiding branch：自包含地证明 $X\subseteq V(T)$ 时，dual general position 等价于 $\Delta(T[X])\le1$ 且每个 $x\in X$ 至多有一个未选 tree neighbor；并推出该分支最大值为 $\beta(T)$。
- 完成 research note 的两分支合并：先证明以 $q_2(T)$ 与 $\beta(T)$ 表示的精确公式，再自包含地分类树的两 clique 分割、证明 $q_2(T)>0$ 恰好对应 $P_3,P_4$，核对 $\beta(P_3)=2$、$\beta(P_4)=3$，并推出引言中的简化公式。
- 完成 research note 的 $\beta(T)$ 局部刻画：用每个入选点的入选/未选邻点计数证明原始两个约束等价于“度至少 3 的点禁选、度 2 的入选点恰有一个入选邻点”，显式覆盖度 0、1 边界，并推出所有叶子构成可行集及 $\beta(T)\ge |L(T)|$。
- 完成 research note 的 rooted-tree DP：定义父点标签边界状态与不可行状态，给出精确递推并用树高归纳证明，说明保存最优子标签后可自顶向下重构最大 $\beta$-feasible set，并证明求值、存储和回溯均为线性规模。
- 完成 research note 的 worked examples：证明 $\beta(K_{1,k})=k$ 与 once-subdivided star 的 $\beta=2k$，恢复 $K_{1,3}$ 反例；再用三点分块上界与周期选择词独立证明 $\beta(P_n)=\lceil2n/3\rceil$，推出任意 $r$ 的 path 公式，并明确把 $r=1$ 的 fan 公式标为已发表结果的一致性检查。
- 完成 research note 的可复现性 section：从实际源码、测试与 JSON 核对两套独立路线，记录 985 次 DP/穷举比较、11,003 次换根比较、985 次回溯检查和 184 次公式/最短路定义比较全部零失败；2026-08-29 重跑得到相同矩阵与 `29 passed`，并记录环境、命令、重叠计数限制和五个关键 artifact 的 SHA-256。
- 完成 research note 的首次全稿一致性审计：逐条核对定义、两分支证明、树特化、DP、例子、计算计数、范围和引用；未发现数学错误。修正引言未来时，补入 $\beta$ 与 dissociation set 不等价的 $K_{1,3}$ 见证，完善 reference [1]/[3] 元数据，并确认 76 个 display-math delimiters、2 个 code fences、7 对 cases 环境、6 个唯一公式标签及全部定理编号/交叉引用配对。
- 完成 research note 的 Conclusion and limitations：总结两分支、简化公式、$\beta(T)$ 局部刻画与线性重构；明确 fan 为 prior subfamily、计算非证明、Jiang 仍为 preprint、订阅数据库覆盖与全领域 novelty/priority 保持 `UNKNOWN`，并排除 arbitrary first factor、一般 mixed complete joins 和 dormant $P_n\circ T$。
- 完成首轮稿最终整理：补充 Abstract，更新 README 的当前研究问题与真实 `drafts/` 路径，修正 brute-force helper 的陈旧 7 阶 docstring（主审计实际到 12 阶），将该实际依赖加入 hash 表，把历史 notes 的旧 next step 标为已完成，并更新 canonical draft 描述；结构扫描无未配对项，文档修正后测试仍为 `29 passed`。
- 完成稿后有边界版本/文献刷新：Zenodo/DataCite 仍只有 Jiang v1.0.0/v1.0.1 且无 journal related identifier；arXiv、DataCite、zbMATH、Crossref/OpenCitations 未给出新的目标命中或直接引文。OpenAlex 连已知 product DOI 都返回 0，继续作为覆盖失败；Elsevier API/ScienceDirect 分别返回未授权 400/403，in-app Browser 停在 CAPTCHA，未绕过，因此 fan VOR 正文公式仍为 `UNKNOWN`。
- 完成 `drafts/mixed_join_research_note.tex`：由 Markdown 机械转换后规范化为 `article` + `amsmath/amsthm` 稿，恢复标准 Abstract/Section 层级、共享定理编号、公式标签与交叉引用、`thebibliography` 引用，并修正长表、SHA-256 与 PowerShell 命令的换行风险；全部证明、限制、计算证据和 5 处 `UNKNOWN` 均保留。
- 完成 LaTeX 静态验收：Pandoc 2.12 可反向解析；35 个 label 全部唯一，46 个 `ref/eqref` 与 10 个 `cite` 均有定义，50 对环境按栈配对，未转义花括号 395/395，34 对 display delimiters 加 6 对 equation environments 共保留 40 个显示公式，5 个 SHA-256 可从排版断点无损还原；测试仍为 `29 passed`。本机没有 `pdflatex`、`xelatex`、`lualatex`、`latexmk`、`tectonic`、`latex` 或 `texify`，所以未生成 PDF、未获得真实编译日志，这一点不得被写成编译成功。
- 完成 Markdown--LaTeX 逐节一致性验收，并由独立只读审计复核：Abstract、Sections 1--8、13 条定理类陈述、13 个证明、40 个显示公式和 447 个非 QED 行内公式逐项保留；定理自动编号为 3.1--3.8、4.1--4.2、5.1--5.2、6.1，公式编号为 5.1--5.3、6.1--6.3。四条文献与十处引文全部解析；两张表、实验数字、三条 PowerShell 命令、五个 SHA-256、反例、范围限制和五处 `UNKNOWN` 均无丢失或语义漂移。最终 TeX 为 1,069 行，SHA-256 `B0EE092172447B08480C9CBA14D80BBC7CAD4E475067B8FE762797EE9F7642C9`。
- 建立并审计 `notes/collaborator_reading_guide.md`（约 1,119 个英文词）：用主公式与依赖图概括两分支证明、树特化、$\beta(T)$ 局部刻画和 DP；列出六个优先人工审阅点、Jiang/fan 文献边界、计算证据强度、完整交付顺序和必须保留的限制。说明明确把两条计算路线称为“校验逻辑不同但共享 audit/NetworkX 基础设施”，避免夸大为完全独立软件栈；补入主审计实际导入的 `experiments/audit_extension_candidates.py`、`tests/` 与 `requirements.txt`。三次只读审计未发现数学或事实错误；修正了“independent proof note”歧义，并将完整 `UNKNOWN` 清单权威指向本文件 Section 8。Pandoc 解析通过，无非 ASCII 或尾随空白，当前 SHA-256 为 `4008075091B15508FECEE6FFA07219CA859545DD4EDD2B695CE90B4C49CBA89E`。

- 建立并验证 `notes/review_package_manifest.md`：分为核心审阅文件、复现依赖闭包、可选历史材料和故意不哈希的动态交接文件；记录 19 个稳定文件的字节数与 SHA-256，逐项现场复算为 19/19 一致。审计确认主脚本的传递本地依赖恰为两个 `src` 模块、`src/__init__.py` 与 `experiments/audit_extension_candidates.py`，第三方运行依赖为 NetworkX，测试另需 pytest，JSON 是输出而非隐藏输入。manifest 还记录 requirements 未锁版本、跨环境 JSON 可能因内嵌版本字段而字节不同，加入可选 `notes/literature_notes.md`，并明确缺失的历史 `notes/literature_search_log.md` 仍为 `UNKNOWN`。Pandoc 解析通过，无非 ASCII/尾随空白；manifest 为 137 行、902 词，SHA-256 `22BB0301F048D62503BCD49C060476001881B902362F519BA4B2E01A21005667`。
- 已将稳定的 `drafts/mixed_join_research_note.tex` 上传到 Google Drive 的 `ai4math` 文件夹；原 Drive 中未找到该文件夹，按用户授权在 My Drive 根目录创建。上传后通过文件元数据和文件夹列表双重读回核验：文件名为 `mixed_join_research_note.tex`，MIME type 为 `application/x-tex`，大小 43,228 bytes，父目录 ID 与新建文件夹一致；本地 SHA-256 仍为 `B0EE092172447B08480C9CBA14D80BBC7CAD4E475067B8FE762797EE9F7642C9`。这只是源文件交付，不是实际编译，也没有产生 PDF 或 TeX 编译日志。
- 收到用户从上一版 TeX 编译的 13 页 PDF（SHA-256 `2516C872A6ACCAFE8F0690AB3D2DD33B813EF514CA3FAA486F24264509185540`）；元数据识别为 pdfTeX 1.40.27 / TeX Live 2025。逐页渲染、文字边界、字体和链接检查确认：全部字体已嵌入且有 Unicode 映射，56 个内部链接均可解析，未见 `??`、裁切、重叠、缺字或黑块。因用户未同时提供 `.log`，不能断言 overfull/underfull 等 warning 为零。
- 完成数学、文献措辞和版式三路独立审阅：未发现 critical/major 数学错误；唯一形式问题是允许 $X=\varnothing$ 时没有声明空图最大度，现已明确约定为 0。另修正 apex-meeting 边界句、避免把共享 audit/NetworkX 基础设施的两条计算路线夸大为完全独立，并把 fan 公式证据精确限定到 removal paper 的 arXiv v2。
- 修订 `drafts/mixed_join_research_note.tex` 与 `.md`：补入 abstract 中的 $\beta(T)$ 定义、$q_2(G)=0$ 约定和 Jiang 定理定位；修复三处引导句/显示公式跨页、Lemma 3.7 孤立标题、两张表的断词/路径换行和参考文献分页。修订稿仍有 13 条定理类陈述、13 个证明、40 个显示公式、448 个非 QED 行内公式和 5 处 `UNKNOWN`；Pandoc 解析成功，35 个 labels 无重复，46 个 `ref/eqref` 和 11 个 `cite` 均解析，环境栈配对，五个源码哈希可还原。当前 TeX 为 43,773 bytes，SHA-256 `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F`；Markdown SHA-256 为 `9A76A7E8E6AE9BD0505224234C5BEF6379F713B4753D11FB11F5AEEA03E531A7`。
- 重新运行测试得到 `29 passed in 0.44s`；pytest 另报告 `.pytest_cache` 不可写的一条非数学 cache warning，未隐藏。随后将修订 TeX 原位替换到 Google Drive 同一文件 ID；文件夹和元数据双重读回均为 43,773 bytes、`application/x-tex`、原父目录不变。
- 收到已编号 v2 的完整 pdfTeX/TeX Live 2025 日志与 13 页 PDF。日志从 banner 到内存/PDF statistics 完整，成功输出 13 页；没有 error、fatal error、undefined reference/citation、missing character、underfull box 或 rerun 请求。唯一真实警告是同一 longtable 在 `endhead` 前后两个 alignment chunk 各报告一次 `Overfull \hbox (2.68097pt too wide)`；这是一个表格总宽度问题，不是两个独立正文错误。
- 对 v2 PDF 完成 13 页 160 dpi 逐页目检、字体、链接和文字快检：22 个字体资源全部嵌入、子集化并有 Unicode 映射，57 个内部链接全部解析，另有 6 个 URI 链接；未见 `??`、裁切、重叠、黑块或缺字。仍有两处低严重度分页：第 2--3 页的 dual-number 引导句与公式分离，第 10--11 页的 audit-report 引导句与 longtable 分离；表格的 2.68097pt overfull 视觉上未裁切，但仍应修复。
- 保留制品溯源限制：日志写明原始 `output.pdf` 为 343,488 bytes，而收到的附件为 347,353 bytes、SHA-256 `CBAD3BEE3568FEC000847095610D021F7C40F1CDADF6D0CB21818B8E372A649C`。附件头明确含 `/Linearized 1 /L 347353`，因此大小、哈希和对象布局变化与编译后线性化重写一致；正文中的本轮独特修订、日志告警行号、页数、时间和 Producer 也与 v2 高度一致。但现有证据仍不能把附件断言为日志原始输出的字节级副本。
- 按用户要求建立不可覆盖的 TeX 版本管理：Drive 已有 `ai4math/v2/` 与空的 `ai4math/v3/`，因此将当前已编译源稿冻结为 `drafts/mixed_join_research_note_v2.tex`（43,773 bytes，SHA-256 `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F`），从它新建 `drafts/mixed_join_research_note_v3.tex`。以后每次修改只从最高版本复制到新的 `vN`，旧编号稿不得覆盖；映射记录在 `drafts/TEX_VERSION_HISTORY.md`。
- v3 只做三项排版修改：在 dual-number 定义和 audit report 表格前分别预留页面空间，并把首张复现表的两个文本列从 `0.26/0.41\textwidth` 缩为 `0.25/0.40\textwidth`。Pandoc 2.12 解析成功；35 个 labels 唯一，46 个 `ref/eqref`、11 个 `cite`、4 个 bibliography keys 全部解析，环境栈配对；13 条定理类陈述、13 个证明、40 个显示公式和 5 处 `UNKNOWN` 保持不变。v3 为 44,087 bytes，SHA-256 `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`。
- 将 v3 作为新文件上传到 Google Drive 空的 `ai4math/v3/` 文件夹，没有覆盖 v2 或无版本号旧文件。上传后用文件元数据和文件夹列表双重读回：文件 ID `1A2MepYtCLU80SR9pb011T-lM7iyU2X8M`，名称 `mixed_join_research_note.tex`，大小 44,087 bytes，MIME type `application/x-tex`，父目录 ID `1JKUCmJoC7E18skB_FmfbwxtTqG_GvXx_`。
- 收到 v3 的 13 页 A4 编译件（347,402 bytes，SHA-256 `566A99646FFEA83983445A1F2BEBEE44B122911061304AC4DBCC839A948D2712`）和 10 页日志打印件（45,700 bytes，SHA-256 `9E1A279A710538140F70403CD50EC921A9A17B91A0B27E26BC8F54589C60CC5D`）。日志内容从 pdfTeX banner 到 PDF statistics 完整，记录原始 `output.pdf` 为 13 页、343,570 bytes；没有任何 error、warning、overfull/underfull、undefined reference/citation、missing character 或 rerun 请求。逐页 160/200 dpi 双路目检、页面坐标、字体、链接和书签检查均通过：22/22 字体嵌入、子集化且有 Unicode 映射，57/57 内部链接、58/58 named destinations 和 16/16 书签有效，6 个 URI 结构有效；v2 的三处排版目标全部修复，13 页未见新缺陷。附件明确线性化，日志又是 PDF 打印件而非原生 `.log`，故保留字节级溯源限制，但 v3 typesetting audit 已完成。
- 完成期刊目标的官网核对与分层定位：DMGT 的 structural graph theory scope、无 APC、首次投稿普通 LaTeX 单栏逐行编号、PDF 不超过 10 MB、2020 MSC/关键词/通讯作者元数据和录用后才强制 `dmgt` 样式等要求均从官网读回；同时核对 Graphs and Combinatorics、Discrete Mathematics、Discrete Applied Mathematics 与 Computational and Applied Mathematics 的 scope 和直接相关发表先例。形成 `notes/target_journals_and_author_info.md`，明确推荐与文献事实的区别、个人信息清单和投稿门槛。
- 按不可覆盖规则从 v3 新建本地 `drafts/mixed_join_research_note_v4.tex`，没有修改 v3，也没有触碰 Google Drive。v4 面向 DMGT 首次投稿，加入 `lineno`、作者/单位/邮箱/ORCID 占位、关键词、2020 MSC `05C12`（primary）及 `05C05/05C69/05C76/05C85`（secondary）、funding/competing interests/author contributions/data-code availability/AI-assisted-tools 声明占位，并移除内部工作稿横幅。
- 为投稿定位补入已核验的 general-position survey v5 和 DMGT 上 standard general position/graph operations 论文，明确后者不推出本文的 dual 结果；将投稿稿中的内部 `UNKNOWN` 标记改写为出版语言，但没有改变 `PROJECT_STATUS.md` 中任何事实状态。v4 静态验收中先发现并修复一个新引入的错误标签 `cor:path-family`，最终 Pandoc 解析成功，35 个 labels 唯一，47 个 `ref/eqref`、13 个 cite commands 与 6 个 bibliography keys 全部解析，环境栈配对；13 条定理类陈述、13 个证明、34 对 display delimiters 加 6 个 equation environments 与 v3 一致。v4 尚未真实编译或视觉验收。
- 收到用户确认的单作者信息并填充本地 v4：发表姓名为 Yi Yuteng，通讯邮箱已写入，当前无机构职位，故采用 `Independent Researcher, Shanghai, China`；无 ORCID、无 funding、无 competing interests。代码与机器可读审计输出采用“向通讯作者合理索取”的本地兼容方案，没有声称存在公共仓库。致谢没有虚构个人，而是准确披露 OpenAI Codex 在文献整理、证明草拟、代码开发、计算核验、稿件起草和编辑修订中的辅助角色，并明确它不是作者、最终责任属于人类作者。
- 核对上海交通大学浦江国际学院官网当前英文名为 `SJTU Global College`；由于用户已经毕业且没有当前机构职位，该教育经历没有写成现 affiliation。作者信息填充后，v4 的 Pandoc 解析、标签/引用/引文/环境检查再次通过，0 个投稿占位；35 个 labels、47 个 `ref/eqref`、6 个 bibliography keys、13 个 cite commands、13 条定理类陈述、13 个证明和 40 个显示公式保持。v3 哈希仍为 `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`。本阶段没有修改数学实现、没有重跑旧测试、没有触碰 Google Drive。
- 完成 GitHub 连接的只读核验：认证身份为 `Star5Dust`，但 installed accounts 与 accessible repositories 均为空，本机没有 `gh` CLI，且现有连接没有新建仓库接口；没有创建仓库、上传文件或改动远端状态。用户要求把代码公开列为待定事项，待其回家使用电脑后再创建私有仓库并授权 Codex；在实际公共 URL 经核验前，v4 的 availability-on-request 声明保持不变。
- 完成五个目标期刊的官方格式复核并建立本地期刊名版本：DMGT 保留普通单栏逐行编号的首次投稿路线；Graphs and Combinatorics 使用官方 `svjour3` 的 `smallextended` 路线；Discrete Mathematics 与 Discrete Applied Mathematics 使用 Elsevier `elsarticle` 的 preprint 路线；Computational and Applied Mathematics 使用 Springer Nature `sn-jnl` 的 line-numbered `sn-mathphys-ay` 路线并按作者年制重排 bibliography。五份的 author/front matter、keywords/MSC、declarations 和引用样式按各路线分流，但 Introduction--Conclusion 与 v4 精确一致。Pandoc 五份均返回 0；标签、交叉引用、引文、环境、定理/证明和占位扫描全部通过。DMGT 文件与 v4 同哈希，v3/v4 均未覆盖。新增 `drafts/journal_versions/README.md`，并同步更新版本历史、目标期刊说明、README、review manifest、status 和 research log；没有调用 Google Drive，也没有修改数学代码或伪称重跑测试。
- 收到用户分别从 ChatGPT、DeepSeek、Gemini 和 GLM 网页版取得的四份原始 AI 审稿回复，记录字节数与 SHA-256 后完整裁决。没有按多数投票：逐项对照 v4、canonical proof 和定义。判定 ChatGPT 的证明核验与五项小修订有效；DeepSeek 的 Lemma 3.1 致命 objection 为明确误报，因为非相邻端点在 join 中距离为 2，`u-c-v` 仍是测地线，另一条同长测地线不改变这一事实；Gemini 只提供低权重编辑意见；GLM 未收到稿件且混淆 standard 与 dual general position，不能作为有效审稿。没有发现可复现的 critical/major 数学错误。完整证据与逐项理由写入 `notes/external_ai_review_adjudication.md`。
- 按不可覆盖规则从冻结 v4 新建 `drafts/mixed_join_research_note_v5.tex`，只实施术语、空类约定、$P_4,r=1$ tie 和 DP 边界/存储澄清，没有改变主公式、任何定理值、证明依赖、实验数字、引用事实或作者声明。v5 为 47,256 bytes、1,162 行，SHA-256 `0516949DBC02887615A01E8D3A61E441A19188F0E8342AADA3F23E659DABF2E2`；Pandoc 返回 0，35 个 labels 唯一，47 个 `ref/eqref`、13 个 cite commands 和 6 个 bibliography keys 全部解析，13 条定理类陈述、13 个证明、环境栈与 0 投稿占位均通过。重跑测试得到 `29 passed in 0.23s`。五份 v4 期刊衍生稿已明确标为 superseded format references；本轮没有真实 TeX 编译、Drive 操作或 GitHub push。
- 完整读取并裁决用户提供的 GLM 5.3 对抗审稿报告（14,927 bytes，SHA-256 `148C257B0F1F73E9D7FD6C942AA76B146F2570CD8499C8913918194FEDA8B284`）。报告未找到数学错误；Jiang 连通性和 complete-join 范围、fan 的 $n\ge4$ 公式均由原文重新核对。接受复现包、计算路线边界、自含术语、$F_3$ 和小树范围、以及最优值分离例子等意见；完整证据写入 `notes/glm_5_3_review_adjudication.md`。
- 从冻结 v5 新建 `drafts/mixed_join_research_note_v6.tex`，不改主定理值或证明依赖；删除内部阶段行话，修改摘要术语，显式说明 Jiang 无需第二因子连通、$|V(T)|\ge3$ 的作用和 $F_3$ 例外，并用深度 2 完全二叉树证明较弱的 induced-maximum-degree-one 优化可有不同最优值。该例由子集穷举、DP 和 definition-first checker 独立核对为 $\beta=4$，较弱问题有大小 5 的可行集，且 $gp_d(K_1+T)=4$。
- 扩展 `experiments/audit_mixed_join_dp.py`：在 46 棵 3--8 阶非同构树与 $r=1,2,3,4$ 的 184 个 mixed joins 上，将 DP 重构出的树侧集合直接交给 shortest-path dual-GP checker，184/184 可行；原四类比较仍全为零失败。新增回归测试后得到 `30 passed in 0.33s`。新增锁定环境、`REPRODUCIBILITY.md` 和可随稿上传的固定 ZIP；ZIP 在干净目录解压后测试通过并逐字节复现 `results/mixed_join_dp_audit.json`。
- 使用用户安装的 MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 对 v6 三遍真实编译。最终原生日志无 warning/error/overfull/underfull/未定义引用/引文/缺字/rerun，输出 14 页 A4 PDF。全部字体嵌入，邮件/DOI/arXiv 链接可枚举，14 页渲染逐页核验无裁切、重叠、断表、黑块、缺字或异常分页。当前 TeX/PDF/log 的大小和 SHA-256 已记录在当前阶段、版本历史和 GLM 裁决笔记中。
- 在用户准备实际投稿时重新读取 DMGT 2026 官网、作者指南、注册、登录与编辑部联系页。确认 DMGT 仍是当前稿的首选：scope 包含 structural graph results、无 APC，首投稿只公开要求通讯作者信息、摘要、关键词、2020 MSC 和不超过 10 MB 的单栏逐行编号 PDF；`dmgt` class、TeX source 和附加文件在录用后要求。当前 470,046-byte v6 PDF 完全符合公开首投文件要求。登录后的 supplement 字段不可公开查看，若不存在则应联系 `dmgt@wmie.uz.zgora.pl` 询问 ZIP 附件方式，不能假称已经随稿提供或因此强制先公开 GitHub。
- 按用户要求建立 `github_upload/` 手动上传包：根目录含中文 `README.md`、复现说明和依赖文件；`paper/` 保存冻结 v6 TeX/PDF；`docs/` 保存合作者导读、证明说明和文献定位；`src/`、`experiments/`、`tests/`、`results/` 保留可运行的原相对结构；`release/` 保存固定补充 ZIP。没有纳入 v2--v5、期刊格式旧稿、第三方论文、本地环境、缓存或 AI 原始回复。TeX、PDF、ZIP 与 canonical v6 的 SHA-256 全部一致，从该文件夹直接运行测试得到 `30 passed in 0.30s`。README 已说明 GitHub 网页端逐步上传、目录关联、上传后核验、private/public 与 license 边界；本轮没有改动或上传远端仓库。
- 用户已通过 GitHub Desktop 将 `main` 推送，并把 `Star5Dust/dual-general-position-mixed-joins` 改为 public；GitHub REST API 于 2026-08-29 读回 `visibility=public`、`default_branch=main`、无 license。公开审计未发现常见 token/private-key 模式。根 README 已改为面向公开读者的英文首页，直接给出主结果、论文/PDF/证明/复现包链接、运行命令、证据边界和无 license 的真实状态。误提交的 `回复/` 已在后续提交从当前树移除并加入 `.gitignore`；其历史副本仍存在于早期 commit。重复的 `github_upload/` 现准备从 Git 跟踪中移除但保留本地，并加入 `.gitignore`。冻结 v6 未覆盖；若论文要加入公开 URL，必须新建 v7。
- 对 public repository 做匿名只读审计：`main`/`HEAD` 为 `6f60b4d006943b9fdab83f364b37139a5891213d`，v6 PDF、固定复现 ZIP 和主 JSON 与本地 canonical 文件 SHA-256 完全相同，TeX 仅有 Git 行尾归一化造成的字节差异且规范化文本相同。按不可覆盖规则建立 v7，只加入 repository URL/固定 archive 路径，三遍编译、日志、字体、URI、文本、14 页视觉和 30 项测试全部通过。该公开 URL 取代单独 ZIP 上传或邮件询问。

尚未开始：

- 外部合格人类数学审阅仍未取得；用户目前不认识合适审阅者，已选择用多模型 AI 筛查作为现实替代，但该流程不等于人类同行评审。尚需权限的订阅数据库与 fan VOR 正文核验也未完成；
- 原生纯文本 v3 `.log` 的归档尚未取得；现有 PDF 打印件已完整保留可见日志内容，但不能证明原始日志字节或外部编译输入源码哈希；
- version-of-record fan 公式的正文比对，以及只有在获得权限时才能做的 MathSciNet/Scopus/Web of Science 最终查重；
- public GitHub repository 已建立、读回核验并写入 v7；尚待作者决定代码与文稿的 license、是否精简公开历史，以及是否建立带版本号的 GitHub Release/Zenodo DOI；
- GPT 审稿提出的任意非完全第二因子 $K_r+G$ 局部团邻域推广已经有直接证明机制，但尚未完成专门的系统文献、命名参数和计算审计；它不属于 v5，不能作为本文已确立 novelty；
- 任意 first factor $F$ 的一般理论；$P_n\circ T$ 候选保持 dormant，不并行启动。

## 5. 本地论文与可靠读取状态

`papers_local/` 在本阶段开始时与旧状态不一致：目录实际为空。为完成当前审计，已从 Zenodo 重新恢复以下两份文件；均不得修改或提交到 Git：

1. `Jiang - 2026 - Dual General Position in Lexicographic Products with a Complete First Factor v1.0.1.pdf`
   - Zenodo 预印本，共 10 页；DOI `10.5281/zenodo.22116770`；
   - SHA-256 `ADB5DB88FD600C1AB031B51BBB9FC1771B905A7CD800D22E219184E05B7ACA34`；
   - Zenodo MD5 `ec460cc54eb00426b564476da3084c1b` 已核对一致；
   - 页面 2--5 已渲染目视核对。
2. `Jiang - 2026 - Dual General Position supplement v1.0.1.zip`
   - 预印本的完整复现补充材料；manifest 和运行结果已核验；
   - SHA-256 `604A86672EE6B6E7F8BE801EABC069C13806F08767CF5782CE71AC22F553BE84`；
   - Zenodo MD5 `fa70a97d33f8a1a514c0b7f2a166d752` 已核对一致。

旧状态曾列出的核心论文、Tian--Klavžar 期刊版、Anand et al. 预印本和 survey v5 当前不在工作区。它们的既有核验笔记保留，但本阶段未伪造或重建缺失文件；是否恢复这些本地快照留待以后按任务需要决定。

## 6. 已核验的文献

### 核心论文

Pakanun Dokyeesun, Sandi Klavžar, Dorota Kuziak, and Jing Tian, “General position problems in strong and lexicographic products of graphs,” *Computational and Applied Mathematics* 45, Article 97 (2026).

- DOI: `10.1007/s40314-025-03547-7`
- 作者明确提出一般问题：determine $gp_d(K_m\circ G)$。
- 我们的 $gp_d(K_m\circ T)$ 是该问题在 $G=T$ 时的 restricted case。
- 核心论文没有解决一般树情形。

### Dual general position 基础论文

Jing Tian and Sandi Klavžar, “Variety of general position problems in graphs,” *Bulletin of the Malaysian Mathematical Sciences Society* 48:5 (2025).

- DOI: `10.1007/s40840-024-01788-z`
- arXiv: `2402.17338`
- 已核验 dual general position 的定义、Theorem 3.1、Corollary 3.2、Theorem 3.9 和 Proposition 3.10。

### Lexicographic product 凸集基础论文

B. S. Anand, M. Changat, Sandi Klavžar, and I. Peterin, “Convex sets in lexicographic products of graphs,” *Graphs and Combinatorics* 28:77–84 (2012).

- DOI: `10.1007/s00373-011-1031-4`
- arXiv: 未找到，记录为 `UNKNOWN`
- 已从作者预印本核验 Theorem 2.1 的完整假设与三个条件。

### 窄范围前向引文检索结果

- 2026 核心论文的两篇可识别前向引用是：
  1. “On the variety of general position problems under vertex and edge removal”，DOI `10.1016/j.dam.2026.02.044`，arXiv:`2510.01294`；
  2. “General position and mutual-visibility in shadow graphs”，arXiv:`2601.19769`。
- 第一篇研究 dual general position，但问题是删点/删边；第二篇研究 standard general position 与 mutual visibility，包括树的 shadow graphs。两篇都不研究 $gp_d(K_m\circ T)$。
- Tian and Klavžar (2025) 的其他已核验前向引用中，确有 glued t-ary graphs 和 Sierpiński graphs 上的 dual general position 结果，但没有 lexicographic product 目标结果。
- 本次对引用 Anand et al. (2012) 的候选进行题名和主题筛选，没有发现核心论文之外同时明确涉及 dual general position 与 lexicographic product 的工作。
- **本次窄范围检索没有找到解决 $gp_d(K_m\circ T)$ 的论文。** 这是文献检索结果，不是数学定理，也不是全领域 novelty claim。
- Springer/Dimensions、OpenAlex 和 OpenCitations 的引用计数存在差异；完整方法、逐篇判定和覆盖限制见 `notes/literature_notes.md` 与 `notes/research_log.md`。

### 系统主题检索发现的 exact-target 预印本

Weiqi Jiang, “Dual General Position in Lexicographic Products with a Complete First Factor,” Zenodo preprint v1.0.1 (2026-08-27).

- DOI: `10.5281/zenodo.22116770`
- Concept DOI: `10.5281/zenodo.22081165`
- Earlier v1.0.0 DOI: `10.5281/zenodo.22081166`（2026-08-24）
- Zenodo/DataCite 类型：`publication/preprint`；开放获取；CC BY 4.0。
- 预印本明确引用核心论文，并声称回答 complete-first-factor 开放问题。
- Theorem 3.2 声称：对任意非空有限简单图 $G$ 和 $m\ge2$，

  $$
  gp_d(K_m\circ G)=m q_2(G),
  $$

  其中 $q_2(G)$ 是将 $V(G)$ 分割为两个 induced cliques 时一侧的最大大小；Proposition 3.3 将其等价表示为 $\overline G$ 的二部划分问题。
- 这是对当前目标的精确、且更一般的公开解答主张，不是只相关的旁支论文。
- **重要限制：** 没有检索到同行评审版本。2026-08-28 本项目已完成逐步 proof audit、supplement 复现与第二套独立计算验证，因此内部采用该公式；这仍不等于同行评审结论。

### 当前领域综述

Ullas Chandran S.V., Sandi Klavžar, and James Tuite, “The General Position Problem: A Survey,” arXiv:`2501.19385v5`。

- v5 于 2026-08-16 修订；
- 其 Section 3.5 收录 foundation、核心 product paper、Sierpiński、glued trees 和 removal 等 dual general position 工作；
- 它把核心论文概括为只在 many cases 确定 dual lexicographic-product number；
- Jiang v1.0.0 晚于 survey v5 八天，因此 survey 没有收录它。

### Jiang 未覆盖方向的有边界检索

- 2026-08-28 的系统定位重新核对了 Jiang Zenodo/DataCite version record，并检索 arXiv、DataCite、zbMATH、Crossref、OpenCitations、survey v5 和通用网页；OpenAlex 与 Semantic Scholar 的 429/不一致响应作为覆盖失败保留，不用于负面推断。
- arXiv 精确短语检索返回 foundation、product 和 removal 三篇；加 `join`、`cone`、`universal vertex`、`tree` 或 `dynamic programming` 均未得到目标命中。DataCite 题名字段只返回 Jiang concept/version 三条记录；zbMATH 的精确短语结果也是 foundation、product 和 removal 三篇。
- **直接既有子族：** removal paper 明确处理 fan graph $F_n=K_1+P_n$。已核对的 arXiv v2 对 $n\ge4$ 给出

  $$
  gp_d(F_n)=\left\lfloor\frac{2(n+1)}3\right\rfloor=\left\lceil\frac{2n}3\right\rceil.
  $$

  因此 mixed-join 定理的 $r=1$、path 子族是对既有 fan 结果的恢复，不是本项目的新结果。
- removal paper 的旧 author-hosted v1 把上述式子写成 ceiling，而 arXiv v2 已改为 floor，并加入“最大独立边端点集”的说明；version-of-record 正文当前无法直接读取，所以期刊正文的精确显示保持 `UNKNOWN`，不能自行选定。
- 未找到覆盖 all trees、任意 $r$ 的 $gp_d(K_r+T)$ 分类，也未找到与本项目附加边界条件完全等价的既有命名参数或递推；严格标签仍只是 **NOT FOUND IN THIS BOUNDED AUDIT**，不是开放性或 novelty 证明。
- β(T) 与 dissociation set 相邻但不等价：二者都要求诱导最大度至多 1，但 β 还要求每个入选顶点至多有一个外部邻点。例如 $K_{1,3}$ 的中心与一片叶子构成 dissociation set，却不满足 β 的外部邻点条件。
- 现有证据支持 **CONDITIONAL GO FOR AN INTERNAL DRAFT**：可写的实际增量是 all-tree、任意 $r$ 的两分支结构定理、β(T) 的树上局部刻画，以及线性时间最大集合回溯；稿件必须明确引用 fan 子族，并把全领域新颖性保持为 `UNKNOWN`。完整查询矩阵、逐篇纳入/排除理由和覆盖限制见 `notes/mixed_join_literature_positioning.md`。

## 7. 已确认的数学事实

以下各条明确区分既有文献事实、本项目独立证明和计算实验。

### 一般定义与判据

- dual general position set 首先必须是 general position set。
- Tian–Klavžar Theorem 3.1：$X$ 是 dual general position set，当且仅当 $X$ 是 general position set 且 $G-X$ convex。
- “补集 convex”只是 dual 的一个必要组成部分，不能脱离 general position 条件单独使用。

### $K_m\circ T$ 的边界情形

- $K_1\circ T\cong T$；对非平凡树，已有 block-graph 结果可给出 $gp_d(T)$。
- $T=K_1$ 时，$gp_d(K_m\circ K_1)=m$。
- $T=K_2$ 时，核心论文 Theorem 5.8(ii) 给出 $gp_d(K_m\circ K_2)=2m$。

### 早期文献对主范围 $m\ge2$、$|V(T)|\ge3$ 的限制

- 此时 $T$ 非完全。
- 核心论文 Lemma 5.1 表明 $K_m\circ T$ 没有 simplicial vertices。
- 没有 simplicial vertices **不能** 推出 $gp_d=0$。
- Anand et al. Theorem 2.1 排除 proper、non-complete convex induced subgraph。因此，如果 dual 候选集 $X$ 的补集非空且 proper，那么该补集必须诱导 complete graph。
- Tian–Klavžar Proposition 3.10 与“无 simplicial vertices”合用，可排除 nonadjacent 的两点 dual set。
- 若单独研究 adjacent 两点集，仍可用 Tian–Klavžar Theorem 3.9 检查；该子分类未完成，但已不影响最大值公式。
- Jiang 之前已核验的三篇论文没有给出一般树情形的 $gp_d(K_m\circ T)$ 公式。

### Jiang v1.0.1 与本项目独立审计后的公式

- 截至 2026-08-28，公开文献中已经存在一篇精确覆盖 $gp_d(K_m\circ T)$ 的 Zenodo 预印本；因此“没有文献处理这个问题”不再成立。
- **预印本文献主张：** 对非空有限简单图 $G$ 和 $m\ge2$，$gp_d(K_m\circ G)=m q_2(G)$。
- **本项目独立证明审计：** Theorems 3.1--3.2 与 Proposition 3.3 的每个已列步骤均判为“正确”，没有发现需要补充、错误或 `UNKNOWN` 的步骤；详见 `proofs/jiang_v1_0_1_audit.md`。
- **本项目独立证明：** 对树 $T$ 和 $m\ge2$，

  $$
  gp_d(K_m\circ T)=
  \begin{cases}
  m,&T=K_1,\\
  2m,&T\in\{K_2,P_3,P_4\},\\
  0,&\text{其他树}.
  \end{cases}
  $$

  证明见 `proofs/tree_corollary.md`。
- **计算实验：** supplement 的 1,064 次比较和项目独立实现的 217 个最大值比较、4,780 个集合级分类比较均为 0 mismatch；这些实验支持但不构成上述证明。

### Mixed join $K_r+T$ 的精确结果

- **文献事实：** Jiang Theorem 5.1 只处理全部因子均非空、非完全的 complete joins；PDF p. 9 明确排除同时含完全与非完全因子的 mixed joins。
- **直接逻辑推论：** $P_3\circ T\cong T+2T$ 对非完全树 $T$ 已落入 Jiang Theorem 5.1，不能作为新扩展。
- **本项目独立证明：** 对 $r\ge1$ 和 $|V(T)|\ge3$，令

  $$
  \beta(T)=\max\{|X|:\Delta(T[X])\le1,\ |N_T(x)\setminus X|\le1\ \forall x\in X\}.
  $$

  则

  $$
  gp_d(K_r+T)=
  \begin{cases}
  r+2,&T\in\{P_3,P_4\},\\
  \beta(T),&\text{其他树}.
  \end{cases}
  $$

  更一般的两分支形式为：$q_2(T)>0$ 时取 $\max\{\beta(T),r+q_2(T)\}$，否则取 $\beta(T)$。正式证明见 `proofs/mixed_join_tree.md`。
- **本项目独立证明：** $X$ 对 $\beta(T)$ 可行，当且仅当每个入选的度 2 顶点恰有一个入选邻点，而度至少 3 的顶点均不入选；度 0 或 1 的入选顶点没有额外限制。基于“当前顶点是否入选、父点是否入选”的 rooted-tree DP 在线性时间和空间内求值并回溯最大集合，正确性证明亦见上述 proof note。
- **保留反例：** 对所有 $r\ge1$，$gp_d(K_r+K_{1,3})=3$；三片叶子构成最大 dual set，而 $q_2(K_{1,3})=0$。正式定理恢复了该例，没有隐藏它。
- **计算实验：** DP 与子集穷举的 985 次比较、11,003 次换根比较、985 次回溯检查，以及公式与 shortest-path 定义 checker 的 184 次比较均为 0 mismatch/failure。实验支持实现但不构成证明。先前的 92 次 mixed-join 和 17 个 dormant path-first 筛选结果仍保留。
- **本项目独立证明（worked families）：** 对 $k\ge3$，$\beta(K_{1,k})=k$ 且 $\operatorname{gp}_d(K_r+K_{1,k})=k$；若 $S_k$ 是每条边恰细分一次的 $K_{1,k}$，则 $\beta(S_k)=\operatorname{gp}_d(K_r+S_k)=2k$。对 $n\ge3$，$\beta(P_n)=\lceil2n/3\rceil$，从而 $P_3,P_4$ 的值为 $r+2$，而 $n\ge5$ 时 $\operatorname{gp}_d(K_r+P_n)=\lceil2n/3\rceil$；$r=1,n\ge4$ 与已核验的 fan 文献公式一致。
- **本轮独立审阅：** 对主稿、proof note 和 13 页编译件的数学复核未发现 critical/major 错误；两分支完备性、$r=1$、$P_3/P_4$、$K_{1,3}$、路径周期词和 DP 边界状态均通过人工逐项检查。唯一 minor/formal 缺口是未声明 $\Delta(T[\varnothing])=0$，修订稿已明确该约定；这不改变 $\beta(T)$ 或任何定理值。

## 8. 必须保持 UNKNOWN 的问题

- Jiang 预印本是否会出现同行评审版本、修订或勘误。
- 系统定位没有找到覆盖 all trees、任意 $r$ 的 $gp_d(K_r+T)$ 既有结果，但 MathSciNet、Scopus、Web of Science 尚未人工核验，部分开放索引又出现限流；因此该完整结果在全领域是否开放、是否具有 novelty，以及本项目的 priority 均为 `UNKNOWN`。
- removal paper 的 arXiv v2 中 fan 公式已经核对，但 version-of-record 正文的精确显示仍为 `UNKNOWN`。
- $\beta(T)$ 已有精确局部结构刻画、线性 DP 和最大集合回溯；是否已有完全等价的命名参数/递推，以及是否存在明显更简洁的无递推闭式，仍为 `UNKNOWN`。
- 当前证据已经解决“是否值得开始内部稿”的阶段判断（conditional go），并形成以 DMGT 为 fit-first 主目标的初步投稿定位；但该推荐不等于 scope 预审、接收保证或同行评审，最终可发表性和 novelty 仍为 `UNKNOWN`。
- arbitrary first factor $F$ 和一般 mixed complete joins 的完整分类仍为 `UNKNOWN`；$P_n\circ T$ 方向保持 dormant。
- 对任意非完全第二因子 $G$，以每个入选点的入选邻域和未入选邻域分别诱导团为条件的 $K_r+G$ 两分支公式已有直接 proof candidate；但其既有文献覆盖、参数命名、全领域 novelty/priority、最合适表述和是否值得并入本文均为 `UNKNOWN`。v5 没有声称或使用该推广。
- 旧状态所列但当前缺失的四份本地论文快照和 `notes/literature_search_log.md` 是否能从原来源或备份完整恢复。

`FORMULA INTERNALLY PROOF-VERIFIED` 仍然不等于 `PEER REVIEWED`，也不产生本项目的 novelty 或 priority claim。

2026-08-29 的 research-note 起草与一致性审计没有产生新的文献事实；重跑只复现既有计算矩阵，没有扩大实验范围，因此以上 `UNKNOWN` 项均保持不变。

2026-08-29 的稿后刷新再次确认 Jiang 当前仍为 v1.0.1 preprint 且没有 related journal identifier；开放索引没有新目标命中。Elsevier 正文访问仍被未授权响应/CAPTCHA 阻断，OpenAlex 仍不可靠。因此 Jiang 后续状态、fan VOR 精确显示、订阅数据库覆盖和全领域 novelty/priority 等 `UNKNOWN` 均保持不变。

2026-08-29 的 LaTeX 转写只改变载体、编号和排版结构，没有改变数学结论或文献事实。由于本机没有 TeX engine，实际 PDF 版面与编译日志状态为尚未核验；这不是新的数学 `UNKNOWN`，但必须作为制品验证限制保留。其余 `UNKNOWN` 项均未变化。

2026-08-29 的 Markdown--LaTeX 内容验收没有发现实质丢失或语义漂移，也没有产生新的数学或文献事实。LaTeX 实际编译/PDF 版面仍未核验；所有数学、文献与 novelty/priority `UNKNOWN` 项保持不变。

2026-08-29 的合作者说明只是从 canonical sources 提取审阅路线和交付依赖，没有新增定理、实验或文献结论。它明确保留全套 `UNKNOWN`，并纠正“独立计算路线”可能被理解为完全独立软件栈的风险；所有 `UNKNOWN` 状态不变。

2026-08-29 的 review-package manifest 只登记现有制品、依赖和已完成验证，没有运行新实验或形成新文献/数学结论。未锁版本导致的 JSON 字节差异边界已经显式记录；实际 TeX 编译、外部数据库覆盖、fan VOR、publishability 和 novelty/priority 等状态均未改变。

2026-08-29 的 Google Drive 操作只创建交付文件夹并上传已稳定验收的 TeX 源文件；云端大小和父目录已经读回核验。它没有运行 TeX engine、生成 PDF/日志、改变数学内容或增加文献事实，因此实际编译、外部数据库覆盖、fan VOR、publishability 和 novelty/priority 等状态均未改变。

2026-08-29 的第一份外部 PDF 审阅和后续修订没有产生新的文献事实、实验范围或 novelty/priority 结论。PDF 证明上一版确实由 pdfTeX 成功生成并可读，但完整编译日志仍缺失；当前修订版又尚未重编译，因此 warning 级排版状态仍待核验。空图最大度约定只封闭形式边界，不改变主定理。所有文献、命名参数、订阅数据库、fan VOR、publishability 与 novelty/priority `UNKNOWN` 均保持不变。

2026-08-29 的 v2 完整日志与第二份外部 PDF 审阅没有产生新的数学、实验或文献事实。它确认 v2 可成功编译，并把剩余问题限定为一个重复报告的 longtable overfull 和两处低严重度分页。日志中的 343,488-byte 原始输出与 347,353-byte 优化附件无法作字节级绑定，这是制品溯源限制，不改变任何数学结论。该阶段的 v3 只含排版修复、当时尚待真实编译；所有文献、命名参数、订阅数据库、fan VOR、publishability 与 novelty/priority `UNKNOWN` 均保持不变。

2026-08-29 的 v3 外部编译、完整显示日志和 13 页审阅只关闭了 typesetting 阶段：v2 的三处排版问题已消失且无新 warning/视觉缺陷。日志以 PDF 打印件而非原生 `.log` 提供，线性化附件也不能与日志原始输出作字节级绑定；这些是制品溯源限制，不是新的数学或文献结论。Jiang 后续状态、订阅数据库覆盖、fan VOR 精确显示、命名参数、publishability、novelty/priority 和超出范围的图类等全部 `UNKNOWN` 仍保持不变。

2026-08-29 的目标期刊筛选与本地 v4 投稿化改写只形成基于官网 scope/格式要求的推荐，并增加投稿元数据、两条已核验定位文献和出版化措辞。v4 中不再显示字面量 `UNKNOWN` 是写作层面的转换，不表示相关事实已经查明；Jiang 后续状态、订阅数据库覆盖、fan VOR 精确显示、命名参数、publishability、novelty/priority 和超出范围的图类等 `UNKNOWN` 全部保持不变。v4 未真实编译，不能继承 v3 的 warning-free/13-page 结论。

2026-08-29 的单作者元数据填充与 Codex 使用披露只改变署名、声明和交接文档，没有产生新的数学证明、实验或文献结论。`Independent Researcher` 是基于作者已毕业且无当前机构职位的真实 affiliation 选择；官网英文校名核对只用于避免误写，不构成机构背书。代码/审计输出的“合理索取”是当前本地交付方案，不表示已公开存档。所有数学、文献、publishability、novelty/priority 与外部数据库覆盖 `UNKNOWN` 均保持不变；人类审阅和 v4 真实编译仍未完成。

2026-08-29 的 GitHub 连接核验与待定事项登记只是外部交付准备：它确认关联身份但没有发现可访问仓库，也没有创建或上传任何内容。未来仓库名称、公开时间、license 与 Zenodo DOI 尚未决定，因此这些是 administrative TODO，而不是新的数学或文献 `UNKNOWN`；v4 当前的 availability-on-request 仍准确，其他全部 `UNKNOWN` 状态不变。

2026-08-29 的五份期刊格式转换只改变 LaTeX class、front matter、声明位置和所需引用呈现；Introduction--Conclusion 已验证与 v4 逐字节相同。官方格式核对不等于期刊预审、接收保证或 novelty 审计，静态解析也不等于真实编译。Jiang 后续状态、订阅数据库覆盖、fan VOR 精确显示、命名参数、publishability、novelty/priority 和超出范围的图类等全部 `UNKNOWN` 仍保持不变。

2026-08-29 的四模型网页 AI 审稿裁决没有发现有效的 critical/major 数学缺陷，但这不是人类同行评审，也不能把 publishability 或 novelty 从 `UNKNOWN` 改为已知。DeepSeek 的核心 objection 已由距离定义直接否定；GLM 没有收到稿件；Gemini 没有完成逐定理审计；ChatGPT 的无反例结论及其未附原始制品的自称新计算都不能单独构成证明。v5 只吸收经独立核对的小修订，未改变任何定理值。GPT 提出的 $K_r+G$ 推广只记录为有证明依据的后续候选，其文献/priority 状态保持 `UNKNOWN`。v5 尚未真实编译，因此不能继承 v3 的 13 页 warning-free 排版结论。

2026-08-29 的 GLM 5.3 二次审稿裁决、v6、锁定补充包和本机 MiKTeX 验收关闭了本地复现与排版 gate，但没有把 AI 审查变成人类同行评审。Jiang 的定理范围和 fan 预印本的 $n\ge4$ 边界已按原文复核；这只确认稿件对既有来源的使用，没有证明全领域 novelty 或 priority。新增的 184 次重构集合 definition-first 检查和深度 2 完全二叉树分离例均为有限计算/边界验证，不替代证明。订阅数据库覆盖、fan version of record、期刊编辑判断、publishability、acceptance 和一般 $K_r+G$ 推广仍为 `UNKNOWN` 或本稿范围外。

2026-08-29 的 public repository 匿名审计与 v7 只关闭交付一致性问题：仓库及固定 archive 已可公开访问，稿件不再需要声称 ZIP 随稿附加。此改动没有新增数学、实验或文献事实，也不构成人类同行评审；publishability、acceptance、全领域 novelty/priority、订阅数据库覆盖和 fan version of record 等 `UNKNOWN` 全部保持不变。

## 9. 当前任务队列

### Next — 只做这一项

在 DMGT 投稿草稿中删除当前 v6 PDF，上传 `output/pdf/mixed_join_research_note_v7.pdf` 并打开预览，确认文件名、14 页正文和 GitHub availability statement 正确，然后完成最终提交。首投不另附 ZIP、不发邮件、不上传 TeX；五份 v4 期刊衍生稿不得提交。

### After that — 暂不执行

提交后只处理编辑或审稿人的实际来信；任何内容改动必须从冻结 v7 新建 v8，不得覆盖 v3--v7。若获得人类数学同行的审阅，单独记录并裁决。license、可选 GitHub Release/Zenodo DOI 和公开历史精简仍是非阻塞 administrative TODO。$K_r+G$ 一般推广另立研究阶段，不与本次投稿并行。

## 10. Canonical notes

- `notes/definitions.md`：已核验定义、直观解释、小例子和 prerequisite 清单。
- `notes/literature_notes.md`：核心论文结果、开放问题、citation chain 和基础论文全文核验。
- `notes/literature_search_log.md`：旧状态记录的系统检索日志；当前文件缺失，恢复状态为 `UNKNOWN`，不得假装已经读取。
- `notes/theorem_applicability.md`：早期定理适用性审计及 2026-08-28 post-audit update。
- `notes/extension_feasibility_audit.md`：Jiang 未覆盖方向的有边界检索、候选覆盖审计、反例、最小计算与唯一 mixed-join 目标。
- `notes/mixed_join_literature_positioning.md`：mixed join 的系统查询矩阵、fan 既有子族、版本差异、真实增量、覆盖限制与 conditional-go research-note 结构。
- `notes/research_log.md`：从 2026-08-28 proof-and-reproducibility audit 起保存详细日志；更早阶段的独立日志文件未在工作区发现。
- `notes/conjectures.md`：猜想记录；当前不应加入未经依据支持的猜想。
- `proofs/jiang_v1_0_1_audit.md`：Definitions、Theorems 3.1--3.2、Proposition 3.3 的逐步证明审计和复现结论。
- `proofs/tree_corollary.md`：树情形精确公式的独立证明。
- `proofs/mixed_join_tree.md`：mixed join 两分支精确公式、$\beta(T)$ 局部刻画、rooted-tree DP 及正确性证明。
- `drafts/mixed_join_research_note.md`：自包含英文 research-note 工作稿；已同步本轮形式边界与证据措辞修订，当前 SHA-256 为 `9A76A7E8E6AE9BD0505224234C5BEF6379F713B4753D11FB11F5AEEA03E531A7`。
- `drafts/mixed_join_research_note_v2.tex`：冻结的外部编译基线，与旧的无版本号 43,773-byte 源稿字节相同；完整日志和 13 页 PDF 已审，SHA-256 为 `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F`，不得再覆盖。
- `drafts/mixed_join_research_note_v3.tex`：当前最新的已编译/逐页审阅 submission-style 基线；只修两处分页和首张复现表总宽度，Pandoc/结构/引用检查及真实 pdfTeX/显示日志/13 页验收全部通过，SHA-256 为 `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`；不得覆盖。
- `drafts/mixed_join_research_note_v4.tex`：从冻结 v3 建立、现已冻结的四模型 AI 审稿输入基线；含逐行编号、已确认的单作者/通讯作者元数据、无 funding/competing-interests 声明、code/audit availability-on-request、透明 Codex 使用披露、关键词、2020 MSC 和两条新增已核验引文。静态检查通过且投稿占位为 0，但未真实编译；46,222 bytes、1,147 行，SHA-256 `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF`，不得覆盖。
- `drafts/mixed_join_research_note_v5.tex`：从冻结 v4 建立的四模型 AI-review-adjudicated 基线；47,256 bytes、1,162 行，SHA-256 `0516949DBC02887615A01E8D3A61E441A19188F0E8342AADA3F23E659DABF2E2`，不得覆盖。
- `drafts/mixed_join_research_note_v6.tex`：冻结的 GLM 5.3 意见裁决与复现强化基线；49,825 bytes、1,203 行，SHA-256 `6C8C1812C64FB3B55909A7CFC82383944A93D4C34DBD1423DBC839FA51E0B9FE`，不得覆盖。
- `drafts/mixed_join_research_note_v7.tex`：当前唯一投稿内容候选；只在 v6 上加入经核验的 public repository URL 与固定 archive 路径，没有改变数学内容。Pandoc、`30 passed`、三遍 MiKTeX、原生日志、字体/URI/文本与 14 页视觉检查全部通过；50,063 bytes，SHA-256 `8668552914DFC5B177FC951D102C3A8BB75EB0DFD92E5495DE51DED7A902D992`。
- `notes/external_ai_review_adjudication.md`：四份网页 AI 原始报告的字节数/哈希、有效意见、误报、无效审稿、v5 变更与 $K_r+G$ scope candidate 的证据级裁决；9,095 bytes，SHA-256 `FF81C5CCEC231092A5532C9DE91F1A41E50FC949C03C9F038ACA7F037239DA3D`。
- `notes/glm_5_3_review_adjudication.md`：GLM 5.3 报告逐项裁决、原文引用复核、深度 2 二叉树分离例、v6 修改和不接受事项的证据记录；7,209 bytes，SHA-256 `B812A198C15E0760E160D66686C632FBE8EA0C4BC5C2A5DEE15833D24F095D45`。
- `drafts/TEX_VERSION_HISTORY.md`：TeX 不可覆盖版本规则、本地/Drive 映射、v2--v7 与五份 v4 期刊格式衍生稿的哈希、编译状态和制品溯源边界。
- `drafts/journal_versions/README.md`：五份 v4 期刊名 TeX 的路径、class/引用路线、官方说明链接、SHA-256、共同正文一致性和未编译边界；已明确全部被 v6 supersede，只作格式参考；4,149 bytes，SHA-256 `7297CF46CFB324510EC26DB240ACF6EA9F84E4BEA43C3A327EC38556970C72A5`。
- `drafts/journal_versions/*.tex`：DMGT、Graphs and Combinatorics、Discrete Mathematics、Discrete Applied Mathematics、Computational and Applied Mathematics 五份 v4 本地格式参考；只分流 preamble/front matter/declarations/reference presentation，Introduction--Conclusion 与 v4 逐字节一致，但均已被 v6 内容 supersede，不得直接投稿。精确逐文件哈希见该目录 README 和版本历史。
- `drafts/mixed_join_research_note.tex`：遗留的无版本号文件，当前与 v2 字节相同；不再作为编辑目标。
- `notes/collaborator_reading_guide.md`：当前 v7 人工审阅入口，列出证明依赖、复现路线、30 项测试、编译证据和必须保留的限制。
- `notes/target_journals_and_author_info.md`：目标期刊分层、作者信息/声明清单、独立研究者 affiliation、Codex 披露、public repository、MSC 和提交 gate；已按 DMGT 2026 公开首投流程复核；14,924 bytes，SHA-256 `4F44652DA2F728D8FDCEB62B5BED55F2682C64233D45918D0351021B6526F01D`。
- `notes/review_package_manifest.md`：v7 内部审阅/投稿包的非自引用制品、大小、哈希、依赖和编译状态清单；manifest 自身及持续变化的状态/日志故意不自哈希。
- `REPRODUCIBILITY.md`：从全新环境复现实验、测试和主 JSON 的命令；1,442 bytes，SHA-256 `C287D53518F003976243CEFB00B29E4E41881F32D4FFA6AD1F51F8937DFF0E36`。
- `requirements-lock.txt`：v6 补充包的锁定 Python 环境；340 bytes，SHA-256 `4811AEA9E5C13E192FB5865D7095ECBA19A33887ACC1D567AB5368E1D31DDE5E`。
- `artifacts/mixed_join_v6_reproducibility.zip`：固定随稿复现包；干净目录得到 `30 passed` 且主 JSON 字节一致；21,868 bytes，SHA-256 `0E91BAAC07EFA121784CA94355C93F304A7AF8FF89AB480E952E9C62DC316A33`。
- `artifacts/v6_build/mixed_join_research_note_v6.pdf` 与 `.log`：MiKTeX 三遍编译的原生制品；PDF 470,046 bytes、SHA-256 `C41FDA75669A253273CF05BC90F0B04DE9020884F982B1E6E56784583919DE44`，log 27,395 bytes、SHA-256 `7696F4DCF9A5AF6B1F2EC40E0F899CFDA4DEF4ED883A8973FFC05B2007BC13D1`。相同 PDF 已复制到 `output/pdf/`。
- `artifacts/v7_build/mixed_join_research_note_v7.pdf` 与 `.log`：MiKTeX 三遍编译的当前制品；PDF 470,873 bytes、SHA-256 `B10D50C0A77F76AD24E87A78DCFC9C9A1D9D7385FD42D38AA311C1989C887500`，log 27,395 bytes、SHA-256 `EB46D421FF2D3293C2F177156BF10349D198881E8053C64C810B18D34147C3F2`。相同 PDF 已复制到 `output/pdf/`。
- `results/jiang_v1_0_1_supplement_report.json`：supplement 实际运行报告。
- `results/jiang_v1_0_1_independent_report.json`：项目第二套实现的实际运行报告。
- `experiments/audit_extension_candidates.py`：只用于目标选择的最小可复现筛选脚本。
- `results/extension_feasibility_audit.json`：92 个 mixed-join 和 17 个 path-first 筛选比较的机器可读结果。
- `src/mixed_join_tree.py`：不依赖 shortest-path checker 的线性 DP 与最大集合回溯实现。
- `experiments/audit_mixed_join_dp.py`：DP/子集穷举与公式/定义 checker 的两套有边界审计驱动。
- `results/mixed_join_dp_audit.json`：985 次 DP 比较、11,003 次换根比较、985 次回溯局部检查、184 次公式/定义比较和 184 次 DP 重构集合 definition-first 检查的机器可读结果，全部零失败。

若本文件的简短摘要与 canonical notes 冲突，应暂停并核对原 PDF；不能自行选择更方便的版本。

## 11. Repository and environment status

- Git repository：已初始化，当前分支为 `main`，本地 root commit 为 `e274fd3` (`Initial research code and reproducibility package`)。
- 当前 Git 状态：`main` 已推送并跟踪 `origin/main`；本轮 v7 工作开始时本地 `HEAD` 与远端均为 `6f60b4d`。v7 和本轮文档更新尚未 push；这不影响 v7 所引用的 public v6 archive 已经可用。
- GitHub repository：`https://github.com/Star5Dust/dual-general-position-mixed-joins` 已由 GitHub REST API 读回为 public，默认分支为 `main`，当前无 license、无 topics、无 Zenodo DOI。`origin` 指向该 URL。常见 token/private-key 模式扫描为零命中；公开树仍包含作者在论文中主动列出的通讯邮箱以及若干内部研究/投稿交接说明，是否进一步精简历史由作者决定。
- `papers_local/`：已加入 `.gitignore`；不要提交其中 PDF。
- Python virtual environment：`.venv` 已创建，Python 3.13.5。
- 文档工具：Pandoc 2.12 可用；本机 MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 已用于 v6 和 v7 三遍编译。v7 原生 `.log`、14 页 PDF、字体/URI/文本和逐页渲染均已验收；v4/v5 与五份 v4 期刊衍生稿仍未真实编译，不能套用 v7 结论。
- 外部制品交付：Google Drive 的 v2/v3 历史基线保持不变；本轮没有 Drive 操作。v6 TeX、PDF、固定 ZIP、代码、测试和审计结果已在 public GitHub repository 可读并完成匿名一致性审计。v7 PDF 直接引用该仓库，因此 DMGT 首投不需要另附 ZIP 或发邮件；本地 v7 源/PDF尚未 push 也不影响链接有效性。
- `requirements.txt` 已列出 `networkx`、`numpy`、`pandas`、`sympy`、`pytest`、`matplotlib`。
- 上述 packages 已安装并核对：NetworkX 3.6.1、NumPy 2.5.2、pandas 3.0.5、SymPy 1.14.0、pytest 9.1.1、Matplotlib 3.11.1。
- 项目独立实现、extension audit 与 mixed-join DP 测试：v7 验收时为 `30 passed in 0.36s`；运行命令为 `.\.venv\Scripts\python.exe -m pytest -q tests`。184 次 DP 重构树侧集合的 definition-first dual-GP 可行性检查仍全部零失败；这些有限实验是验证，不构成证明或全范围 exhaustive claim。

## 12. 每轮结束时的更新规则

完成一项任务后，必须同时：

1. 更新本文件的 `Last updated`；
2. 把完成项移入“已经完成”；
3. 更新“已确认事实”和 `UNKNOWN`，但只写有证据支持的变化；
4. 指定唯一明确的下一步；
5. 在 `notes/research_log.md` 留下详细日志；
6. 若新增或修改数学实现，增加测试和复现信息。

这样，新窗口只需遵循 `AGENTS.md` 的自动指示并读取本文件，就能安全接续项目。
