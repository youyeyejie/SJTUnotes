# Ch4 零知识证明

- [Back to Course Home](index.md)

## 零知识证明的定义以及应用

### 零知识证明简介

- **零知识证明**（Zero Knowledge Proof, ZKP）：一种密码学两方协议，允许一个证明者 (Prover) 向一个验证者 (Verifier) 证明某个声明为真，而不泄露任何关于证明内容的额外信息。
- **语法定义**：
	- $x$：公开输入（statement / public input）
	- $w$：秘密输入（witness / secret input）
	- $R$：关系函数（relation function），输出 1 或 0
	- **证明目标**：“我知道 $w$ 使得 $R(x,w)=1$”
- **安全目标**：
	1. **完备性**（Completeness）：如果 Prover 和 Verifier 都诚实地遵循协议，那么 Verifier 最终会输出接受（$b=1$）。
	2. **可靠性/知识可靠性**（Soundness / Knowledge Soundness）：抵御恶意的 Prover。
		- **可靠性**（Soundness）：如果 Prover 使用了无效的秘密，那么 Verifier 能以极高的概率捕获并拒绝（$b=0$）。
		- **知识可靠性**（Knowledge Soundness）：如果 Verifier 接受了证明，那么 Prover 必定真正“知道”该 witness。形式化地，存在一个提取器（Extractor）可以利用 Prover 提取出 witness（允许比 Verifier 具有更高的计算能力）。
	3. **零知识性**（Zero Knowledge, ZK）：抵御恶意的 Verifier。
		- Verifier 除了确信声明为真外，学不到关于 Prover 秘密的任何额外信息。形式化地，零知识性通过证明存在一个模拟器（Simulator）来保证，该模拟器在不知道秘密的情况下也能生成与真实交互无法区分的证明转录 (transcript)。

### 非交互式零知识证明与 Fiat-Shamir 变换
#### 非交互式零知识证明（NIZK）

- **消除交互**：理想情况下，Prover 应该直接生成一个一次性的证明字符串 $\pi$。Verifier 收到后异步验证 $\pi$ 即可。这样的 $\pi$ 也可以被复用，并被潜在的多个验证者检验。
- **可信设置**的类型：
	1. 结构化参考字符串（Structured Reference String, SRS）：需要一个可信的第三方生成并分发 SRS，且该 SRS 可能包含一些秘密信息。
	2. 将哈希函数建模为随机预言机 (Random Oracle, RO)：不需要可信设置，但需要对哈希函数的安全性进行强假设。
	3. 或两者兼有。

#### Fiat-Shamir 变换 [FS87]

- **NIZK 构造范式**：通过局部哈希生成挑战，将交互式协议转为非交互式。
	- **Step 1**：构造一个“公开抛币（public-coin）”的交互式协议。
		- Verifier 不需要保密状态。
		- 满足诚实验证者零知识（Honest-Verifier ZK）。
	- **Step 2**：非交互式 Prover 和 Verifier 通过对截至目前的部分转录进行局部哈希来获得挑战（challenge）。
- **额外应用**（Bonus）：如果将消息 $m$ 也加入哈希函数的输入中，基于 FS 变换的 NIZK 可以直接转化为数字签名。
	- 代表算法：Schnorr / EdDSA, CRYSTALS-Dilithium, PLONK, Bulletproofs 等。
	- 很多现代 SNARKs 都是通过将多项式交互式预言机证明（Polynomial IOPs）结合 Fiat-Shamir 变换转化为 NIZK 的。

### 零知识证明的分类与评价指标

