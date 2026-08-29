# Literature Notes

## PDF inventory

- `Dokyeesun 等 - 2026 - General position problems in strong and lexicographic products of graphs.pdf`（13 页，文本可提取，关键页面已用渲染图核对）

## Core paper

Pakanun Dokyeesun, Sandi Klavžar, Dorota Kuziak, and Jing Tian, “General position problems in strong and lexicographic products of graphs,” *Computational and Applied Mathematics* 45, Article 97 (2026), DOI: 10.1007/s40314-025-03547-7.

### Result 1 — dual general position 的凸性刻画

Statement:

若 $X$ 是连通图 $G$ 的 general position set，则 $X$ 是 dual general position set，当且仅当 $G-X$ 是 convex。

Assumptions:

- $G$ 连通；
- $X\subseteq V(G)$；
- $X$ 已经是 general position set。

What it tells us:

检查 dual general position 可以分成两个严格步骤：先检查 $X$ 是否 general position，再检查补集是否 convex。这一判据可用于任何候选图，包括 $K_m\circ T$。

What it does NOT tell us:

它没有直接给出最大集合的大小，也没有给出 $gp_d(K_m\circ T)$ 的公式。

Source:

核心论文 PDF p. 3 of 13，Theorem 2.1(iii)。论文说明该刻画来自 Tian and Klavžar (2025, Theorem 3.1)。

### Result 2 — $K_m\circ H$ 的 total general position number

Statement:

Corollary 5.2 说明：若 $G,H$ 的阶都至少为 2，则

$$
gp_t(G\circ H)=
\begin{cases}
s(G)n(H),&H\text{ 是完全图},\\
0,&H\text{ 不是完全图}.
\end{cases}
$$

特别地，取 $G=K_m$ 且 $m\ge 2$，因为 $s(K_m)=m$，可得到相应的 $gp_t(K_m\circ H)$。

Assumptions:

- 两个因子的阶至少为 2；
- $s(G)$ 是 simplicial vertices 的数目，$n(H)=|V(H)|$。

What it tells us:

论文已经完整处理了该方向的 **total** general position number。

What it does NOT tell us:

$gp_t$ 不是 $gp_d$。这个结论不能当作 dual general position number 的公式。

Source:

核心论文 PDF p. 9 of 13，Corollary 5.2。

### Result 3 — $K_m\circ H$ 的 outer general position number（无 universal vertex 情形）

Statement:

若 $H$ 的阶至少为 2 且没有 universal vertex，并且 $m\ge 2$，则：

$$
gp_o(K_m\circ H)=
\begin{cases}
gp_o(H),&\operatorname{diam}(H)=2,\\
gp_o(K_1+H),&\operatorname{diam}(H)>2.
\end{cases}
$$

Assumptions:

- $|V(H)|\ge 2$；
- $H$ 没有 universal vertex；
- $m\ge 2$。

What it tells us:

论文已经在所列条件下精确处理了 $K_m\circ H$ 的 **outer** general position number。

What it does NOT tell us:

- 这是 $gp_o$，不是 $gp_d$。
- 它不覆盖有 universal vertex 的图，例如星图。
- 即使对某棵树能使用该定理，也不能由此推出该树对应的 $gp_d$。

Source:

核心论文 PDF p. 11 of 13，Theorem 5.7(1)。

### Result 4 — 论文调用的 lexicographic product 凸集限制

Statement:

论文在进入 dual general position 部分时回顾了 Anand et al. (2012, Theorem 2.1) 的一个条件：$G\circ H$ 若含有非完全的 convex subgraph，则 $H$ 必须是完全图。

Assumptions:

完整条件现已从 Anand et al. 作者预印本 Theorem 2.1 核对：$G\circ H$ 必须 nontrivial、connected，且 $Y$ 必须是 proper、non-complete induced subgraph；另外还要求 $p_G(Y)$ convex、$Y$ $\Lambda$-complete、$H$ complete。详见本文件后面的 “Full-text verification of foundational papers”。

What it tells us:

当第二因子 $H$ 非完全时，这个条件会强烈限制 convex set；结合 Theorem 2.1(iii)，它会限制 dual general position set 的补集结构。

What it does NOT tell us:

“补集受到限制”不等于已经知道最大 dual general position set 的大小。论文随后仍把 $K_m\circ G$ 的一般 dual 问题明确留作开放问题。

Source:

核心论文 PDF p. 11 of 13，Section 5.2 开头；该段引用 Anand et al. (2012, Theorem 2.1)。

### Result 5 — 无 simplicial vertices 时的零值结论

Statement:

如果 $G$ 与 $H$ 都没有 simplicial vertices，则

$$
gp_d(G\circ H)=0.
$$

Assumptions:

- Theorem 5.8 的总假设写明 $G$ 连通；
- 第 (i) 项要求 $G,H$ 都没有 simplicial vertices；
- 论文的全局约定通常还把所研究的图视为简单、连通图。

What it tells us:

它精确解决了一类 lexicographic products 的 dual general position number。

