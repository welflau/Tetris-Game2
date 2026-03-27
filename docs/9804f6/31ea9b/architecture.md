# 架构设计 - 开发行消除逻辑系统

## 架构模式
模块化架构（Module Pattern）

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: 无（客户端游戏）
- **others**: Canvas 2D API, requestAnimationFrame, 事件监听器

## 模块设计

### LineDetector
职责: 检测游戏网格中的完整行，识别需要消除的行索引
- detectFullLines(grid)
- isLineFull(row)
- getFullLineIndices(grid)

### LineClearer
职责: 执行行消除操作，清空指定行的方块数据
- clearLines(grid, lineIndices)
- clearSingleLine(grid, lineIndex)
- markLinesForRemoval(grid, lineIndices)

### GravityProcessor
职责: 处理消除行后的重力效果，让上方方块下落填补空隙
- applyGravity(grid, clearedLineIndices)
- dropBlocksDown(grid, fromRow, steps)
- compactGrid(grid)

### LineRemovalAnimator
职责: 提供行消除的视觉动画效果，增强用户体验
- animateLineRemoval(lineIndices, callback)
- flashLines(lineIndices)
- fadeOutLines(lineIndices)

### ScoreCalculator
职责: 根据消除的行数计算得分，支持连击奖励机制
- calculateScore(linesCleared, currentLevel)
- getLineBonus(lineCount)
- applyLevelMultiplier(baseScore, level)

### LineRemovalManager
职责: 协调整个行消除流程，管理各个子模块的调用顺序
- processLineRemoval(grid)
- executeRemovalSequence(grid)
- onLinesRemoved(lineCount)

## 数据流
游戏主循环调用LineRemovalManager.processLineRemoval() → LineDetector检测完整行 → LineClearer清除标记行 → GravityProcessor处理重力下落 → ScoreCalculator计算得分 → LineRemovalAnimator播放动画效果 → 更新游戏状态并触发回调

## 风险点
- 多行同时消除时的重力计算复杂度较高
- 动画效果可能影响游戏帧率性能
- 边界情况处理（如连续多次消除）可能出现逻辑错误
- 不同消除模式的分数计算可能不准确

## 关键决策
- 采用自上而下的行检测算法，确保消除顺序的一致性
- 使用数组splice和unshift操作实现高效的重力下落
- 分离动画逻辑和游戏逻辑，避免动画阻塞游戏状态更新
- 实现批量处理机制，一次性处理所有完整行以提高性能
- 采用回调机制通知主游戏循环更新UI和分数显示
