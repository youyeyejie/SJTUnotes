# Chapter 2. Congruences

- [Back to Course Home](index.md)

## Congruences

- **Def 2.1 Congruence**: Let $a,b\in \mathbb{Z}$ and $m\in \mathbb{Z}^+$, we say $a$ is congruent to $b$ modulo $m$ if

    $$
    m\mid (a-b)
    $$

    Denoted by $a\equiv b \pmod m$.

- **Thm 2.2 Properties of Congruences**: Let $a,b,c,d\in \mathbb{Z}$ and $m\in \mathbb{Z}^+$, then
	1. $a\equiv b \pmod m$ and $c\equiv d \pmod m \implies$
		- $a+c\equiv b+d \pmod m$
		- $a-c\equiv b-d \pmod m$
		- $ac\equiv bd \pmod m$
	2. $m>\gcd(m,c), ac\equiv bc \pmod m \implies a\equiv b \pmod{\frac{m}{\gcd(m,c)}}$

	???+ info "Proof"

		1. We only prove the last one. $\exists u,v\in \mathbb{Z}$ s.t. $a-b=um$ and $c-d=vm$, thus $ac-bd=ac-ad+ad-bd=a(c-d)+(a-b)d=avm+umd=m(av+ud)$, thus $ac\equiv bd \pmod m$.
		2. Let $d=\gcd(m,c)$, then $m\mid(a-b)c \implies \frac{m}{d}\mid (a-b)\frac{c}{d}$, since $\gcd(\frac{m}{d},\frac{c}{d})=1$, we have $\frac{m}{d}\mid a-b$, i.e. $a\equiv b \pmod{\frac{m}{\gcd(m,c)}}$.

## Residue Classes

- **Def 2.3 Residue Class**: Let $r\in \mathbb{Z}$ and $m\in \mathbb{Z}^+$, the residue class of $r$ modulo $m$ is defined to be

	$$
	\begin{aligned} {[r]}_{m} &=\{x\in \mathbb{Z}: x\equiv r \pmod m\} \\ &=\{r+im: i\in \mathbb{Z}\} \\ & = r+m\mathbb{Z} \end{aligned}
	$$

	If there is no confusion, we simply denote $[r]_m$ by $\bar{r}$ and even $r$.

- **Thm 2.4 Properties of Residue Classes**:
	1. $\forall r_1,r_2\in \mathbb{Z}$, we have $[r_1]_m=[r_2]_m$ or $[r_1]_m\cap [r_2]_m=\emptyset$.
	2. $\bigcup_{i=0}^{m-1} [i]_m=\mathbb{Z}$, i.e. $\{[0]_m,[1]_m,\cdots,[m-1]_m\}$ is a partition of $\mathbb{Z}$.

	???+ info "Proof"

		1. if $[r_1]_m\cap [r_2]_m\neq \emptyset$, choose $r\in [r_1]_m\cap [r_2]_m$, then $r\equiv r_1 \pmod m, r\equiv r_2 \pmod m$, thus $r_1\equiv r_2 \pmod m$. So $\forall x\in [r_1]_m$, we have $x\equiv r_1 \equiv r_2 \pmod m$, thus $x\in [r_2]_m$, i.e. $[r_1]_m\subseteq [r_2]_m$. Similarly, we can prove $[r_2]_m\subseteq [r_1]_m$, thus $[r_1]_m=[r_2]_m$.
		2. $\forall 0\leq i<j\leq m-1$, we have $i\neq j \pmod m$, thus $[i]_m\cap [j]_m=\emptyset$. Then $\forall x\in \mathbb{Z}$, by the division algorithm, $\exists q,r\in \mathbb{Z}$ s.t. $x=qm+r$ and $0\leq r<m$, thus $x\in [r]_m$, i.e. $\bigcup_{i=0}^{m-1} [i]_m=\mathbb{Z}$.