What it does NOT tell us:

它不能用于 $K_m\circ T$：完全图 $K_m$ 的每个顶点都是 simplicial vertex；非平凡树也有 simplicial leaves。因此关键假设不成立。

Source:

核心论文 PDF pp. 11-12 of 13，Theorem 5.8(i)。

### Result 6 — 第二因子为完全图时的乘法公式

Statement:

若 $G$ 连通且 $n\ge 1$，则

$$
gp_d(G\circ K_n)=gp_d(G)\,n.
$$

Assumptions:

- $G$ 连通；
- $n\ge 1$；
- 第二因子必须是完全图 $K_n$。

What it tells us:

完整解决了第二因子为完全图的情形。因为一棵完全的树只能是 $K_1$ 或 $K_2$，所以候选树问题中的这两个最小特例可由此覆盖。

What it does NOT tell us:

- 它不覆盖第二因子为一般非完全树的 $K_m\circ T$。
- 把 $G=T$ 代入只得到 $T\circ K_n$，而不是 $K_n\circ T$。
- lexicographic product 一般不可交换，因此不能交换两个因子来套用定理。

Source:

核心论文 PDF pp. 11-12 of 13，Theorem 5.8(ii)。证明使用 $G\circ K_n\cong K_n\boxtimes G$ 及 Theorem 4.7。

### Result 7 — block graph 情形的等式（因子顺序必须保留）

Statement:

论文在结尾总结：当 $G$ 是 block graph 时，

$$
gp_t(G\circ K_n)=gp_o(G\circ K_n)=gp_d(G\circ K_n).
$$

Assumptions:

- $G$ 是 block graph；
- 乘积写作 $G\circ K_n$，完全图在第二因子。

What it tells us:

树属于 block graphs，所以该总结适用于 $T\circ K_n$。

What it does NOT tell us:

它不是关于 $K_m\circ T$ 的结果。因子顺序相反，不能利用“树是 block graph”直接解决候选问题。

Source:

核心论文 PDF p. 12 of 13，Section 6 第一段；这里是作者对论文结果的总结，没有另给编号。

## Open problems explicitly stated by the authors

### Open problem 1 — determine $gp_d(K_m\circ G)$

Statement:

作者明确留下的问题是：确定 lexicographic product $K_m\circ G$ 的 dual general position numbers。

Meaning:

这里的 “determine” 是要对这一乘积族给出足够完整的精确刻画或计算结果，而不只是计算少数例子。作者说明 total 和 outer 两类已经得到综合处理，但 dual 情形仍待确定。

Source:

核心论文 PDF p. 12 of 13，Section 6 “Open problems” 第二段；该问题没有单独的 Problem 编号。

## Future work explicitly suggested by the authors

作者提出一个“natural direction for future research”：刻画除 block graphs 之外，还存在什么图类 $G$ 使

$$
gp_t(G\circ K_n)=gp_o(G\circ K_n)=gp_d(G\circ K_n)
$$

成立。来源为核心论文 PDF p. 12 of 13，Section 6 第一段。作者将它表述为 future research direction；本笔记不把它与上面明确写成 open problem 的 $K_m\circ G$ 问题混为一谈。

## Wider-literature status

系统性 topic-based search 已于 2026-08-28 完成。检索发现 Weiqi Jiang 于 2026-08-27 在 Zenodo 发布的 v1.0.1 预印本，题为 “Dual General Position in Lexicographic Products with a Complete First Factor”，它明确声称解决所有 $gp_d(K_m\circ G)$，从而覆盖树情形。因此不能再写“没有文献处理 restricted tree case”。该记录是非常新的公开预印本，尚未找到同行评审版本。2026-08-28 本项目已完成独立 proof-and-reproducibility audit：Theorems 3.1--3.2 与 Proposition 3.3 的证明通过逐步审计，supplement 成功复现，项目第二套独立实现没有发现 mismatch。当前标签是：**EXACT PUBLIC PREPRINT CLAIM FOUND — INTERNALLY PROOF-VERIFIED — NOT PEER REVIEWED**。本项目不作 novelty claim。原先记录为完整查询入口的 `notes/literature_search_log.md` 在本阶段开始时不在工作区；无法恢复的早期查询细节继续记为 `UNKNOWN`。

## Candidate restricted problem status

Candidate:

Determine $gp_d(K_m\circ T)$ for trees $T$.

1. **它是否是原论文开放问题的一个特例？**

   是。树 $T$ 是图 $G$ 的一个特殊类别，所以把开放问题中的 $G$ 限制为树就得到该候选问题。通常应明确 $m\ge 2$；$m=1$ 时 $K_1\circ T\cong T$。

2. **论文是否给出足以直接推出一般树情形的定理？**

   没有。Theorem 5.8(i) 的“两个因子都没有 simplicial vertices”假设对 $K_m\circ T$ 不成立；Theorem 5.8(ii) 要求第二因子为完全图，只覆盖 $T=K_1,K_2$ 等完全树特例。关于 block graph 的总结处理的是 $T\circ K_n$，因子顺序相反。

