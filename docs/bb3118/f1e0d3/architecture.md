# 架构设计 - 消行系统和计分系统

## 架构模式
MVC模式 + 组件化设计

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### LineDetector
职责: 检测游戏区域中的满行，返回需要清除的行号列表
- detectFullLines(gameBoard): number[]
- isLineFull(lineData): boolean

### LineClearAnimator
职责: 处理消行动画效果，包括闪烁、消失和下落动画
- playLineClearAnimation(lineNumbers): Promise
- flashLines(lineNumbers, duration): Promise
- clearLines(lineNumbers): void
- dropLinesDown(clearedLines): Promise

### ScoreCalculator
职责: 计算分数、等级和统计数据，实现计分规则
- calculateScore(linesCleared, level): number
- updateLevel(totalLines): number
- getSpeedMultiplier(level): number
- updateStatistics(linesCleared): void

### GameStateManager
职责: 管理游戏状态数据，包括分数、等级、统计信息的持久化
- updateScore(points): void
- updateLevel(newLevel): void
- saveGameData(): void
- loadGameData(): GameState
- resetGameData(): void

### LineClearController
职责: 协调消行流程，整合检测、动画、计分和状态更新
- processLineClear(gameBoard): Promise<boolean>
- handleLineClearComplete(linesCleared): void

### AudioManager
职责: 管理消行相关音效，包括单行、多行消除音效
- playLineClearSound(linesCount): void
- playLevelUpSound(): void
- setVolume(volume): void

## 数据流
游戏主循环检测到方块落地后，调用LineClearController.processLineClear() → LineDetector检测满行 → 如有满行，LineClearAnimator播放消行动画 → ScoreCalculator计算分数和等级 → GameStateManager更新游戏状态并保存到LocalStorage → AudioManager播放相应音效 → 返回游戏主循环继续

## 风险点
- 消行动画可能影响游戏流畅性，需要优化动画性能
- 多行同时消除时的动画同步问题
- LocalStorage容量限制可能影响数据保存
- 不同浏览器的Canvas渲染性能差异

## 关键决策
- 使用Promise链处理消行动画序列，确保动画完成后再继续游戏逻辑
- 采用经典俄罗斯方块计分规则：单行100分，双行300分，三行500分，四行800分
- 等级系统基于消除行数，每10行提升一级，影响下落速度
- 使用requestAnimationFrame实现流畅的消行动画效果
- LocalStorage存储游戏数据，包括最高分、统计信息和用户设置
