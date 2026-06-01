# 特征降维

- 为什么需要降维
    - 解决维度诅咒问题
    - 提升模型性能
    - 降低计算成本

## 主成分分析（PCA）
### 核心思想

- **核心思想**：  寻找一组正交的投影方向，通过最大化数据投影后的方差，保留数据的主要特征信息，从而提升坐标可分性，实现无监督的线性降维。
- **符号定义与预备知识**
    - **样本集**：$X = \{\mathbf{x}_1, \mathbf{x}_2, \cdots, \mathbf{x}_n\}$，其中每个样本 $\mathbf{x}_i \in \mathbb{R}^d$，$d$ 为原特征维度
    - **投影方向**：用单位向量 $\mathbf{w} \in \mathbb{R}^d$ 表示，满足 $\|\mathbf{w}\|^2 = \mathbf{w}^\top \mathbf{w} = 1$。
    - **样本均值**：$\bar{\mathbf{x}} = \frac{1}{n} \sum_{i=1}^n \mathbf{x}_i$。
    - **投影结果**：样本 $\mathbf{x}_i$ 在 $\mathbf{w}$ 方向上的投影值为标量 $z_i = \mathbf{w}^\top \mathbf{x}_i$。
- **目标**：为了最大化投影后的方差，即求解

    $$
    \mathbf{w} = \arg\max_{\mathbf{w}} \frac{1}{n}  \sum_{i=1}^n (\mathbf{w}^\top \mathbf{x}_i - \bar{z})^2 \quad \text{s.t.} \quad \|\mathbf{w}\|^2=1
    $$

### 推导核心

1. **数据中心化**：为了简化方差的计算，首先将数据中心化：令 $\tilde{\mathbf{x}}_i = \mathbf{x}_i - \bar{\mathbf{x}}$。此时投影后的均值 $\bar{z} = \mathbf{w}^\top \left( \frac{1}{n} \sum_{i} \tilde{\mathbf{x}}_i \right) = 0$。
2. **目标函数简化**：

    $$
    \arg\max_{\mathbf{w}} \frac{1}{n} \sum_{i=1}^n (\mathbf{w}^\top \tilde{\mathbf{x}}_i)^2 \quad \text{s.t.} \quad \|\mathbf{w}\|^2=1
    $$

3. **矩阵化简与协方差矩阵**：提取 $\mathbf{w}$，将目标函数改写为矩阵乘法形式：

    $$
    \begin{aligned}
    & \frac{1}{n} \sum_{i=1}^n (\mathbf{w}^\top \tilde{\mathbf{x}}_i)^2 \\
    =& \frac{1}{n} \sum_{i=1}^n (\mathbf{w}^\top \tilde{\mathbf{x}}_{i})(\tilde{\mathbf{x}}_{i}^\top \mathbf{w}) \\
    =& \mathbf{w}^\top \left( \frac{1}{n} \sum_{i=1}^n \tilde{\mathbf{x}}_{i} \tilde{\mathbf{x}}_{i}^\top \right) \mathbf{w} \\
    =& \mathbf{w}^\top \Sigma \mathbf{w}
    \end{aligned}
    $$

    其中 $\Sigma = \frac{1}{n} \sum_{i=1}^n \tilde{\mathbf{x}}_{i} \tilde{\mathbf{x}}_{i}^\top$ 是数据的 **协方差矩阵**，对称且半正定，所有特征值 $\lambda_j \ge 0$。

4. **拉格朗日乘子法求解**：构造拉格朗日函数：

    $$
    L(\mathbf{w}, \lambda) = \mathbf{w}^\top \Sigma \mathbf{w} - \lambda(\mathbf{w}^\top \mathbf{w} - 1)
    $$

    对 $\mathbf{w}$ 求导并令其为 0，得到：

    $$
    \frac{\partial L}{\partial \mathbf{w}} = 2\Sigma \mathbf{w} - 2\lambda \mathbf{w} = 0 \implies \Sigma \mathbf{w} = \lambda \mathbf{w}
    $$

5. **结论**：最佳投影方向 $\mathbf{w}$ 必须是协方差矩阵 $\Sigma$ 的 **特征向量**。此时，投影后的方差为：

    $$
    \mathbf{w}^\top \Sigma \mathbf{w} = \mathbf{w}^\top (\lambda \mathbf{w}) = \lambda \mathbf{w}^\top \mathbf{w} = \lambda \|\mathbf{w}\|^2 = \lambda
    $$

    则

    $$
    \mathbf{w} = \arg\max_{\mathbf{w}} \mathbf{w}^\top \Sigma \mathbf{w} = \max_{j} \lambda_j
    $$

### 实现步骤（降维至 $k$ 维）

- **训练阶段**（拟合 PCA 模型）
    1. 计算原训练数据的均值向量 $\bar{\mathbf{x}}$
    2. 对原数据进行特征中心化：$\tilde{\mathbf{x}}_i = \mathbf{x}_i - \bar{\mathbf{x}}$
    3. 计算协方差矩阵 $\Sigma$
    4. 对 $\Sigma$ 进行特征值分解（或直接对中心化后的数据矩阵进行奇异值分解 SVD*）
    5. 将特征值按降序排列：$\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_d$
    6. 选取前 $k$ 个最大特征值对应的特征向量，按列拼接组成投影矩阵 $\mathbf{W} = [\mathbf{w}_1, \mathbf{w}_2, \cdots, \mathbf{w}_k] \in \mathbb{R}^{d \times k}$