3. **有没有明显原因说明树情形已经 trivially solved？**

   仅根据该论文，没有。树的 leaves 是 simplicial vertices，这使某些定理无法使用，却不会自动给出 $gp_d$。论文给出的 convex 限制也只是结构约束，不是最大值公式。

4. **仅根据该论文的状态标签：**

   **NOT SOLVED IN PAPER**

这表示论文没有解决整个树族；它不表示整个数学文献中无人解决，也不否认 $K_1,K_2$ 等小特例已经被覆盖。

## Citation-chain literature search

### Search scope and reliability rules

- 本节只沿当前核心论文的正文引用和 references 建立检索起点，没有进行互联网大范围搜索。
- 核心论文使用作者—年份引用制，文末 references 没有编号。因此下列每项的 “Exact reference number” 都记为 `NONE`；这不是漏查，也不能虚构数字编号。
- 核心论文本身没有列 DOI。后续定向检索已确认 C1、C2 的 DOI；其余候选若未另行核对，继续记为 `UNKNOWN`。
- “Why relevant” 只依据核心论文明确说明的引用用途。尚未取得全文的论文，不根据标题推断其定理或结论。

### Candidate C1 — dual general position 的直接基础来源

Title:

Variety of general position problems in graphs

Authors:

Jing Tian; Sandi Klavžar

Year:

2025

Journal / arXiv:

*Bulletin of the Malaysian Mathematical Sciences Society* 48:5; arXiv:2402.17338

DOI:

10.1007/s40840-024-01788-z

How it is cited in the core paper:

核心论文 PDF p. 2 说明 total、outer、dual 这组 general position 变体由 Tian and Klavžar (2025) 引入；PDF p. 3 又把核心论文 Theorem 2.1 的三项刻画分别归于该文 Theorems 2.1、2.3、3.1。其中特别包括“$X$ dual 当且仅当 $X$ general position 且 $G-X$ convex”的结构刻画。

Why relevant:

这是核对 dual general position 的原始定义、记号、边界情况和 convex-complement 刻画的第一优先全文，不能只依赖当前核心论文的转述。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C2 — lexicographic product 凸集结构的直接来源

Title:

Convex sets in lexicographic products of graphs

Authors:

B. S. Anand; M. Changat; Sandi Klavžar; I. Peterin

Year:

2012

Journal / arXiv:

*Graphs and Combinatorics* 28:77-84; author-hosted preprint `LexConvexFinal.pdf`（未查到 arXiv 编号）

DOI:

10.1007/s00373-011-1031-4

How it is cited in the core paper:

核心论文 PDF p. 11，Section 5.2 引用 Anand et al. (2012, Theorem 2.1)，称其用三个条件刻画 lexicographic products 的非完全 convex sets，并明确转述其中一个必要条件：若 $G\circ H$ 含非完全 convex subgraph，则 $H$ 必须是完全图。

Why relevant:

dual general position 的关键条件是补集 convex，而我们的对象正是 lexicographic product。必须从全文核对该定理的完整三个条件、所有假设及例外情形。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C3 — standard general position 的基础来源之一

Title:

A general position problem in graph theory

Authors:

P. Manuel; Sandi Klavžar

Year:

2018

Journal / arXiv:

*Bulletin of the Australian Mathematical Society* 98:177-187

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF p. 2 把 Manuel and Klavžar (2018) 与 Chandran and Parthasarathy (2016) 并列为 standard general position 在图论中的独立引入来源。核心论文还说明其 Lemma 3.1 中 general position 部分的论证与 Manuel and Klavžar (2018, Theorem 3.1) 的证明相同。

Why relevant:

dual general position 首先要求集合是 standard general position set。该文是核对基本定义、早期术语和标准判定思路的重要原始来源。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C4 — standard general position 的另一独立来源

Title:

The geodesic irredundant sets in graphs

Authors:

S. V. Chandran; G. J. Parthasarathy

Year:

2016

Journal / arXiv:

*International Journal of Mathematical Combinatorics* 4:135-143

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF p. 2 将它与 Manuel and Klavžar (2018) 并列，称 standard general position sets 在这两项工作中被独立引入。

Why relevant:

它提供 standard general position 的另一条原始来源，可用于检查早期定义是否使用不同术语或表述。具体定理内容在取得全文前保持 `UNKNOWN`。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C5 — lexicographic product 的 strong-resolving 结构来源

Title:

Closed formulae for the strong metric dimension of lexicographic product graphs

Authors:

Dorota Kuziak; Ismael G. Yero; Juan A. Rodríguez-Velázquez

Year:

2016

Journal / arXiv:

*Discussiones Mathematicae Graph Theory* 36:1051-1064

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF pp. 9-10 在 Section 5.1 中使用该文的 Remark 6，并把该文 Propositions 8、11、13、16 汇总为核心论文 Proposition 5.4，用于描述 lexicographic products 的 strong resolving graphs，随后推导 outer general position 结果。

Why relevant:

