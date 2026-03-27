# 架构设计 - 实现行消除和计分系统

## 架构模式
MVC + 模块化组件架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生JavaScript + Canvas API
- **database**: LocalStorage (本地存储)
- **others**: HTML5 Canvas, CSS3, Web APIs

## 模块设计

### LineManager
职责: 负责检测完整行、执行行消除逻辑、管理行消除动画效果
- checkCompleteLines()
- clearLines(lineNumbers)
- animateLineClear()
- compactGrid()

### ScoreSystem
职责: 管理游戏计分逻辑、等级系统、速度调整和统计数据
- calculateScore(linesCleared)
- updateLevel()
- getSpeed()
- getStats()

### GameGrid
职责: 维护游戏网格状态、提供网格操作接口、支持行消除后的网格重组
- getRow(index)
- removeRow(index)
- insertEmptyRow()
- isRowComplete(index)

### UIManager
职责: 更新分数显示、等级显示、统计信息显示和游戏状态提示
- updateScore()
- updateLevel()
- updateStats()
- showLineClearEffect()

### GameEngine
职责: 协调各模块工作、管理游戏主循环、处理行消除触发时机
- processLineClear()
- updateGameState()
- handlePiecePlace()

### EffectManager
职责: 管理行消除视觉效果、音效播放、粒子效果和动画过渡
- playLineClearEffect()
- showScorePopup()
- createParticles()

## 数据流
1. 方块放置后触发行检测 -> 2. LineManager检测完整行 -> 3. 播放消除动画效果 -> 4. ScoreSystem计算得分和等级 -> 5. GameGrid执行行消除和网格重组 -> 6. UIManager更新显示界面 -> 7. GameEngine调整游戏速度和状态

## 风险点
- 行消除动画可能影响游戏流畅性
- 多行同时消除的计分算法复杂度
- 网格重组时的数据一致性问题
- 等级提升时速度调整的平衡性

## 关键决策
- 采用基于Tetris标准的计分系统（单行100分，双行300分，三行500分，四行800分）
- 使用requestAnimationFrame实现流畅的行消除动画
- 实现等级系统，每10行消除提升一个等级
- 使用事件驱动模式处理行消除触发
- 支持连击加分机制提升游戏趣味性
