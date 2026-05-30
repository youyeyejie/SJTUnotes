# Chapter 5. Polynomials

- [Back to Course Home](index.md)

???+ abstract "Recap of Ring and Field"

	- A **ring** is a set $R$ equipped with $+$ and $\cdot$ operations such that $(R, +)$ is an abelian group, $(R, \cdot)$ is a semigroup, and $\cdot$ distributes over $+$.
	- A **field** is a commutative ring with identity in which every non-zero element is a unit, i.e. every non-zero element has a multiplicative inverse. In particular, a field is an integral domain.
		- $\mathbb{Q}$: the field of rational numbers.
		- $\mathbb{R}$: the field of real numbers.
		- $\mathbb{C}$: the field of complex numbers.
		- $\mathbb{Z}_p$: the field of integers modulo a prime $p$.

## Polynomials

- **Def 5.1 Polynomial**: A polynomial over a field $F$ has the form

	$$
	f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0,\quad a_i \in F
	$$

	- If $a_n \neq 0$, then $n$ is called the **degree** of $f(x)$ and is denoted $\deg(f)$, and $a_n$ is called the **leading coefficient** of $f(x)$. If $a_n=1$, then $f$ is called **monic**. (首一的)
	- An element $a \in F$ is called a **constant polynomial**. The degree of the zero polynomial is defined to be $-\infty$, others degree is defined to be $0$, i.e.

		$$
		\deg(a) = \begin{cases} 0 & a \neq 0 \\ -\infty & a = 0 \end{cases}
		$$

- **Def 5.2 Addition and Multiplication**: Let $f(x)=a_0 + a_1 x + \cdots + a_n x^n$ and $g(x)=b_0 + b_1 x + \cdots + b_m x^m$ be two polynomials.
	- The **sum** of $f(x)$ and $g(x)$ is defined as

		$$
		(f + g)(x) = f(x) + g(x) = \sum_{i=0}^{\max(n, m)} (a_i + b_i) x^i
		$$

	- The **product** of $f(x)$ and $g(x)$ is defined as

		$$
		(f \cdot g)(x) = f(x) \cdot g(x) = c_0 + c_1 x + \cdots + c_{n+m} x^{n+m}
		$$

- **Thm 5.3 Properties of Degree**: Let $f(x), g(x)$ be two polynomials. Then
	1. $\deg(f + g) \leq \max(\deg(f), \deg(g))$.
	2. $\deg(f \cdot g) = \deg(f) + \deg(g)$.
	3. $\deg(a \cdot f) = \deg(f)$ if $a \in F \setminus \{0\}$.
- **Def 5.4 Polynomial Ring**: The polynomial ring over field $F$ is defined as

	$$
	F[x] = \left\{\sum_{i=0}^n a_i x^i : n \geq 0, a_i \in F\right\}
	$$

	Indeed $(F[x], +, \cdot)$ forms a commutative ring with additive identity $0$ and multiplicative identity $1$. Furthermore, $F[x]$ is an integral domain.

- **Thm 5.5**: The unit group of $F[x]$ is $F^* = F \setminus \{0\}$.
	- **Notation**: The unit group of a ring $R$ is the set of all invertible elements in $R$, denoted by $R^*$.

	???+ info "Proof"

		- Let $f\in F[x]$ be a unit. Then $\exists g \in F[x]$ s.t. $f \cdot g = 1$. By Thm 5.3, $\deg(f) + \deg(g) = \deg(f\cdot g) = \deg(1) = 0$. Thus $\deg(f) = \deg(g) = 0$, which means $f, g \in F^*$.
		- Conversely, if $f \in F^*$, then $f^{-1} \in F^*$ and $f \cdot f^{-1} = 1$.

## Divisibility
### Divisibility

- **Def 5.6 Divisibility**: A polynomial $f$ is divisible by a polynomial $g$ if

	$$
	\exists h \in F[x] \text{ s.t. } f = g \cdot h
	$$

	Then we say $g$ divides $f$, denoted $g \mid f$.

- **Thm 5.7 Property of Divisibility**: Let $f, g, h, u, v \in F[x]$.
	1. $g\mid f \implies \forall h\in F[x]\setminus\{0\},  gh \mid fh$
	2. $g\mid f, f\mid h \implies g\mid h$
	3. $g\mid f, f\mid g \implies f = a g$ for some $a \in F^*$
	4. $f\mid u, f\mid v \implies \forall a, b \in F[x], f\mid (au + bv)$
- **Axiom 5.8**: Let $S\subseteq\mathbb{Z}^+ \cup \{0, -\infty\}$
	1. If $S\neq \emptyset$, $S$ contains the smallest number (including $-\infty$).
	2. If $S$ contains a non-negative integer, then $S$ contains the smallest non-negative integer.
	3. If $S$ contains a positive integer, then $S$ contains the smallest positive integer.
- **Thm 5.9**: Let $f, g \in F[x]$ with $g \neq 0$. Then there exist unique pair of polynomials $q, r \in F[x]$ satisfying

	$$
	f = q \cdot g + r, \quad \deg(r) < \deg(g)
	$$

	???+ info "Proof"

		- **Uniqueness**: Assume taht $(q_1, r_1), (q_2, r_2)$ are two pairs of polynomials satisfying $\begin{cases} f = q_1 \cdot g + r_1 \\ f = q_2 \cdot g + r_2 \end{cases}$. Then $(q_1 - q_2) \cdot g = r_2 - r_1$, so we have

			$$
			\begin{aligned} &\deg((q_1 - q_2) \cdot g) = \deg(q_1 - q_2) + \deg(g) \\ &\deg(r_2 - r_1) \leq \max\{\deg(r_1), \deg(r_2)\} < \deg(g) \end{aligned}
			$$

			Then $\deg(q_1 - q_2) < 0 \implies \deg(q_1 - q_2) = -\infty \implies q_1 = q_2 \implies r_1 = r_2$. Thus the two pairs are the same.

		- **Existence**: Consider the set $S = \{\deg(f - h \cdot g) : h \in F[x]\}$, thus $S\neq\emptyset$. By Axiom 5.8, $S$ contains the smallest number $t$ (including $-\infty$), thus $\exists q \in F[x]$ s.t. $\deg(f - q \cdot g) = t$. Let $r = f - q \cdot g$, thus $\deg(r) = t$. Claim that $\deg(r) < \deg(g)$:
			- Suppose $\deg(r) \geq \deg(g)$, then write

				$$
				\begin{aligned} r(x) &= r_n x^n + r_{n-1} x^{n-1} + \cdots + r_0 \quad (r_n \neq 0) \\ g(x) &= g_m x^m + g_{m-1} x^{m-1} + \cdots + g_0 \quad (g_m \neq 0) \end{aligned}
				$$

				Let $u(x) = r(x) - r_n g_m^{-1} x^{n-m} g(x)$, then $\deg(u) \leq n-1 < n = \deg(r) = t$, thus $r(x) = u(x) + r_n g_m^{-1} x^{n-m} g(x) = f(x) - q(x) \cdot g(x)$, thus $u(x) = f(x) - (q(x) + r_n g_m^{-1} x^{n-m}) \cdot g(x)$, which means $\deg(u) \in S$ and $\deg(u) < t$, contradicting the definition of $t$.