它不是 dual general position 的定义来源，但它是核心论文处理 lexicographic product 层结构、true twins、边界和 strong resolving graph 的主要技术来源。获取全文有助于理解核心论文的 product-specific 工具；不能把其中的 outer 结果直接当作 dual 结果。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C6 — tree-specific general position 检索入口

Title:

The general position number of Cartesian product of two trees

Authors:

Jing Tian; Kexiang Xu; Sandi Klavžar

Year:

2021

Journal / arXiv:

*Bulletin of the Australian Mathematical Society* 14:1-10, **as printed in the core paper**. 该卷页记载可能需要从全文或期刊目录独立核对，目前不擅自改正。

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF p. 2 把 Tian et al. (2021) 列在“general position sets of graph operations”既有研究中；文末 reference 给出上述题名。

Why relevant:

这是核心 references 中唯一题名明确同时出现 general position 与 two trees 的条目，因此是 tree-specific 文献链的重要入口。但它研究的是 standard general position 和 Cartesian product；在取得全文前，不能推断其结论或方法适用于 dual general position 或 $K_m\circ T$。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C7 — general position 与 strong resolving graph 的连接

Title:

The general position problem and strong resolving graphs

Authors:

Sandi Klavžar; Ismael G. Yero

Year:

2019

Journal / arXiv:

*Open Mathematics* 17:1126-1135

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF p. 2 把该文作为 strong products 上 general position 研究，并提到其中关于 $gp(G\boxtimes H)$ 是否等于 $gp(G)gp(H)$ 的问题；核心论文 PDF p. 5 还引用其 Proposition 2.4 作为 diameter-two、无 true twins 情形的相关 standard-general-position 结果。

Why relevant:

它连接 standard general position、strong resolving graphs 和 graph products，可帮助理解核心论文为何能把某些 outer general position 问题转化为 clique 问题。它不是 $K_m\circ T$ 的直接解决结果。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Candidate C8 — graph operations 上 general position 的后续入口

Title:

The general position problem on Kneser graphs and on some graph operations

Authors:

M. Ghorbani; Sandi Klavžar; H. R. Maimani; M. Momeni; F. Rahimi-Mahid; G. Rus

Year:

2021

Journal / arXiv:

*Discussiones Mathematicae Graph Theory* 41:1199-1213

DOI:

`UNKNOWN`

How it is cited in the core paper:

核心论文 PDF p. 2 把 Ghorbani et al. (2021) 列入“general position sets of graph operations”的既有研究。

Why relevant:

它是沿 graph-operations 方向继续检索的候选入口。但核心论文没有说明该文具体研究哪些 operations，因此它是否含 lexicographic product 内容目前为 `UNKNOWN`，不能依据题名自行判断。

Exact reference number in the core paper:

`NONE` — unnumbered author-year reference list.

### Highest-priority full texts and acquisition status

1. Tian and Klavžar (2025), *Variety of general position problems in graphs* — **已获得并核对** dual general position 的定义及 Theorem 3.1。
2. Anand et al. (2012), *Convex sets in lexicographic products of graphs* — **已获得作者预印本并核对** convex-set 定理的完整条件。
3. Manuel and Klavžar (2018), *A general position problem in graph theory* — 核对 standard general position 的基础定义与早期结构结果。
4. Kuziak, Yero, and Rodríguez-Velázquez (2016), *Closed formulae for the strong metric dimension of lexicographic product graphs* — 理解核心论文实际调用的 lexicographic-product 结构工具。
5. Tian, Xu, and Klavžar (2021), *The general position number of Cartesian product of two trees* — 建立 tree-specific general-position 文献入口，同时明确其 product 和 invariant 与当前问题不同。

### Two most critical foundations for dual general position

1. **Tian and Klavžar (2025)**：dual general position 定义及“general position + convex complement”结构刻画的直接来源。
2. **Anand et al. (2012)**：理解这一 convex-complement 条件在 lexicographic products 中如何受限的关键来源。

这两篇的角色不同：第一篇定义 dual 并给出一般结构刻画；第二篇研究 lexicographic product 中的 convex sets。两者合起来才直接支撑当前文献理解阶段。

## Full-text verification of foundational papers

### Foundation 1 — Tian and Klavžar (2025)

Local file:

`Tian和Klavžar - 2025 - Variety of General Position Problems in Graphs.pdf`（Springer 版本，14 页）

Verified definitions:

- PDF p. 3，Section 2 正式引入 general、total、outer、dual general position sets，并定义 $gp_d(G)$。
- dual 的原始定义与核心论文的重述一致：既要求 $X$ 中的点对 $X$-positionable，也要求补集中的点对 $X$-positionable。
- 由定义直接有 $gp(G)\ge gp_d(G)\ge gp_t(G)$；这只是参数间的不等式，不是 $gp_d$ 的计算公式。

Verified structural results:

