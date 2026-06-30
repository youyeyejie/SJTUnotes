# Chapter 4. Quadratic Residues

- [Back to Course Home](index.md)

## Quadratic Residues

- **Def 4.1 Quadratic Residue**: Let $p$ be an odd prime, then $a\in\mathbb{Z}$ with $\gcd(a,p)=1$ is called a quadratic residue (QR) modulo $p$ if the congruence

	$$
	x^2 \equiv a \pmod p
	$$

	has a solution. Otherwise $a$ is called a quadratic non-residue (QNR) modulo $p$.

- **Thm 4.2 Property of QR**:

	1. Let $g$ be a primitive root modulo $p$, then $a$ is a QR modulo $p \iff a=g^{2k} \pmod p$ for some integer $k$.

		???+ info "Proof of 1"

			- $\implies$: Assume $a=QR$, then $\exists b\in\mathbb{Z}$ s.t. $b^2 \equiv a \pmod p$. Let $b \equiv g^k \pmod p$ for some integer $k$, then $a \equiv b^2 \equiv g^{2k} \pmod p$.

			- $\impliedby$: Assume $a \equiv g^{2k} \pmod p$ for some integer $k$, then $g^k$ is a solution to $x^2 \equiv a \pmod p$, so $a$ is a QR.

	2. $a = QR, b = QR \implies ab = QR$.

	3. $a = QNR, b = QNR \implies ab = QR$.

	4. $a = QR, b = QNR \implies ab = QNR$.

	5. The number of $QR$ / $QNR$ modulo $p$ is $\frac{p-1}{2}$.

		???+ info "Proof of 5"

			- Since there are $p-1$ non-zero elements in $\mathbb{Z}_p^*$, consider $x\in\mathbb{Z}_p^*$, then $(p-x)^2 \equiv p^2 - 2px + x^2 \equiv x^2 \pmod p$.

			- Consider $x^2$ for $x\in\{1, 2, \cdots, \frac{p-1}{2}\}$, claim that $\forall 1\leq x < y \leq \frac{p-1}{2}, x^2 \not\equiv y^2 \pmod p$.

				- If $x^2 \equiv y^2 \pmod p$, then $y^2 - x^2 \equiv (y-x)(y+x) \equiv 0 \pmod p$, thus $p \mid y-x$ or $p \mid y+x$.

				- Since $1\leq x < y \leq \frac{p-1}{2}$, $y+x < \frac{p-1}{2} + \frac{p-1}{2} = p-1 < p$ and $y-x < p$, thus $p \nmid x+y$ and $p \nmid x-y$, contradiction.

			- Thus $x^2$ for $x\in\{1, 2, \cdots, \frac{p-1}{2}\}$ are $\frac{p-1}{2}$ distinct $QR$ modulo $p$, and the remaining $\frac{p-1}{2}$ non-zero elements are $QNR$ modulo $p$.

## Legendre Symbol

- **Def 4.3 Legendre Symbol**: Let $p$ be an odd prime, then for any $a\in\mathbb{Z}$, the Legendre symbol $\left(\frac{a}{p}\right)$ is defined as

	$$
	\left(\frac{a}{p}\right) = \begin{cases} 0 ,& p \mid a \\ 1 ,& a \text{ is a QR modulo } p \\ -1 ,& a \text{ is a QNR modulo } p \end{cases}
	$$

- **Thm 4.4**: The number of solutions to $x^2 \equiv a \pmod p$ is $1 + \left(\frac{a}{p}\right)$.

	???+ info "Proof"

		1. **Case 1**: $p \mid a$, then $x^2 \equiv a \equiv 0 \pmod p$ has exactly one solution $x \equiv 0 \pmod p$. Thus $1 = 1 + \left(\frac{a}{p}\right)$, done.

		2. **Case 2**: $a$ is a QR modulo $p$, then $a \equiv g^{2k} \pmod p$ for some $k\in\mathbb{Z}$. Then $x^2 \equiv g^{2k} \pmod p$, so $x \equiv \pm g^k \pmod p$ are two distinct solutions to $x^2 \equiv a \pmod p$. Thus $2 = 1 + \left(\frac{a}{p}\right)$, done.

		3. **Case 3**: $a$ is a QNR modulo $p$, then there are no solutions to $x^2 \equiv a \pmod p$. Thus $0 = 1 + \left(\frac{a}{p}\right)$, done.