- **推理阶段（对新数据降维）**
    1. 使用训练阶段得到的均值向量 $\bar{\mathbf{x}}$，对新样本 $\mathbf{x}_{new}$ 进行中心化：$\tilde{\mathbf{x}}_{new} = \mathbf{x}_{new} - \bar{\mathbf{x}}$
    2. 使用投影矩阵 $\mathbf{W}$ 进行投影变换，得到降维后的 $k$ 维特征：$\mathbf{z}_{new} = \mathbf{W}^\top \tilde{\mathbf{x}}_{new}$

## Fisher 线性判别式分析（LDA）
### 核心思想

- **核心思想**：寻找投影坐标轴，通过最大化类间距离、最小化类内散布度，从而提升分类可分性，实现有监督的线性降维。

### 两分类 LDA

- **目标函数**：分子为类间距离，分母为类内散布度和：

    $$
    J(\mathbf{v})=\frac{(\tilde{\mu}_1-\tilde{\mu}_2)^2}{\tilde{s}_1^2+\tilde{s}_2^2}
    $$

- **目标**：为了最大化类间距离、最小化类内散布度和，即最大化 $J(\mathbf{v})$，也即求解

    $$
    \mathbf{v}^* = \arg\max_{\mathbf{v}} J(\mathbf{v})
    $$

    其中：

    - $\tilde{\mu}_j = \frac{1}{|C_j|} \sum_{\mathbf{x}_i\in C_j} \mathbf{v}^\top \mathbf{x}_i = \mathbf{v}^\top \mu_j$ 是类别 $j$ 的投影均值
    - $\tilde{s}_j^2 = \sum_{\mathbf{x}_i\in C_j} (\mathbf{v}^\top \mathbf{x}_i - \tilde{\mu}_j)^2$ 是类别 $j$ 的投影方差
- **最优化推导过程简述**
    1. 定义：
        - **类间散度矩阵** $\mathbf{S}_B = (\mu_1 - \mu_2)(\mu_1 - \mu_2)^\top$
        - **类内散度矩阵** $\mathbf{S}_W = \sum_{j=1}^2 \sum_{\mathbf{x}_i\in C_j} (\mathbf{x}_i - \mu_j)(\mathbf{x}_i - \mu_j)^\top = \mathbf{S}_1 + \mathbf{S}_2$
    2. 将 $J(\mathbf{v})$ 改写为矩阵形式：

        $$
        J(\mathbf{v}) = \frac{(\mathbf{v}^\top \mu_1 - \mathbf{v}^\top \mu_2)^2}{\sum_{j=1}^2 \sum_{\mathbf{x}_i\in C_j} (\mathbf{v}^\top \mathbf{x}_i - \mathbf{v}^\top \mu_j)^2} = \frac{\mathbf{v}^\top \mathbf{S}_B \mathbf{v}}{\mathbf{v}^\top \mathbf{S}_W \mathbf{v}}
        $$

    3. 令导数为 0，得到最优解 $\mathbf{v}^*$ 为 $\mathbf{S}_W^{-1}\mathbf{S}_B$ 的特征向量：

        $$
        \begin{aligned}
        &\frac{\partial J(\mathbf{v})}{\partial \mathbf{v}} = \frac{2\mathbf{S}_B \mathbf{v} \cdot (\mathbf{v}^\top \mathbf{S}_W \mathbf{v}) - 2\mathbf{S}_W \mathbf{v} \cdot (\mathbf{v}^\top \mathbf{S}_B \mathbf{v})}{(\mathbf{v}^\top \mathbf{S}_W \mathbf{v})^2} = 0 \\
        \implies & \mathbf{S}_B \mathbf{v} \cdot (\mathbf{v}^\top \mathbf{S}_W \mathbf{v}) = \mathbf{S}_W \mathbf{v} \cdot (\mathbf{v}^\top \mathbf{S}_B \mathbf{v}) \\
        \implies & \mathbf{S}_B \mathbf{v} = J(\mathbf{v}) \mathbf{S}_W \mathbf{v} \\
        \implies & \mathbf{S}_W^{-1} \mathbf{S}_B \mathbf{v} = J(\mathbf{v}) \mathbf{v} \\
        \implies & \mathbf{v} = \mathbf{S}_W^{-1} (\mu_1 - \mu_2)
        \end{aligned}
        $$

### 多分类 LDA

- 各类中心：$\mu_j = \frac{1}{|C_j|} \sum_{\mathbf{x}_i\in C_j} \mathbf{x}_i$
- 整体数据均值：$\mu = \frac{1}{c} \sum_{j=1}^c \mu_j$
- 类内散度矩阵：$\mathbf{S}_W = \sum_{j=1}^c \mathbf{S}_j = \sum_{j=1}^c \sum_{\mathbf{x}_i\in C_j} (\mathbf{x}_i - \mu_j)(\mathbf{x}_i - \mu_j)^\top$
- 类间散度矩阵：$\mathbf{S}_B = \sum_{j=1}^c |C_j| (\mu_j - \mu)(\mu_j - \mu)^\top$
- 目标函数：

    $$
    J(\mathbf{v}) = \frac{\det(\mathbf{v}^\top \mathbf{S}_B \mathbf{v})}{\det(\mathbf{v}^\top \mathbf{S}_W \mathbf{v})}
    $$

- 最优解 $\mathbf{v}^*$ 为 $\mathbf{S}_W^{-1}\mathbf{S}_B$ 的前 $k$ 个特征向量组成的矩阵。