1. **Theorem 3.1（PDF p. 6）**：若 $X$ 是 $G$ 的 general position set，则 $X$ 是 dual general position set，当且仅当 $G-X$ convex。
2. **Corollary 3.2（PDF p. 6）**：若 $X\subseteq S(G)$，即 $X$ 只含 simplicial vertices，则 $X$ 是 dual general position set。
3. **Non-hereditary warning（PDF p. 5）**：dual general position 不向下遗传。论文给出的例子是 $C_5$：两个相邻顶点能构成 dual set，但其中一个单点集合不能。
4. **Block graphs（PDF pp. 3-4）**：对 block graph，$gp(G)=gp_o(G)=gp_d(G)=gp_t(G)=s(G)$。论文还明确列出 $P_n$ 的最大 dual sets。
5. **Theorem 3.9（PDF pp. 10-11）**：对相邻顶点 $x,y$，$\{x,y\}$ 是 dual set、$G-\{x,y\}$ convex，以及论文给出的邻域完备性/距离条件三者等价。
6. **Proposition 3.10（PDF p. 11）**：对不相邻顶点 $x,y$，$\{x,y\}$ 是 dual set，当且仅当二者都是 simplicial vertices。

Plain-language significance:

Theorem 3.1 是最核心的检查方法：一个候选集合要成为 dual set，必须同时通过“集合内部没有第三点落在最短路径上”和“删掉该集合后，剩余顶点对的所有最短路径仍留在剩余图中”两项检查。Corollary 3.2 只给出一类保证可行的集合，并不保证它们一定达到最大。

What this does NOT establish:

- 它确定了 $gp_d(T)$ 对 block-graph/tree 本身的情况，但没有处理 $gp_d(K_m\circ T)$。
- Theorem 3.9 与 Proposition 3.10 只刻画大小为 2 的集合，不能直接确定最大集合。
- 这些结果没有建立 restricted tree-product problem 的 novelty。

### Foundation 2 — Anand et al. (2012)

Local file:

`LexConvexFinal.pdf`（作者公开预印本，9 页；定理编号与核心论文引用一致）

Verified terminology:

- PDF p. 2 明确把 geodesics 说明为 shortest paths。
- PDF p. 3 定义 lexicographic product、$G$-layers、$H$-layers 和 projections，并明确指出该乘积可结合但一般不可交换。
- PDF p. 3 定义 $\Lambda$-vertex：一个顶点邻接两个彼此不相邻的顶点。
- PDF p. 3 定义 $\Lambda$-complete：对投影 $p_G(Y)$ 中每个 $\Lambda$-vertex $g$，整个 $H$-layer ${}^gH$ 都必须包含在 $Y$ 中。

### Result — Anand et al. Theorem 2.1

Statement:

设 $G\circ H$ 是 nontrivial、connected lexicographic product。它的一个 proper、non-complete induced subgraph $Y$ 是 geodesically convex，当且仅当以下三项同时成立：

1. $p_G(Y)$ 在 $G$ 中 convex；
2. $Y$ 是 $\Lambda$-complete；
3. $H$ 是 complete graph。

Assumptions:

- $G\circ H$ nontrivial，即两个因子都至少有两个顶点；
- 乘积连通；
- $Y$ 是诱导子图；
- $Y$ proper，即 $Y\ne G\circ H$；
- $Y$ non-complete。

What it tells us:

它完整补上了核心论文只转述的一项条件。特别是：若第二因子 $H$ 非完全，则 $G\circ H$ 不可能有 proper、non-complete convex induced subgraph。这个结论会限制 dual set 的 convex complement，但仍必须与 general position 条件一起使用。

What it does NOT tell us:

- 定理不描述 complete convex induced subgraphs，也不描述整个 $G\circ H$；它们被 “proper, non-complete” 假设排除。
- $\Lambda$-complete 与“完全图”不是同一个概念。
- 仅凭这个凸集定理不能直接得到 $gp_d(K_m\circ T)$ 的最大值。
- 定理的因子顺序不能交换；条件 (iii) 指的是第二因子 $H$ complete。

Source:

Anand et al. author preprint PDF pp. 3-4 of 9，Theorem 2.1。核心论文在 PDF p. 11 of 13 引用同一定理，但只转述了条件 (iii)。

### Version and verification notes

- Tian and Klavžar 文件是期刊版，页码和定理号可直接用于当前笔记。
- Anand et al. 文件是作者公开预印本；Theorem 2.1 的编号和内容与核心论文的引用相符，但最终期刊版页码尚未核对，期刊版页码记为 `UNKNOWN`。
- 两份 PDF 均可可靠提取文本，关键定义与定理页已通过渲染图目视核对。
- restricted tree-product problem 在更广文献中的状态仍为 `UNKNOWN`；本次核验不构成系统文献检索。

## Theorem applicability audit

已建立 `notes/theorem_applicability.md`，逐项审计已核验定理对 $K_m\circ T$ 的适用范围。审计使用以下分类：直接适用、只给必要条件、只覆盖边界特例、不适用，以及代入后仍为 `UNKNOWN`。

当前审计没有提出一般公式，也没有作 novelty claim。它只记录从三篇已核验论文可以安全推出什么，以及哪些关键问题仍未由这些结果回答。

