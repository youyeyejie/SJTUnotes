# Chapter 3. Primitive roots and discrete logarithm

- [Back to Course Home](index.md)

## Order

- **Thm 3.1 Euler's Theorem**: Let $m\geq 2$, then $\forall a\in \mathbb{Z}$ with $\gcd(a,m)=1$, we have $a^{\varphi(m)}\equiv 1 \pmod m$.

	???+ info "Proof"

		- Since $\gcd(a,m)=1$, then $\bar{a}\in \mathbb{Z}_m^*$, $\forall \bar{b}\in \mathbb{Z}_m^*$, we claim that $\overline{ab}\in \mathbb{Z}_m^*$:

			- Since $\gcd(a,m)=1$ and $\gcd(b,m)=1$, thus $\gcd(ab,m)=1$, so $\overline{ab}\in \mathbb{Z}_m^*$.

		- Label all elements of $\mathbb{Z}_m^*$ as $\bar{a}_1,\bar{a}_2,\cdots,\bar{a}_{\varphi(m)}$, consider $\mathbb{Z}'=\{\bar{a}\bar{a}_1,\bar{a}\bar{a}_2,\cdots,\bar{a}\bar{a}_{\varphi(m)}\}\subseteq \mathbb{Z}_m^*$, we claim that $\mathbb{Z}'=\mathbb{Z}_m^*$

			- Since $\bar{a}\bar{a}_i=\bar{a}\bar{a}_j$ implies $\bar{a}_i=\bar{a}_j$, thus $\bar{a}\bar{a}_i\neq \bar{a}\bar{a}_j$ for $1\leq i<j\leq \varphi(m)$, so $\mathbb{Z}'$ has $\varphi(m)$ distinct elements, thus $\mathbb{Z}'=\mathbb{Z}_m^*$.

		- So, $\prod_{i=1}^{\varphi(m)} \bar{a}_i=\prod_{i=1}^{\varphi(m)} \bar{a}\bar{a}_i=\bar{a}^{\varphi(m)}\prod_{i=1}^{\varphi(m)} \bar{a}_i$, thus $\bar{a}^{\varphi(m)}=\bar{1}$, i.e. $a^{\varphi(m)}\equiv 1 \pmod m$.

- **Thm 3.2 Little Fermat's Theorem**: If $p\in \mathbb{P}$, then $\forall a\in \mathbb{Z}$,

	$$
	a^p\equiv a \pmod p
	$$

	???+ info "Proof"

		- **Case 1**: $p\mid a$, then $a^p\equiv 0 \equiv a \pmod p$.

		- **Case 2**: $p\nmid a$, then $\gcd(a,p)=1$ and $a\in \mathbb{Z}_p^*$, by Thm 3.1, $a^{\varphi(p)}=a^{p-1}\equiv 1 \pmod p$, thus $a^p\equiv a \pmod p$.

- **Def 3.3 Order**: Let $m\geq 2$, $\bar{a}\in \mathbb{Z}_m^*$, the order of $\bar{a}$ is defined to be the least positive integer $k$ satisfying

	$$
	a^k\equiv 1 \pmod m
	$$

	- **Notation**: Denote the order of $\bar{a}$ by $\mathrm{ord}_m(\bar{a})$.

	???+ info "Proof"

		- **Existence**: Since $\mathbb{Z}_m^*$ is finite, there exist $i,j$ with $0\leq i<j\leq \varphi(m)$ such that $\bar{a}^i=\bar{a}^j$, thus $\bar{a}^{j-i}=\bar{1}$, so there exists a positive integer $k$ such that $\bar{a}^k=\bar{1}$.

		- **Uniqueness**: Let $S=\{k\in \mathbb{Z}^+: a^k\equiv 1 \pmod m\}$, thus $S$ contains positive integer. By WOP, there exists a least positive integer $k_0\in S$, thus $\mathrm{ord}_m(\bar{a})=k_0$.