### Greatest Common Divisor

- **Def 5.10 GCD**: Let $f, g \in F[x]$ and $(f,g)\neq (0,0)$, then a greatest common divisor (GCD) of $f$ and $g$ is defined to be the monic polynomial $d$ satisfying
	1. $d \mid f, d \mid g$.
	2. $d_1 \mid f, d_1 \mid g \implies d_1 \mid d$.
- **Thm 5.11**: The GCD of $f, g$ exists and is unique, denoted by $\gcd(f,g)$.

	???+ info "Proof"

		- **Uniqueness**: Assume that $d_1, d_2$ are two GCDs of $f, g$. Then $d_1 \mid d_2$ and $d_2 \mid d_1$, thus $\exists a,b \in F[x]$ s.t. $d_1 = a d_2$ and $d_2 = b d_1$, thus $d_1 = a b d_1 \implies d_1 (1 - a b) = 0 \implies ab = 1 \implies a, b \in F^*$. So $a=b=1$, thus $d_1 = d_2$.
		- **Existence**: Consider the set $S = \{\deg(uf + vg) : u, v \in F[x], (u,v) \neq (0,0)\}$, thus $S\neq\emptyset$. By Axiom 5.8, $S$ contains the smallest non-negative integer $t$, thus $\exists a, b \in F[x]$ s.t. $\deg(af + bg) = t$. Let $d = af + bg$, thus $\deg(d) = t$. WLOG, we assume that $d$ is monic, otherwise we can divide it by its leading coefficient. Claim that $d=\gcd(f,g)$:
			- Let $f=q\cdot d + r$ with $\deg(r) < \deg(d)$, then

				$$
				\begin{aligned} r &= f - q \cdot d \\ &= f - q \cdot (af + bg) \\ &= (1 - qa)f + (-qb)g \end{aligned}
				$$

				Thus $\deg(r) \in S \implies \deg(r) = -\infty \implies r=0 \implies d \mid f$. Similarly, $d \mid g$.

			- If $d_1 \mid f, d_1 \mid g$, then $d_1 \mid (af + bg)$, i.e. $d_1 \mid d$.

- **Def 5.12 Coprime**: Two polynomials $f, g \in F[x]$ are said to be coprime if $\gcd(f,g) = 1$.
- **Cor 5.13 Bézout's Identity**: Let $f, g \in F[x]$ with $(f,g) \neq (0,0)$, then $\exists u, v \in F[x]$ s.t. $uf + vg = \gcd(f,g)$.
- **Thm 5.14 Properties of GCD**: Let $f, g, h, f_i \in F[x]$, then
	1. $a(x)$ is monic $\implies \gcd(af, ag) = a \cdot \gcd(f,g)$
	2. $\gcd\left(\frac{f}{\gcd(f,g)}, \frac{g}{\gcd(f,g)}\right) = 1$
	3. $\gcd(f_i,g)=1, i=1,2,\cdots,t \implies \gcd\left(\prod_{i=1}^t f_i, g\right)=1$
	4. $h\mid fg,~\gcd(h,g)=1 \implies h\mid f$
	5. $\forall r\in F[x], \gcd(f,g)=\gcd(f, g+rf)$

### Euclidean Algorithm

- **Thm 5.15 Euclidean Algorithm**: Give $f, g \in F[x]$ with $g \neq 0$, let $r_0=f, r_1=g$, we can compute $r_2, r_3, \cdots$ by long division:

	$$
	\begin{cases} r_0 = q_1 \cdot r_1 + r_2, & 0 \leq \deg(r_2) < \deg(r_1) \\ r_1 = q_2 \cdot r_2 + r_3, & 0 \leq \deg(r_3) < \deg(r_2) \\ \cdots \\ r_{n-2} = q_{n-1} \cdot r_{n-1} + r_n, & 0 \leq \deg(r_n) < \deg(r_{n-1}) \\ r_{n-1} = q_n \cdot r_n, & \deg(r_{n+1}) = -\infty \text{ (i.e. } r_{n+1} = 0\text{)} \end{cases}
	$$

- **Thm 5.16**: By the Euclidean Algorithm given above, $\gcd(r_i, r_{i+1}) = \gcd(r_{i+1}, r_{i+2})$ for $i=0,1,\cdots,n-2$.
	- In particular, $\gcd(f,g) = u^{-1} r_n$, where $u$ is the leading coefficient of $r_n$.
- **Thm 5.17 Extended Euclidean Algorithm**: Given $f, g \in F[x]$ with $g \neq 0$, let $r_0=f, r_1=g, s_0=1, s_1=0, t_0=0, t_1=1$, we can compute $r_2, r_3, \cdots$ by long division, and compute $s_i,t_i$ by

	$$
	\begin{cases} s_{i+1}=s_{i-1}-q_is_i \\ t_{i+1}=t_{i-1}-q_it_i \end{cases}
	$$

- **Thm 5.17**: By the Extended Euclidean Algorithm given above, $r_i=f s_i+g t_i$ for $i=0,1,\cdots,n$.
	- In particular, $\gcd(f,g) = u^{-1} r_n= u^{-1} (f s_n + g t_n)$, where $u$ is the leading coefficient of $r_n$.

### Least Common Multiple

- **Def 5.18 LCM**: Let $f, g \in F[x]$ with $(f,g) \neq (0,0)$, then a least common multiple (LCM) of $f$ and $g$ is defined to be the monic polynomial $D$ satisfying
	1. $f \mid D, g \mid D$.
	2. $\forall D' \in F[x], f \mid D', g \mid D' \implies D \mid D'$.