- **Thm 4.5 Euler's Criterion**: Let $p$ be an odd prime, then

	$$
	\left(\frac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p
	$$

	???+ info "Proof"

		1. **Case 1**: $p \mid a$, then $a=kp$ for some $k\in\mathbb{Z}$. Then $\left(\frac{a}{p}\right) \equiv 0 \equiv (kp)^{\frac{p-1}{2}} \pmod p$, done.

		2. **Case 2**: $a$ is a QR modulo $p$, then $a \equiv g^{2k} \pmod p$ for some $k\in\mathbb{Z}$. Then $\left(\frac{a}{p}\right) \equiv 1 \equiv (g^{2k})^{\frac{p-1}{2}} \equiv g^{(p-1)k} \pmod p$, done.

		3. **Case 3**: $a$ is a QNR modulo $p$, then $(a^{\frac{p-1}{2}})^2 \equiv a^{p-1} \equiv 1 \pmod p$, i.e. $a^{\frac{p-1}{2}}$ is a solution to $x^2 \equiv 1 \pmod p$, thus $a^{\frac{p-1}{2}} \equiv \pm 1 \pmod p$. Let $a\equiv g^k \pmod p$ with odd $k$, then

			$$
			\mathrm{ord}_p(a) = \mathrm{ord}_p(g^k) = \frac{\mathrm{ord}_p(g)}{\gcd(\mathrm{ord}_p(g), k)} = \frac{p-1}{\gcd(p-1, k)}
			$$

			Suppose $a^{\frac{p-1}{2}} \equiv 1 \pmod p$, then $\frac{p-1}{\gcd(p-1, k)} \mid \frac{p-1}{2}$, i.e. $\exists t\in\mathbb{Z}$ s.t. $\frac{p-1}{\gcd(p-1, k)} \cdot t = \frac{p-1}{2}$, thus $\gcd(p-1, k) = 2t$, which contradicts the fact that $k$ is odd. Thus $a^{\frac{p-1}{2}} \equiv -1 \pmod p$, done.

- **Thm 4.6 Properties of Legendre Symbol**: Let $p$ be an odd prime, then for any $a, m, n\in\mathbb{Z}$, we have

	1. $\left(\frac{mn}{p}\right) = \left(\frac{m}{p}\right)\left(\frac{n}{p}\right)$

	2. $\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}} = \begin{cases} 1 ,& p \equiv 1 \pmod 4 \\ -1 ,& p \equiv 3 \pmod 4 \end{cases}$

	3. $\left(\frac{2}{p}\right) = (-1)^{\frac{p^2-1}{8}} = \begin{cases} 1 ,& p \equiv 1, 7 \pmod 8 \\ -1 ,& p \equiv 3, 5 \pmod 8 \end{cases}$

	4. $\sum_{a\in\mathbb{Z}_p} \left(\frac{a}{p}\right) = 0$.

	???+ info "Proof"

		1. By Euler's Criterion, $\left(\frac{mn}{p}\right) \equiv (mn)^{\frac{p-1}{2}} \equiv m^{\frac{p-1}{2}} n^{\frac{p-1}{2}} \equiv \left(\frac{m}{p}\right)\left(\frac{n}{p}\right) \pmod p$. Since $\left(\frac{mn}{p}\right), \left(\frac{m}{p}\right), \left(\frac{n}{p}\right) \in \{-1, 0, 1\}$, we have $\left(\frac{mn}{p}\right) = \left(\frac{m}{p}\right)\left(\frac{n}{p}\right)$, done.

		2. By Euler's Criterion, $\left(\frac{-1}{p}\right) \equiv (-1)^{\frac{p-1}{2}} \pmod p$. Since $\left(\frac{-1}{p}\right), (-1)^{\frac{p-1}{2}} \in \{-1, 1\}$, we have $\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}}$. If $p \equiv 1 \pmod 4$, then $\frac{p-1}{2}$ is even, thus $\left(\frac{-1}{p}\right) = 1$. If $p \equiv 3 \pmod 4$, then $\frac{p-1}{2}$ is odd, thus $\left(\frac{-1}{p}\right) = -1$, done.

		3. Consider $S = 2\cdot 4\cdot 6\cdots (p-1) = 2^{\frac{p-1}{2}} \cdot 1\cdot 2\cdot 3\cdots \frac{p-1}{2} \equiv 2^{\frac{p-1}{2}} \cdot \left(\frac{p-1}{2}\right)! \pmod p$.

			- Case 1: $p \equiv 1 \pmod 4$:

				$$
				\begin{aligned} S &\equiv 2\cdot 4\cdot 6\cdots (p-1) \\ &= 2\cdot 4\cdots \frac{p-1}{2} \cdot \frac{p+3}{2} \cdot \frac{p+7}{2} \cdots (p-1) \\ &\equiv 2\cdot 4\cdots \frac{p-1}{2} \cdot (\frac{p+3}{2}-p) \cdot (\frac{p+7}{2}-p) \cdots (p-1-p) \pmod p \\ &\equiv 2\cdot 4\cdots \frac{p-1}{2} \cdot (-\frac{p-3}{2}) \cdot (-\frac{p-7}{2}) \cdots (-1) \pmod p \\ &\equiv (-1)^{\frac{p-1}{4}} \cdot (\frac{p-1}{2})! \pmod p \\ \end{aligned}
				$$

				Thus $2^{\frac{p-1}{2}} \equiv (-1)^{\frac{p-1}{4}} \pmod p$, i.e. $\left(\frac{2}{p}\right) = (-1)^{\frac{p-1}{4}}$. If $p \equiv 1 \pmod 8$, then $\frac{p-1}{4}$ is even, thus $\left(\frac{2}{p}\right) = 1$. If $p \equiv 5 \pmod 8$, then $\frac{p-1}{4}$ is odd, thus $\left(\frac{2}{p}\right) = -1$, done.

			- Case 2: $p \equiv 3 \pmod 4$:

				$$
				\begin{aligned} S &\equiv 2\cdot 4\cdot 6\cdots (p-1) \\ &= 2\cdot 4\cdots \frac{p-3}{2} \cdot \frac{p+1}{2} \cdot \frac{p+5}{2} \cdots (p-1) \\ &\equiv 2\cdot 4\cdots \frac{p-3}{2} \cdot (\frac{p+1}{2}-p) \cdot (\frac{p+5}{2}-p) \cdots (p-1-p) \pmod p \\ &\equiv 2\cdot 4\cdots \frac{p-3}{2} \cdot (-\frac{p-1}{2}) \cdot (-\frac{p-5}{2}) \cdots (-1) \pmod p \\ &\equiv (-1)^{\frac{p+1}{4}} \cdot (\frac{p-1}{2})! \pmod p \\ \end{aligned}
				$$

				Thus $2^{\frac{p-1}{2}} \equiv (-1)^{\frac{p+1}{4}} \pmod p$, i.e. $\left(\frac{2}{p}\right) = (-1)^{\frac{p+1}{4}}$. If $p \equiv 3 \pmod 8$, then $\frac{p+1}{4}$ is odd, thus $\left(\frac{2}{p}\right) = -1$. If $p \equiv 7 \pmod 8$, then $\frac{p+1}{4}$ is even, thus $\left(\frac{2}{p}\right) = 1$, done.

			- Thus, combine the two cases, we have $\left(\frac{2}{p}\right) = (-1)^{\frac{p^2-1}{8}}$, done.

		4. Since $\left(\frac{0}{p}\right) = 0$, $\left(\frac{a}{p}\right) = 1$ for $\frac{p-1}{2}$ $QR$ and $\left(\frac{a}{p}\right) = -1$ for $\frac{p-1}{2}$ $QNR$, we have $\sum_{a\in\mathbb{Z}_p} \left(\frac{a}{p}\right) = 0 + \frac{p-1}{2} \cdot 1 + \frac{p-1}{2} \cdot (-1) = 0$, done.