## Citation-forward literature search — 2026-08-28

### Scope and method

本轮只做窄范围前向引文检索，检索截止日期为 2026-08-28。使用的入口包括：

- Springer Nature 论文页及 Dimensions citation count；
- OpenAlex 的 `cites` 关系；
- OpenCitations Index v2 的 DOI、OMID 和 arXiv 标识符；
- arXiv、出版社页面、作者公开全文和期刊终稿；
- 精确题名、DOI，以及 `dual general position`、`lexicographic product`、`K_m`、`trees` 等组合查询。

引用次数只作为发现入口，不作为论文内容证据。不同索引的计数并不同步：检索时 Tian–Klavžar 论文的 Springer 页面显示 6 次引用，核心论文显示 2 次引用；OpenAlex 对两者分别返回 6 和 1；OpenCitations 对只有 DOI 的记录又有不同覆盖。最终判断以下文逐篇元数据、摘要或全文为准。

此外，`gp_d` 也可能表示 **general d-position number**，不是 dual general position number；只出现该字符串而没有 dual 定义的搜索结果已排除，不能当作相关论文。

### Individually verified citing papers

| Citing paper | Verified citation link | Reliable scope check | Relevance to $gp_d(K_m\circ T)$ |
|---|---|---|---|
| Z.-L. Li and S.-C. Gong, “Graphs Whose Edge General Position Number is 4,” DOI `10.1007/s40840-025-01870-0` | 期刊 references 明列 Tian–Klavžar (2025) | 摘要和全文预览研究 edge general position number $gp_e$ 的值 4 | 不研究 dual、lexicographic product 或目标问题 |
| S. Klavžar et al., “Moving through Cartesian products, coronas and joins in general position,” DOI `10.1016/j.dam.2025.10.041` | 全文 reference [30] 引用 Tian–Klavžar (2025) | 研究 mobile general position；正文为下界调用 outer general position，运算是 Cartesian product、corona、join | 不研究 dual lexicographic product |
| Z. Hamed-Labbafian et al., “Three algorithmic approaches to the general position problem,” DOI `10.1017/S0004972725100178` | 全文 reference [17] 引用 Tian–Klavžar (2025) | 摘要与全文只为 standard general position 提出 ILP、genetic algorithm 和 simulated annealing | 不研究 dual 或目标乘积 |
| S. Klavžar, A. Lakshmanan S., and D. Roy, “Counting Largest Mutual-Visibility and General Position Sets of Glued t-ary Trees,” DOI `10.1007/s00025-025-02529-9` | 期刊全文 reference [24] 引用 Tian–Klavžar (2025) | 确实计算 glued binary/t-ary graphs 的四种 general position invariants；其中 $gp_d=0$ 的结果是关于 glued graphs | 有 dual 和 tree-shaped construction，但没有 lexicographic product，未处理 $K_m\circ T$ |
| P. Dokyeesun et al., 核心论文，DOI `10.1007/s40314-025-03547-7` | 全文引用 Tian–Klavžar (2025) 与 Anand et al. (2012) | 已在前述全文核验中记录；作者明确留下 $gp_d(K_m\circ G)$ | 这是目标问题来源，不是后续解答 |
| J. Tian, P. Dokyeesun, and S. Klavžar, “On the variety of general position problems under vertex and edge removal,” DOI `10.1016/j.dam.2026.02.044`；arXiv:`2510.01294` | 全文 references [17]、[6] 分别引用 Tian–Klavžar (2025) 与核心论文 | 摘要、目录和全文显示主题是删点/删边对 $gp_t,gp_o,gp_d$ 的影响；全文只在研究史中提到 strong/lexicographic products | 是 dual 的真正后续论文，但没有求 $K_m\circ T$ |
| D. Roy et al., “Varieties of Mutual-Visibility and General Position on Sierpiński Graphs,” DOI `10.7151/dmgt.2625`；arXiv:`2504.19671` | 期刊终稿 reference [31] 引用 Tian–Klavžar (2025) | 终稿研究 Sierpiński graphs 上八种 invariants，包括 dual general position | 不研究 lexicographic product 或 $K_m\circ T$ |
| H. S. and U. Chandran S. V., “General position and mutual-visibility in shadow graphs,” arXiv:`2601.19769` | 全文 references [14]、[37] 分别引用核心论文与 Tian–Klavžar (2025)；OpenCitations v2 用 arXiv 标识解析出核心论文的第二条引用 | 摘要、章节和全文只研究 standard $gp$ 与 mutual visibility；Theorem 3.9 处理的是 tree 的 **shadow graph** $S(T)$ | 虽出现 trees，但没有 dual general position，也没有 lexicographic product |

### Forward citations of the core paper

已逐篇识别 Springer/Dimensions 所显示的两条核心论文引用：

1. “On the variety of general position problems under vertex and edge removal”；
2. “General position and mutual-visibility in shadow graphs”。