- **Thm 5.19**: The LCM of $f, g$ exists and is unique, denoted by $\mathrm{lcm}(f,g)$.

	???+ info "Proof"

		- **Uniqueness**: Assume that $D_1, D_2$ are two LCMs of $f, g$. Then $D_1 \mid D_2$ and $D_2 \mid D_1$, thus $\exists a,b \in F[x]$ s.t. $D_1 = a D_2$ and $D_2 = b D_1$, thus $D_1 = a b D_1 \implies D_1 (1 - a b) = 0 \implies ab = 1 \implies a, b \in F^*$. So $a=b=1$, thus $D_1 = D_2$.
		- **Existence**: Consider the set $S = \{\deg(u): f \mid u, g \mid u\}$, thus $fg \in S$, so $S\neq\emptyset$. By Axiom 5.8, $S$ contains the smallest non-negative integer $t$, thus $\exists D \in F[x]$ s.t. $\deg(D) = t$ and $f \mid D, g \mid D$. WLOG, we assume that $D$ is monic, otherwise we can divide it by its leading coefficient. Claim that $D=\mathrm{lcm}(f,g)$:
			- If $D' \in F[x]$ satisfies $f \mid D', g \mid D'$, then $\deg(D') \in S$, thus $\deg(D') \geq t = \deg(D)$, let $D' = q \cdot D + r$ with $\deg(r) < \deg(D)$, then $r = D' - q \cdot D$, thus $f \mid r, g \mid r$, thus $\deg(r) \in S$, thus $\deg(r) = -\infty$, thus $r=0$, thus $D \mid D'$.

- **Thm 5.20 Properties of LCM**: Let $f, g, h, f_i \in F[x]$, then
	1. $a(x)$ is monic $\implies \mathrm{lcm}(af, ag) = a \cdot \mathrm{lcm}(f,g)$
	2. $\gcd(f,g)=1$ and $f,g$ are monic $\implies \mathrm{lcm}(f,g) = f \cdot g$
	3. $f,g$ are monic $\implies \gcd(f,g) \cdot \mathrm{lcm}(f,g) = f \cdot g$

		???+ info "Proof of 3"

			- Let $d = \gcd(f,g)$, then $\gcd\left(\frac{f}{d}, \frac{g}{d}\right) = 1$, thus we have:

				$$
				\frac{\mathrm{lcm}(f,g)}{d} = \mathrm{lcm}\left(\frac{f}{d}, \frac{g}{d}\right) = \frac{f}{d} \cdot \frac{g}{d}
				$$

			- Thus $\gcd(f,g) \cdot \mathrm{lcm}(f,g) = d \cdot d \cdot \mathrm{lcm}\left(\frac{f}{d}, \frac{g}{d}\right) = f \cdot g$.

### Irreducible Polynomials

- **Def 5.21 Irreducible Polynomial**: A non-constant polynomial $f$ is called **irreducible** if $f$ is only divisible by $a$ or $af$ for some $a \in F^*$.
- **Thm 5.22**: $f$ is irreducible $\iff (f\mid ab \implies f\mid a \text{ or } f\mid b)$.

	???+ info "Proof"

		- $\implies$:
			- If $f\mid a$, done.
			- If $f\nmid a$, then $\gcd(f,a) = 1$, thus $f\mid b$, done.
		- $\impliedby$: Suppose $f$ were not irreducible, then $f=g\cdot h$ with $1\leq \deg(g), \deg(h) < \deg(f)$, thus $f\mid g\cdot h \implies f\mid g \text{ or } f\mid h$, thus $\deg(f) \leq \deg(g)$ or $\deg(f) \leq \deg(h)$, contradiction.

- **Lemma 5.23**: $\forall f \in F[x]$ with $\deg(f) \geq 1, \exists p \in F[x]$ s.t. $p\mid f$ and $p$ is irreducible.

	???+ info "Proof"

		- Consider the set $S = \{\deg(u): u\mid f, \deg(u) \geq 1\}$, thus $f \in S$, so $S\neq\emptyset$. By Axiom 5.8, $S$ contains the smallest positive integer $t$, thus $\exists p \in F[x]$ s.t. $\deg(p) = t$ and $p \mid f$. Claim that $p$ is irreducible: Assume that $q\mid p$, then $\deg(q) \leq \deg(p)$
			- If $q\in F^*$, then $p$ is irreducible.
			- If $q\notin F^*$, then $\deg(q) \geq 1$, thus $q\mid p, p\mid f \implies q\mid f$, thus $\deg(q) \in S$, thus $\deg(q) \geq t \implies \deg(q) = \deg(p)$. Let $p = q \cdot r$, then $\deg(r) = \deg(p) - \deg(q) = 0$, thus $r \in F^*$ and $q=r^{-1} p$, thus $p$ is irreducible.

- **Thm 5.24**: There are infinitely many monic irreducible polynomials in $F[x]$.
- **Thm 5.25**: Every non-zero polynomial $f$ can be uniquely factorized into a product of $a\in F^*$ and monic irreducible polynomials $p_i$, i.e.

	$$
	f(x) = a \cdot p_1(x) \cdot p_2(x) \cdots p_t(x)
	$$

	- **Notation**: Let $p$ be an irreducible polynomial, if $p^k \mid f$ and $p^{k+1} \nmid f$, then we denote $v_p(f) = k$ and call it the **exponent** of $p$ in $f$.
- **Thm 5.26**: Let $f, g \in F[x]$ be two non-zero polynomials, $p$ be monic irreducible polynomial, then
	1. $$
	    f = a \cdot \prod_{p} p^{v_p(f)}
	    $$

	1. $$
	    \gcd(f,g) = \prod_{p} p^{\min\{v_p(f), v_p(g)\}}
	    $$

	2. $$
	    \mathrm{lcm}(f,g) = \prod_{p} p^{\max\{v_p(f), v_p(g)\}}
	    $$

## Congruence
### Congruence and Residue Classes

- **Def 5.27 Congruence**: Let $m \in F[x]$ with $\deg(m) \geq 1$, then two polynomials $a,b \in F[x]$ are said to be congruent modulo $m$ if

	$$
	m(x) \mid a(x) - b(x)
	$$

	Denoted by $a(x)\equiv b(x) \pmod{m(x)}$.

- **Thm 5.28 Properties of Congruence**:
	1. $a\equiv b \pmod m$ and $c\equiv d \pmod m \implies$
		- $a+c\equiv b+d \pmod m$
		- $a-c\equiv b-d \pmod m$
		- $ac\equiv bd \pmod m$
	2. $m>\gcd(m,c), ac\equiv bc \pmod m \implies a\equiv b \pmod{\frac{m}{\gcd(m,c)}}$
- **Def 5.29 Residue Class**: Let $r,m\in F[x]$, the residue class of $r$ modulo $m$ is defined to be

	$$
	[r]_m = \{a \in F[x]: a \equiv r \pmod{m}\}
	$$

	If there is no confusion, we denote $[r]_m$ by $\bar{r}$ for simplicity.

- **Lemma 5.30**:
	1. $\forall r_1,r_2\in F[x]$, we have $[r_1]_m=[r_2]_m$ or $[r_1]_m\cap [r_2]_m=\emptyset$.
	2. $F[x] = \bigcup_{r\in F[x]} [r]_m = \overset{\centerdot}{\bigcup}_{\deg(r)<\deg(m)} [r]_m$.
		- **Notation**: $\overset{\centerdot}{\bigcup}$ means the union of disjoint sets.

		???+ info "Proof of 2"

			- For any $f \in F[x]$, let $f = q \cdot m + r$ with $\deg(r) < \deg(m)$, then $f \equiv r \pmod m$, thus $f \in [r]_m$, thus $F[x] \subseteq \bigcup_{\deg(r)<\deg(m)} [r]_m$. Since $\forall r, [r]_m \subseteq F[x]$, we have $\bigcup_{\deg(r)<\deg(m)} [r]_m \subseteq F[x]$. Thus $F[x] = \bigcup_{\deg(r)<\deg(m)} [r]_m$.
			- Let $r_1 \neq r_2$ with $\deg(r_1), \deg(r_2) < \deg(m)$. Thus $r_1 - r_2 \neq 0$ and $\deg(r_1 - r_2) < \deg(m)$, thus $m \nmid (r_1 - r_2)$, i.e. $r_1 \not\equiv r_2 \pmod m$. By Lemma 5.30(1), we have $[r_1]_m \cap [r_2]_m = \emptyset$, thus the union is disjoint.

- **Def 5.31 Complete Residue System**: $F[x]/(mF[x])$ is the set of all residue classes modulo $m$, i.e.

	$$
	F[x]/(mF[x]) = \{\bar{r}: \deg(r) < \deg(m)\} = \left\{\overline{\sum_{i=0}^{\deg(m)-1} a_i x^i} : a_i \in F\right\}
	$$

	If there is no confusion, we denote $F[x]/(mF[x])$ by $F[x]/(m)$ for simplicity.

	???+ note "Example"

		1. $m(x)=x$, then $\deg(m) = 1$, thus

			$$
			F[x]/(m) = F[x]/(x) = \{\bar{r}: \deg(r) < 1\} = \{\bar{a}: a \in F\} \cong F
			$$

		2. $m(x)=x^2+1$, then $\deg(m) = 2$, thus

			$$
			F[x]/(m) = \{\bar{r}: \deg(r) < 2\} = \{\overline{a + bx}: a,b \in F\} \cong F^2
			$$

- **Def 5.32 Addition and Multiplication**: Define addition $+$ and multiplication $\cdot$ on $F[x]/(m)$ by

	$$
	\begin{aligned} \bar{r}_1 + \bar{r}_2 &= \overline{r_1 + r_2} \\ \bar{r}_1 \cdot \bar{r}_2 &= \overline{r_1 \cdot r_2} \end{aligned}
	$$

- **Thm 5.33**: Under the above addition and multiplication, $F[x]/(m)$ forms a **commutative ring** with the additive identity $\bar{0}$ and the multiplicative identity $\bar{1}$.
- **Def 5.34 Invertible Element**: A polynomial $a\in F[x]$ is called invertible modulo $m$ if $\exists b\in F[x]$ s.t.

	$$
	a\cdot b \equiv 1 \pmod m
	$$

	I.e. $a$ is a **unit** in the commutative ring $F[x]/(m)$, and $b$ is called the inverse of $a$ modulo $m$, denoted by $a^{-1}$.

- **Thm 5.35 Properties of Invertible**: $a$ is invertible modulo $m \iff \gcd(a,m) = 1$.

	???+ info "Proof"

		- $\implies$: If $a$ is invertible modulo $m$, then $\exists b\in F[x]$ s.t. $a\cdot b \equiv 1 \pmod m$, thus $\exists u\in F[x]$ s.t. $a\cdot b - 1 = u \cdot m$, thus $a\cdot b - u \cdot m = 1$, thus $\gcd(a,m) = 1$.
		- $\impliedby$: By Bézout's Identity, $\exists u,v\in F[x]$ s.t. $a\cdot u + m \cdot v = 1$, thus $a\cdot u \equiv 1 \pmod m$, thus $a$ is invertible modulo $m$ and $u$ is the inverse of $a$ modulo $m$.

- **Def 5.36 Unit Group**: The unit group of the ring $F[x]/(m)$ is denoted by

	$$
	(F[x]/(m))^* = \{\bar{r} \in F[x]/(m) : \gcd(r,m) = 1\}
	$$

### Euler Function and Chinese Remainder Theorem

- **Def 5.37 Euler Function**: The Euler function $\Phi_p(m)$ is defined to be the number of invertible elements in the ring $\mathbb{Z}_p[x]/(m)$ with $\deg(m) \geq 1$, i.e.

	$$
	\Phi_p(m) = |(\mathbb{Z}_p[x]/(m))^*| = \#\{\bar{r} \in \mathbb{Z}_p[x]/(m) : \gcd(r,m) = 1\}
	$$

	- When $\deg(\alpha) = 0$, we define $\forall \alpha \in \mathbb{Z}_p^*, \Phi_p(\alpha) \triangleq 1$.

	???+ note "Example"

		1. To compute $\Phi_2(x)$, consider the ring

			$$
			\mathbb{Z}_2[x]/(x) = \{\bar{r}: \deg(r) < 1\} = \{\bar{a}: a \in \mathbb{Z}_2\} = \{\bar{0}, \bar{1}\}
			$$

			Thus

			$$
			(\mathbb{Z}_2[x]/(x))^* = \{\bar{1}\}
			$$

			Thus $\Phi_2(x) = 1$.

		2. To compute $\Phi_2(x^3)$, consider the ring

			$$
			\mathbb{Z}_2[x]/(x^3) = \{\bar{r}: \deg(r) < 3\} = \{\overline{a + bx + cx^2}: a,b,c \in \mathbb{Z}_2\}
			$$

			Thus

			$$
			\begin{aligned} (\mathbb{Z}_2[x]/(x^3))^* &= \{\bar{r} \in \mathbb{Z}_2[x]/(x^3) : \gcd(r,x^3) = 1\} \\ &= \{\overline{1 + bx + cx^2}: b,c \in \mathbb{Z}_2\} \end{aligned}
			$$

			Thus $\Phi_2(x^3) = 4$.

- **Thm 5.38 Chinese Remainder Theorem**: Let $m_1, m_2, \cdots, m_t$ be pairwise coprime polynomials in $F[x]$ with $\deg(m_i) \geq 1$, then $\forall a_1,a_2,\cdots,a_t\in F[x]$, the system of congruences

	$$
	\begin{cases} x\equiv a_1 \pmod {m_1} \\ x\equiv a_2 \pmod {m_2} \\ \cdots \\ x\equiv a_t \pmod {m_t} \end{cases}
	$$

	has a unique solution $x\in F[x]/(M)$ with $M=\prod_{i=1}^t m_i$.

- **Thm 5.39 Properties of Euler Function**: Let $m,n,d\in \mathbb{Z}_p[x]$
	1. If $\gcd(m,n) = 1$, then

		$$
		\Phi_p(mn) = \Phi_p(m) \cdot \Phi_p(n)
		$$

	2. If $q(x)$ is an irreducible polynomial, then

		$$
		\begin{aligned} \Phi_p(q^n) &= p^{(n-1)\deg(q)} (p^{\deg(q)} - 1) \\ &= p^{n\deg(q)} \left(1 - \frac{1}{p^{\deg(q)}}\right) \end{aligned}
		$$

		- In particular, $q$ irreducible $\implies \Phi_p(q) = p^{\deg(q)} - 1$.
	3. For any polynomial $m$, we have

		$$
		\Phi_p(m) = p^{\deg(m)} \prod_{q\mid m, \atop q \text{ monic irreducible}} \left(1 - \frac{1}{p^{\deg(q)}}\right)
		$$

		- In prticular, $\deg(m) = 1 \implies \Phi_p(m) = p - 1$.

	???+ info "Proof"

		1. If $m\in \mathbb{Z}_p^*$, then $\Phi_p(mn) = \Phi_p(n) = \Phi_p(m) \cdot \Phi_p(n)$ since $\Phi_p(m) = 1$. So we just need to consider the case when $\deg(m) \geq 1$ and $\deg(n) \geq 1$:
			- Since $\begin{cases}\Phi_p(mn) = |(\mathbb{Z}_p[x]/(mn))^*| \\ \Phi_p(m)\Phi_p(n) = |(\mathbb{Z}_p[x]/(m))^* \times (\mathbb{Z}_p[x]/(n))^*| \end{cases}$, it is sufficient to show that there is a bijection between $(\mathbb{Z}_p[x]/(mn))^*$ and $(\mathbb{Z}_p[x]/(m))^* \times (\mathbb{Z}_p[x]/(n))^*$. 
			- Consider the map:

				$$
				\begin{aligned} \varphi: (\mathbb{Z}_p[x]/(mn))^* &\to (\mathbb{Z}_p[x]/(m))^* \times (\mathbb{Z}_p[x]/(n))^* \\ [r]_{mn} &\mapsto ([r]_m, [r]_n) \end{aligned}
				$$

				It is easy to prove that $\varphi$ is well-defined and is a ring isomorphism, thus $\varphi$ is a bijection, thus $\Phi_p(mn) = \Phi_p(m) \cdot \Phi_p(n)$.

		2. Consider the set

			$$
			\begin{aligned} S &= (\mathbb{Z}_p[x]/(q^n)) \backslash (\mathbb{Z}_p[x]/(q^n))^* = \{\bar{r} \in \mathbb{Z}_p[x]/(q^n) : \gcd(r,q^n) \neq 1\} \\ &= \{\overline{uq}: u \in \mathbb{Z}_p[x]\} \\ &= \{\overline{uq}: \deg(uq) < \deg(q^n)\} \\ &= \{\overline{uq}: \deg(u) < (n-1)\deg(q)\} \\ &= \{\overline{\sum_{i=0}^{(n-1)\deg(q)-1} u_i x^i q}: u_i \in \mathbb{Z}_p\} \end{aligned}
			$$

			Thus $|S| = p^{(n-1)\deg(q)}$, thus

			$$
			\begin{aligned} \Phi_p(q^n) &= |\mathbb{Z}_p[x]/(q^n)| - |S| \\ &= p^{n\deg(q)} - p^{(n-1)\deg(q)} \\ &= p^{n\deg(q)} \left(1 - \frac{1}{p^{\deg(q)}}\right) \end{aligned}
			$$

		3. Let $m = \alpha \cdot \prod_{i=1}^t q_i^{e_i}$ be the standard factorization of $m$, $\alpha \in \mathbb{Z}_p^*$ is the leading coefficient of $m$, $q_i$ are monic irreducible polynomials, then

			$$
			\begin{aligned} \Phi_p(m) &= \prod_{i=1}^t \Phi_p(q_i^{e_i}) \\ &= \prod_{i=1}^t p^{e_i \deg(q_i)} \left(1 - \frac{1}{p^{\deg(q_i)}}\right) \\ &= p^{\deg(m)} \prod_{i=1}^t \left(1 - \frac{1}{p^{\deg(q_i)}}\right) \\ \end{aligned}
			$$

- **Thm 5.40**:

    $$
    \sum_{d\mid m, \atop d \text{ monic}} \Phi_p(d) = p^{\deg(m)}
    $$

	???+ info "Proof"

		- Let $m = \alpha \cdot \prod_{i=1}^t q_i^{e_i}$ be the standard factorization of $m$, $\alpha \in \mathbb{Z}_p^*$ is the leading coefficient of $m$, $q_i$ are monic irreducible polynomials, then $d = \prod_{i=1}^t q_i^{k_i}, 0 \leq k_i \leq e_i$ is a monic divisor of $m$, thus

			$$
			\begin{aligned} \sum_{d\mid m, \atop d \text{ monic}} \Phi_p(d) &= \sum_{0\leq k_i \leq e_i} \Phi_p\left(\prod_{i=1}^t q_i^{k_i}\right) \\ &= \sum_{0\leq k_i \leq e_i} \prod_{i=1}^t \Phi_p(q_i^{k_i}) \\ &= \prod_{i=1}^t \left(\sum_{k_i=0}^{e_i} \Phi_p(q_i^{k_i})\right) \\ &= \prod_{i=1}^t \left(\sum_{k_i=0}^{e_i} \left(p^{k_i \deg(q_i)} - p^{(k_i-1) \deg(q_i)}\right)\right) \\ &= \prod_{i=1}^t \left(p^{e_i \deg(q_i)}\right) \\ &= p^{\deg(m)} \end{aligned}
			$$

## Primitive Elements

- **Thm 5.41**: $\gcd(a,m) = 1 \implies a^{\Phi_p(m)} \equiv 1 \pmod m$

	???+ info "Proof"

		- Let $l = \Phi_p(m)$, then we can label the elements of $(\mathbb{Z}_p[x]/(m))^*$ by $\{\bar{r}_1, \bar{r}_2, \cdots, \bar{r}_l\}$ with $\bar{r}_1 = \bar{a}$. Consider the set $S = \{\bar{a} \cdot \bar{r}_1, \bar{a} \cdot \bar{r}_2, \cdots, \bar{a} \cdot \bar{r}_l\}$, then $S = (\mathbb{Z}_p[x]/(m))^*$, thus $\prod_{i=1}^l \bar{r}_i = \prod_{i=1}^l (\bar{a} \cdot \bar{r}_i) = \bar{a}^l \cdot \prod_{i=1}^l \bar{r}_i$, thus $\bar{a}^l = 1$, thus $a^{\Phi_p(m)} \equiv 1 \pmod m$.

- **Def 5.42 Order**: Let $a\in F[x]$ be a non-zero polynomial with $\gcd(a,m) = 1$, the order of $a$ modulo $m$ is defined to be the smallest positive integer $k$ s.t.

	$$
	a^k \equiv 1 \pmod m
	$$

	Denoted by $\mathrm{ord}_m(a)$.

- **Thm 5.43 Properties of Order**:
	1. $a^l \equiv 1 \pmod m \implies \mathrm{ord}_m(a) \mid l$
	2. $\mathrm{ord}_m(a^t) = \frac{\mathrm{ord}_m(a)}{\gcd(\mathrm{ord}_m(a), t)}$
	3. $\gcd(\mathrm{ord}_m(a), \mathrm{ord}_m(b)) = 1 \implies \mathrm{ord}_m(ab) = \mathrm{ord}_m(a) \cdot \mathrm{ord}_m(b)$
- **Def 5.44 Primitive Element**: An element $g \in F[x]$ with $\gcd(g,m) = 1$ is called a primitive element modulo $m$ if

	$$
	\mathrm{ord}_m(g) = \Phi_p(m)
	$$

- **Thm 5.45**: Let $m \in \mathbb{Z}_p[x]$ with $\deg(m) \geq 1$, if there exists a primitive element modulo $m$, then there are exactly $\varphi(\Phi_p(m))$ primitive elements modulo $m$.

	???+ info "Proof"

		- Let $g$ be a primitive element modulo $m$, then $(\mathbb{Z}_p[x]/(m))^* = \{\bar{g}^0, \bar{g}^1, \cdots, \bar{g}^{\Phi_p(m)-1}\}$, thus $\bar{g}^k$ is a primitive element modulo $m \iff \mathrm{ord}_m(\bar{g}^k) = \frac{\Phi_p(m)}{\gcd(\Phi_p(m), k)} = \Phi_p(m) \iff \gcd(\Phi_p(m), k) = 1$, thus there are exactly $\varphi(\Phi_p(m))$ primitive elements modulo $m$.

- **Thm 5.46**: $\mathbb{Z}_p[x]/(q)$ is a field $\iff q$ is irreducible.

	???+ info "Proof"

		- $\impliedby$: Let $u\in \mathbb{Z}_p[x]/q$ with $u \neq 0$. and $\deg(u) < \deg(q)$, since $q$ is irreducible, we have $\gcd(u,q) = 1$, then by the Bézout's Identity, $\exists a,b\in \mathbb{Z}_p[x]$ s.t. $a\cdot u + b \cdot q = 1$, thus $a\cdot u \equiv 1 \pmod q$, thus $u$ is a unit in $\mathbb{Z}_p[x]/(q)$, thus $\mathbb{Z}_p[x]/(q)$ is a field.
		- $\implies$: Suppose not, thus $q$ is reducible, then $\exists u,v \in \mathbb{Z}_p[x]$ with $1 \leq \deg(u), \deg(v) < \deg(q)$ s.t. $u\cdot v = q$, thus $\bar{u} \cdot \bar{v} = \bar{0}$, thus $\bar{u}$ is a zero divisor in $\mathbb{Z}_p[x]/(q)$, thus $\mathbb{Z}_p[x]/(q)$ is not a field, contradiction.

- **Thm 5.47**: If $q\in \mathbb{Z}_p[x]$ is irreducible, then there exists a primitive element modulo $q$.

	???+ info "Proof structure"

		1. Factorize $\Phi_p(q) = p^{\deg(q)} - 1 = \prod_{i=1}^t p_i^{e_i}$
		2. Find $g_i$ s.t. $\mathrm{ord}_q(g_i) = p_i^{e_i}$ for each $i$.
		3. Let $g = \prod_{i=1}^t g_i$, then it is a primitive element modulo $q$.

- **Thm 5.48**: If $q\in \mathbb{Z}_p[x]$ is irreducible and $k \geq 2$, then there exists a primitive element modulo $q^k \iff$
	- $p\neq 2$, $k=2$ and $\deg(q) = 1$, or
	- $p=2$, $2\leq k \leq 3$ and $\deg(q) = 1$.

	???+ info "Proof"

		- $\impliedby$:
			1. $k=2$: Let $g\in \mathbb{Z}_p[x]$ be a primitive element modulo $q$, then $\mathrm{ord}_q(g) = \Phi_p(q) = p^{\deg(q)} - 1 = p - 1$. Then we have:

				$$
				\begin{aligned} & g^{\mathrm{ord}_{q^2}(g)} \equiv 1 \pmod{q^2} \\ \implies & g^{\mathrm{ord}_{q^2}(g)} \equiv 1 \pmod{q} \\ \implies & p - 1 = \Phi_p(q) \mid \mathrm{ord}_{q^2}(g) \mid \Phi_p(q^2) = p(p - 1) \\ \end{aligned}
				$$

				- Thus if $\mathrm{ord}_{q^2}(g) = p(p - 1)$, then $g$ is a primitive element modulo $q^2$.
				- Else if $\mathrm{ord}_{q^2}(g) = p - 1$, then consider the element $g + q$, we have $\mathrm{ord}_{q^2}(g + q) = p-1$ or $p(p-1)$. Suppose $\mathrm{ord}_{q^2}(g + q) = p - 1$, then we have:

					$$
					\begin{aligned} (g + q)^{p - 1} &= g^{p - 1} + \binom{p - 1}{1} g^{p - 2} q + \cdots + \binom{p - 1}{p - 2} g q^{p - 2} + q^{p - 1} \\ &\equiv g^{p - 1} + (p-1)g^{p - 2} q \\ &\equiv 1 - g^{p - 2} q \not\equiv 1 \pmod{q^2} \end{aligned}
					$$

					Thus contradiction, so $\mathrm{ord}_{q^2}(g + q) = p(p - 1)$, thus $g + q$ is a primitive element modulo $q^2$.

			2. $k=3$: Let $g\in \mathbb{Z}_2[x]$ be a primitive element modulo $q^2$, then

				$$
				\begin{aligned} 2 = p(p-1) = \mathrm{ord}_{q^2}(g) \mid \mathrm{ord}_{q^3}(g) \mid \Phi_2(q^3) = p^2(p-1) = 4 \end{aligned}
				$$

				Thus $\mathrm{ord}_{q^3}(g) = 2$ or $4$. Suppose $\mathrm{ord}_{q^3}(g) = 2$, thus

				$$
				\begin{aligned} & g^2 \equiv 1 \pmod{q^3} \\ \implies & q^3 \mid g^2 - 1 = (g - 1)^2 \\ \implies & q^2 \mid g - 1 \end{aligned}
				$$

				Thus $\mathrm{ord}_{q^2}(g) = 1$, contradiction, thus $\mathrm{ord}_{q^3}(g) = 4$, thus $g$ is a primitive element modulo $q^3$.

		- $\implies$: We have $\Phi_p(q^k) = (p^d - 1) \cdot p^{(k-1)d}$ with $d = \deg(q)$. Let $g$ be a primitive element modulo $q^k$, then $\mathrm{ord}_{q^k}(g) = \Phi_p(q^k)$. Let $t = \lceil \log_p(k)\rceil$, then $p^t \geq k$. Since $\gcd(g, q^k) = 1 \implies \gcd(g, q) = 1$, we have

			$$
			\begin{aligned} & g^{\Phi_p(q)} \equiv 1 \pmod q \\ \implies & q \mid g^{\Phi_p(q)} - 1 \\ \implies & q^k \mid q^{p^t} \mid (g^{\Phi_p(q)} - 1)^{p^t} = g^{\Phi_p(q) \cdot p^t} - 1 \\ \implies & g^{\Phi_p(q) \cdot p^t} \equiv 1 \pmod{q^k} \\ \implies & (p^d - 1)p^{(k-1)d} = \Phi_p(q^k) = \mathrm{ord}_{q^k}(g) \mid \Phi_p(q)p^t = (p^d - 1)p^t \\ \implies & p^{(k-1)d} \mid p^t \\ \implies & (k-1)d \leq t \end{aligned}
			$$

			- If $p\neq 2$, then $(k-1)d \leq t = \lceil \log_p(k) \rceil \leq \lceil \ln(k) \rceil \leq \lceil k-1 \rceil = k-1$, thus $d = 1$, thus $\lceil \log_p(k) \rceil = k-1$, thus $k=2$.
			- If $p=2$:
				- If $d\geq 2$, then $2k-2 \leq (k-1) \leq \lceil \log_2(k) \rceil$. Since linearly $2k-2$ grows faster than $\lceil \log_2(k) \rceil$ and $k=2$ not satisfies the inequality, contradiction, thus $d=1$.
				- If $d=1$, then $k-1 \leq \lceil \log_2(k) \rceil$. Since linearly $k-1$ grows faster than $\lceil \log_2(k) \rceil$ and $k=4$ not satisfies the inequality, contradiction, thus $k \leq 3$.
			- Thus we have:
				1. $p\neq 2$, $k=2$ and $\deg(q) = 1$, or
				2. $p=2$, $2\leq k \leq 3$ and $\deg(q) = 1$.

- **Thm 5.49**: Let $m(x) \in \mathbb{Z}_p[x]$ have the standard factorization $m(x) = \alpha \prod_{i=1}^n q_i^{e_i}(x)$. There exists a primitive element modulo $m(x) \iff$
	1. $\prod_{i=1}^n \Phi_p(q_i^{e_i}) = \mathrm{lcm}\{\Phi_p(q_1^{e_1}), \dots, \Phi_p(q_n^{e_n})\}$. I.e. $\forall 1 \leq i \leq j \leq n$, $\gcd(\Phi_p(q_i^{e_i}), \Phi_p(q_j^{e_j})) = 1$.
	2. $\forall 1 \leq i \leq n$, there exists a primitive element modulo $q_i^{e_i}$. I.e. satisfies the condition in Thm 5.48.

	???+ info "Proof"

		-  By the Chinese Remainder Theorem for rings, we have the isomorphism of groups of units:

			$$
			(\mathbb{Z}_p[x]/(m(x)))^* \cong (\mathbb{Z}_p[x]/(q_1^{e_1}(x)))^* \times \dots \times (\mathbb{Z}_p[x]/(q_n^{e_n}(x)))^*
			$$

			Let $G = (\mathbb{Z}_p[x]/(m(x)))^*$ and $G_i = (\mathbb{Z}_p[x]/(q_i^{e_i}(x)))^*$.

		- Then we have:
			- $\qquad$ A primitive element modulo $m(x)$ exists
			- $\iff G$ is a cyclic group
			- $\iff G_1 \times \dots \times G_n$ is cyclic
			- $\iff \forall 1 \leq i \leq n, G_i$ is cyclic and their orders $|G_i| = \Phi_p(q_i^{e_i})$ are pairwise coprime
			- $\iff \forall 1 \leq i \leq n$, there exists a primitive element modulo $q_i^{e_i}$ and $\forall 1 \leq i \leq j \leq n$, $\gcd(\Phi_p(q_i^{e_i}), \Phi_p(q_j^{e_j})) = 1$.

- **Thm 5.50**: There exists a primitive element modulo $m(x) \iff$
	- $p \neq 2$:
		- $m(x)$ is irreducible;
		- $m(x) = \alpha(x-\beta)^2$ for some $\alpha\in \mathbb{Z}_p^*$, $\beta \in \mathbb{Z}_p$;
	- $p = 2$: $m(x) = \alpha(x-\beta)^e \prod q_i(x)$ for some $\alpha \in \mathbb{Z}_2^*$, $\beta \in \mathbb{Z}_2$, satisfying:
		- $0 \leq e \leq 3$;
		- $\forall 1 \leq i < j \leq n$, $\gcd(\deg(q_i), \deg(q_j)) = 1$;
		- $x-\beta, q_i$ are distinct monic irreducible polynomials.

	???+ info "Proof"

		- $p\neq 2$: 
			- $m(x)$ is irreducible: Proof by Thm 5.46 and Thm 5.47.
			- $m(x) = \alpha(x-\beta)^2$: Proof by Thm 5.48.
		- $p=2$: 
			- $m(x) = \alpha$: $\alpha = 1 \in \mathbb{Z}_2^*$, thus $\Phi_2(m) = 1$, thus $1$ is a primitive element modulo $m$.
			- $m(x) = \alpha(x-\beta)$: Proof by Thm 5.46 and Thm 5.47.
			- $m(x) = \alpha(x-\beta)^2$ or $m(x) = \alpha(x-\beta)^3$: Proof by Thm 5.48.
			- $m(x) = \alpha(x-\beta)^e \prod q_i(x)$: $\deg(q_i)$ are pairwise coprime, since $\gcd(2^a-1, 2^b-1) = 2^{\gcd(a,b)}-1$, thus $\Phi_2(q_i) = 2^{\deg(q_i)} - 1$ are pairwise coprime. Since $e \leq 3$, thus $\Phi_2((x-\beta)^e) = 2^{e-1} \in \{1, 2, 4\}$ and is coprime to $\Phi_2(q_i)$. Thus by Thm 5.49, there exists a primitive element modulo $m$.

## Lagrange interpolation
### Roots

- **Def 5.51 Root**: An element $r \in F$ is called a root of $f \in F[x]$ if

	$$
	f(r) = 0
	$$

- **Lemma 5.52**: An element $r \in F$ is a root of $f \in F[x] \iff (x-r) | f(x)$

	???+ info "Proof"

		- $\implies$: Write $f(x) = q(x)(x-r) + r_0$ with $\deg(r_0) < \deg(x-r) = 1$, then $r_0 \in F$, thus $0 = f(r) = r_0$, thus $f(x) = q(x)(x-r)$, thus $(x-r) | f(x)$.
		- $\impliedby$: If $(x-r) | f(x)$, then $f(x) = q(x)(x-r)$, thus $f(r) = 0$, thus $r$ is a root of $f$.

- **Def 5.53 Derivative**: If $f(x) = a_0 + a_1x + \cdots + a_nx^n$, then the derivative $f'$ of $f$ is defined by

	$$
	f' = a_1 + 2a_2x + \cdots + na_nx^{n-1}
	$$

- **Def 5.54 Multiplicity of Root**: Let $r \in F$ be a root of $f \in F[x]$. If $k$ is a positive integer s.t. $(x-r)^k | f$ but $(x-r)^{k+1} \nmid f$, then $k$ is called the multiplicity of root $r$.
	- If $k \ge 2$, the $r$ is called a multiple root. Otherwise, it is called a simple root.
- **Thm 5.55 Property of Multiple Roots**: An element $r \in F$ is a multiple root of $f \in F[x] \iff r$ is a common root of $f$ and $f'$.
- **Thm 5.56**: Let $F$ be a field and $f \in F[x]$ with $n := \deg(f) \ge 1$. Then $F$ contains at most $n$ distinct roots of $f$.

	???+ info "Proof"

		- We prove by induction on $n$. If $n=1$, then $f(x) = a_1x + a_0$ with $a_1 \neq 0$, thus $f$ has exactly one root, thus the statement holds.
		- Assume that the statement holds for any polynomial with degree less than $n$.
			- If $f$ has no root, then the statement holds.
			- Otherwise, let $r$ be a root of $f$, then by Lemma 5.52, we have $f(x) = (x-r)g(x)$ with $\deg(g) = n-1$, thus any root of $f$ is either $r$ or a root of $g$, thus the number of distinct roots of $f$ is at most $(n-1) + 1 = n$, thus the statement holds.

### Lagrange Interpolation

- **Thm 5.57**: The set $F[x]_{<n} = \{f \in F[x] : \deg(f) < n\}$ forms a vector space over $F$ with $\dim(F[x]_{<n}) = n$. And It has a canonical basis $\{1, x, \cdots, x^{n-1}\}$ and a lagrange basis $\{L_i(x) = \prod_{j \ne i}(x-a_j)\}_{i=1}^n$, where $a_1, \cdots, a_n$ are $n$ distinct elements of $F$.

	???+ info "Proof of lagrange basis"

		- It is sufficient to show that they are linearly independent. Suppose $\sum_{i=1}^n \lambda_i L_i(x) = 0$ for some $\lambda_i \in F$, then $\forall k$, we have

			$$
			0 = \sum_{i=1}^n \lambda_i \prod_{j \ne i}(a_k - a_j) = \lambda_k \prod_{j \ne k}(a_k - a_j), \quad \prod_{j \ne k}(a_k - a_j) \neq 0
			$$

			Since in the sum, when $i \neq k$, the term $\prod_{j \ne i}(a_k - a_j) = 0$, only when $i = k$, the term $\prod_{j \ne i}(a_k - a_j) = \prod_{j \ne k}(a_k - a_j) \neq 0$. Thus $\forall k, \lambda_k = 0$, thus they are linearly independent.

- **Thm 5.58 Lagrange Interpolation**: For $n > 0$, let $a_1, \cdots, a_n$ be $n$ distinct elements of $F$, and let $b_1, \cdots, b_n$ be $n$ arbitrary elements of $F$. Then there exists a unique polynomial $f \in F[x]$ with $\deg(f) \le n-1$ s.t.

	$$
	f(a_i) = b_i, \quad i=1,2,\cdots,n
	$$

	Furthermore, this polynomial $f$ is given by

	$$
	f(x) = \sum_{i=1}^n \prod_{j \ne i} \frac{(x-a_j)}{(a_i-a_j)} b_i
	$$

	???+ info "Proof method 1"

		- Let $f(x) = \sum_{i=0}^{n-1} \lambda_i x^i$ satisfy $f(a_i) = b_i$ for each $i$. Then we have

			$$
			\begin{pmatrix} 1 & a_1 & a_1^2 & \cdots & a_1^{n-1} \\ 1 & a_2 & a_2^2 & \cdots & a_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & a_n & a_n^2 & \cdots & a_n^{n-1} \end{pmatrix} \begin{pmatrix} \lambda_0 \\ \lambda_1 \\ \lambda_2 \\ \vdots \\ \lambda_{n-1} \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_n \end{pmatrix}
			$$

			Since the coefficient matrix is a Vandermonde matrix with distinct $a_i$, it is invertible, thus there exists a unique solution $\lambda_i$, thus there exists a unique polynomial $f$ with $\deg(f) \le n-1$ s.t. $f(a_i) = b_i$ for each $i$.

	???+ info "Proof method 2"

		- Let $f(x) = \sum_{i=1}^n \lambda_i L_i(x) = \sum_{i=1}^n \lambda_i \prod_{j \ne i}(x-a_j)$ satisfy $f(a_i) = b_i$ for each $i$. Then we have

			$$
			b_k = f(a_k) = \sum_{i=1}^n \lambda_i \prod_{j \ne i}(a_k - a_j) = \lambda_k \prod_{j \ne k}(a_k - a_j)
			$$

			Thus $\lambda_k = \frac{b_k}{\prod_{j \ne k}(a_k - a_j)}$, thus there exists a unique polynomial $f=\sum_{i=1}^n \prod_{j \ne i} \frac{(x-a_j)}{(a_i-a_j)} b_i$ with $\deg(f) \le n-1$ s.t. $f(a_i) = b_i$ for each $i$.