- **Thm 3.4 Properties of order**: Let $m\geq 2$, $\bar{a}\in \mathbb{Z}_m^*$, then

	1. $a^l\equiv 1 \pmod m \iff \mathrm{ord}_m(a)\mid l$.

		- In particular, $\mathrm{ord}_m(a)\mid \varphi(m)$.

	2. $\mathrm{ord}_m(a)=k \implies\mathrm{ord}_m(a^l)=\frac{k}{\gcd(k,l)}$.

	3. $\gcd(\mathrm{ord}_m(a),\mathrm{ord}_m(b))=1 \implies \mathrm{ord}_m(ab)=\mathrm{ord}_m(a)\cdot \mathrm{ord}_m(b)$.

	???+ info "Proof"

		1. Let $k=\mathrm{ord}_m(a)$

			- $\implies$: Write $l=kq+r$ with $0\leq r<k$, thus $1\equiv a^l=a^{kq+r}=(a^k)^qa^r\equiv a^r \pmod m$, thus $r=0$, so $k\mid l$.

			- $\impliedby$: Let $l=kq$, then $a^l=(a^k)^q\equiv 1 \pmod m$.

		2. Proof of 2

			- Consider $(a^l)^\frac{k}{\gcd(k,l)}=(a^k)^\frac{l}{\gcd(k,l)}\equiv 1 \pmod m$, thus $\mathrm{ord}_m(a^l)\mid \frac{k}{\gcd(k,l)}$.

			- Let $r=\mathrm{ord}_m(a^l)$, then $(a^{l})^r\equiv 1 \pmod m$, thus $k\mid lr$. Since $\frac{k}{\gcd(k,l)} \mid \frac{l}{\gcd(k,l)}r$ and $\gcd(\frac{k}{\gcd(k,l)}, \frac{l}{\gcd(k,l)})=1$, we have $\frac{k}{\gcd(k,l)}\mid r = \mathrm{ord}_m(a^l)$.

			- So $\mathrm{ord}_m(a^l)=\frac{k}{\gcd(k,l)}$.

		3. Let $u=\mathrm{ord}_m(a)$, $v=\mathrm{ord}_m(b)$, $w=\mathrm{ord}_m(ab)$

			- Since $(ab)^{uv}=(a^u)^v(b^v)^u\equiv 1 \pmod m$, thus $w\mid uv$.

			- Since $(ab)^w\equiv 1 \pmod m$, thus $1\equiv ((ab)^{wu}=(a^u)^w(b^w)^u\equiv b^{wu} \pmod m$, thus $v\mid wu$, so $v\mid w$ since $\gcd(u,v)=1$. Similarly, $u\mid w$, so $uv\mid w$.

			- So $\mathrm{ord}_m(ab) = w = uv = \mathrm{ord}_m(a)\cdot \mathrm{ord}_m(b)$.

## Primitive root

- **Def 3.5 Primitive root**: Let $m\geq 2$, $g$ is called a primitive root modulo $m$ if

    $$
    \mathrm{ord}_m(g)=\varphi(m)
    $$

    I.e. $g$ is a generator of the multiplicative cyclic group $\mathbb{Z}_m^*$.

- **Thm 3.6**: Let $g$ be a primitive root modulo $m$, then

	1. $\mathbb{Z}_m^*=\langle\bar{g}\rangle=\{\bar{1},\bar{g},\bar{g}^2,\cdots,\bar{g}^{\varphi(m)-1}\}$ is a cyclic group.

	2. There are $\varphi(\varphi(m))$ primitive roots modulo $m$, and they are $\{g^l: 1\leq l\leq \varphi(m), \gcd(\varphi(m),l)=1\}$.

	???+ info "Proof"

		1. Obviously, $\{\bar{1},\bar{g},\bar{g}^2,\cdots,\bar{g}^{\varphi(m)-1}\}\subseteq \mathbb{Z}_m^*$. we claim that $\{\bar{1},\bar{g},\bar{g}^2,\cdots,\bar{g}^{\varphi(m)-1}\}$ has $\varphi(m)$ distinct elements, thus $\{\bar{1},\bar{g},\bar{g}^2,\cdots,\bar{g}^{\varphi(m)-1}\}=\mathbb{Z}_m^*$.

			- If $\bar{g}^i=\bar{g}^j$ with $0\leq i<j\leq \varphi(m)-1$, then $\bar{g}^{j-i}=\bar{1}$, thus $\mathrm{ord}_m(g)\mid j-i$, so $\varphi(m)\mid j-i$, which is impossible since $0<j-i<\varphi(m)$.

		2. $g^l$ is a primitive root modulo $m \iff \mathrm{ord}_m(g^l)=\frac{\varphi(m)}{\gcd(\varphi(m),l)}=\varphi(m) \iff \gcd(\varphi(m),l)=1$, thus all primitive roots modulo $m$ are $\{g^l: 1\leq l\leq \varphi(m), \gcd(\varphi(m),l)=1\}$, and the total number of them is $\varphi(\varphi(m))$.

- **Thm 3.7**: If $p\in \mathbb{P}$, then there exists primitive root modulo $p$.

	- **Recap**: A field $F$ is a commutative ring with identity in which every nonzero element is invertible.

		- Fact 1: $\mathbb{Z}_p$ is a field.

		- Fact 2: A polynomial of degree $n$ over a field $F$ has at most $n$ roots in $F$.

	- **Goal**: Find a $g\in \mathbb{Z}_p^*$ s.t. $\mathrm{ord}_p(g)=p-1$.

	???+ info "Proof"

		- Let $\varphi(p)=p-1$ has canonical factorization

		    $$
		    p-1=\prod_{i=1}^k p_i^{e_i}
		    $$

		    with $e_i\geq 1$ and $p_i\in \mathbb{P}$ are pairwise distinct. So the **sub-goal** is to find $g_i\in \mathbb{Z}_p^*$ s.t. $\mathrm{ord}_p(g_i)=p_i^{e_i}$ for $1\leq i\leq k$, then $g=\prod_{i=1}^k g_i$ is a primitive root modulo $p$ since $\gcd(p_i^{e_i},p_j^{e_j})=1$ for $1\leq i<j\leq k$.

		- Consider the equation

		    $$
		    x^{p-1} -1\equiv 0 \pmod p
		    $$

		    which has $\varphi(p)=p-1$ roots and all roots are $\mathbb{Z}_p^*$.

		- Since $x^{p-1}-1=(x^{p_i^{e_i}})^{\frac{p-1}{p_i^{e_i}}}-1=(x^{p_i^{e_i}}-1)\cdot(\cdots)$, thus $x^{p_i^{e_i}}-1$ is a factor of $x^{p-1}-1$, and there are $p_i^{e_i}$ roots in $\mathbb{Z}_p^*$.

		- Consider $x^{p_i^{e_i-1}}-1$ has at most $p_i^{e_i-1}$ roots, thus $\exists g_i\in \mathbb{Z}_p^*$ satisfying $g_i$ is a root of $x^{p_i^{e_i}}-1$ but not a root of $x^{p_i^{e_i-1}}-1$, we claim that $\mathrm{ord}_p(g_i)=p_i^{e_i}$.

			- Since $g_i$ is a root of $x^{p_i^{e_i}}-1$, thus $\mathrm{ord}_p(g_i)\mid p_i^{e_i}$.

			- Since $g_i$ is not a root of $x^{p_i^{e_i-1}}-1$, suppose $\mathrm{ord}_p(g_i)=p_i^r$ with $r\leq e_i-1$, then $g_i^{p_i^{e_i-1}}=(g_i^{p_i^r})^{p_i^{e_i-1-r}}\equiv 1 \pmod p$, thus $g_i$ is a root of $x^{p_i^{e_i-1}}-1$, which is a contradiction, so $r=e_i$, i.e. $\mathrm{ord}_p(g_i)=p_i^{e_i}$.

		- Thus, $\mathrm{ord}_p(g)=\mathrm{ord}_p(\prod_{i=1}^k g_i)=\prod_{i=1}^k \mathrm{ord}_p(g_i)=\prod_{i=1}^k p_i^{e_i}=p-1$, so $g$ is a primitive root modulo $p$.

	???+ info "Proof method 2"

		$\forall d\mid p-1$, let $\pi(d) = \{\bar{a}\in \mathbb{Z}_p^*: \mathrm{ord}_p(a)=d\}$, we claim that $\pi(p-1)$ is not empty by showing that $\pi(d)$ has $\varphi(d)$ elements.

		- Due to the definition of $\pi(d)$, we have $\bigcup_{d\mid p-1} \pi(d)=\mathbb{Z}_p^*$, and $\pi(d_1)\cap \pi(d_2)=\emptyset$ for $d_1\neq d_2$ with $d_1,d_2\mid p-1$. So $\sum_{d\mid p-1} |\pi(d)| = |\mathbb{Z}_p^*| = p-1$

		- Claim that $\sum_{d\mid p-1} \varphi(d) = p-1$:

			- Consider the set $S=\{\frac{1}{n}, \frac{2}{n}, \cdots, \frac{n}{n}\}$, obviously $|S|=n$ and every element in $S$ can be written as $\frac{a}{d}$ with $d\mid n$ and $\gcd(a,d)=1$.

			- Thus, we can partition $S$ into $\bigcup_{d\mid n} S_d$ where $S_d=\{\frac{a}{d}: 1\leq a\leq d, \gcd(a,d)=1\}$, so $|S_d|=\varphi(d)$, thus $\sum_{d\mid n} \varphi(d) = |S|=n$.

		- Claim that $|\pi(d)| = \varphi(d)$ for all $d\mid p-1$:

			- If $\pi(d) = \emptyset$, then $|\pi(d)| = 0 \le \varphi(d)$, done.

			- If $\pi(d) \neq \emptyset$, then $\exists a \in \pi(d)$ s.t. $\mathrm{ord}_p(a) = d$. Consider the set $S = \{1, a, a^2, \dots, a^{d-1}\}$:

				- Since $\mathrm{ord}_p(a) = d$, the elements in $S$ are distinct modulo $p$.

				- Since $a^d \equiv 1 \pmod p$, each element in $S$ is a root of $x^d - 1 \equiv 0 \pmod p$. And by Fact 2, $x^d - 1$ has at most $d$ roots in $\mathbb{Z}_p$. Thus $S$ is exactly the set of all roots of $x^d - 1 \equiv 0 \pmod p$.

				- Since $\forall x \in \pi(d)$, $x$ is a root of $x^d - 1 \equiv 0 \pmod p$, so $\pi(d)\subseteq S$.

				- Due to Thm 3.4(2), $\mathrm{ord}_p(a^k) = \frac{d}{\gcd(k, d)}$, thus $a^k \in \pi(d) \implies \mathrm{ord}_p(a^k) = d \iff \gcd(k, d) = 1$.

				- Thus, $|\pi(d)| = \varphi(d)$.

			- Since $\sum_{d\mid p-1} |\pi(d)| = \sum_{d\mid p-1} \varphi(d) = p-1$ and $\forall d\mid p-1, |\pi(d)| \le \varphi(d)$, we have $|\pi(d)| = \varphi(d)$ for all $d\mid p-1$.

		- In particular, $|\pi(p-1)| = \varphi(p-1) > 0$, so there exists a primitive root modulo $p$.

- **Algorithm 3.8**: Find all primitive roots modulo $p$ for odd prime $p\in \mathbb{P}$.

	1. Factor $\varphi(p)=p-1$ into its prime factorization $\prod_{i=1}^k p_i^{e_i}$.

	2. **Find a primitive root**: 

		- For each $1\leq i\leq k$, find $g_i\in \mathbb{Z}_p^*$ s.t. $\mathrm{ord}_p(g_i)=p_i^{e_i}$. Let $g=\prod_{i=1}^k g_i$, then $g$ is a primitive root modulo $p$.

			- i.e. Find $g_i$ s.t. $g_i^{p_i^{e_i}}\equiv 1 \pmod p$ and $\forall 0\leq r\leq p_i^{e_i-1}-1, g_i^r\not\equiv 1 \pmod p$.

		- Or search $2\leq a\leq p-1$ until find $a$ s.t. $\forall 1\leq i\leq k, a^{\frac{p-1}{p_i}}\not\equiv 1 \pmod p$, then $a$ is a primitive root modulo $p$.

	3. **Find all primitive roots**:

		- For each $1\leq l\leq \varphi(p)$ with $\gcd(\varphi(p),l)=1$, $g^l$ is a primitive root modulo $p$.

		- Thus, all $\varphi(\varphi(p))$ primitive roots modulo $p$ are $G = \{g^l: 1\leq l\leq \varphi(p), \gcd(\varphi(p),l)=1\} = \{g^l \in \mathbb{Z}_p^* \mid l \in \mathbb{Z}_{p-1}^*\}$.

	???+ abstract "Table of primitive roots"

		| $p$ | Primitive roots modulo $p$ |
		| --- | --- |
		| 2 | 1 |
		| 3 | 2 |
		| 5 | 2, 3 |
		| 7 | 3, 5 |
		| 11 | 2, 6, 7, 8 |
		| 13 | 2, 6, 7, 11 |
		| 17 | 3, 5, 6, 7, 10, 11, 12, 14 |
		| 19 | 2, 3, 10, 13, 14, 15, 16, 17 |

- **Thm 3.9**: There exists primitive root modulo $p^k$ for **odd** prime $p$ and $k\geq 1$, and there exists primitive root modulo $2^k$ for $k=1,2$.

	???+ info "Proof"

		Let $g$ be a primitive root modulo $p$, then $\mathrm{ord}_p(g)=\varphi(p)=p-1$.

		- For $k=1$, show in Thm 3.7, done.

		- For $k=2$:

			- If $\mathrm{ord}_{p^2}(g)=\varphi(p^2)=p(p-1)$, done.

			- If $\mathrm{ord}_{p^2}(g)<\varphi(p^2)$

				- Claim that $\mathrm{ord}_{p}(g) \mid \mathrm{ord}_{p^2}(g) \mid \varphi(p^2)$, so $p-1 \mid \mathrm{ord}_{p^2}(g) \mid p(p-1) \implies \mathrm{ord}_{p^2}(g)=p-1$:

					- Due to Thm 3.4(1), $\mathrm{ord}_{p^2}(g)\mid \varphi(p^2)$.

					- Since $g^{\mathrm{ord}_{p^2}(g)}\equiv 1 \pmod{p^2} \implies g^{\mathrm{ord}_{p^2}(g)}\equiv 1 \pmod p$, thus $\mathrm{ord}_p(g)\mid \mathrm{ord}_{p^2}(g)$.

				- Consider $g+p$, we claim that $\mathrm{ord}_{p^2}(g+p)=p(p-1)$:

					- Since $g+p\equiv g \pmod p$, thus $\mathrm{ord}_p(g+p)=\mathrm{ord}_p(g)=p-1$, thus similarly we have $p-1 \mid \mathrm{ord}_{p^2}(g+p) \mid p(p-1)$

					- Thus we claim that $\mathrm{ord}_{p^2}(g+p)=p(p-1)$ by $\mathrm{ord}_{p^2}(g+p) \neq p-1$:

						$$
						\begin{aligned} (g+p)^{p-1} &= \sum_{i=0}^{p-1} \binom{p-1}{i} g^i p^{p-1-i} \\ &\equiv g^{p-1} + p(p-1)g^{p-2} \pmod{p^2} \\ &\equiv 1 - p g^{p-2} \pmod{p^2} \\ &\not\equiv 1 \pmod{p^2} \end{aligned}
						$$

					- So $\mathrm{ord}_{p^2}(g+p)=p(p-1)$, thus $g+p$ is a primitive root modulo $p^2$.

				- Thus, $g_1=\begin{cases} g & \mathrm{ord}_{p^2}(g)=p(p-1) \\ g+p & \mathrm{ord}_{p^2}(g)=p-1 \end{cases}$ is a primitive root modulo $p^2$.

		- For $k\geq 3$, let $g_1$ be a primitive root modulo $p^2$, we claim that $g_1$ is a primitive root modulo $p^k$ for all $k\geq 3$:

			- Since $p(p-1) = \mathrm{ord}_{p^2}(g_1) \mid \mathrm{ord}_{p^k}(g_1) \mid \varphi(p^k)=p^{k-1}(p-1)$, thus $\mathrm{ord}_{p^k}(g_1)=p^t(p-1)$ for some $1\leq t\leq k-1$.

			- Suppose $t \leq k-2$, then $g_1^{p^{k-2}(p-1)}\equiv (g_1^{p^t(p-1)})^{p^{k-2-t}}\equiv 1 \pmod{p^k}$.

				- Since $g_1^{p-1} \equiv g^{p-1} \equiv 1 \pmod p$, thus $\exists a \in \mathbb{Z}$ s.t. $g_1^{p-1} = 1 + ap$ and $\gcd(a,p)=1$

					- If $\gcd(a,p)\neq 1$, then $p\mid a$, thus $g_1^{p-1} \equiv 1 \pmod{p^2}$, which is a contradiction since $\mathrm{ord}_{p^2}(g_1)=p(p-1)$.

				- Then we have: (Line 3 uses the fact that $p$ is **odd prime**, so for $i\geq 2$, $\binom{p^{k-2}}{i} (ap)^i \equiv 0 \pmod {p^k}$)

					$$
					\begin{aligned} g_1^{p^{k-2}(p-1)} &= (1 + ap)^{p^{k-2}} = \sum_{i=0}^{p^{k-2}} \binom{p^{k-2}}{i} (ap)^i \\ &= 1 + p^{k-2} ap + \binom{p^{k-2}}{2} (ap)^2 + \cdots \\ &\equiv 1 + ap^{k-1} \pmod{p^k} \\ &\not\equiv 1 \pmod{p^k} \end{aligned}
					$$

			- So causes a contradiction, thus $t=k-1$, so $\mathrm{ord}_{p^k}(g_1)=p^{k-1}(p-1)$, so $g_1$ is a primitive root modulo $p^k$ for all $k\geq 3$.

- **Thm 3.10**: There exists primitive root modulo $2\cdot p^k$ for **odd** prime $p$ and $k\geq 1$.

	???+ info "Proof"

		Let $g$ be a primitive root modulo $p^k$

		- **Case 1**: $g$ is odd, claim that $\mathrm{ord}_{2p^k}(g)=\varphi(2p^k)$:

			- Since $g^l\equiv 1 \pmod{2p^k} \implies g^l\equiv 1 \pmod{p^k}$, we have $\mathrm{ord}_{p^k}(g) \mid \mathrm{ord}_{2p^k}(g)$.

			- Since $\gcd(g,p^k)=1$ and $g$ is odd, we have $\gcd(g,2p^k)=1$, thus $\mathrm{ord}_{2p^k}(g)\mid \varphi(2p^k)$.

			- Since $\varphi(2p^k)=\varphi(2)\cdot \varphi(p^k)=\varphi(p^k) = \mathrm{ord}_{p^k}(g)$, thus $\mathrm{ord}_{2p^k}(g)=\varphi(2p^k)$, so $g$ is a primitive root modulo $2p^k$.

		- **Case 2**: $g$ is even, then $g+p^k$ is a primitive root modulo $p^k$ and is odd. By case 1, $\mathrm{ord}_{2p^k}(g+p^k)=\varphi(2p^k)$.

- **Thm 3.11**: For $m\geq 3$, there exists primitive root modulo $m \iff m$ is of the form $2,4,p^k,2p^k$ for odd prime $p$ and $k\geq 1$.

	???+ info "Proof"

		- $\implies$: Assume that $m$ has the standard factorization $m=\prod_{i=1}^r p_i^{e_i}$ with $e_i\geq 1$, then $\varphi(m) = \prod_{i=1}^r p_i^{e_i-1}(p_i-1)$. Let $g$ be a primitive root modulo $m$, then $\mathrm{ord}_m(g)=\varphi(m)$

			- Let $t = \mathrm{lcm}(\varphi(p_1^{e_1}), \varphi(p_2^{e_2}), \cdots, \varphi(p_r^{e_r}))$, thus $t\leq \varphi(m)$ and $\varphi(p_i^{e_i})\mid t$ for $1\leq i\leq r$, so we have

				$$
				\begin{aligned} &g^t = g^{k\cdot\varphi(p_i^{e_i})}\equiv 1 \pmod{p_i^{e_i}} \\ \implies &p_i^{e_i}\mid g^t-1 \\ \implies &m = \prod_{i=1}^r p_i^{e_i}\mid g^t-1 \\ \implies &g^t\equiv 1 \pmod m \\ \implies &\mathrm{ord}_m(g)\mid t \\ \implies &\varphi(m)\leq t \end{aligned}
				$$

			- So $\varphi(m)=t$, i.e. $\mathrm{lcm}(\varphi(p_1^{e_1}), \varphi(p_2^{e_2}), \cdots, \varphi(p_r^{e_r})) = \prod_{i=1}^r \varphi(p_i^{e_i})$, so $\gcd(\varphi(p_i^{e_i}), \varphi(p_j^{e_j}))=1$ for $1\leq i<j\leq r$, i.e. $\gcd(p_i^{e_i-1}(p_i-1), p_j^{e_j-1}(p_j-1))=1$. Thus $m=2^a p^b$ for some $a,b\geq 0$ and $p\in \mathbb{P}$ is odd.

				- **Case** 1: $b\geq 1$, then $\gcd(\varphi(2^a), \varphi(p^b))=\gcd(2^{a-1}, p^{b-1}(p-1))=1$, thus $a\leq 1$ since $2\mid p-1$, so $m=p^b$ or $2p^b$.

				- **Case** 2: $b=0$, $m=2^a$, $\mathrm{ord}_{m}(g)=\varphi(m)=2^{a-1}$, so $g^{2^{a-2}} \not\equiv 1 \pmod{2^a}$. Since $\gcd(g,2^a)=1$, thus $g$ is odd. Let $g=2k+1$ for some $k\in \mathbb{Z}$, claim that $a\leq 2$: Suppose $a\geq 3$, then:

					$$
					\begin{aligned} g^{2^{a-2}} &= (2k+1)^{2^{a-2}} = \sum_{i=0}^{2^{a-2}} \binom{2^{a-2}}{i} (2k)^i \\ &= 1 + 2^{a-1} k + \frac{2^{a-2} (2^{a-2}-1) (2k)^2}{2} + \frac{2^{a-2} (2^{a-2}-1) (2^{a-2}-2) (2k)^3}{6} + \cdots \\ &\equiv 1 + 2^{a-1} k + 2^{a-3} (2^{a-2}-1) (2k)^2 \pmod{2^a} \\ &= 1 + 2^{a-1}(k + k^2(2^{a-2}-1)) \pmod{2^a} \end{aligned}
					$$

					Since $a\geq 3$, we have $(k+ k^2(2^{a-2}-1)) = k^2\cdot 2^{a-2} - k(k-1)$ is even, thus $g^{2^{a-2}} \equiv 1 \pmod{2^a}$, which is a contradiction, so $a\leq 2$.

		- $\impliedby$:

			- $m=2$: $g=1$ is a primitive root modulo $2$.

			- $m=4$: $g=3$ is a primitive root modulo $4$.

			- $m=p^k$ for odd prime $p$ and $k\geq 1$: Show in Thm 3.9

			- $m=2p^k$ for odd prime $p$ and $k\geq 1$: Show in Thm 3.10

- **Algorithm 3.12**: Find all primitive roots modulo $n$.

	1. If $n$ is not of the form $2,4,p^k,2p^k$ for odd prime $p$ and $k\geq 1$, then there is no primitive root modulo $n$, done.

		- If $n=2$, $g=1$

		- If $n=4$, $g=3$

	2. Let $g$ be a primitive root modulo $p$ and $G = \{g^l \in \mathbb{Z}_p^* \mid l \in \mathbb{Z}_{p-1}^*\}$ be the set of all primitive roots modulo $p$.

		1. $G_1 = \{g+ap \mid g \in G, a \in \mathbb{Z}_p, ap \not\equiv g^p-g \pmod{p^2}\}$ is the set of all primitive roots modulo $p^2$.

		2. $G_2 = \{g+ap^2 \mid g \in G_1, a \in \mathbb{Z}_{p^{k-2}}\}$ is the set of all primitive roots modulo $p^k$ for $k\geq 3$.

		3. $G_3 = \{g \mid g \in G_2, 2\nmid g\} \cup \{g+p^k \mid g \in G_2, 2\mid g\}$ is the set of all primitive roots modulo $2p^k$.

	???+ info "Proof of 2"

		1. $G_1$ is the set of all primitive roots modulo $p^2$:

			- If $g_1$ is a primitive root modulo $p^2$, then $g_1$ is a primitive root modulo $p$, so $g_1 = g + ap$ for some $g \in G$ and $a \in \mathbb{Z}_p$.

				- If $g_1$ is not a primitive root modulo $p$, then $g_1^d\equiv 1 \pmod p$ for some $d\mid p-1$ with $d<p-1$, thus $(g_1^d)^p = (1+kp)^p \equiv 1 \pmod{p^2}$ with $dp < p(p-1)$, so $g_1$ is not a primitive root modulo $p^2$, which is a contradiction.

			- Suppose $g_1=g+ap$ is a primitive root modulo $p^2$, then we have

				$$
				\begin{aligned} g_1^{p-1} &= (g+ap)^{p-1} = \sum_{i=0}^{p-1} \binom{p-1}{i} g^i (ap)^{p-1-i} \\ &\equiv g^{p-1} + ap(p-1)g^{p-2} \pmod{p^2} \\ &\equiv g^{p-1} - ap g^{p-2} \pmod{p^2} \\ &\not\equiv 1 \pmod{p^2} \\ \end{aligned}
				$$

				Thus

				$$
				apg^{p-1} \not\equiv g^p-g \pmod{p^2}
				$$

				Since $g$ is a primitive root modulo $p$, thus $g^{p-1}\equiv 1 \pmod p$, so $apg^{p-1} \equiv ap(1+kp) \equiv ap \pmod{p^2}$, thus

				$$
				ap \not\equiv g^p-g \pmod{p^2} \iff a \not\equiv \frac{g^p-g}{p} \pmod p
				$$

				I.e. there is a unique $a$ not satisfying the condition, so there are $p-1$ choices for $a$ for each $g\in G$.

			- So $G_1$ has totally $(p-1)\varphi(\varphi(p))$ distinct elements, and they are all primitive roots modulo $p^2$.

				$$
				\begin{aligned} &g+ap\equiv g'+a'p \pmod{p^2}\\ \implies &g+ap\equiv g'+a'p \pmod p \\ \implies &g\equiv g' \pmod p \\ \implies &g=g' \\ \implies &ap\equiv a'p \pmod{p^2} \\ \implies &a\equiv a' \pmod p \\ \implies &a=a' \end{aligned}
				$$

			- Since $\varphi(\varphi(p^2))=(p-1)\varphi(\varphi(p))=(p-1)|G|=|G_1|$, $G_1$ is the set of all primitive roots modulo $p^2$.

		2. $G_2$ is the set of all primitive roots modulo $p^k$ for $k\geq 3$:

			- If $g_2$ is a primitive root modulo $p^k$, then $g_2$ is a primitive root modulo $p^2$, so $g_2 = g + ap^2$ for some $g \in G_1$ and $a \in \mathbb{Z}_{p^{k-2}}$.

			- Suppose $g_2=g+ap^2$ is a primitive root modulo $p^k$, then we have

				$$
				\begin{aligned} g_2^{p^{k-2}(p-1)} &= (g+ap^2)^{p^{k-2}(p-1)} \\ &= \sum_{i=0}^{p^{k-2}(p-1)} \binom{p^{k-2}(p-1)}{i} g^i (ap^2)^{p^{k-2}(p-1)-i} \\ &\equiv g^{p^{k-2}(p-1)} \pmod{p^k} \\ &\not\equiv 1 \pmod{p^k} \end{aligned}
				$$

				Since $g$ is a primitive root modulo $p^2$, we have $g^{p-1} \not\equiv 1 \pmod{p^2}$, so $g^{p^{k-2}(p-1)} \not\equiv 1 \pmod{p^k}$ for all $k\geq 3$, thus the formula above always holds.

			- So $G_2$ has totally $|\mathbb{Z}_{p^{k-2}}||G_1|$ distinct elements. Since $\varphi(\varphi(p^k))=p^{k-2}\varphi(\varphi(p^2))=|G_2|$, $G_2$ is the set of all primitive roots modulo $p^k$ for all $k\geq 3$.

		3. $G_3$ is the set of all primitive roots modulo $2p^k$:

			- Due to the proof of Thm 3.9, the primitive roots modulo $2p^k$ are of the form $g$ or $g+p^k$ for some $g \in G_2$.

			- Since $\varphi(\varphi(2p^k))=\varphi(\varphi(p^k))=|G_2|=|G_3|$, $G_3$ is the set of all primitive roots modulo $2p^k$.

- **Cor 3.13**: For odd prime $p$ and $\forall k \geq 2$

	1. $\mathrm{ord}_{p^k}(g)=\varphi(p^k) \implies \mathrm{ord}_{p^{k+1}}(g)=\varphi(p^{k+1})$.

	2. $\mathrm{ord}_{p^{k}}(g)=\varphi(p^{k}) \implies \mathrm{ord}_{p^{k-1}}(g)=\varphi(p^{k-1})$.

	???+ info "Proof"

		1. Since $\mathrm{ord}_{p^k}(g)=\varphi(p^k)$, thus $g^{\varphi(p^{k-1})}\not\equiv 1 \pmod{p^k}$ and $g^{\varphi(p^{k-1})}\equiv 1 \pmod{p^{k-1}}$, thus $g^{\varphi(p^{k-1})}=1+ap^{k-1}$ with $\gcd(a,p)=1$. Since $p^{k-1}(p-1) = \mathrm{ord}_{p^k}(g) \mid \mathrm{ord}_{p^{k+1}}(g) \mid \varphi(p^{k+1})=p^{k}(p-1)$, we have $\mathrm{ord}_{p^{k+1}}(g)=p^{k-1}(p-1)$ or $p^{k}(p-1)$. Since

			$$
			\begin{aligned} g^{p^{k-1}(p-1)} &= g^{\varphi(p^{k-1})p} \\ &= (1+ap^{k-1})^{p} \\ &\equiv 1 + ap^{k} \pmod{p^{k+1}} \\ &\not\equiv 1 \pmod{p^{k+1}} \end{aligned}
			$$

			So $\mathrm{ord}_{p^{k+1}}(g)\neq \varphi(p^{k})=p^{k-1}(p-1)$, thus $\mathrm{ord}_{p^{k+1}}(g)=\varphi(p^{k+1})$.

		2. Suppose $\mathrm{ord}_{p^{k-1}}(g)=d$, then $d\mid \varphi(p^{k-1})$ and $g^d\equiv 1 \pmod{p^{k-1}}$, thus $g^d=1+ap^{k-1}$ for some $a\in \mathbb{Z}$, then we have

			$$
			(g^d)^p = (1+ap^{k-1})^p \equiv 1 \pmod{p^{k}}
			$$

			So $\mathrm{ord}_{p^{k}}(g) \mid pd$, thus $\varphi(p^{k})\mid pd$, thus $\varphi(p^{k-1})\mid d$, so $\mathrm{ord}_{p^{k-1}}(g)=d=\varphi(p^{k-1})$.

## Discrete Logarithm

- **Def 3.14 Discrete Logarithm**: Let $g$ be a primitive root modulo $m$, then discrete logarithm of $a$ modulo $m$ with $\gcd(a,m)=1$ is defined to be an integer $x$ satisfying

	$$
	g^x \equiv a \pmod m
	$$

	Denoted by $x = \log_g a \pmod{\varphi(m)}$.

- **Thm 3.15 Properties of Discrete Logarithms**: Let $g$ be a primitive root modulo $m$, then for $\gcd(a,m)=1$ and $\gcd(b,m)=1$, we have

	1. $\log_g 1 \equiv 0 \pmod{\varphi(m)}$.

	2. $\log_g g \equiv 1 \pmod{\varphi(m)}$.

	3. $\log_g (ab) \equiv \log_g a + \log_g b \pmod{\varphi(m)}$.

	4. $\log_g a^n \equiv n \cdot \log_g a \pmod{\varphi(m)}$.

- **Thm 3.16**: Let $g$ be a primitive root modulo $m$, then $\log_g a \equiv \log_g b \pmod{\varphi(m)} \iff a \equiv b \pmod m$.

	???+ info "Proof"

		- $\implies$: Since $g^{\log_g a} \equiv a \pmod m$ and $g^{\log_g b} \equiv b \pmod m$, thus $a \equiv g^{\log_g a} \equiv g^{\log_g b} \equiv b \pmod m$.

		- $\impliedby$: Since $a \equiv b \pmod m$, thus $g^{\log_g a} \equiv g^{\log_g b} \pmod m$, thus $\mathrm{ord}_m(g)\mid (\log_g a - \log_g b)$, so $\log_g a \equiv \log_g b \pmod{\varphi(m)}$.

- **Thm 3.17**: Let $g$ be a primitive root modulo $m$, then the equation $x^b \equiv a \pmod m$ has a solution $\iff \gcd(b, \varphi(m)) \mid \log_g a$.

	???+ info "Proof"

		- $\impliedby$: Since $\gcd(b, \varphi(m)) \mid \log_g a$, thus $\exists u,v\in \mathbb{Z}$ s.t. $ub + v\varphi(m) = \log_g a$, thus $g^{ub} \equiv g^{ub + v\varphi(m)} \equiv g^{\log_g a} \equiv a \pmod m$, so $x=g^u$ is a solution to the equation.

		- $\implies$: Since $g$ is a primitive root modulo $m$, thus $x=g^k$ and $a=g^l$ for some $1\leq k,l \leq \varphi(m)$, thus the equation is equivalent to $g^{kb} \equiv g^l \pmod m$, thus $kb \equiv l \pmod{\varphi(m)}$, let $d=\gcd(b, \varphi(m))$, then $k \equiv \frac{l}{d} \cdot \left(\frac{b}{d}\right)^{-1} \pmod{\frac{\varphi(m)}{d}}$, this requires $\frac{l}{d} \in \mathbb{Z}$, so $d \mid l$, i.e. $\gcd(b, \varphi(m)) \mid \log_g a$.

		- Thus, the solution to the equation is $x = g^{\frac{l}{d} \cdot \left(\frac{b}{d}\right)^{-1} + t\cdot \frac{\varphi(m)}{d}}$ for $t=0,1,\cdots,d-1$.