- **分类**
	- **通用零知识证明**（General-Purpose ZKP）：
		- **特点**：支持任意 NP 关系 $R$，关系通常使用算术电路（Arithmetic circuit）描述。

			$$
			R_C=\{(x,w): C(x,w)=1\}
			$$

			- 算术电路是有向无环图，内部节点为加法或乘法操作，定义了一个多元多项式及其求值方法。
		- **优点**：可以证明任意程序的正确执行；适合可验证计算和外包计算。
		- **缺点**：对于某些非线性计算（如椭圆曲线算术、比较、表查找等），电路规模会变得非常复杂。
	- **专用零知识证明 (Specialized ZKP)**：
		- **特点**：为特定类型的 NP 关系设计。

			$$
			\begin{aligned} R_{DL} &= \{(X, w): X = w \cdot G\} \\ R_{SIS} &= \{(x, w): x = A w \mod q, \|w\| \leq \beta\} \\ R_{Lookup} &= \{(x, w): w \text{ is a subset of } x\} \end{aligned}
			$$

		- **优点**：对于指定的特殊关系，证明和验证极为高效。适用于正确加密证明、分布式密钥生成、数字签名等。
		- **缺点**：若要支持复杂的声明，需要与通用 ZKP 进行小心谨慎的集成。
- **评价指标**：
	1. **证明大小**（Proof Size）：更小的证明节约存储和通信带宽。例如 Groth16 仅需 3 个群元素。
	2. **假设**（Assumptions）：为了最小化信任假设，应尽量避免使用 SRS；更好的替代方案是仅信任哈希函数（透明设置 Transparent setup，如 STARK, Bulletproofs）或使用可更新的 SRS（Updatable SRS）。
	3. **设置、证明与验证成本**：
		- **全局设置**（Universal Setup）：一次设置后，其输出的 SRS 可用于所有特定规模内的电路。
		- Verifier 耗时最好在电路规模 $|C|$ 上是亚线性的。
		- Prover 耗时最好在非线性门的数量上是线性的。
	4. **可扩展性**（Scalability）：高效证明庞大的 statement。
		- 证明聚合 (Proof Aggregation)
		- 增量可验证计算 (IVC / 递归 SNARK，如 Halo2, Nova)

### 实际应用场景

1. **匿名凭证**（Anonymous Credentials）：用户证明自己拥有发行方 (Issuer) 颁发的合法属性，但不泄露具体身份（如仅证明“年龄 $\geq 21$ 岁”）。
2. **可验证与外包计算**（Verifiable and Outsourced Computation）：确保云服务器正确无误地执行了计算，通过 ZKP 证明合规性。
3. **高效后量子数字签名**：例如 Dilithium，是一个基于后量子 LWE/SIS 困难问题的 NIZK 协议，具有与 DLOG 上的 Schnorr 签名相似的结构。
4. **区块链 Rollup 与隐私交易**：
	- **隐私**：加密隐藏交易细节，利用 ZKP 证明交易的正确性与合规性。
	- **效率**（L2 Rollup）：将大量交易打包在一起，仅提交一个聚合的 ZKP 证明到 L1，无需逐一校验。

## NARK 与 (zk)SNARK 简介
### NARK（Non-interactive ARgument of Knowledge）

- **公共算术电路** $\mathrm{C}(\mathbf{x}, \mathbf{w}) \to \mathbb{F}$
- 包含预处理过程的 NARK 由三个算法 $(S, P, V)$ 组成：
	- **预处理**（Setup）：$\mathrm{S}(C) \to (pp, vp)$，生成给 Prover 和 Verifier 的公开参数。
	- **证明**（Prover）：$\mathrm{P}(pp, \mathbf{x}, \mathbf{w}) \to$ 证明 $\pi$
	- **验证**（Verifier）：$\mathrm{V}(vp, \mathbf{x}, \pi) \to$ 接受或拒绝
	- **要求**：
		- 完备性（Completeness）
		- 自适应知识可靠性（Adaptively knowledge sound）
		- 可选具备零知识性（Zero knowledge）

### SNARK（Succinct NARK）

- SNARK 是一种强调简洁性（Succinctness）的 NARK：
	- **极短的证明**：$\text{len}(\pi)$ 在秘密输入长度 $|w|$ 上是亚线性的 (sublinear)。对于强简洁性，要求 $\text{len}(\pi) = O_\lambda(\log|C|)$。
	- **极快的验证**：$\text{time}(V)$ 在电路大小 $|C|$ 上是亚线性的。对于强简洁性，验证时间为 $O_\lambda(|\mathbf{x}|, \log|C|)$，这意味着 Verifier 甚至没有时间去完整读取整个电路 $C$。
	- **zk-SNARK** = 具备零知识性的 SNARK。