## Jacobi Symbol

- **Def 4.7 Jacobi Symbol**: Let $m\geq 3$ be an odd integer, assume that $m$ has the standard factorization $m = \prod_{i=1}^r p_i^{e_i}$ with $p_i$ are distinct odd primes and $e_i \geq 1$, then for any $a\in\mathbb{Z}$, the Jacobi symbol $\left(\frac{a}{m}\right)$ is defined as

	$$
	\left(\frac{a}{m}\right) = \prod_{i=1}^r \left(\frac{a}{p_i}\right)^{e_i}
	$$

- **Thm 4.8 Properties of Jacobi Symbol**: Let $m,n\geq 3$ be odd integers, then for any $a, b\in\mathbb{Z}$, we have

	1. $\left(\frac{a}{m}\right) = 0 \iff \gcd(a, m) > 1$.

	2. $\left(\frac{ab}{m}\right) = \left(\frac{a}{m}\right)\left(\frac{b}{m}\right)$.

	3. $\left(\frac{a}{mn}\right) = \left(\frac{a}{m}\right)\left(\frac{a}{n}\right)$.

	4. $\left(\frac{n^2}{m}\right) = \left(\frac{n}{m^2}\right) = 1 \iff \gcd(n, m) = 1$.

	5. $\left(\frac{-1}{m}\right) = (-1)^{\frac{m-1}{2}}$.

	6. $\left(\frac{2}{m}\right) = (-1)^{\frac{m^2-1}{8}}$.

	???+ info "Proof"

		1. Let $m = \prod_{i=1}^r p_i^{e_i}$ be the standard factorization of $m$, then

			- $\implies$: Assume $\left(\frac{a}{m}\right) = 0$, then $\exists i\in\{1, 2, \cdots, r\}$ s.t. $\left(\frac{a}{p_i}\right) = 0$, thus $p_i \mid a$, so $p_i \mid \gcd(a, m)$, thus $\gcd(a, m) > 1$, done.

			- $\impliedby$: Assume $\gcd(a, m) > 1$, then $\exists i\in\{1, 2, \cdots, r\}$ s.t. $p_i \mid a$, thus $\left(\frac{a}{p_i}\right) = 0$, so $\left(\frac{a}{m}\right) = 0$, done.

		2. We have

			$$
			\begin{aligned} \left(\frac{ab}{m}\right) &= \prod_{i=1}^r \left(\frac{ab}{p_i}\right)^{e_i} \\ &= \prod_{i=1}^r \left(\frac{a}{p_i}\right)^{e_i} \cdot \prod_{i=1}^r \left(\frac{b}{p_i}\right)^{e_i} \\ &= \left(\frac{a}{m}\right)\left(\frac{b}{m}\right) \end{aligned}
			$$

		3. Let $m=\prod_{i=1}^r p_i^{e_i}$ and $n=\prod_{i=1}^r p_i^{f_i}$ with $e_i, f_i \geq 0$, then

			$$
			\begin{aligned} \left(\frac{a}{mn}\right) &= \left(\frac{a}{\prod_{i=1}^r p_i^{e_i+f_i}}\right) = \prod_{i=1}^r \left(\frac{a}{p_i}\right)^{e_i+f_i} \\ &= \prod_{i=1}^r \left(\frac{a}{p_i}\right)^{e_i} \cdot \prod_{i=1}^r \left(\frac{a}{p_i}\right)^{f_i} \\ &= \left(\frac{a}{m}\right)\left(\frac{a}{n}\right) \end{aligned}
			$$

		4. Follows from (1), (2) and (3).

		5. Proof of 5:

			- **Method 1**: Let $m = \prod_{i=1}^r p_i^{e_i}$ be the standard factorization of $m$, then

				$$
				\begin{aligned} \left(\frac{-1}{m}\right) &= \prod_{i=1}^r \left(\frac{-1}{p_i}\right)^{e_i} \\ &= \prod_{i=1}^r (-1)^{\frac{p_i-1}{2} e_i} \\ &= (-1)^{\sum_{i=1}^r \frac{p_i-1}{2} e_i} \overset{?}{=} (-1)^{\frac{m-1}{2}} \end{aligned}
				$$

				Claim that $\sum_{i=1}^r \frac{p_i-1}{2} e_i \equiv \frac{m-1}{2} \pmod 2$.

			- **Method 2**: We can prove by induction on $m$:

				1. If $m=3$, done.

				2. Assume the claim holds for all odd integers $\leq m$, then consider $m+2 = pk$ for some odd prime $p$ and odd integer $k\geq 1$. Then

					$$
					\begin{aligned} \left(\frac{-1}{m+2}\right) &= \left(\frac{-1}{pk}\right) = \left(\frac{-1}{p}\right)\left(\frac{-1}{k}\right) \\ &= (-1)^{\frac{p-1}{2}} \cdot (-1)^{\frac{k-1}{2}} \\ &= (-1)^{\frac{p-1}{2} + \frac{k-1}{2}} \end{aligned}
					$$

					It is sufficient to prove $\frac{p-1}{2} + \frac{k-1}{2} \equiv \frac{pk-1}{2} \pmod 2$. Let $p = 2u + 1$ and $k = 2v + 1$, then

					$$
					\begin{aligned} &\frac{p-1}{2} + \frac{k-1}{2} - \frac{pk-1}{2} \\ =& \frac{p+k-pk-1}{2} \\ =& \frac{-(p-1)(k-1)}{2} \\ =& -2uv \equiv 0 \pmod 2 \end{aligned}
					$$

					Thus $\frac{p-1}{2} + \frac{k-1}{2} \equiv \frac{pk-1}{2} \pmod 2$, done.

		6. Similar to (5), we can prove by induction on $m$:

			1. If $m=3$, done.

			2. Assume the claim holds for all odd integers $\leq m$, then consider $m+2 = pk$ for some odd prime $p$ and odd integer $k\geq 1$. Then

				$$
				\begin{aligned} \left(\frac{2}{m+2}\right) &= \left(\frac{2}{pk}\right) = \left(\frac{2}{p}\right)\left(\frac{2}{k}\right) \\ &= (-1)^{\frac{p^2-1}{8}} \cdot (-1)^{\frac{k^2-1}{8}} \\ &= (-1)^{\frac{p^2-1}{8} + \frac{k^2-1}{8}} \end{aligned}
				$$

				It is sufficient to prove $\frac{p^2-1}{8} + \frac{k^2-1}{8} \equiv \frac{(pk)^2-1}{8} \pmod 2$. Let $p = 2u + 1$ and $k = 2v + 1$, then

                $$
                \begin{aligned} &\frac{p^2-1}{8} + \frac{k^2-1}{8} - \frac{(pk)^2-1}{8} \\ =& \frac{p^2+k^2-(pk)^2-1}{8} \\ =& \frac{-(p^2-1)(k^2-1)}{8} \\ =& \frac{-(4u(u+1))(4v(v+1))}{8} \\ =& -2u(u+1)v(v+1) \equiv 0 \pmod 2 \end{aligned}
                $$

                Thus $\frac{p^2-1}{8} + \frac{k^2-1}{8} \equiv \frac{(pk)^2-1}{8} \pmod 2$, done.