- **Def 2.5 Complete Residue System**: Let $r_1,r_2,\cdots,r_m\in \mathbb{Z}$ and $m\in \mathbb{Z}^+$, if
	1. $\forall i\neq j, [r_i]_m\cap [r_j]_m=\emptyset$
	2. $\bigcup_{i=1}^m [r_i]_m=\mathbb{Z}$

	then $\{[r_1]_m,\cdots,[r_m]_m\}$ is called a complete residue system modulo $m$, denoted by $\mathbb{Z}_m$.

	- In particular, $\{[0]_m,[1]_m,\cdots,[m-1]_m\}$ is called the canonical complete residue system modulo $m$.
	- If $[r_1]_m,\cdots,[r_m]_m$ is a complete residue system modulo $m$, then

		$$
		\begin{aligned} \mathbb{Z}_m &=\{[r_1]_m,\cdots,[r_m]_m\} \\ &=\{[0]_m,[1]_m,\cdots,[m-1]_m\} \\ &=\{\bar{0},\bar{1},\cdots,\overline{m-1}\} \\ &=\{0,1,\cdots,m-1\} \end{aligned}
		$$

- **Def 2.6 Addition and Multiplication**: Define addition $+$ and multiplication $\cdot$ on $\mathbb{Z}_m$ as follows: $\forall a,b\in \mathbb{Z}$,

	$$
	\begin{aligned} \bar{a}+\bar{b} &=\overline{a+b} \\ \bar{a}\cdot \bar{b} &=\overline{ab} \end{aligned}
	$$

	- **Claim**: $+$ and $\cdot$ defined above are well-defined, i.e. if $\bar{a}=\bar{a}_1$ and $\bar{b}=\bar{b}_1$, then $\overline{a+b}=\overline{a_1+b_1}$ and $\overline{ab}=\overline{a_1b_1}$.

		???+ info "Proof"

			Since $\bar{a}=\bar{a}_1$ and $\bar{b}=\bar{b}_1$, we have $a\equiv a_1 \pmod m, b\equiv b_1 \pmod m$, thus $\exists u,v\in \mathbb{Z}$ s.t. $a-a_1=um$ and $b-b_1=vm$, thus $(a+b)-(a_1+b_1)=(a-a_1)+(b-b_1)=um+vm=(u+v)m$, thus $\overline{a+b}=\overline{a_1+b_1}$. Similarly, we can prove $\overline{ab}=\overline{a_1b_1}$.

	- **Conclusion**: $\mathbb{Z}_m$ is a commutative ring with zero element $\bar{0}$ and multiplicative identity element $\bar{1}$.
- **Def 2.7 Invertible Element**: An element $\bar{r}\in \mathbb{Z}_m$ is called invertible if there exists $\bar{r}'\in \mathbb{Z}_m$ s.t.

    $$
    \bar{r}\cdot \bar{r}'=\bar{1}
    $$

    In this case we call $\bar{r}'$ the inverse of $\bar{r}$, denoted by $\bar{r}^{-1}$.

	- Every element $\bar{r}\in \mathbb{Z}_m$ have the additive inverse $-\bar{r}=\overline{-r}$ since $\bar{r}+(-\bar{r})=\overline{r+(-r)}=\bar{0}$, but not every element $\bar{r}\in \mathbb{Z}_m$ have the multiplicative inverse.
