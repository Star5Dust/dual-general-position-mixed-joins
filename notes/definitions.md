# Definitions

本文档只记录已经从本地论文原文中核对过的定义。当前三篇来源论文的默认约定均以简单、连通图为主；Anand et al. (2012) 还明确假设图有限。

### graph distance

Formal definition:

对图 $G$ 的两个顶点 $u,v$，距离 $d_G(u,v)$ 是一条最短 $u,v$-路径所含的边数。

Plain-language explanation:

从 $u$ 沿着图的边走到 $v$，可能有多条路线。选用边数最少的路线，其边数就是距离。这里数的是“边”，不是顶点。

Tiny example:

设路径图 $P_3$ 的顶点依次为 $a-b-c$。则 $d_{P_3}(a,b)=1$，而 $d_{P_3}(a,c)=2$。

Source:

核心论文 PDF p. 3 of 13；Tian and Klavžar (2025) PDF p. 2 of 14；Anand et al. (2012) 预印本 PDF p. 2 of 9。三处均按 shortest path 定义距离，没有单独的 Definition 编号。

Important pitfalls:

- 距离取最短路线的长度，不是任意一条路线的长度。
- 路径长度按边数计算；例如 $a-b-c$ 有 2 条边。
- 论文默认图连通，所以任意两个顶点之间都有有限距离。

### geodesic

Formal definition:

与论文用语保持一致，我们把长度等于 $d_G(u,v)$ 的 $u,v$-路径称为一条 $u,v$-geodesic；也就是一条 shortest $u,v$-path（最短 $u,v$-路径）。

Plain-language explanation:

geodesic 就是顶点之间的一条最短路线。两个顶点之间可能不止一条最短路线。

Tiny example:

在四边形 $C_4=a-b-c-d-a$ 中，从 $a$ 到 $c$ 有两条 geodesic：$a-b-c$ 和 $a-d-c$，它们的长度都为 2。

Source:

Anand et al. (2012) 预印本 PDF p. 2 of 9 明确把 geodesics 写作 “shortest paths”，并把距离定义为 shortest path 的长度；没有单独的 Definition 编号。核心论文 PDF pp. 1、3 使用等价用语 “shortest $u,v$-path”。

Important pitfalls:

- “一条 geodesic” 不等于“唯一的 geodesic”。
- 本文定义中的 “any shortest path” 表示所有最短路径都要检查，不能只挑其中一条。

### general position set

Formal definition:

先设 $X\subseteq V(G)$。若对顶点 $u,v\in V(G)$ 的任意最短 $u,v$-路径 $P$，都有

$$
V(P)\cap X\subseteq\{u,v\},
$$

则论文称 $u,v$ 是 $X$-positionable。集合 $X$ 是 general position set，当且仅当每一对 $u,v\in X$ 都是 $X$-positionable。

等价地说：不存在三个互不相同的 $X$ 中顶点，使其中一个顶点位于另外两个顶点之间的某条最短路径上。

Plain-language explanation:

从集合 $X$ 中任取两个点作为最短路线的起点和终点，这条路线的内部不能再经过 $X$ 中的第三个点。

Tiny example:

在 $P_3=a-b-c$ 中，$\{a,c\}$ 是 general position set，因为最短路径 $a-b-c$ 的内部顶点 $b$ 不在集合中。$\{a,b,c\}$ 不是 general position set，因为 $b$ 位于 $a$ 与 $c$ 的最短路径上。

Source:

原始来源 Tian and Klavžar (2025) PDF p. 3 of 14，Section 2 “The Variety”；没有单独的 Definition 编号。核心论文 PDF pp. 1-2 of 13 重述了同一定义。

Important pitfalls:

- 路径的两个端点可以属于 $X$；禁止的是路径内部出现 $X$ 中的其他顶点。
- 若两个端点之间有多条最短路径，必须全部满足条件。
- general position 是关于“最短路径”的条件，不是平面几何里“点不共线”的直接照搬。

### convex set

Formal definition:

子图 $H$ 是图 $G$ 的 convex subgraph，当且仅当对任意 $u,v\in V(H)$，$G$ 中的每一条最短 $u,v$-路径都完全位于 $H$ 中。对 $X\subseteq V(G)$，论文称 $X$ 是 convex set，是指 $X$ 诱导的子图 $G[X]$ 是 convex subgraph。

Plain-language explanation:

