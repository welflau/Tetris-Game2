# 架构设计 - 消行系统与计分机制开发

## 架构模式
MVC + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### LineDetector
职责: 检测游戏区域中的满行，返回需要清除的行索引
- detectFullLines(gameBoard)
- isLineFull(lineArray)

### LineClearer
职责: 执行消行操作，包括动画效果和行数据清理
- clearLines(lineIndexes)
- animateLineClear(lineIndexes)
- removeLines(gameBoard, lineIndexes)

### ScoreManager
职责: 管理分数计算、等级提升和统计数据
- calculateScore(linesCleared, level)
- updateLevel(totalLines)
- getScoreMultiplier(linesCleared)
- saveHighScore()

### AnimationController
职责: 控制消行动画的播放和渲染
- startClearAnimation(lines)
- updateAnimation(deltaTime)
- isAnimationComplete()

### GameStateManager
职责: 管理游戏状态，协调各模块间的交互
- onLinesCleared(count)
- updateGameState()
- pauseGame()
- resumeGame()

### UIRenderer
职责: 渲染分数、等级、消行数等UI信息
- renderScore(score)
- renderLevel(level)
- renderLines(totalLines)
- renderCombo(combo)

## 数据流
游戏循环中，LineDetector检测满行 -> LineClearer执行消行动画 -> ScoreManager计算分数和等级 -> GameStateManager更新游戏状态 -> UIRenderer刷新界面显示 -> 数据持久化到LocalStorage

## 风险点
- 消行动画可能影响游戏流畅度
- 分数计算复杂度可能导致性能问题
- 多行同时消除时的动画同步问题
- LocalStorage容量限制可能影响数据保存

## 关键决策
- 采用观察者模式实现模块间解耦，便于扩展和维护
- 使用requestAnimationFrame确保动画流畅性
- 实现分层的分数计算系统（单行、多行、连击奖励）
- 采用状态机管理消行过程的不同阶段
- 使用Canvas离屏渲染优化消行动画性能