- 近期进展代表：Groth'16（依赖可信设置）、Plonk、Bulletproofs、STARK（透明设置且抗量子）

## SNARK 的构造

现代高效 SNARK （如 STARK）的通用构造框架为：

$$
\text{多项式承诺方案(PCS)} + \text{多项式交互式预言机证明(PIOP)} \xrightarrow{\text{Fiat-Shamir}} \text{SNARK}
$$

### 交互式预言机证明（IOP & PIOP）

- **IOP（Interactive Oracle Proof）**：在协议交互中，Prover 发送的多维字符串过大，无法全部传给 Verifier。因此，Prover 发送字符串的“预言机”，Verifier 随后只通过抛币产生短随机挑战，并**仅查询预言机的少量对应单元格**来决定接受与否。
	- 要求：完备性、可靠性，并满足**简洁性**（即 $\mathrm{V}$ 查询极少，验证时间亚线性）。
- **PIOP（Polynomial IOP）**：一种特殊 IOP。在每一轮中，Prover 响应该有限域上多项式 $f_i$ 的预言机；Verifier 可以在其选择的特定点上查询 $f_i$ 的少量求值。

### 多项式承诺方案（Polynomial Commitment Scheme, PCS）

- PCS 允许 Prover 对一个多项式 $f(X)$ 作出承诺，并在随后揭示其在某一点的求值。包含两个阶段：
	1. **承诺**（Commit）：首先承诺一个 $\deg(f) \leq d$ 的多项式 $f$，生成很短的 $\mathrm{com}_f$。
	2. **求值证明**（Eval/Open）：对于公开点 $u, v \in \mathbb{F}_p$，Prover 证明该被承诺的多项式满足 $f(u) = v$ 且 $\deg(f) \leq d$。生成证明 $\pi$。
		- **要求**：求值证明 $\pi$ 的大小和验证时间必须是 $O_\lambda(\log d)$。朴素的系数哈希法由于生成长度线性的证明而无法作为真正的 PCS。

#### Merkle 树承诺

- 使用哈希函数对长向量/字符串进行树状承诺。叶子节点为数据，逐层向上哈希直至根节点（Root）。
- 揭示某个数据点时，只需提供从该叶子到根节点的身份验证路径（Authentication path, 包含同层兄弟节点的哈希值），大小对数为 $O(\log n)$。

#### 基于 FRI 的多项式承诺方案（FRI-based PCS）

- **核心思想**：低次证明 + 单点求值。
	- 通过 Merkle 树对低次多项式 $g(x)$ 的求值表进行承诺。
	- 如果 $\deg(g) \leq k$ 且 $g(r)=v$，那么 $f(x) = \frac{g(x)-v}{x-r}$ 且 $\deg(f) \leq k-1$。
	- 则由 $g$ 的承诺可以衍生出 $f$ 的承诺，并通过单点求值证明 $f$ 的低次性。
- **FRI（Fast Reed-Solomon IOP of Proximity）**：一种针对线性码的交互式邻近度预言机证明。
	- **折叠操作**：给定承诺的 $f$，随机挑选 $\alpha$，计算 $\mathrm{Fold}(f, \alpha) = f_0(x^2) + \alpha f_1(x^2)$。此操作将多项式的度数和评估域规模均折半。
	- **递归递推**：通过多轮 Fold 操作，最后化简至一个常数。Verifier 在每一轮只需进行极少量的点校验（一致性检查）。
- **线性码的邻近度间隙**（Proximity gap for linear codes）：
	- FRI 每轮的可靠性依赖于编码理论。如果 $f$ 距离 RS 码字很远（$\delta$-far），那么在极高概率下，折叠后的 $\mathrm{Fold}(f, \alpha)$ 依然距离低次多项式很远。
	- 相关理论边界：Johnson bound 等。

### SNARK 构造范式

- FRI $\implies$ RS-IOPP $\implies$ PCS
- PIOP（将多项式预言机替换为多项式承诺与评估证明） $\implies$ 交互式证明 (IP)
- 交互式证明 $\xrightarrow{\text{Fiat-Shamir 变换}}$ 适用于通用电路的 (zk)SNARK