- **Thm 2.8**: Let $r\in \mathbb{Z}$ and $m\in \mathbb{Z}^+$, then $\bar{r}\in \mathbb{Z}_m$ is multiplicative invertible $\iff \gcd(r,m)=1$. In this case, the inverse is unique, denoted by $\bar{r}^{-1}$.

	???+ info "Proof"

		1. $\implies$: Since $\bar{r}$ is invertible, there exists $\bar{r}'\in \mathbb{Z}_m$ s.t. $\bar{r}\cdot \bar{r}'=\bar{1}$, thus $\overline{rr'}=\bar{1}$, thus $rr'\equiv 1 \pmod m$, thus $\exists u\in \mathbb{Z}$ s.t. $rr'-1=um$, thus $rr'-um=1$, thus $\gcd(r,m)\mid 1$, thus $\gcd(r,m)=1$.
		2. $\impliedby$: Since $\gcd(r,m)=1$, by Bézout's identity, $\exists u,v\in \mathbb{Z}$ s.t. $ur+vm=1$, thus $ur\equiv 1 \pmod m$, thus $\overline{ur}=\bar{1}$, thus $\overline{u}\cdot \bar{r}=\bar{1}$, thus $\bar{r}$ is invertible and $\bar{r}^{-1}=\overline{u}$.
			- **Uniqueness**: If $\bar{r}\cdot \bar{u}_1=\bar{1}$ and $\bar{r}\cdot \bar{u}_2=\bar{1}$, then $u_1 r\equiv 1 \equiv u_2 r \pmod m$, thus $(u_1-u_2)r\equiv 0 \pmod m$, thus $m\mid (u_1-u_2)r$. Due to $\gcd(r,m)=1$, we have $m\mid u_1-u_2$, thus $\bar{u}_1=\bar{u}_2$.

## Euler Function and Chinese Remainder Theorem

- **Def 2.9 Euler Function**: For $m\in \mathbb{Z}^+$, the Euler function $\varphi(m)$ is defined to be the cardinality of invertible elements of the set

    $$
    \mathbb{Z}_m^* = \{\bar{r}\in \mathbb{Z}_m: \gcd(r,m)=1\}
    $$

    i.e. $\varphi(m)=|\mathbb{Z}_m^*|$.

	- Remark: $\mathbb{Z}_m^*$ forms a multiplicative group with identity element $\bar{1}$.
	- Example: $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$.
- **Thm 2.10 Chinese Remainder Theorem**: Let $m_1,m_2,\cdots,m_r\in \mathbb{Z}^+$ be pairwise coprime integers $\geq 2$, (i.e. $\forall i\neq j, \gcd(m_i,m_j)=1$), then $\forall a_1,a_2,\cdots,a_r\in \mathbb{Z}$, the system of congruences

	$$
	\begin{cases} x\equiv a_1 \pmod {m_1} \\ x\equiv a_2 \pmod {m_2} \\ \cdots \\ x\equiv a_r \pmod {m_r} \end{cases}
	$$

	has a unique solution modulo $M=\prod_{i=1}^r m_i$, and the solution $x=\sum_{i=1}^r a_i M_i y_i$, where $M_i=\frac{M}{m_i}$ and $y_i$ is the inverse of $M_i$ in $\mathbb{Z}_{m_i}$.

	???+ info "Proof"

		- **Uniqueness**: If $x_1$ and $x_2$ are two solutions, then $\forall 1\leq i\leq r, x_1\equiv a_i \equiv x_2 \pmod {m_i}$, thus $x_1\equiv x_2 \pmod {m_i}$, since $\gcd(m_i,m_j)=1$ for $i\neq j$, we have $x_1\equiv x_2 \pmod M$.
		- **Existence**: Let $M_i=\frac{M}{m_i}$, so $\gcd(M_i,m_i)=1$, by Thm 2.8, there exists $y_i\in \mathbb{Z}$ s.t. $\overline{M_i}\cdot \overline{y_i}=\bar{1}$ in $\mathbb{Z}_{m_i}$, thus $M_i y_i\equiv 1 \pmod {m_i}$ and $\forall j\neq i, M_i y_i\equiv 0 \pmod {m_j}$. Let $x=\sum_{i=1}^r a_i M_i y_i$, then $\forall 1\leq i\leq r, x\equiv a_i M_i y_i \equiv a_i \cdot 1 \equiv a_i \pmod {m_i}$, thus $x$ is a solution.

- **Thm 2.11 Properties of Euler Function**: Let $m,n\in \mathbb{Z}^+$, then
	1. $m,n\geq 2, \gcd(m,n)=1 \implies \varphi(mn)=\varphi(m)\varphi(n)$
	2. $\forall n\geq 2$, if $n=\prod_{i=1}^k p_i^{r_i}$ with $r_i\in \mathbb{Z}^+$ and $p_i$ are distinct primes, then 

		$$
		\varphi(n)=\prod_{i=1}^k p_i^{r_i-1}(p_i-1)=n\prod_{p\mid n}(1-\frac{1}{p})
		$$

	???+ info "Proof"

		1. Claim that $|\mathbb{Z}_{mn}^*|=|\mathbb{Z}_m^*||\mathbb{Z}_n^*|$. Consider the map

			$$
			\begin{aligned} \pi: \mathbb{Z}_{mn}^* &\to \mathbb{Z}_m^* \times \mathbb{Z}_n^* \\ [r]_{mn} &\mapsto ([r]_m, [r]_n) \end{aligned}
			$$

			- $\pi$ is well-defined: $[r_1]_{mn}=[r_2]_{mn} \iff mn\mid (r_1-r_2) \iff m\mid (r_1-r_2)$ and $n\mid (r_1-r_2) \iff [r_1]_m=[r_2]_m$ and $[r_1]_n=[r_2]_n$.
			- $\pi$ is injective: $\forall ([r_1]_m, [r_2]_n)\in \mathbb{Z}_m^* \times \mathbb{Z}_n^*$, by the Chinese Remainder Theorem, then $\exists r\in \mathbb{Z}$ s.t. $r\equiv r_1 \pmod m$ and $r\equiv r_2 \pmod n$, thus $\pi([r]_{mn})=([r]_m, [r]_n)=([r_1]_m, [r_2]_n)$.

			So, $\pi$ is a bijection, thus $|\mathbb{Z}_{mn}^*|=|\mathbb{Z}_m^*||\mathbb{Z}_n^*|$, i.e. $\varphi(mn)=\varphi(m)\varphi(n)$.

		2. First consider $n=p^r$ where $p$ is a prime and $r\in \mathbb{Z}^+$, consider

			$$
			\mathbb{Z}_n \backslash \mathbb{Z}_n^* =\{\overline{0},\overline{1p},\overline{2p},\cdots,\overline{(p^{r-1}-1)p}\}
			$$

			then $|\mathbb{Z}_n \backslash \mathbb{Z}_n^*|=p^{r-1}$, thus

			$$
			\varphi(n)=|\mathbb{Z}_n^*|=|\mathbb{Z}_n|-|\mathbb{Z}_n \backslash \mathbb{Z}_n^*|=p^r-p^{r-1}=p^r(1-\frac{1}{p})
			$$

			For general $n$, let $p_1,p_2,\cdots,p_k$ be the distinct prime divisors of $n$, then $n=\prod_{i=1}^k p_i^{r_i}$, thus

			$$
			\varphi(n)=\prod_{i=1}^k \varphi(p_i^{r_i})=\prod_{i=1}^k p_i^{r_i}(1-\frac{1}{p_i})=n\prod_{p\mid n}(1-\frac{1}{p})
			$$

- **Cor 2.12**:
	- Let $p$ be a prime and $r\in \mathbb{Z}^+$, then $\varphi(p^r)=p^r-p^{r-1}$.
	- $\varphi(n)=n-1 \iff n$ is a prime.

		???+ info "Proof"

			- If $n$ is a prime, then $\varphi(n)=n-1$.
			- If $n$ is not a prime, then $\exists 1<p<n$ s.t. $p\mid n$, thus $\gcd(p,n)=p\neq 1$, thus $\bar{p}\not\in \mathbb{Z}_n^*$, thus $\mathbb{Z}_n^* \subseteq \mathbb{Z}_n\backslash \{\bar{0},\bar{p}\}$, thus $\varphi(n)=|\mathbb{Z}_n^*| \leq |\mathbb{Z}_n\backslash \{\bar{0},\bar{p}\}|=n-2<n-1$.

	- Set $\varphi(1)=1$, then $\forall n\geq 1, \sum_{d\mid n} \varphi(d)=n$.

		???+ info "Proof"

			Let $n=\prod_{i=1}^k p_i^{e_i}$ be the canonical factorization, consider

			$$
			\begin{aligned} \sum_{d\mid n} \varphi(d) &=\sum_{0\leq k_i\leq e_i} \varphi(p_1^{k_1}\cdots p_t^{k_t}) \\ &=\sum_{0\leq k_i\leq e_i} \varphi(p_1^{k_1})\cdots \varphi(p_t^{k_t}) \\ &=\prod_{i=1}^k \sum_{0\leq k_i\leq e_i} \varphi(p_i^{k_i}) \\ &=\prod_{i=1}^k\left(\varphi(p_i^0)+\sum_{1\leq k_i\leq e_i} \varphi(p_i^{k_i})\right) \\ &=\prod_{i=1}^k\left(1+\sum_{1\leq k_i\leq e_i} p_i^{k_i}-p_i^{k_i-1}\right) \\ &=\prod_{i=1}^k p_i^{e_i} \\ &=n \end{aligned}
			$$

