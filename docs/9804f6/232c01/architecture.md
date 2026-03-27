# 架构设计 - 实现随机方块生成系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: 无（客户端游戏）
- **others**: Canvas 2D API, Web APIs, CSS3

## 模块设计

### TetrominoGenerator
职责: 负责方块类型的随机生成，实现7-bag算法确保公平性，管理方块生成队列
- generateNext(): Tetromino - 生成下一个方块
- peek(): Tetromino - 预览下一个方块不消费
- reset(): void - 重置生成器状态

### TetrominoFactory
职责: 方块对象工厂，负责创建具体的方块实例，包含方块的形状、颜色、旋转状态等属性
- createTetromino(type: string): Tetromino - 创建指定类型方块
- getTetrominoData(type: string): Object - 获取方块数据定义

### TetrominoQueue
职责: 方块队列管理器，维护当前方块和下个方块的状态，处理方块切换逻辑
- getCurrentTetromino(): Tetromino - 获取当前方块
- getNextTetromino(): Tetromino - 获取下个方块
- spawnNext(): Tetromino - 生成下个方块并更新队列
- hasNext(): boolean - 检查是否有下个方块

### Tetromino
职责: 方块实体类，包含方块的形状矩阵、颜色、位置、旋转状态等属性和基础操作方法
- getShape(): number[][] - 获取当前形状矩阵
- getColor(): string - 获取方块颜色
- getPosition(): {x: number, y: number} - 获取位置
- setPosition(x: number, y: number): void - 设置位置
- rotate(): void - 旋转方块
- clone(): Tetromino - 克隆方块实例

### PreviewRenderer
职责: 下个方块预览渲染器，负责在UI预览区域绘制下个方块
- render(tetromino: Tetromino): void - 渲染预览方块
- clear(): void - 清空预览区域
- setCanvas(canvas: HTMLCanvasElement): void - 设置预览画布

### RandomUtils
职责: 随机数工具类，提供高质量的随机数生成和数组洗牌算法
- shuffle(array: any[]): any[] - 数组洗牌算法
- randomInt(min: number, max: number): number - 生成随机整数
- setSeed(seed: number): void - 设置随机种子（可选）

## 数据流
TetrominoGenerator使用7-bag算法生成方块序列 -> TetrominoFactory根据类型创建具体方块实例 -> TetrominoQueue管理当前和下个方块状态 -> 游戏主循环从队列获取当前方块进行游戏逻辑处理 -> PreviewRenderer在UI中显示下个方块预览 -> 当前方块放置完成后，队列自动切换到下个方块并生成新的预览方块

## 风险点
- 7-bag算法实现复杂度可能导致性能问题
- 方块预览渲染可能与主游戏区域渲染产生冲突
- 随机数生成质量可能影响游戏公平性
- 方块队列状态管理可能出现同步问题

## 关键决策
- 采用7-bag算法而非纯随机，确保每7个方块包含所有类型，提升游戏公平性
- 使用工厂模式创建方块实例，便于后续扩展新方块类型
- 分离预览渲染器，避免与主游戏渲染逻辑耦合
- 实现方块队列管理器，统一处理方块切换逻辑
- 使用Fisher-Yates洗牌算法确保随机分布质量
- 方块对象采用不可变设计，避免意外修改导致的bug