## Quadratic Reciprocity

- **Thm 4.6 Law of Quadratic Reciprocity**: Let $m,n$ be odd integers with $\gcd(m, n) = 1$, then

	$$
	\left(\frac{m}{n}\right)\left(\frac{n}{m}\right) = (-1)^{\frac{m-1}{2} \cdot \frac{n-1}{2}}
	$$

	Equivalently, $\left(\frac{m}{n}\right) = \left(\frac{n}{m}\right) \cdot (-1)^{\frac{m-1}{2} \cdot \frac{n-1}{2}}$

	???+ note "Example"

		1. Since

			$$
			\begin{aligned} \left(\frac{3}{17}\right) &= \left(\frac{17}{3}\right) \cdot (-1)^{\frac{3-1}{2} \cdot \frac{17-1}{2}} \\ &= \left(\frac{2}{3}\right) \cdot 1 \\ &= -1 \end{aligned}
			$$

			Thus $3$ is a NQR modulo $17$.

		2. Since

			$$
			\begin{aligned} \left(\frac{6}{17}\right) &= \left(\frac{2}{17}\right) \cdot \left(\frac{3}{17}\right) \\ &= (-1)^{\frac{17^2-1}{8}} \cdot (-1) \\ &= -1 \end{aligned}
			$$

			Thus $6$ is a NQR modulo $17$.