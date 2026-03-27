# 架构设计 - 实现游戏结束判定系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: HTML5 Canvas
- **database**: LocalStorage（游戏状态持久化）
- **others**: CSS3, Web APIs, RequestAnimationFrame

## 模块设计

### GameOverDetector
职责: 游戏结束条件检测，包括顶部堆积检测和新方块放置检测
- checkGameOver(gameBoard, currentPiece): boolean
- isTopRowBlocked(gameBoard): boolean
- canPlaceNewPiece(gameBoard, piece, position): boolean

### GameStateManager
职责: 管理游戏状态转换，处理游戏结束后的状态变更
- setGameState(state): void
- getGameState(): string
- handleGameOver(): void
- resetGame(): void

### GameOverUI
职责: 游戏结束界面显示和用户交互处理
- showGameOverScreen(finalScore, level): void
- hideGameOverScreen(): void
- bindRestartEvents(): void
- displayFinalStats(stats): void

### ScoreRecorder
职责: 记录和管理最高分数，处理分数持久化
- saveHighScore(score): void
- getHighScore(): number
- isNewHighScore(score): boolean
- getScoreHistory(): Array

### GameController
职责: 协调游戏结束流程，整合各个模块的功能
- processGameOverCheck(): void
- triggerGameOver(): void
- handleRestart(): void
- pauseGameLoop(): void

## 数据流
游戏主循环 → GameOverDetector检测结束条件 → GameController触发结束流程 → GameStateManager更新状态 → ScoreRecorder保存分数 → GameOverUI显示结束界面 → 用户选择重新开始 → GameController重置游戏状态

## 风险点
- 顶部堆积检测可能出现边界情况误判
- 游戏状态切换时可能出现竞态条件
- LocalStorage存储失败导致分数丢失
- 游戏结束动画可能影响性能

## 关键决策
- 采用双重检测机制：既检查顶部堆积又检查新方块放置可能性
- 使用状态机模式管理游戏状态转换，确保状态一致性
- 实现分数本地持久化，提升用户体验
- 游戏结束时暂停主游戏循环，避免资源浪费
- 提供快速重新开始功能，减少用户操作步骤
