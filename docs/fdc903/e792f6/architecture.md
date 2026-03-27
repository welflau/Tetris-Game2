# 架构设计 - 实现行消除检测和处理

## 架构模式
MVC + 观察者模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生Canvas API或HTML5游戏引擎
- **database**: LocalStorage（本地存储）
- **others**: Canvas 2D API, RequestAnimationFrame, 事件系统

## 模块设计

### LineDetector
职责: 检测网格中的满行，返回需要消除的行索引列表
- detectFullLines(grid): number[]
- isLineFull(row): boolean

### LineClearProcessor
职责: 处理行消除逻辑，包括移除满行和重排网格
- clearLines(grid, lineIndices): void
- dropLinesAbove(grid, clearedLine): void

### ScoreCalculator
职责: 根据消除行数计算分数，支持连击加分机制
- calculateScore(linesCleared, level): number
- updateLevel(totalLines): number

### ClearAnimationManager
职责: 管理行消除的视觉动画效果
- startClearAnimation(lineIndices): Promise<void>
- renderClearEffect(progress): void

### GameStateManager
职责: 管理游戏状态变化，协调各模块间的交互
- onLinesCleared(count): void
- updateGameStats(score, level, lines): void

## 数据流
1. 方块落地后触发行检测 -> 2. LineDetector扫描网格识别满行 -> 3. ClearAnimationManager播放消除动画 -> 4. LineClearProcessor执行行消除和网格重排 -> 5. ScoreCalculator计算得分和等级 -> 6. GameStateManager更新游戏状态并通知UI刷新

## 风险点
- 动画播放期间的状态同步问题
- 大量行同时消除时的性能优化
- 网格重排算法的正确性验证
- 分数计算公式的平衡性调整

## 关键决策
- 采用Promise-based的动画系统确保消除流程的顺序执行
- 使用双缓冲机制避免动画期间的视觉闪烁
- 实现分层的分数计算系统支持多种加分规则
- 设计可配置的动画参数便于后期调优
