---
comments: false
---

# NIS2336-编译原理

---

> 授课老师：胡易坤

> 学年学期：2024-2025 学年春季学期

---

???+ info 各类文法与解析方法
    - **LL(1) Grammar**
        - L: 从左到右扫描输入；L：最左派生；1：提前看一个输入符号
        - 无左递归和左因子
        - $\mathbf{A} \rightarrow \mathbf{\alpha} \ | \ \mathbf{\beta}$ 表示两个不同的产生式，则 $\mathbf{FIRST(\alpha)}$ 和 $\mathbf{FIRST(\beta)}$ 是互不相交的集合
            - 二者不会同时派生以 $\mathbf{a}$ 开头的字符串
            - 至多一个 $\mathbf{\alpha}$ 和 $\mathbf{\beta}$ 可以派生空字符串
        - 如果 $\mathbf{\epsilon} \in \mathbf{FIRST(\beta)}$，则 $\mathbf{FIRST(\alpha)}$ 和 $\mathbf{FOLLOW(A)}$ 是互不相交的集合
    - **LL(1) Parsing**
        - 提取左因子
        - 消除直接左递归
        - 计算 $\mathbf{FIRST}$ 和 $\mathbf{FOLLOW}$
        - 构造预测分析表（列为终结符，行为非终结符）
        - 从 Start Symbol 开始预测/或使用栈和输入缓冲区进行预测分析
            - 查表（最左侧非终结符，最左侧未匹配输入符号）作为派生的产生式进行派生
            - 若使用栈和输入缓冲区，则
                - 若栈顶符号为终结符且与输入符号匹配，则出栈并将输入指针后移
                - 若栈顶符号为非终结符，则查表（栈顶符号，输入指针对应符号）得到派生的产生式，将栈顶符号出栈并将产生式右侧符号逆序入栈
                - 直到栈为空，输入指针指向 $\$$，则接受输入
    - **OG Grammar（算符文法）**
        - 任意生成式不含两个相邻的非终结符
        - 不含空生成式
    - **OPP Grammar（算符优先文法）**
        - 首先满足 OG Grammar 的要求
        - 任意两个终结符号对（有序）之间一定满足唯一的优先级关系
    - **OPP Parsing**
        - 计算 $\mathbf{LEADING}$ 和 $\mathbf{TRAILING}$
        - 构造优先级关系表
        - 使用栈和输入缓冲区进行运算符优先解析/或使用优先级爬升法
            - 若栈顶终结符号优先级 <· / =· 输入符号优先级，则移进
            - 若栈顶终结符号优先级 >· 输入符号优先级，则归约
    - **LR(0) Grammar**
        - L: 从左到右扫描输入；R：最右派生，最左归约；0：提前看一个输入符号
        - 任一项集的状态转移不含归约-归约或移进-归约冲突
    - **LR(0) Parsing**
        - 扩展文法
        - 通过 $\mathbf{GOTO}$ 和 $\mathbf{CLOSURE}$ 构造 LR(0)项集族
        - 构造 LR(0)分析表（列为输入符号，行为状态）
        - 使用栈和输入缓冲区进行 LR(0)解析
            - 查表，（栈顶，输入符号）为 s n，则移进并 push 状态 n 到栈顶，
            - 若为 r m，则用第 m 条产生式进行归约，pop 栈顶的符号数目等于产生式右侧符号数目，查（栈顶符号，产生式左侧符号）为 n，则 push 状态 n 到栈顶
            - 若为 ACCEPT，则接受输入
    - **SLR(1) Grammar**
        - 任一项集的状态转移不含归约-归约或移进-归约冲突
            - LR(0) 项目集中存在归约-归约冲突时，两个 $\mathbf{FOLLOW}$ 集的交集为空
            - LR(0) 项目集中存在移进-归约冲突时，移进的终结符号不在归约的 $\mathbf{FOLLOW}$ 集中
    - **SLR(1) Parsing**
        - 扩展文法、构造集族同 LR(0)
        - 构造 SLR(1) 分析表时：
            - 对 $\mathbf{A} \rightarrow \mathbf{\beta} \cdot$ 归约时, 只对 $\mathbf{FOLLOW(A)}$ 中的终结符进行归约
            - 对 $\mathbf{S'} \rightarrow \mathbf{S'}$ 赋值 ACCEPT 时, 只对 $\$$ 接受
        - 使用栈和输入缓冲区进行SLR(1)解析
    - **LR(1) Grammar**
        - L: 从左到右扫描输入；R：最右派生，最左归约；1：提前看一个输入符号
        - LR(1) 的项由两部分组成：LR(0) 的项和一个 lookahead 符号
        - 任一项集的状态转移不含归约-归约或移进-归约冲突
            - 无归约-归约冲突：同一状态下如果有多个归约，则前瞻符号不相交
            - 无移进-归约冲突：同一状态下如果同时有移进和归约，则移进的终结符号不在归约的前瞻符号中
    - **LR(1) Parsing**
        - 扩展文法
        - 通过 $\mathbf{GOTO}$ 和 $\mathbf{CLOSURE}$ 构造 LR(1)项集族
        - 构造 LR(1)分析表时：
            - 对 $[\mathbf{A} \rightarrow \mathbf{\beta} \cdot, a]$ 归约时, 只对 $\mathbf{a}$ 进行归约
            - 对 $[\mathbf{S'} \rightarrow \mathbf{S} \cdot, \$]$ 赋值 ACCEPT 时, 只对 $\ $$ 接受
        - 使用栈和输入缓冲区进行 LR(1)解析
    - **LALR(1) Grammar**
        - LA: LookAhead；L: 从左到右扫描输入；R：最右派生，最左归约；1：提前看一个输入符号
        - LALR(1)的项集族是 LR(1)的项集族的同心集合并
        - 任一项集的状态转移不含归约-归约或移进-归约冲突
    - **LALR(1) Parsing**
        - 扩展文法、构造集族同 LR(0) 作为心
        - 对每个状态的初始项的心，用占位符#作为前瞻符号，通过闭包计算自发生成的前瞻符号和传递关系
        - 对于传递关系，保留每个状态的内核项，构造传播表
        - 根据传播表和自发生成的前瞻符号，通过若干轮传播得到每个心最终对应的前瞻符号，得到归约内核项的 [心，前瞻符号(若干个)] 对
        - 构造 LALR(1) 分析表，与 LR(1) 相同
        - 使用栈和输入缓冲区进行 LALR(1) 解析

---

## Chapter Index

- [Ch1 Intro](Ch1-Intro.md)
- [Ch2 Syntax Definition](Ch2-Syntax-Definition.md)
- [Ch3 Scanning](Ch3-Scanning.md)
- [Ch4 Parsing](Ch4-Parsing.md)