在 $X$ 内任选两个点，从一个点到另一个点的任何最短路线都不能跑出 $X$。

Tiny example:

在 $P_3=a-b-c$ 中，$\{a,b\}$ 是 convex set。$\{a,c\}$ 不是 convex set，因为 $a$ 到 $c$ 的最短路径必须经过不在集合中的 $b$。

Source:

Tian and Klavžar (2025) PDF p. 2 of 14 给出一般 convex subgraph 定义；Anand et al. (2012) 预印本 PDF pp. 2-3 使用同一 geodesic convexity。核心论文 PDF p. 3 of 13 重述该定义。没有单独的 Definition 编号。

Important pitfalls:

- 条件是“每一条”最短路径都留在集合中，而不是只要存在一条即可。
- 这里的 convex 是图上的最短路径凸性，不是欧氏空间中直线段的凸性。
- “$X$ convex” 实际指诱导子图 $G[X]$ convex，不能随意选择别的边集。

### dual general position set

Formal definition:

设 $X\subseteq V(G)$，并记 $\overline X=V(G)\setminus X$。集合 $X$ 是 dual general position set，当且仅当：

1. 每一对 $u,v\in X$ 都是 $X$-positionable；
2. 每一对 $u,v\in\overline X$ 都是 $X$-positionable。

论文的 Theorem 2.1(iii) 给出等价刻画：在连通图中，如果 $X$ 已经是 general position set，那么 $X$ 是 dual general position set，当且仅当 $G-X=G[\overline X]$ 是 convex。

Plain-language explanation:

它同时要求两件事：首先，$X$ 自己必须是 general position set；其次，集合外的任意两个点之间，任何最短路线都不能穿过 $X$。第二件事等价于“补集 $\overline X$ 是凸的”。

Tiny example:

在 $P_3=a-b-c$ 中，$X=\{a,c\}$ 是 dual general position set：它是 general position set，而补集 $\{b\}$ 是 convex。相反，$X=\{b\}$ 不是 dual general position set，因为补集 $\{a,c\}$ 不是 convex；$a$ 到 $c$ 的最短路径会穿过 $b\in X$。

Source:

原始定义见 Tian and Klavžar (2025) PDF p. 3 of 14，Section 2；convex-complement 刻画见该文 PDF p. 6 of 14，Theorem 3.1。核心论文在 PDF pp. 1-3 重述了定义和刻画。

Important pitfalls:

- “dual” 不是简单地说“$X$ 和补集都各自是 general position set”。补集需要满足更强的 convex 条件。
- general position 条件与补集 convex 条件都必须满足。
- 第二条仍然检查所有最短路径。
- dual general position **不具有向下遗传性**：$X$ 是 dual set，并不保证每个子集也是 dual set。Tian and Klavžar (2025) PDF p. 5 用 $C_5$ 给出反例。

### dual general position number $gp_d$

Formal definition:

图 $G$ 的 dual general position number 是 $G$ 中最大 dual general position set 的基数：

$$
gp_d(G)=\max\bigl\{|X|:X\subseteq V(G),\ X\text{ 是 dual general position set}\bigr\}.
$$

Plain-language explanation:

在所有满足 dual general position 条件的顶点集合中，找出顶点数最多的集合；这个最大顶点数就是 $gp_d(G)$。

Tiny example:

在 $P_3=a-b-c$ 中，$\{a,c\}$ 是大小为 2 的 dual general position set，而三个顶点的全集不是 general position set。因此 $gp_d(P_3)=2$。

Source:

原始来源 Tian and Klavžar (2025) PDF p. 3 of 14，Section 2；没有单独的 Definition 编号。核心论文 PDF p. 2 of 13 使用相同记号 $\operatorname{gp}_d(G)$。

Important pitfalls:

- $gp_d(G)$ 是一个数；达到这个大小的集合才称为一个 $gp_d$-set。
- 它不同于普通 general position number $gp(G)$、outer general position number $gp_o(G)$ 和 total general position number $gp_t(G)$。
- 找到一个较大的可行集合只能给出下界；除非排除了所有更大集合，否则不能声称已经算出 $gp_d(G)$。

### lexicographic product $G\circ H$

Formal definition:

两个图 $G,H$ 的 lexicographic product $G\circ H$ 的顶点集为

$$
V(G\circ H)=V(G)\times V(H).
$$