第一篇研究 dual 但不研究 lexicographic product；第二篇只研究 standard general position 与 mutual visibility。两篇都没有解决 $gp_d(K_m\circ T)$。

### Forward citations of Anand et al. (2012)

OpenAlex 检索时列出 42 条引用 Anand et al. (2012) 的记录。按题名、年份与主题筛选后：

- 2026 核心论文是唯一同时明确涉及 dual general position 与 lexicographic product 的命中；
- “A Steiner general position problem in graph theory” (2021) 虽含 general position，但研究 Steiner general position，且早于 dual general position 的引入；
- 其余命中研究 graph convexity、Steiner concepts、distance preservation、equidistant dimension 或其他 graph products，不是 dual general position。

精确 DOI/题名与 `dual general position` 的组合搜索也只返回已经核验的核心论文。没有发现一篇新的、引用 Anand et al. 且处理目标问题的论文。

### Result and limits

**找到相关后续论文：是。** 特别是删点/删边论文和 Sierpiński graphs 论文确实继续研究 dual general position。

**找到解决 $gp_d(K_m\circ T)$ 的论文：否（在本次窄范围前向引文检索内）。**

这个“否”只描述本次检索结果，不是全领域不存在性结论。引用索引存在收录延迟、计数差异和假阳性；没有引用三篇起点论文的独立工作也不会被 citation-forward 方法发现。因此 restricted tree problem 的全领域 novelty 和 solved/unsolved status 继续记为 `UNKNOWN`。

后续系统主题检索确实发现了一篇没有被上述前向引文链捕获的 Zenodo 预印本；因此本节最后一句只保留为当时阶段的历史记录，当前状态以下一节为准。

## Systematic topic-based search — 2026-08-28

### Coverage

本轮检查了 OpenAlex、arXiv、zbMATH Open、DataCite、Crossref、Zenodo、通用网页检索，以及 2026-08-16 更新的领域综述 *The General Position Problem: A Survey* v5。Semantic Scholar API 因 HTTP 429 无法使用；MathSciNet、Scopus、Web of Science 没有直接访问条件。各查询式、原始计数、去重规则和覆盖缺口均记录在 `notes/literature_search_log.md`。

最关键的索引差异是：新预印本能由 OpenAlex 的 `gp_d` + `lexicographic product` 查询和 DataCite/Zenodo 找到，但截至检索时没有被 arXiv、zbMATH、Crossref、领域综述或通用网页结果收录。这解释了 citation-forward search 为何漏掉它，也说明不能依赖单一数据库作否定判断。

### Exact-target preprint

Reference:

Weiqi Jiang, “Dual General Position in Lexicographic Products with a Complete First Factor,” Zenodo preprint v1.0.1, 2026-08-27, DOI `10.5281/zenodo.22116770`; concept DOI `10.5281/zenodo.22081165`.

Verified metadata:

- Zenodo 类型为 `publication/preprint`，开放获取，CC BY 4.0；
- v1.0.0 发布于 2026-08-24，DOI `10.5281/zenodo.22081166`；
- v1.0.1 发布于 2026-08-27；
- 当前 PDF 10 页，并附完整复现 ZIP；
- 预印本作者信息列为 Jiang, Weiqi，Institute of Theoretical Physics, Chinese Academy of Sciences；记录没有 ORCID；
- 没有检索到期刊版或其他同行评审版本。

Full-text claim:

预印本 Theorem 3.2 声称：对任意非空有限简单图 $G$ 和 $m\ge2$，

$$
gp_d(K_m\circ G)=m q_2(G),
$$

其中

$$
q_2(G)=\max\{|A|:A\subseteq V(G),\ G[A]\text{ 与 }G[V(G)\setminus A]\text{ 都是完全图}\},
$$

如果没有这样的 $A$，则定义 $q_2(G)=0$。

预印本 Theorem 3.1 声称一个逐 layer 的充要条件：除空集外，$K_m\circ G$ 的 dual general-position set 在每个 $G$-layer 中的 selected part 和 unselected part 都必须诱导完全图；反过来该条件也充分。Proposition 3.3 再把这种分割等价地写成 $\overline G$ 的二部划分。

Scope verdict after the 2026-08-28 audit:

- 这不是“相关但不同”的论文，而是对核心开放问题的**精确解答主张**；
- 它的公式比树 restricted case 更一般；
- 这里的 “claim” 是文献事实，即预印本确实这样陈述；
- 本项目已独立重做 Theorems 3.1--3.2 与 Proposition 3.3 的论证并确认每个必要性、充分性和边界步骤；详细记录见 `proofs/jiang_v1_0_1_audit.md`；
- supplement 的 36 个测试和 1,064 次比较在 Python 3.13.5 下复现成功；项目第二套不同数据结构与算法的实现也通过 217 个最大值比较和 4,780 个集合级分类比较；
- 这些结果支持内部采用该公式，但不改变其“预印本、未找到同行评审版本”的文献状态。

### Independently proved consequence for trees