两个不同顶点 $(g,h)$ 与 $(g',h')$ 相邻，当且仅当满足以下至少一项：

1. $g=g'$ 且 $hh'\in E(H)$；
2. $gg'\in E(G)$。

Plain-language explanation:

把 $G$ 的每个顶点替换成一整份 $H$。同一份 $H$ 内部按 $H$ 的边连接；如果 $G$ 中两个顶点相邻，那么对应的两份 $H$ 之间所有顶点两两相连。

Tiny example:

令 $G=P_2$，顶点为 $a-b$；令 $H=P_3$。则 $P_2\circ P_3$ 有 6 个顶点，分成 $a$-层和 $b$-层。每一层内部都是一条 $P_3$，并且因为 $ab\in E(P_2)$，$a$-层的每个顶点都与 $b$-层的每个顶点相邻。

Source:

Anand et al. (2012) 预印本 PDF p. 3 of 9 给出定义，并明确说明 lexicographic product 可结合但一般不可交换。核心论文 PDF p. 9 of 13 使用相同定义。没有单独的 Definition 编号。

Important pitfalls:

- 第二种相邻条件只看 $gg'\in E(G)$；此时 $h,h'$ 是否相邻完全无关。
- lexicographic product 一般不可交换：$G\circ H$ 与 $H\circ G$ 通常不是同一个图，甚至不一定同构。
- 因此，关于 $G\circ K_n$ 的定理不能自动改写成关于 $K_n\circ G$ 的定理。

### $\Lambda$-vertex and $\Lambda$-complete

Formal definition:

图中的顶点 $u$ 称为 $\Lambda$-vertex，当且仅当 $u$ 邻接两个彼此不相邻的顶点。设 $Y$ 是 $G\circ H$ 的诱导子图，$p_G(Y)$ 是 $Y$ 在第一因子 $G$ 上的投影。若对 $p_G(Y)$ 中每个 $\Lambda$-vertex $g$ 都有

$$
{}^gH\cap Y={}^gH,
$$

即对应的整个 $H$-layer 都包含在 $Y$ 中，则称 $Y$ 是 $\Lambda$-complete。

Plain-language explanation:

如果投影中的某个点 $g$ 位于一个三点诱导路径的中间，那么 $Y$ 不能只取 $g$ 对应那一层的一部分；它必须把整份 $H$ 都收进来。

Tiny example:

令 $G=P_3=a-b-c$、$H=K_2$。因为 $b$ 同时邻接互不相邻的 $a,c$，所以 $b$ 是 $\Lambda$-vertex。若 $p_G(Y)$ 包含 $a,b,c$，则 $Y$ 要成为 $\Lambda$-complete，必须包含 $b$ 对应的整个 $K_2$-layer。

Source:

Anand et al. (2012) 预印本 PDF p. 3 of 9，Section 2、Theorem 2.1 之前的定义；没有独立 Definition 编号。

Important pitfalls:

- $\Lambda$-complete 不表示 $Y$ 本身是完全图；它是一个“某些层必须完整包含”的条件。
- 定理中检查的是投影 $p_G(Y)$ 里的 $\Lambda$-vertices。
- 该术语是理解 Anand et al. Theorem 2.1 的必要条件之一，不能省略。

## Prerequisites I need to learn

- **必须掌握**：顶点、边、相邻、路径、路径长度、连通图、诱导子图。
- **必须掌握**：最短路径、graph distance、geodesic，以及“可能有多条最短路径”。
- **必须掌握**：集合、补集、基数、最大值，以及“对任意/存在”这两个量词的区别。
- **必须掌握**：general position set、convex set、dual general position set 和 $gp_d$ 的定义。
- **必须掌握**：lexicographic product 的顶点与相邻规则，特别是两个因子的顺序不能随意交换。
- **只需知道概念**：完全图 $K_m$、树、叶子、simplicial vertex（单纯顶点）、universal vertex（全邻接顶点）。
- **只需知道概念**：图同构；理解“两个不同写法描述的是同一个结构”即可。
- **只需知道概念**：lexicographic product 的 layer、projection、$\Lambda$-vertex 与 $\Lambda$-complete。
- **暂时可以跳过**：strong resolving graph、MMD、TF-boundary 的技术细节；它们主要服务于论文的 outer general position 部分。
- **暂时可以跳过**：strong product 的一般理论；目前只需知道论文曾用一个特定同构证明 Theorem 5.8(ii)。