本项目在主定理通过审计后，独立使用“树中每个 clique 至多有两个顶点”证明：能够被两个 clique 分割的树只有 $K_1,K_2,P_3,P_4$。因此对 $m\ge2$ 有

$$
gp_d(K_m\circ T)=
\begin{cases}
m,&T=K_1,\\
2m,&T\in\{K_2,P_3,P_4\},\\
0,&\text{其他树}.
\end{cases}
$$

其中 $K_{1,3}$ 虽然只有四个顶点，但没有完美匹配，不能分割成两个二点 clique；阶至少为 5 的树则因为两个 clique 最多覆盖 4 个顶点而被排除。完整独立证明见 `proofs/tree_corollary.md`。

### Current literature judgment

- “核心论文没有解决树情形”仍然正确。
- “前向引文论文没有解决树情形”仍然正确。
- “没有文献给出解答”已经不正确：Zenodo 上存在精确目标预印本。
- “该公式已经通过同行评审”没有证据支持。
- “该公式已被本项目内部 proof audit 和两套计算实现验证”成立；这不等于同行评审。
- restricted problem 的独立 novelty 不得声称；下一阶段应寻找有文献依据、尚未被该预印本覆盖的扩展方向。

## Post-Jiang extension audit — 2026-08-28

The bounded target-selection audit is complete and recorded in
`notes/extension_feasibility_audit.md`.

- Jiang Theorem 5.1 already covers complete joins whose factors are all
  nonempty and noncomplete.  PDF page 9 explicitly leaves mixed joins with
  complete and noncomplete factors, and arbitrary `F circ G`, unclassified.
- A fresh arXiv exact-phrase query returned the foundation, product, and removal
  papers; adding `join` returned no record.  A DataCite title-field query for
  `dual general position` plus `join` also returned no record.  OpenAlex was
  unavailable because of HTTP 429.  Hence the strict status is **NOT FOUND IN
  THIS BOUNDED AUDIT**, not a proof of openness.
- `P_3 circ T` was rejected as a candidate because it decomposes as `T + 2T`
  and is already covered by Jiang Theorem 5.1 for noncomplete `T`.
- Two concrete candidates were screened: mixed joins `K_r + T` and path-first
  products `P_n circ T`, `n >= 4`.  Only the mixed-join family was selected.
- The selected problem is to determine `gp_d(K_r + T)` for `r >= 1` and trees
  of order at least three by formally proving a two-branch reduction and
  characterizing the apex-avoiding parameter `beta(T)`.
- The preserved counterexample `gp_d(K_r + K_{1,3}) = 3` with
  `q_2(K_{1,3}) = 0` shows that a mixed-join formula cannot simply add a
  complete-factor contribution to Jiang's `q_2` expression.

No novelty claim or formal conjecture was made in this audit.

## Systematic mixed-join positioning — 2026-08-28

The post-proof literature-positioning stage is complete.  The full query
matrix, database counts, inclusion/exclusion decisions, version discrepancies,
coverage limitations, and research-note verdict are recorded in
`notes/mixed_join_literature_positioning.md`.

The most important new finding is a direct prior subcase.  Tian, Dokyeesun,
and Klavžar, “On the variety of general position problems under vertex and edge
removal,” *Discrete Applied Mathematics* 388 (2026), 56--64, DOI
`10.1016/j.dam.2026.02.044`, treats the fan graph
`F_n=K_1+P_n`.  Its arXiv v2 states, for `n>=4`,

```text
gp_d(F_n) = floor(2(n+1)/3) = ceil(2n/3).
```

Hence the `r=1`, path-tree subfamily of the project theorem is already known
and must be cited as prior work.  The older author-hosted v1 PDF instead displays
`ceil(2(n+1)/3)`; arXiv v2 corrects this to a floor and adds the independent-edge
description.  The version-of-record body was not accessible for a direct
floor/ceiling comparison, so that exact display in the VOR remains `UNKNOWN`.

No exact theorem for all `gp_d(K_r+T)`, all cone-over-tree graphs, or the
project parameter `beta(T)` was found in the recorded arXiv, DataCite, zbMATH,
Crossref-screening, web, citation, and survey checks.  This is strictly **NOT
FOUND IN THIS AUDIT**.  OpenAlex returned HTTP 429 and contradictory zeros;
Semantic Scholar returned HTTP 429; MathSciNet, Scopus, and Web of Science were
not directly accessible.  Global openness and novelty therefore remain
`UNKNOWN`.

The closest optimization concept is a dissociation set, which only requires
`Delta(T[X])<=1`.  A beta-feasible set has the additional condition that every
selected vertex has at most one neighbor outside `X`, so the two notions are not
equivalent.  No established name for this stricter tree parameter was found.

The feasibility verdict is **CONDITIONAL GO FOR AN INTERNAL RESEARCH-NOTE
DRAFT**.  The real increment is the all-tree, arbitrary-`r` mixed-join
classification plus linear maximum-set reconstruction; it is not the already
known fan formula, the Tian--Klavžar criterion, or Jiang's all-noncomplete join
theorem.  No novelty or priority claim is authorized.
